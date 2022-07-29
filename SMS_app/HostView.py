
import json

import requests
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import AddTeacherForm, AddStudentForm, EditStudentForm, SelectYearForm
from .models import CustomUser, Teachers, Classes, SessionYearModel, Students, NotificationStudent, \
    NotificationTeacher, FeedBackTeacher, FeedBackStudent, LeaveReportTeacher, LeaveReportStudent,  \
    LessonTimeSet, Timetable, \
    SubjectsTeacher


def admin_home(request,session):
    Session = SessionYearModel.object.get(id=session)
    student_cnt = Students.objects.filter(session_year_id=session).all().count()
    teacher_cnt = Teachers.objects.all().count()
    class_cnt = Classes.objects.filter(year=session).all().count()
    student_girl = Students.objects.filter(session_year_id=session, gender="Nữ").all().count()
    student_boy = Students.objects.filter(session_year_id=session, gender="Nam").all().count()

    cnt_10=0
    cnt_11=0
    cnt_12=0
    classes_10= Classes.objects.filter(year=session, name=10).all()
    student_count_list = []
    class_name_list_10 = []
    for classe in classes_10:
        students= Students.objects.filter(class_id=classe).all().count()
        cnt_10 = cnt_10 + students
        class_name_list_10.append(classe.class_name)
        student_count_list.append(students)

    classes_11 = Classes.objects.filter(year=session, name=11).all()
    student_count_list11 = []
    class_name_list_11 = []
    for classe in classes_11:
        students = Students.objects.filter(class_id=classe).all().count()
        cnt_11 = cnt_11 + students
        class_name_list_11.append(classe.class_name)
        student_count_list11.append(students)

    classes_12 = Classes.objects.filter(year=session, name=12).all()
    student_count_list12 = []
    class_name_list_12 = []
    for classe in classes_12:
        students = Students.objects.filter(class_id=classe).all().count()
        cnt_12 = cnt_12 + students
        class_name_list_12.append(classe.class_name)
        student_count_list12.append(students)

    return render(request, "Admin/home_admin.html",
                  {"session": Session,"id":session, 'student_cnt':student_cnt,'teacher_cnt':teacher_cnt,
                   'class_cnt':class_cnt,'cnt_10':cnt_10,'cnt_11':cnt_11,'cnt_12':cnt_12,
                   'student_girl':student_girl, 'student_boy':student_boy,
                   'class_name_list_10':class_name_list_10,'student_count_list':student_count_list,
                   'class_name_list_11':class_name_list_11,'student_count_list11':student_count_list11,
                   'class_name_list_12':class_name_list_12,'student_count_list12':student_count_list12})

def admin_select_year(request):
    return render(request,"Admin/select_year.html")

def MajorFields(request):
        return render(request, "Admin/MajorField.html")

    #----------------------------------------- Teacher ----------------------------------------#


def add_teacher(request):
    form = AddTeacherForm()
    return render(request,"Admin/add_teacher.html",{"form":form})

def add_teacher_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddTeacherForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            position = form.cleaned_data["position"]
            subject = form.cleaned_data["subject"]
            address = form.cleaned_data["address"]
            sex = form.cleaned_data["sex"]
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,last_name=last_name, first_name=first_name, user_type=2)
                user.teachers.address = address
                user.teachers.gender = sex
                user.teachers.major = subject
                user.teachers.position = position
                user.teachers.phone = "0"
                user.teachers.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "Đã Thêm Giáo Viên")
                return HttpResponseRedirect(reverse("add_teacher"))
            except:
                messages.error(request, "Lỗi! Không Thêm Được Giáo Viên")
                return HttpResponseRedirect(reverse("add_teacher"))
        else:
            form = AddTeacherForm(request.POST)
            return render(request, "Admin/add_teacher.html", {"form": form})

def edit_teacher(request,teacher_id,session):
    teacher=Teachers.objects.get(admin=teacher_id)
    return render(request,"admin/edit_teacher.html",{"teacher":teacher,"teacher_id":teacher_id, 'id':session})

def edit_teacher_save(request,session):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        teacher_id=request.POST.get("teacher_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        position=request.POST.get("position")
        major = request.POST.get("major")
        sdt = request.POST.get("sdt")
        username=request.POST.get("username")
        address=request.POST.get("address")
        gender=request.POST.get("sex")
        try:
            user=CustomUser.objects.get(id=teacher_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            teacher_model=Teachers.objects.get(admin=teacher_id)
            teacher_model.address=address
            teacher_model.gender=gender
            teacher_model.position = position
            teacher_model.major = major
            teacher_model.phone = sdt
            teacher_model.save()
            messages.success(request,"Đã Chỉnh Sửa Giáo Viên")
            return HttpResponseRedirect(reverse("manage_teacher_in_session",kwargs={"session":session}))
        except:
            messages.error(request,"Lỗi! Không Chỉnh Sửa Được Giáo Viên")
            return HttpResponseRedirect(reverse("edit_teacher",kwargs={"teacher_id":teacher_id, 'session':session}))


def manage_teacher(request):
    teachers=Teachers.objects.all()
    teachers_cnt=Teachers.objects.all().count()
    Maths_teachers = Teachers.objects.filter(major="Toán").all()
    Maths_teachers_cnt = Teachers.objects.filter(major="Toán").all().count()
    Maths_teachers_per = (Maths_teachers_cnt*100)/teachers_cnt
    Physics_teachers = Teachers.objects.filter(major="Lí").all()
    Physics_teachers_cnt = Teachers.objects.filter(major="Lí").all().count()
    Physics_teachers_per = (Physics_teachers_cnt * 100) / teachers_cnt
    Chemis_teachers = Teachers.objects.filter(major="Hoá Học").all()
    Chemis_teachers_cnt = Teachers.objects.filter(major="Hoá Học").all().count()
    Chemis_teachers_per = (Chemis_teachers_cnt * 100) / teachers_cnt
    Bio_teachers = Teachers.objects.filter(major="Sinh").all()
    Bio_teachers_cnt = Teachers.objects.filter(major="Sinh").all().count()
    Bio_teachers_per = (Bio_teachers_cnt * 100) / teachers_cnt
    IT_teachers = Teachers.objects.filter(major="Tin Học-Công Nghệ").all()
    IT_teachers_cnt = Teachers.objects.filter(major="Tin Học-Công Nghệ").all().count()
    IT_teachers_per = (IT_teachers_cnt * 100) / teachers_cnt
    Liters_teachers = Teachers.objects.filter(major="Văn").all()
    Liters_teachers_cnt = Teachers.objects.filter(major="Văn").all().count()
    Liters_teachers_per = (Liters_teachers_cnt * 100) / teachers_cnt
    socials_teachers = Teachers.objects.filter(major="Sử-Địa-GDCD").all()
    socials_teachers_cnt = Teachers.objects.filter(major="Sử-Địa-GDCD").all().count()
    socials_teachers_per = (socials_teachers_cnt * 100) / teachers_cnt
    PD_teachers = Teachers.objects.filter(major="TD-QPAN").all()
    PD_teachers_cnt = Teachers.objects.filter(major="TD-QPAN").all().count()
    PD_teachers_per = (PD_teachers_cnt * 100) / teachers_cnt
    Languages_teachers = Teachers.objects.filter(major="Ngoại Ngữ").all()
    Languages_teachers_cnt = Teachers.objects.filter(major="Ngoại Ngữ").all().count()
    Languages_teachers_per = (Languages_teachers_cnt * 100) / teachers_cnt
    feedbacks= FeedBackTeacher.objects.all()
    return render(request,"Admin/manage_teacher.html", {'teachers': teachers,'teachers_cnt':teachers_cnt,'Maths_teachers':Maths_teachers,'Physics_teachers':Physics_teachers,'Chemis_teachers':Chemis_teachers,'Bio_teachers':Bio_teachers,'IT_teachers':IT_teachers,'Liters_teachers':Liters_teachers,'socials_teachers':socials_teachers,'PD_teachers':PD_teachers,'Languages_teachers':Languages_teachers,
    'Maths_teachers_cnt': Maths_teachers_cnt, 'Physics_teachers_cnt': Physics_teachers_cnt, 'Chemis_teachers_cnt': Chemis_teachers_cnt, 'Bio_teachers_cnt': Bio_teachers_cnt, 'IT_teachers_cnt': IT_teachers_cnt, 'Liters_teachers_cnt': Liters_teachers_cnt, 'socials_teachers_cnt': socials_teachers_cnt, 'PD_teachers_cnt': PD_teachers_cnt, 'Languages_teachers_cnt': Languages_teachers_cnt,
    'Maths_teachers_per': Maths_teachers_per, 'Languages_teachers_per':Languages_teachers_per,'PD_teachers_per':PD_teachers_per,'socials_teachers_per':socials_teachers_per,'Liters_teachers_per':Liters_teachers_per,'IT_teachers_per':IT_teachers_per,'Bio_teachers_per':Bio_teachers_per,'Chemis_teachers_per':Chemis_teachers_per,'Physics_teachers_per':Physics_teachers_per,
    'feedbacks':feedbacks})

def manage_teacher_in_session(request,session):
    teachers = Teachers.objects.all()
    teachers_cnt = Teachers.objects.all().count()
    Maths_teachers = Teachers.objects.filter(major="Toán").all()
    Maths_teachers_cnt = Teachers.objects.filter(major="Toán").all().count()
    Maths_teachers_per = (Maths_teachers_cnt * 100) / teachers_cnt
    Physics_teachers = Teachers.objects.filter(major="Lí").all()
    Physics_teachers_cnt = Teachers.objects.filter(major="Lí").all().count()
    Physics_teachers_per = (Physics_teachers_cnt * 100) / teachers_cnt
    Chemis_teachers = Teachers.objects.filter(major="Hoá Học").all()
    Chemis_teachers_cnt = Teachers.objects.filter(major="Hoá Học").all().count()
    Chemis_teachers_per = (Chemis_teachers_cnt * 100) / teachers_cnt
    Bio_teachers = Teachers.objects.filter(major="Sinh").all()
    Bio_teachers_cnt = Teachers.objects.filter(major="Sinh").all().count()
    Bio_teachers_per = (Bio_teachers_cnt * 100) / teachers_cnt
    IT_teachers = Teachers.objects.filter(major="Tin Học-Công Nghệ").all()
    IT_teachers_cnt = Teachers.objects.filter(major="Tin Học-Công Nghệ").all().count()
    IT_teachers_per = (IT_teachers_cnt * 100) / teachers_cnt
    Liters_teachers = Teachers.objects.filter(major="Văn").all()
    Liters_teachers_cnt = Teachers.objects.filter(major="Văn").all().count()
    Liters_teachers_per = (Liters_teachers_cnt * 100) / teachers_cnt
    socials_teachers = Teachers.objects.filter(major="Sử-Địa-GDCD").all()
    socials_teachers_cnt = Teachers.objects.filter(major="Sử-Địa-GDCD").all().count()
    socials_teachers_per = (socials_teachers_cnt * 100) / teachers_cnt
    PD_teachers = Teachers.objects.filter(major="TD-QPAN").all()
    PD_teachers_cnt = Teachers.objects.filter(major="TD-QPAN").all().count()
    PD_teachers_per = (PD_teachers_cnt * 100) / teachers_cnt
    Languages_teachers = Teachers.objects.filter(major="Ngoại Ngữ").all()
    Languages_teachers_cnt = Teachers.objects.filter(major="Ngoại Ngữ").all().count()
    Languages_teachers_per = (Languages_teachers_cnt * 100) / teachers_cnt
    feedbacks = FeedBackTeacher.objects.all()
    leaves = LeaveReportTeacher.objects.all()
    return render(request, "Admin/manage_teacher_in_session.html",
                  {'id':session,'teachers': teachers, 'teachers_cnt': teachers_cnt, 'Maths_teachers': Maths_teachers,
                   'Physics_teachers': Physics_teachers, 'Chemis_teachers': Chemis_teachers,
                   'Bio_teachers': Bio_teachers, 'IT_teachers': IT_teachers, 'Liters_teachers': Liters_teachers,
                   'socials_teachers': socials_teachers, 'PD_teachers': PD_teachers,
                   'Languages_teachers': Languages_teachers,
                   'Maths_teachers_cnt': Maths_teachers_cnt, 'Physics_teachers_cnt': Physics_teachers_cnt,
                   'Chemis_teachers_cnt': Chemis_teachers_cnt, 'Bio_teachers_cnt': Bio_teachers_cnt,
                   'IT_teachers_cnt': IT_teachers_cnt, 'Liters_teachers_cnt': Liters_teachers_cnt,
                   'socials_teachers_cnt': socials_teachers_cnt, 'PD_teachers_cnt': PD_teachers_cnt,
                   'Languages_teachers_cnt': Languages_teachers_cnt,
                   'Maths_teachers_per': Maths_teachers_per, 'Languages_teachers_per': Languages_teachers_per,
                   'PD_teachers_per': PD_teachers_per, 'socials_teachers_per': socials_teachers_per,
                   'Liters_teachers_per': Liters_teachers_per, 'IT_teachers_per': IT_teachers_per,
                   'Bio_teachers_per': Bio_teachers_per, 'Chemis_teachers_per': Chemis_teachers_per,
                   'Physics_teachers_per': Physics_teachers_per,
                   'feedbacks':feedbacks, 'leaves':leaves})



    # ----------------------------------------- Student ----------------------------------------#


def add_student(request,session):
    Session=SessionYearModel.object.filter(id=session).all()
    classes=Classes.objects.filter(year=session).all()
    st=Students.objects.filter(id=1)
    form=AddStudentForm()
    return render(request,"Admin/add_student.html",{"form":form, "classes": classes, "id": session, "session": Session, "st":st})

def add_student_save(request,session):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        course_id = request.POST.get("classe")
        sex = request.POST.get("gender")
            # profile_pic = request.FILES['profile_pic']
            # fs = FileSystemStorage()
            # filename = fs.save(profile_pic.name, profile_pic)
            # profile_pic_url = fs.url(filename)
        user = CustomUser.objects.create_user(username=username, password=password, email=email,last_name=last_name, first_name=first_name, user_type=3)
        user.students.address = address
        course_obj = Classes.objects.get(id=course_id)
        user.students.class_id = course_obj
        session_year = SessionYearModel.object.get(id=session)
        user.students.session_year_id = session_year
        user.students.gender = sex
        user.save()
        if (SubjectsTeacher.objects.filter(name="Sinh Học",class_id=course_obj, term='1').exists() == False):
            b = SubjectsTeacher(name="Sinh Học",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Sinh Học",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()

        if (SubjectsTeacher.objects.filter(name="Sinh Học",class_id=course_obj, term='2').exists() == False):
            b = SubjectsTeacher(name="Sinh Học",class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Sinh Học",class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()

        if (SubjectsTeacher.objects.filter(name="Toán",class_id=course_obj, term='1').exists() == False):
            b = SubjectsTeacher(name="Toán",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Toán",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()

        if (SubjectsTeacher.objects.filter(name="Toán",class_id=course_obj, term='2').exists() == False):
            b = SubjectsTeacher(name="Toán",class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Toán",class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()

        if (SubjectsTeacher.objects.filter(name="Vật Lí", class_id=course_obj, term='1').exists() == False):

            b = SubjectsTeacher(name="Vật Lí",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Lịch Sử",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()

        if (SubjectsTeacher.objects.filter(name="Hoá Học",class_id=course_obj, term='1').exists() == False):

            b = SubjectsTeacher(name="Hoá Học",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Hoá Học",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()

        if (SubjectsTeacher.objects.filter(name="Lịch Sử",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Lịch Sử",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Lịch Sử",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Địa Lí",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Địa Lí",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Địa Lí",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="GDCD",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="GDCD",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="GDCD",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Ngữ Văn",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Ngữ Văn",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Ngữ Văn",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Thể Dục",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Thể Dục",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Thể Dục",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="GDQP",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="GDQP",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b =SubjectsTeacher.objects.get(name="GDQP",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Công Nghệ",class_id=course_obj, term='1').exists() == False):

            b = SubjectsTeacher(name="Công Nghệ",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Công Nghệ",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Tin Học",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Tin Học",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Tin Học",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Ngoại Ngữ",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Ngoại Ngữ",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Ngoại Ngữ",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Môn Chuyên",class_id=course_obj, term='1').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Môn Chuyên",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Môn Chuyên",class_id=course_obj, term='1')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Vật Lí", class_id=course_obj, term='2').exists() == False):

            b = SubjectsTeacher(name="Vật Lí", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Lịch Sử", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()

        if (SubjectsTeacher.objects.filter(name="Hoá Học", class_id=course_obj, term='2').exists() == False):

            b = SubjectsTeacher(name="Hoá Học", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Hoá Học", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()

        if (SubjectsTeacher.objects.filter(name="Lịch Sử", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Lịch Sử", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Lịch Sử", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Địa Lí", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Địa Lí", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Địa Lí", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="GDCD", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="GDCD", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="GDCD", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Ngữ Văn", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Ngữ Văn", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Ngữ Văn", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Thể Dục", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Thể Dục", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Thể Dục", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="GDQP", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="GDQP", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="GDQP", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Công Nghệ", class_id=course_obj, term='2').exists() == False):

            b = SubjectsTeacher(name="Công Nghệ", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Công Nghệ", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Tin Học", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Tin Học", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Tin Học", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Ngoại Ngữ", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Ngoại Ngữ", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Ngoại Ngữ", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
            print("sdsd")
        if (SubjectsTeacher.objects.filter(name="Môn Chuyên", class_id=course_obj, term='2').exists() == False):
            print("ds")
            b = SubjectsTeacher(name="Môn Chuyên", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        else:
            b = SubjectsTeacher.objects.get(name="Môn Chuyên", class_id=course_obj, term='2')
            b.student_id = user.students
            b.save()
        messages.success(request, "Đã Thêm Học Sinh")
        return HttpResponseRedirect(reverse("add_student", kwargs={'session':session}))


def edit_student(request,student_id,session):
    Session = SessionYearModel.object.filter(id=session).all()
    request.session['student_id']=student_id
    student=Students.objects.get(admin=student_id)
    form=EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['classe'].initial=student.class_id.id
    form.fields['sex'].initial=student.gender
    form.fields['session_year_id'].initial=student.session_year_id.id
    return render(request,"Admin/edit_student.html",{"form":form,"student_id":student_id,"username":student.admin.username,"session":session,"id":session})

def edit_student_save(request,session,student_id):
    Session = SessionYearModel.object.filter(id=session).all()
    print(request)
    print("dxf")
    print(session)
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if student_id==None:
            return HttpResponseRedirect(reverse("manage_student", kwargs={"id": session}))

        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            session_year_id=form.cleaned_data["session_year_id"]
            class_id = form.cleaned_data["classe"]
            sex = form.cleaned_data["sex"]

            if request.FILES.get('profile_pic',False):
                profile_pic=request.FILES['profile_pic']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            try:
                user=CustomUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name=last_name
                user.username=username
                user.email=email
                user.save()

                student=Students.objects.get(admin=student_id)
                student.address=address
                session_year = SessionYearModel.object.get(id=session_year_id)
                student.session_year_id = session_year
                student.gender=sex
                classe=Classes.objects.get(id=class_id)
                student.class_id=classe
                if profile_pic_url!=None:
                    student.profile_pic=profile_pic_url
                student.save()
                del request.session['student_id']
                messages.success(request,"Đã Chỉnh Sửa Học Sinh")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id,"session":session}))
            except:
                messages.error(request,"Lỗi! Không Chỉnh Sửa Được Học Sinh")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id,"session":session}))
        else:
            form=EditStudentForm(request.POST)
            student=Students.objects.get(admin=student_id)
            return render(request,"Admin/edit_student.html",{"form":form,"student_id":student_id,"username":student.admin.username,"id":session,"session":Session})


def manage_student(request,session):
    Session=SessionYearModel.object.get(id=session)
    students=Students.objects.filter(session_year_id=Session).all()
    return render(request,"Admin/manage_student.html",{"students":students,"id":session,"session":Session})

# ----------------------------------------- Classes ----------------------------------------#

@csrf_exempt
def get_class(request):
    session_year = request.POST.get("session_year")

    session=SessionYearModel.object.get(id=session_year)
    classes=Classes.objects.filter(year=session)
    return classes

def add_class(request,session):
    teachers = Teachers.objects.all()
    Session = SessionYearModel.object.filter(id=session).all()
    return render(request,"admin/add_class.html",{"teachers": teachers, "id":session,"session": Session})

def add_class_save(request,session):
    Session = SessionYearModel.object.filter(id=session).all()
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        teacher_id = request.POST.get("teacher")
        session_id = session
        teacher=CustomUser.objects.get(id=teacher_id)
        session =SessionYearModel.object.get(id=session_id)

        Class = Classes(name=name, subject=subject, GVCN=teacher, class_name=str(name)+str(subject), year=session)
        Class.save()
        messages.success(request, "Đã Thêm Lớp Học")
        return HttpResponseRedirect(reverse("add_class",kwargs={"session":session_id}))

def edit_class(request,class_id,session):
    classe=Classes.objects.filter(year=session).get(id=class_id)
    return render(request,"Admin/edit_class.html",{"classe":classe,"id":session, "class_id":class_id})

def edit_class_save(request,session,class_id):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        teacher = request.POST.get("teacher")
        Session = SessionYearModel.object.get(id=session)

        try:
            classe=Classes.objects.get(id=class_id)
            print(classe.class_name)
            classe.name=name
            classe.subject = subject
            classe.teacher = teacher
            classe.year = Session
            classe.class_name = str(name)+str(subject)
            classe.save()
            messages.success(request,"Đã Chỉnh Sửa Lớp Học")
            return HttpResponseRedirect(reverse("edit_class",kwargs={"class_id":class_id,"session":session}))
        except:
            messages.error(request,"Không Chỉnh Sửa Được Khoá Lớp Học")
            return HttpResponseRedirect(reverse("edit_class",kwargs={"class_id":class_id,"session":session}))


def manage_class(request,session):
    Session = SessionYearModel.object.get(id=session)
    session_id = session
    # lớp 10
    classes_10=Classes.objects.filter(year=Session, name="10").all()

    student_count_in_class_10 = []
    maths = []
    for classe in classes_10:
        students = Students.objects.filter(class_id=classe).count()
        classe.ss = students
        classe.save()
        student_count_in_class_10.append(students)
    # lớp 11
    classes_11 = Classes.objects.filter(year=Session, name="11").all()
    student_count_in_class_11 = []
    for classe in classes_11:
        students = Students.objects.filter(class_id=classe).count()
        classe.ss = students
        classe.save()
        student_count_in_class_11.append(students)
    # lớp 12
    classes_12 = Classes.objects.filter(year=Session, name="12").all()
    student_count_in_class_12 = []
    for classe in classes_12:
        students = Students.objects.filter(class_id=classe).count()
        classe.ss = students
        classe.save()
        student_count_in_class_12.append(students)
    #Teacher
    teachers = Teachers.objects.all()
    Maths_teachers = Teachers.objects.filter(major="Toán").all()
    Physics_teachers = Teachers.objects.filter(major="Lí").all()
    Chemis_teachers = Teachers.objects.filter(major="Hoá Học").all()
    Bio_teachers = Teachers.objects.filter(major="Sinh").all()
    IT_teachers = Teachers.objects.filter(major="Tin Học-Công Nghệ").all()
    Liters_teachers = Teachers.objects.filter(major="Văn").all()
    socials_teachers = Teachers.objects.filter(major="Sử-Địa-GDCD").all()
    PD_teachers = Teachers.objects.filter(major="TD-QPAN").all()
    Languages_teachers = Teachers.objects.filter(major="Ngoại Ngữ").all()
    #GVBM

    return render(request,"Admin/manage_class.html",{"maths":maths,"classes_10":classes_10,"classes_11":classes_11,"classes_12":classes_12,
                                                     "student_count_in_class_10":student_count_in_class_10,"student_count_in_class_11":student_count_in_class_11,"student_count_in_class_12":student_count_in_class_12,
                                                     'id':session_id,
                                                     'teachers': teachers,
                                                     'Maths_teachers': Maths_teachers,
                                                     'Physics_teachers': Physics_teachers,
                                                     'Chemis_teachers': Chemis_teachers, 'Bio_teachers': Bio_teachers,
                                                     'IT_teachers': IT_teachers, 'Liters_teachers': Liters_teachers,
                                                     'socials_teachers': socials_teachers, 'PD_teachers': PD_teachers,
                                                     'Languages_teachers': Languages_teachers
                                                     })

def lession_time_set(request,session):
    Session = SessionYearModel.object.get(id=session)
    class_list = Classes.objects.filter(year = session).all()
    lts_mor = LessonTimeSet.objects.filter(session=Session, time="mor").all()
    lts_aft = LessonTimeSet.objects.filter(session=Session, time="aft").all()

    # TimeTable
    # Lesson Time Set
    if (LessonTimeSet.objects.filter(name="m1", session=Session, time="mor").all().count() == 0):
        LessonTimeSet(name="m1", session=Session, time="mor").save()
    if (LessonTimeSet.objects.filter(name="m2", session=Session, time="mor").all().count() == 0):
        LessonTimeSet(name="m2", session=Session, time="mor").save()
    if (LessonTimeSet.objects.filter(name="m3", session=Session, time="mor").all().count() == 0):
        LessonTimeSet(name="m3", session=Session, time="mor").save()
    if (LessonTimeSet.objects.filter(name="m4", session=Session, time="mor").all().count() == 0):
        LessonTimeSet(name="m4", session=Session, time="mor").save()
    if (LessonTimeSet.objects.filter(name="m5", session=Session, time="mor").all().count() == 0):
        LessonTimeSet(name="m5", session=Session, time="mor").save()
    if (LessonTimeSet.objects.filter(name="a1", session=Session, time="aft").all().count() == 0):
        LessonTimeSet(name="a1", session=Session, time="aft").save()
    if (LessonTimeSet.objects.filter(name="a2", session=Session, time="aft").count() == 0):
        LessonTimeSet(name="a2", session=Session, time="aft").save()
    if (LessonTimeSet.objects.filter(name="a3", session=Session, time="aft").count() == 0):
        LessonTimeSet(name="a3", session=Session, time="aft").save()

    mt1 = LessonTimeSet.objects.get(name="m1", session=Session, time="mor")
    mt2 = LessonTimeSet.objects.get(name="m2", session=Session, time="mor")
    mt3 = LessonTimeSet.objects.get(name="m3", session=Session, time="mor")
    mt4 = LessonTimeSet.objects.get(name="m4", session=Session, time="mor")
    mt5 = LessonTimeSet.objects.get(name="m5", session=Session, time="mor")
    at1 = LessonTimeSet.objects.get(name="a1", session=Session, time="aft")
    at2 = LessonTimeSet.objects.get(name="a2", session=Session, time="aft")
    at3 = LessonTimeSet.objects.get(name="a3", session=Session, time="aft")

    return render(request,"Admin/lesson_time_set.html",{'id':session,'lts_mor':lts_mor,'lts_aft':lts_aft,
                                                        'mt1':mt1,'mt2':mt2,'mt3':mt3,'mt4':mt4,'mt5':mt5,
                                                        'at1':at1,'at2':at2,'at3':at3, 'class_list':class_list})
@csrf_exempt
def get_class_divide(request):
    class_id = request.POST.get("classe")
    print(class_id)
    classe = Classes.objects.get(id=class_id)
    print("fdf")
    if(Timetable.objects.filter(class_id=classe, name="l1_2").all().count()==0):
        Timetable(class_id=classe, name="l1_2").save()
    if (Timetable.objects.filter(class_id=classe, name="l1_3").all().count() == 0):
        Timetable(class_id=classe, name="l1_3").save()
    if (Timetable.objects.filter(class_id=classe, name="l1_4").all().count() == 0):
        Timetable(class_id=classe, name="l1_4").save()
    if (Timetable.objects.filter(class_id=classe, name="l1_5").all().count() == 0):
        Timetable(class_id=classe, name="l1_5").save()
    if (Timetable.objects.filter(class_id=classe, name="l1_6").all().count() == 0):
        Timetable(class_id=classe, name="l1_6").save()
    if (Timetable.objects.filter(class_id=classe, name="l1_7").all().count() == 0):
        Timetable(class_id=classe, name="l1_7").save()
    if (Timetable.objects.filter(class_id=classe, name="l2_2").all().count() == 0):
        Timetable(class_id=classe, name="l2_2").save()
    if (Timetable.objects.filter(class_id=classe, name="l2_3").all().count() == 0):
        Timetable(class_id=classe, name="l2_3").save()
    if (Timetable.objects.filter(class_id=classe, name="l2_4").all().count() == 0):
        Timetable(class_id=classe, name="l2_4").save()
    if (Timetable.objects.filter(class_id=classe, name="l2_5").all().count() == 0):
        Timetable(class_id=classe, name="l2_5").save()
    if (Timetable.objects.filter(class_id=classe, name="l2_6").all().count() == 0):
        Timetable(class_id=classe, name="l2_6").save()
    if (Timetable.objects.filter(class_id=classe, name="l2_7").all().count() == 0):
        Timetable(class_id=classe, name="l2_7").save()
    if (Timetable.objects.filter(class_id=classe, name="l3_2").all().count() == 0):
        Timetable(class_id=classe, name="l3_2").save()
    if (Timetable.objects.filter(class_id=classe, name="l3_3").all().count() == 0):
        Timetable(class_id=classe, name="l3_3").save()
    if (Timetable.objects.filter(class_id=classe, name="l3_4").all().count() == 0):
        Timetable(class_id=classe, name="l3_4").save()
    if (Timetable.objects.filter(class_id=classe, name="l3_5").all().count() == 0):
        Timetable(class_id=classe, name="l3_5").save()
    if (Timetable.objects.filter(class_id=classe, name="l3_6").all().count() == 0):
        Timetable(class_id=classe, name="l3_6").save()
    if (Timetable.objects.filter(class_id=classe, name="l3_7").all().count() == 0):
        Timetable(class_id=classe, name="l3_7").save()
    if (Timetable.objects.filter(class_id=classe, name="l4_2").all().count() == 0):
        Timetable(class_id=classe, name="l4_2").save()
    if (Timetable.objects.filter(class_id=classe, name="l4_3").all().count() == 0):
        Timetable(class_id=classe, name="l4_3").save()
    if (Timetable.objects.filter(class_id=classe, name="l4_4").all().count() == 0):
        Timetable(class_id=classe, name="l4_4").save()
    if (Timetable.objects.filter(class_id=classe, name="l4_5").all().count() == 0):
        Timetable(class_id=classe, name="l4_5").save()
    if (Timetable.objects.filter(class_id=classe, name="l4_6").all().count() == 0):
        Timetable(class_id=classe, name="l4_6").save()
    if (Timetable.objects.filter(class_id=classe, name="l4_7").all().count() == 0):
        Timetable(class_id=classe, name="l4_7").save()
    if (Timetable.objects.filter(class_id=classe, name="l5_2").all().count() == 0):
        Timetable(class_id=classe, name="l5_2").save()
    if (Timetable.objects.filter(class_id=classe, name="l5_3").all().count() == 0):
        Timetable(class_id=classe, name="l5_3").save()
    if (Timetable.objects.filter(class_id=classe, name="l5_4").all().count() == 0):
        Timetable(class_id=classe, name="l5_4").save()
    if (Timetable.objects.filter(class_id=classe, name="l5_5").all().count() == 0):
        Timetable(class_id=classe, name="l5_5").save()
    if (Timetable.objects.filter(class_id=classe, name="l5_6").all().count() == 0):
        Timetable(class_id=classe, name="l5_6").save()
    if (Timetable.objects.filter(class_id=classe, name="l5_7").all().count() == 0):
        Timetable(class_id=classe, name="l5_7").save()
    if (Timetable.objects.filter(class_id=classe, name="l6_2").all().count() == 0):
        Timetable(class_id=classe, name="l6_2").save()
    if (Timetable.objects.filter(class_id=classe, name="l6_3").all().count() == 0):
        Timetable(class_id=classe, name="l6_3").save()
    if (Timetable.objects.filter(class_id=classe, name="l6_4").all().count() == 0):
        Timetable(class_id=classe, name="l6_4").save()
    if (Timetable.objects.filter(class_id=classe, name="l6_5").all().count() == 0):
        Timetable(class_id=classe, name="l6_5").save()
    if (Timetable.objects.filter(class_id=classe, name="l6_6").all().count() == 0):
        Timetable(class_id=classe, name="l6_6").save()
    if (Timetable.objects.filter(class_id=classe, name="l6_7").all().count() == 0):
        Timetable(class_id=classe, name="l6_7").save()
    if (Timetable.objects.filter(class_id=classe, name="l7_2").all().count() == 0):
        Timetable(class_id=classe, name="l7_2").save()
    if (Timetable.objects.filter(class_id=classe, name="l7_3").all().count() == 0):
        Timetable(class_id=classe, name="l7_3").save()
    if (Timetable.objects.filter(class_id=classe, name="l7_4").all().count() == 0):
        Timetable(class_id=classe, name="l7_4").save()
    if (Timetable.objects.filter(class_id=classe, name="l7_5").all().count() == 0):
        Timetable(class_id=classe, name="l7_5").save()
    if (Timetable.objects.filter(class_id=classe, name="l7_6").all().count() == 0):
        Timetable(class_id=classe, name="l7_6").save()
    if (Timetable.objects.filter(class_id=classe, name="l7_7").all().count() == 0):
        Timetable(class_id=classe, name="l7_7").save()
    if (Timetable.objects.filter(class_id=classe, name="l8_2").all().count() == 0):
        Timetable(class_id=classe, name="l8_2").save()
    if (Timetable.objects.filter(class_id=classe, name="l8_3").all().count() == 0):
        Timetable(class_id=classe, name="l8_3").save()
    if (Timetable.objects.filter(class_id=classe, name="l8_4").all().count() == 0):
        Timetable(class_id=classe, name="l8_4").save()
    if (Timetable.objects.filter(class_id=classe, name="l8_5").all().count() == 0):
        Timetable(class_id=classe, name="l8_5").save()
    if (Timetable.objects.filter(class_id=classe, name="l8_6").all().count() == 0):
        Timetable(class_id=classe, name="l8_6").save()
    if (Timetable.objects.filter(class_id=classe, name="l8_7").all().count() == 0):
        Timetable(class_id=classe, name="l8_7").save()
    classes_data = Timetable.objects.filter(class_id=classe).all()
    list_data = []

    for data in classes_data:
        data_small = {"name": data.name, "subject": data.subject}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

def run(lb, name, class_id):
    classe = Classes.objects.get(id=class_id)
    print(lb)
    tb = Timetable.objects.get(class_id=classe, name=name)
    if (lb == "Toán"):
        teacher = CustomUser.objects.get(id=classe.maths_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Vật Lí"):
        teacher = CustomUser.objects.get(id=classe.physics_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Hoá Học"):
        teacher = CustomUser.objects.get(id=classe.chemis_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Sinh Học"):
        teacher = CustomUser.objects.get(id=classe.bio_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Lịch Sử"):
        teacher = CustomUser.objects.get(id=classe.history_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Địa Lí"):
        teacher = CustomUser.objects.get(id=classe.geo_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "GDCD"):
        teacher = CustomUser.objects.get(id=classe.GDCD_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Ngữ Văn"):
        teacher = CustomUser.objects.get(id=classe.liters_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Công Nghệ"):
        teacher = CustomUser.objects.get(id=classe.tech_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Tin Học"):
        teacher = CustomUser.objects.get(id=classe.computer_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Thể Dục"):
        teacher = CustomUser.objects.get(id=classe.PE_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "GDQP"):
        teacher = CustomUser.objects.get(id=classe.DE_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Ngoại ngữ"):
        teacher = CustomUser.objects.get(id=classe.languages_name_id)
        tb.teacher = teacher
        tb.save()
    if (lb == "Chuyên Đề"):
        teacher = CustomUser.objects.get(id=classe.major_name_id)
        tb.teacher = teacher
        tb.save()
    return

def timetable_division_save(request,session):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        class_id = request.POST.get("class_id")
        classe = Classes.objects.get(id=class_id)
        l1_2 = request.POST.get("l1_2")
        l1_3 = request.POST.get("l1_3")
        l1_4 = request.POST.get("l1_4")
        l1_5 = request.POST.get("l1_5")
        l1_6 = request.POST.get("l1_6")
        l1_7 = request.POST.get("l1_7")

        l2_2 = request.POST.get("l2_2")
        l2_3 = request.POST.get("l2_3")
        l2_4 = request.POST.get("l2_4")
        l2_5 = request.POST.get("l2_5")
        l2_6 = request.POST.get("l2_6")
        l2_7 = request.POST.get("l2_7")

        l3_2 = request.POST.get("l3_2")
        l3_3 = request.POST.get("l3_3")
        l3_4 = request.POST.get("l3_4")
        l3_5 = request.POST.get("l3_5")
        l3_6 = request.POST.get("l3_6")
        l3_7 = request.POST.get("l3_7")

        l4_2 = request.POST.get("l4_2")
        l4_3 = request.POST.get("l4_3")
        l4_4 = request.POST.get("l4_4")
        l4_5 = request.POST.get("l4_5")
        l4_6 = request.POST.get("l4_6")
        l4_7 = request.POST.get("l4_7")

        l5_2 = request.POST.get("l5_2")
        l5_3 = request.POST.get("l5_3")
        l5_4 = request.POST.get("l5_4")
        l5_5 = request.POST.get("l5_5")
        l5_6 = request.POST.get("l5_6")
        l5_7 = request.POST.get("l5_7")

        l6_2 = request.POST.get("l6_2")
        l6_3 = request.POST.get("l6_3")
        l6_4 = request.POST.get("l6_4")
        l6_5 = request.POST.get("l6_5")
        l6_6 = request.POST.get("l6_6")
        l6_7 = request.POST.get("l6_7")

        l7_2 = request.POST.get("l7_2")
        l7_3 = request.POST.get("l7_3")
        l7_4 = request.POST.get("l7_4")
        l7_5 = request.POST.get("l7_5")
        l7_6 = request.POST.get("l7_6")
        l7_7 = request.POST.get("l7_7")

        l8_2 = request.POST.get("l8_2")
        l8_3 = request.POST.get("l8_3")
        l8_4 = request.POST.get("l8_4")
        l8_5 = request.POST.get("l8_5")
        l8_6 = request.POST.get("l8_6")
        l8_7 = request.POST.get("l8_7")
        try:
            tb = Timetable.objects.get(class_id=classe, name="l1_2")
            tb.subject = l1_2
            tb.save()
            name = "l1_2"
            run(l1_2,name,class_id)
            tb = Timetable.objects.get(class_id=classe, name="l1_3")
            tb.subject = l1_3
            tb.save()
            name = "l1_3"
            run(l1_3, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l1_4")
            tb.subject = l1_4
            tb.save()
            name = "l1_4"
            run(l1_4, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l1_5")
            tb.subject = l1_5
            tb.save()
            name = "l1_5"
            run(l1_5, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l1_6")
            tb.subject = l1_6
            tb.save()
            name = "l1_6"
            run(l1_6, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l1_7")
            tb.subject = l1_7
            tb.save()
            name = "l1_7"
            run(l1_7, name, class_id)

            tb = Timetable.objects.get(class_id=classe, name="l2_2")
            tb.subject = l2_2
            tb.save()
            name = "l2_2"
            run(l2_2, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l2_3")
            tb.subject = l2_3
            tb.save()
            name = "l2_3"
            run(l2_3, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l2_4")
            tb.subject = l2_4
            tb.save()
            name = "l2_4"
            run(l2_4, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l2_5")
            tb.subject = l2_5
            tb.save()
            name = "l2_5"
            run(l2_5, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l2_6")
            tb.subject = l2_6
            tb.save()
            name = "l2_6"
            run(l2_6, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l2_7")
            tb.subject = l2_7
            tb.save()
            name = "l2_7"
            run(l2_7, name, class_id)

            tb = Timetable.objects.get(class_id=classe, name="l3_2")
            tb.subject = l3_2
            tb.save()
            name = "l3_2"
            run(l3_2, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l3_3")
            tb.subject = l3_3
            tb.save()
            name = "l3_3"
            run(l3_3, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l3_4")
            tb.subject = l3_4
            tb.save()
            name = "l3_4"
            run(l3_4, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l3_5")
            tb.subject = l3_5
            tb.save()
            name = "l3_5"
            run(l3_5, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l3_6")
            tb.subject = l3_6
            tb.save()
            name = "l3_6"
            run(l3_6, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l3_7")
            tb.subject = l3_7
            tb.save()
            name = "l3_7"
            run(l3_7, name, class_id)

            tb = Timetable.objects.get(class_id=classe, name="l4_2")
            tb.subject = l4_2
            tb.save()
            name = "l4_2"
            run(l4_2, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l4_3")
            tb.subject = l4_3
            tb.save()
            name = "l4_3"
            run(l4_3, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l4_4")
            tb.subject = l4_4
            tb.save()
            name = "l4_4"
            run(l4_4, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l4_5")
            tb.subject = l4_5
            tb.save()
            name = "l4_5"
            run(l4_5, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l4_6")
            tb.subject = l4_6
            tb.save()
            name = "l4_6"
            run(l4_6, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l4_7")
            tb.subject = l4_7
            tb.save()
            name = "l4_7"
            run(l4_7, name, class_id)

            tb = Timetable.objects.get(class_id=classe, name="l5_2")
            tb.subject = l5_2
            tb.save()
            name = "l5_2"
            run(l5_2, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l5_3")
            tb.subject = l5_3
            tb.save()
            name = "l5_3"
            run(l5_3, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l5_4")
            tb.subject = l5_4
            tb.save()
            name = "l5_4"
            run(l5_4, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l5_5")
            tb.subject = l5_5
            tb.save()
            name = "l5_5"
            run(l5_5, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l5_6")
            tb.subject = l5_6
            tb.save()
            name = "l5_6"
            run(l5_6, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l5_7")
            tb.subject = l5_7
            tb.save()
            name = "l5_7"
            run(l5_7, name, class_id)

            tb = Timetable.objects.get(class_id=classe, name="l6_2")
            tb.subject = l6_2
            tb.save()
            name = "l6_2"
            run(l6_2, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l6_3")
            tb.subject = l6_3
            tb.save()
            name = "l6_3"
            run(l6_3, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l6_4")
            tb.subject = l6_4
            tb.save()
            name = "l6_4"
            run(l6_4, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l6_5")
            tb.subject = l6_5
            tb.save()
            name = "l6_5"
            run(l6_5, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l6_6")
            tb.subject = l6_6
            tb.save()
            name = "l6_6"
            run(l6_6, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l6_7")
            tb.subject = l6_7
            tb.save()
            name = "l6_7"
            run(l6_7, name, class_id)

            tb = Timetable.objects.get(class_id=classe, name="l7_2")
            tb.subject = l7_2
            tb.save()
            name = "l7_2"
            run(l7_2, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l7_3")
            tb.subject = l7_3
            tb.save()
            name = "l7_3"
            run(l7_3, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l7_4")
            tb.subject = l7_4
            tb.save()
            name = "l7_4"
            run(l7_4, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l7_5")
            tb.subject = l7_5
            tb.save()
            name = "l7_5"
            run(l7_5, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l7_6")
            tb.subject = l7_6
            tb.save()
            name = "l7_6"
            run(l7_6, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l7_7")
            tb.subject = l7_7
            tb.save()
            name = "l7_7"
            run(l7_7, name, class_id)

            tb = Timetable.objects.get(class_id=classe, name="l8_2")
            tb.subject = l8_2
            tb.save()
            name = "l8_2"
            run(l8_2, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l8_3")
            tb.subject = l8_3
            tb.save()
            name = "l8_3"
            run(l8_3, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l8_4")
            tb.subject = l8_4
            tb.save()
            name = "l8_4"
            run(l8_4, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l8_5")
            tb.subject = l8_5
            tb.save()
            name = "l8_5"
            run(l8_5, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l8_6")
            tb.subject = l8_6
            tb.save()
            name = "l8_6"
            run(l8_6, name, class_id)
            tb = Timetable.objects.get(class_id=classe, name="l8_7")
            tb.subject = l8_7
            tb.save()
            name = "l8_7"
            run(l8_7, name, class_id)
            messages.success(request, "Đã Cài Đặt Thành Công!")
            return HttpResponseRedirect(reverse("lession_time_set", kwargs={"session": session}))
        except:
            messages.error(request, "Lỗi Cài Đặt!")
            return HttpResponseRedirect(reverse("lession_time_set", kwargs={"session": session}))

def lession_time_set_save(request,session):
    Session = SessionYearModel.object.get(id=session)
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        mt1_s = request.POST.get("mt1_s")
        mt1_e = request.POST.get("mt1_e")
        mt2_s = request.POST.get("mt2_s")
        mt2_e = request.POST.get("mt2_e")
        mt3_s = request.POST.get("mt3_s")
        mt3_e = request.POST.get("mt3_e")
        mt4_s = request.POST.get("mt4_s")
        mt4_e = request.POST.get("mt4_e")
        mt5_s = request.POST.get("mt5_s")
        mt5_e = request.POST.get("mt5_e")
        at1_s = request.POST.get("at1_s")
        at1_e = request.POST.get("at1_e")
        at2_s = request.POST.get("at2_s")
        at2_e = request.POST.get("at2_e")
        at3_s = request.POST.get("at3_s")
        at3_e = request.POST.get("at3_e")
        try:
            if(mt1_s!='None' and mt1_e!='None'):
                lts = LessonTimeSet.objects.get(name="m1", session=Session, time="mor")
                lts.time_start=mt1_s
                lts.time_end=mt1_e
                lts.save()
            if (mt2_s != 'None' and mt2_e != 'None'):
                lts = LessonTimeSet.objects.get(name="m2", session=Session, time="mor")
                print(mt2_s)
                lts.time_start = mt2_s
                lts.time_end = mt2_e
                print(lts)
                lts.save()
            if (mt3_s != 'None' and mt3_e != 'None'):
                lts = LessonTimeSet.objects.get(name="m3", session=Session, time="mor")
                lts.time_start = mt3_s
                lts.time_end = mt3_e
                lts.save()
            if (mt4_s != 'None' and mt4_e != 'None'):
                lts = LessonTimeSet.objects.get(name="m4", session=Session, time="mor")
                lts.time_start = mt4_s
                lts.time_end = mt4_e
                lts.save()
            if (mt5_s != 'None' and mt5_e != 'None'):
                lts = LessonTimeSet.objects.get(name="m5", session=Session, time="mor")
                lts.time_start = mt5_s
                lts.time_end = mt5_e
                lts.save()
            if (at1_s != 'None' and at1_e != 'None'):
                lts = LessonTimeSet.objects.get(name="a1", session=Session, time="aft")
                lts.time_start = at1_s
                lts.time_end = at1_e
                lts.save()
            if (at2_s != 'None' and at2_e != 'None'):
                lts = LessonTimeSet.objects.get(name="a2", session=Session, time="aft")
                lts.time_start = at2_s
                lts.time_end = at2_e
                lts.save()
            if (at3_s != 'None' and at3_e != 'None'):
                lts = LessonTimeSet.objects.get(name="a3", session=Session, time="aft")
                lts.time_start = at3_s
                lts.time_end = at3_e
                lts.save()
            messages.success(request, "Đã Cài Đặt Thành Công!")
            return HttpResponseRedirect(reverse("lession_time_set", kwargs={"session": session}))
        except:
            messages.error(request, "Lỗi!")
            return HttpResponseRedirect(reverse("lession_time_set", kwargs={"session": session}))

# ----------------------------------------- Session Year ----------------------------------------#

def manage_session(request):
    return render(request,"Admin/manage_session.html")

def select_year(request):
    session_list = SessionYearModel.object.all()
    return render(request,"Admin/select_session.html",{'session_list':session_list})

def select_year_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        session = request.POST.get("session")
        try:
            return HttpResponseRedirect(reverse("admin_home", kwargs={"session": session}))
        except:
            messages.error(request, "Lỗi!")
            return HttpResponseRedirect(reverse("admin_select_year"))


def add_session_save(request):
    if request.method!="POST":
        messages.error(request, "Lỗi! Không Thêm Được Niên Khoá")
        return HttpResponseRedirect(reverse("admin_select_year"))
    else:
        session_start_year=request.POST.get("session_start")
        session_end_year=request.POST.get("session_end")

        try:
            sessionyear=SessionYearModel(session_start_year=session_start_year,session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Đã Thêm Niên Khoá")
            return HttpResponseRedirect(reverse("admin_select_year"))
        except:
            messages.error(request, "Lỗi! Không Thêm Được Niên Khoá")
            return HttpResponseRedirect(reverse("admin_select_year"))

# ----------------------------------------- Nontifications ----------------------------------------#

def admin_send_notification_student(request,session):
    students=Students.objects.all()
    return render(request,"Admin/student_notification.html",{"students":students,'id':session})

def admin_send_notification_teacher(request,session):
    teachers=Teachers.objects.all()
    return render(request,"Admin/teacher_notification.html",{"teachers":teachers,'id':session})

@csrf_exempt
def send_student_notification(request):
    id=request.POST.get("id")
    message=request.POST.get("message")
    student=Students.objects.get(admin=id)
    token=student.fcm_token
    url="https://fcm.googleapis.com/fcm/send"
    body={
        "notification":{
            "title":"Student Management System",
            "body":message,
            "click_action": "https://studentmanagementsystem22.herokuapp.com/student_all_notification",
            "icon": "http://studentmanagementsystem22.herokuapp.com/static/dist/img/user2-160x160.jpg"
        },
        "to":token
    }
    headers={"Content-Type":"application/json","Authorization":"key=SERVER_KEY_HERE"}
    data=requests.post(url,data=json.dumps(body),headers=headers)
    notification=NotificationStudent(student_id=student,message=message)
    notification.save()
    print(data.text)
    return HttpResponse("True")

@csrf_exempt
def send_teacher_notification(request):
    id=request.POST.get("id")
    message=request.POST.get("message")
    teacher=Teachers.objects.get(admin=id)
    token=teacher.fcm_token
    url="https://fcm.googleapis.com/fcm/send"
    body={
        "notification":{
            "title":"Student Management System",
            "body":message,
            "click_action":"https://studentmanagementsystem22.herokuapp.com/staff_all_notification",
            "icon":"http://studentmanagementsystem22.herokuapp.com/static/dist/img/user2-160x160.jpg"
        },
        "to":token
    }
    headers={"Content-Type":"application/json","Authorization":"key=SERVER_KEY_HERE"}
    data=requests.post(url,data=json.dumps(body),headers=headers)
    notification=NotificationTeacher(teacher_id=teacher,message=message)
    notification.save()
    print(data.text)
    return HttpResponse("True")


@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def division_teacher_save(request):
    id=request.POST.get("id")
    print(id)
    classe=Classes.objects.get(id=id)
    print(classe)
    maths_teacher_id = request.POST.get("maths")
    if(maths_teacher_id.isdigit() == False):
        maths_teacher_id = 'None'
    physics_teacher_id = request.POST.get("physics")
    if (physics_teacher_id.isdigit()== False):
        physics_teacher_id = 'None'
    chemis_teacher_id = request.POST.get("chemis")
    if (chemis_teacher_id.isdigit()== False):
        chemis_teacher_id = 'None'
    bio_teacher_id = request.POST.get("bio")
    if (bio_teacher_id.isdigit()== False):
        bio_teacher_id = 'None'
    history_teacher_id = request.POST.get("history")
    if (history_teacher_id.isdigit()== False):
        history_teacher_id = 'None'
    print(history_teacher_id)
    geo_teacher_id = request.POST.get("geo")
    if (geo_teacher_id.isdigit()== False):
        geo_teacher_id = 'None'
    GDCD_teacher_id = request.POST.get("GDCD")
    if (GDCD_teacher_id.isdigit()== False):
        GDCD_teacher_id = 'None'
    liters_teacher_id = request.POST.get("liters")
    if (liters_teacher_id.isdigit() == False):
        liters_teacher_id = 'None'
    PE_teacher_id = request.POST.get("PE")
    if (PE_teacher_id.isdigit()== False):
        PE_teacher_id = 'None'
    DE_teacher_id = request.POST.get("DE")
    if (DE_teacher_id.isdigit()== False):
        DE_teacher_id = 'None'
    languages_teacher_id = request.POST.get("languages")
    if (languages_teacher_id.isdigit()== False):
        languages_teacher_id = 'None'
    major_teacher_id = request.POST.get("major")
    if (major_teacher_id.isdigit()== False):
        major_teacher_id = 'None'
    tech_teacher_id = request.POST.get("tech")
    if (tech_teacher_id.isdigit()== False):
        tech_teacher_id = 'None'
    computer_teacher_id = request.POST.get("computer")
    if (computer_teacher_id.isdigit()== False):
        computer_teacher_id = 'None'

    students=Students.objects.filter(class_id=classe).all()
    for student in students:
        # physics
        if (physics_teacher_id != 'None'):
            physics_teacher = CustomUser.objects.get(id=physics_teacher_id)

            if (SubjectsTeacher.objects.filter(name="Vật Lí", class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Vật Lí",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Vật Lí",class_id=classe, student_id=student, term='1')
            b.teacher = physics_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Vật Lí", class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Vật Lí",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Vật Lí",class_id=classe, student_id=student, term='2')
            b.teacher = physics_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.physics_name = str(physics_teacher.first_name) +" "+  str(physics_teacher.last_name)
            classe.physics_name_id = physics_teacher_id
            classe.save()
            print(classe)

        # Chemis
        if (chemis_teacher_id != 'None'):
            chemis_teacher = CustomUser.objects.get(id=chemis_teacher_id)
            if (SubjectsTeacher.objects.filter(name="Hoá Học",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Hoá Học",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Hoá Học",class_id=classe, student_id=student, term='1')
            b.teacher = chemis_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Hoá Học",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Hoá Học",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Hoá Học",class_id=classe, student_id=student, term='2')
            b.teacher = chemis_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.chemis_name = str(chemis_teacher.first_name) +" "+  str(chemis_teacher.last_name)
            classe.chemis_name_id = chemis_teacher_id
            classe.save()
            print(classe)

        # History
        if (history_teacher_id != 'None'):
            history_teacher = CustomUser.objects.get(id=history_teacher_id)
            print(history_teacher)
            if (SubjectsTeacher.objects.filter(name="Lịch Sử",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Lịch Sử",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Lịch Sử",class_id=classe, student_id=student, term='1')
            b.teacher = history_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Lịch Sử",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Lịch Sử",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Lịch Sử",class_id=classe, student_id=student, term='2')
            b.teacher = history_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.history_name = str(history_teacher.first_name) +" "+  str(history_teacher.last_name)
            classe.history_name_id = history_teacher_id
            classe.save()
            print(classe)

        # Geo
        if (geo_teacher_id != 'None'):
            geo_teacher = CustomUser.objects.get(id=geo_teacher_id)
            print(geo_teacher)
            if (SubjectsTeacher.objects.filter(name="Địa Lí",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Địa Lí",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Địa Lí",class_id=classe, student_id=student, term='1')
            b.teacher = geo_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Địa Lí",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Địa Lí",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Địa Lí",class_id=classe, student_id=student, term='2')
            b.teacher = geo_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.geo_name = str(geo_teacher.first_name) +" "+  str(geo_teacher.last_name)
            classe.geo_name_id = geo_teacher.id
            classe.save()
            print(classe)

        # GDCD
        if (GDCD_teacher_id != 'None'):
            GDCD_teacher = CustomUser.objects.get(id=GDCD_teacher_id)
            print(GDCD_teacher)
            if (SubjectsTeacher.objects.filter(name="GDCD",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="GDCD",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="GDCD",class_id=classe, student_id=student, term='1')
            b.teacher = GDCD_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="GDCD",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="GDCD",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="GDCD",class_id=classe, student_id=student, term='2')
            b.teacher = GDCD_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.GDCD_name = str(GDCD_teacher.first_name) +" "+  str(GDCD_teacher.last_name)
            classe.GDCD_name_id = GDCD_teacher_id

            classe.save()
            print(classe)

        # Liters
        if (liters_teacher_id != 'None'):
            liters_teacher = CustomUser.objects.get(id=liters_teacher_id)
            print(liters_teacher)
            if (SubjectsTeacher.objects.filter(name="Ngữ Văn",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Ngữ Văn",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Ngữ Văn",class_id=classe, student_id=student, term='1')
            b.teacher = liters_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Ngữ Văn",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Ngữ Văn",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Ngữ Văn",class_id=classe, student_id=student, term='2')
            b.teacher = liters_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.liters_name = str(liters_teacher.first_name) +" "+  str(liters_teacher.last_name)
            classe.liters_name_id = liters_teacher_id

            classe.save()
            print(classe)
        # Tech
        if (tech_teacher_id != 'None'):
            tech_teacher = CustomUser.objects.get(id=tech_teacher_id)
            print(tech_teacher)
            if (SubjectsTeacher.objects.filter(name="Công Nghệ",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Công Nghệ",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Công Nghệ",class_id=classe, student_id=student, term='1')
            b.teacher = tech_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Công Nghệ",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Công Nghệ",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Công Nghệ",class_id=classe, student_id=student, term='2')
            b.teacher = tech_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.tech_name = str(tech_teacher.first_name) +" "+  str(tech_teacher.last_name)
            classe.tech_name_id = tech_teacher_id
            classe.save()
            print(classe)

        # Computer
        if (computer_teacher_id != 'None'):
            computer_teacher = CustomUser.objects.get(id=computer_teacher_id)
            print(computer_teacher)
            if (SubjectsTeacher.objects.filter(name="Tin Học",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Tin Học",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Tin Học",class_id=classe, student_id=student, term='1')
            b.teacher = computer_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Tin Học",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Tin Học",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Tin Học",class_id=classe, student_id=student, term='2')
            b.teacher = computer_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.computer_name = str(computer_teacher.first_name) +" "+ str(computer_teacher.last_name)
            classe.computer_name_id = computer_teacher_id
            classe.save()
            print(classe)

        # PE
        if (PE_teacher_id != 'None'):
            PE_teacher = CustomUser.objects.get(id=PE_teacher_id)
            print(PE_teacher)
            if (SubjectsTeacher.objects.filter(name="Thể Dục",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Thể Dục",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Thể Dục",class_id=classe, student_id=student, term='1')
            b.teacher = PE_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Thể Dục",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Thể Dục",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Thể Dục",class_id=classe, student_id=student, term='2')
            b.teacher = PE_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.PE_name = str(PE_teacher.first_name) +" "+ str(PE_teacher.last_name)
            classe.PE_name_id = PE_teacher_id
            classe.save()
            print(classe)

        # DE
        if (DE_teacher_id != 'None'):
            DE_teacher = CustomUser.objects.get(id=DE_teacher_id)
            print(DE_teacher)
            if (SubjectsTeacher.objects.filter(name="GDQP",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="GDQP",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="GDQP",class_id=classe, student_id=student, term='1')
            b.teacher = DE_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="GDQP",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="GDQP",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="GDQP",class_id=classe, student_id=student, term='2')
            b.teacher = DE_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.DE_name = str(DE_teacher.first_name) +" "+  str(DE_teacher.last_name)
            classe.DE_name_id = DE_teacher_id
            classe.save()
            print(classe)

        # Languages
        if (languages_teacher_id != 'None'):
            languages_teacher = CustomUser.objects.get(id=languages_teacher_id)
            print(languages_teacher)
            if (SubjectsTeacher.objects.filter(name="Ngoại Ngữ",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Ngoại Ngữ",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Ngoại Ngữ",class_id=classe, student_id=student, term='1')
            b.teacher = languages_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Ngoại Ngữ",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Ngoại Ngữ",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Ngoại Ngữ",class_id=classe, student_id=student, term='2')
            b.teacher = languages_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.languages_name = str(languages_teacher.first_name) +" "+  str(languages_teacher.last_name)
            classe.languages_name_id = languages_teacher_id
            classe.save()
            print(classe)

        # MajorF
        if (major_teacher_id != 'None'):
            major_teacher = CustomUser.objects.get(id=major_teacher_id)
            print(major_teacher)
            if (SubjectsTeacher.objects.filter(name="Môn Chuyên",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Môn Chuyên",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Môn Chuyên",class_id=classe, student_id=student, term='1')
            b.teacher = major_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Môn Chuyên",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Môn Chuyên",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Môn Chuyên",class_id=classe, student_id=student, term='2')
            b.teacher = major_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.major_name = str(major_teacher.first_name) +" "+  str(major_teacher.last_name)
            classe.major_name_id = major_teacher_id
            classe.save()
            print(classe)
        # bio
        if (bio_teacher_id != 'None'):
            bio_teacher = CustomUser.objects.get(id=bio_teacher_id)
            print(bio_teacher)
            if (SubjectsTeacher.objects.filter(name="Sinh Học",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Sinh Học",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Sinh Học",class_id=classe, student_id=student, term='1')
            b.teacher = bio_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Sinh Học",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Sinh Học",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Sinh Học",class_id=classe, student_id=student, term='2')
            b.teacher = bio_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.bio_name = str(bio_teacher.first_name) +" "+  str(bio_teacher.last_name)
            classe.bio_name_id = bio_teacher_id
            classe.save()
            print(classe)
        # maths
        if (maths_teacher_id != 'None'):
            maths_teacher = CustomUser.objects.get(id=maths_teacher_id)

            if (SubjectsTeacher.objects.filter(name="Toán",class_id=classe, student_id=student, term='1').exists() == False):
                b = SubjectsTeacher(name="Toán",class_id=classe, student_id=student, term='1')
            else:
                b = SubjectsTeacher.objects.get(name="Toán",class_id=classe, student_id=student, term='1')
            b.teacher = maths_teacher
            b.save()
            if (SubjectsTeacher.objects.filter(name="Toán",class_id=classe, student_id=student, term='2').exists() == False):
                b = SubjectsTeacher(name="Toán",class_id=classe, student_id=student, term='2')
            else:
                b = SubjectsTeacher.objects.get(name="Toán",class_id=classe, student_id=student, term='2')
            b.teacher = maths_teacher
            b.save()
            classe = Classes.objects.get(id=id)
            print(classe)
            classe.maths_name = str(maths_teacher.first_name) +" "+ str(maths_teacher.last_name)
            classe.maths_name_id = maths_teacher_id
            classe.save()
            print(classe)
            print("ds")

    return HttpResponse("True")

def teacher_feedback_message(request,session):
    feedbacks=FeedBackTeacher.objects.all()
    return render(request,"Admin/teacher_feedback.html",{"feedbacks":feedbacks,'id':session})

def student_feedback_message(request,session):
    feedbacks=FeedBackStudent.objects.all()
    return render(request,"Admin/student_feedback.html",{"feedbacks":feedbacks,'id':session})

@csrf_exempt
def student_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

@csrf_exempt
def teacher_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackTeacher.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def teacher_leave_view(request,session):
    leaves=LeaveReportTeacher.objects.all()
    return render(request,"Admin/teacher_leave_view.html",{"leaves":leaves,'id':session})

def student_leave_view(request,session):
    leaves=LeaveReportStudent.objects.all()
    return render(request,"Admin/student_leave_view.html",{"leaves":leaves,'id':session})

def student_approve_leave(request,leave_id,session):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_view",kwargs={'session':session}))

def student_disapprove_leave(request,leave_id,session):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_view",kwargs={'session':session}))


def teacher_approve_leave(request,leave_id,session):
    leave=LeaveReportTeacher.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("teacher_leave_view",kwargs={'session':session}))

def teacher_disapprove_leave(request,leave_id,session):
    leave=LeaveReportTeacher.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("teacher_leave_view",kwargs={'session':session}))

def admin_profile(request,session):
    student_count1 = Students.objects.filter(session_year_id=session).all().count()
    teacher_count = Teachers.objects.all().count()
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"Admin/admin_profile.html",{"user":user, "student_count":student_count1,"teacher_count":teacher_count,'id':session})

def admin_profile_save(request,session):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            # if password!=None and password!="":
            #     customuser.set_password(password)
            customuser.save()
            messages.success(request, "Đã Cập Nhật Hồ Sơ")
            return HttpResponseRedirect(reverse("admin_profile", kwargs={'id':session}))
        except:
            messages.error(request, "Lỗi! Không Cập Nhật Được Hồ Sơ")
            return HttpResponseRedirect(reverse("admin_profile",  kwargs={'id':session}))


# ----------------------------------------- Nontifications ----------------------------------------#
