import datetime as dt
from datetime import datetime, date
#from .Subject_models import physics_stn,aim,maths_stn, chemis_stn, bio_stn, history_stn, geo_stn, GDCD_stn, liters_stn, PE_stn,DE_stn, computer_stn, tech_stn,languages_stn, major_stn
#from .Subject_models import physics_stn, aim, maths_stn, chemis_stn, languages_stn, history_stn, geo_stn, computer_stn, GDCD_stn, major_stn, DE_stn, liters_stn, bio_stn, tech_stn
from .models import aim, Subjects, Exam, Exam_student, Answer, Answer_student, SubjectsTeacher
#from .forms import Postphysics,Postmaths,Postchemis,Postbio,Posthistory,Postgeo,PostGDCD,Postliters,PostPE,PostDE,Postlanguages,Postmajor,Postcomputer,Posttech
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Students, CustomUser, Attendance, AttendanceReport, \
    LeaveReportStudent, FeedBackStudent, NotificationStudent, OnlineClassRoom, SessionYearModel, Teachers, Classes, \
    LessonTimeSet, Timetable

def create_timetable_mor(class_id):
    classe = Classes.objects.get(id=class_id)
    #time = Timetable.objects.filter(teacher = teacher, class_id=classe).all()
    list= []
    t = Timetable.objects.get(class_id=classe, name='l1_2')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l1_3')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l1_4')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l1_5')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l1_6')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l1_7')
    list.append(t)
    list.append("")

    t = Timetable.objects.get(class_id=classe, name='l2_2')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l2_3')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l2_4')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l2_5')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l2_6')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l2_7')
    list.append(t)
    list.append("")

    t = Timetable.objects.get(class_id=classe, name='l3_2')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l3_3')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l3_4')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l3_5')
    list.append(t)


    t = Timetable.objects.get(class_id=classe, name='l3_6')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l3_7')
    list.append(t)
    list.append("")

    t = Timetable.objects.get(class_id=classe, name='l4_2')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l4_3')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l4_4')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l4_5')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l4_6')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l4_7')
    list.append(t)
    list.append("")

    t = Timetable.objects.get(class_id=classe, name='l5_2')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l5_3')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l5_4')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l5_5')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l5_6')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l5_7')
    list.append(t)
    list.append("")
    return list

def create_timetable_aft(class_id):
    classe = Classes.objects.get(id=class_id)
    # time = Timetable.objects.filter(teacher = teacher, class_id=classe).all()
    list = []
    t = Timetable.objects.get(class_id=classe, name='l6_2')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l6_3')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l6_4')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l6_5')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l6_6')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l6_7')
    list.append(t)
    list.append("")

    t = Timetable.objects.get(class_id=classe, name='l7_2')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l7_3')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l7_4')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l7_5')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l7_6')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l7_7')
    list.append(t)
    list.append("")

    t = Timetable.objects.get(class_id=classe, name='l8_2')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l8_3')
    list.append(t)


    t = Timetable.objects.get(class_id=classe, name='l8_4')
    list.append(t)

    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l8_6')
    list.append(t)

    t = Timetable.objects.get(class_id=classe, name='l8_7')
    list.append(t)

    list.append("")

    return list
def student_home(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
    print(student)
    lts_mor = LessonTimeSet.objects.filter(session=student.class_id.year, time="mor").all()
    lts_aft = LessonTimeSet.objects.filter(session=student.class_id.year, time="aft").all()
    timetable_mor = create_timetable_mor(student.class_id.id)
    timetable_aft = create_timetable_aft(student.class_id.id)
    class_id = student.class_id.id
    # attendance_total=AttendanceReport.objects.filter(student_id=student_obj).count()
    # attendance_present=AttendanceReport.objects.filter(student_id=student_obj,status=True).count()
    # attendance_absent=AttendanceReport.objects.filter(student_id=student_obj,status=False).count()
    # course=Courses.objects.get(id=student_obj.class_id.id)
    # subjects=Subjects.objects.filter(class_id=course).count()
    # subjects_data=Subjects.objects.filter(class_id=course)
    # session_obj=SessionYearModel.object.get(id=student_obj.session_year_id.id)
    # class_room=OnlineClassRoom.objects.filter(subject__in=subjects_data,is_active=True,session_years=session_obj)
    #
    # subject_name=[]
    # data_present=[]
    # data_absent=[]
    # subject_data=Subjects.objects.filter(class_id=student_obj.class_id)
    # for subject in subject_data:
    #     attendance=Attendance.objects.filter(subject_id=subject.id)
    #     attendance_present_count=AttendanceReport.objects.filter(attendance_id__in=attendance,status=True,student_id=student_obj.id).count()
    #     attendance_absent_count=AttendanceReport.objects.filter(attendance_id__in=attendance,status=False,student_id=student_obj.id).count()
    #     subject_name.append(subject.subject_name)
    #     data_present.append(attendance_present_count)
    #     data_absent.append(attendance_absent_count)

    return render(request,"Students/student_home.html",{'user':user,'student':student, 'lts_mor':lts_mor,'lts_aft':lts_aft,
                                                    'timetable_mor':timetable_mor,'timetable_aft':timetable_aft,'class_id':class_id})

def join_class_room(request,subject_name,class_id):
    print(subject_name)
    print(class_id)
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
    classe = Classes.objects.get(id=class_id)
    session_year_obj= classe.year
    if(OnlineClassRoom.objects.filter(class_id=classe,session_years=session_year_obj,subject=subject_name,is_active=True).all().count()>0):
        onlineclass = OnlineClassRoom.objects.get(class_id=classe,session_years=session_year_obj,subject=subject_name,is_active=True)
        return render(request,"Students/join_class_room_start.html",{"user":user,"student":student,"username":request.user.username,"password":onlineclass.room_pwd,"roomid":onlineclass.room_name})
    else:
        messages.error(request, "Hiện tại chưa có lớp học")
        return HttpResponseRedirect(reverse("student_home"))


def student_view_attendance(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
    return render(request,"Students/student_view_attendance.html",{"user":user,"student":student})

def handle_sub(sub, classe_id):
    classe = Classes.objects.get(id=classe_id)
    print(classe.maths_name)
    if(sub=="maths"):
        return classe.maths_name_id
    if (sub == "physics"):
        return classe.physics_name_id
    if (sub == "chemis"):
        return classe.chemis_name_id
    if (sub == "bio"):
        return classe.bio_name_id
    if (sub == "history"):
        return classe.history_name_id
    if (sub == "geo"):
        return classe.geo_name_id
    if (sub == "GDCD"):
        return classe.GDCD_name_id
    if (sub == "PE"):
        return classe.PE_name_id
    if (sub == "DE"):
        return classe.DE_name_id
    if (sub == "tech"):
        return classe.tech_name_id
    if (sub == "computer"):
        return classe.computer_name_id
    if (sub == "languages"):
        return classe.languages_name_id
    if (sub == "liters"):
        return classe.liters_name_id
    if (sub == "major"):
        return classe.major_name_id

def student_view_attendance_post(request):
   #  return HttpResponse("student_view_attendance_post")
    if request.method != "POST":
        return HttpResponseRedirect(reverse("student_view_attendance"))
    else:
        user = CustomUser.objects.get(id=request.user.id)
        student = Students.objects.get(admin=user)
        subject=request.POST.get("subject")
        print(subject)
        user_teacher = CustomUser.objects.get(id=handle_sub(subject,student.class_id.id))
        teacher = Teachers.objects.get(admin=user_teacher)
        start_date=request.POST.get("start_date")
        end_date=request.POST.get("end_date")


        start_data_parse=datetime.strptime(start_date,"%Y-%m-%d").date()
        end_data_parse=datetime.strptime(end_date,"%Y-%m-%d").date()

        user_object=CustomUser.objects.get(id=request.user.id)
        stud_obj=Students.objects.get(admin=user_object)

        attendance=Attendance.objects.filter(attendance_date__range=(start_data_parse,end_data_parse),GVMB_id=teacher)
        attendance_reports=AttendanceReport.objects.filter(attendance_id__in=attendance,student_id=stud_obj)
        return render(request,"Students/student_attendance_data.html",{"user":user,"student":student,"attendance_reports":attendance_reports})

def student_apply_leave(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
    staff_obj = Students.objects.get(admin=request.user.id)
    leave_data=LeaveReportStudent.objects.filter(student_id=staff_obj)
    return render(request,"Students/student_apply_leave.html",{"user":user,"student":student,"leave_data":leave_data})

def student_apply_leave_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_apply_leave"))
    else:
        leave_date=request.POST.get("leave_date")
        leave_msg=request.POST.get("leave_msg")

        student_obj=Students.objects.get(admin=request.user.id)
        try:
            leave_report=LeaveReportStudent(student_id=student_obj,leave_date=leave_date,leave_message=leave_msg,leave_status=0)
            leave_report.save()
            messages.success(request, "Đã Gửi Thành Công")
            return HttpResponseRedirect(reverse("student_apply_leave"))
        except:
            messages.error(request, "Lỗi! Không Gửi Được")
            return HttpResponseRedirect(reverse("student_apply_leave"))


def student_feedback(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)

    feedback_data=FeedBackStudent.objects.filter(student_id=student)
    return render(request,"Students/student_feedback.html",{"user":user,"student":student,"feedback_data":feedback_data})

def student_feedback_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_feedback"))
    else:
        feedback_msg=request.POST.get("feedback_msg")

        student_obj=Students.objects.get(admin=request.user.id)
        try:
            feedback=FeedBackStudent(student_id=student_obj,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request, "Đã Gửi Thành Công")
            return HttpResponseRedirect(reverse("student_feedback"))
        except:
            messages.error(request, "Lỗi! Không Gửi Được")
            return HttpResponseRedirect(reverse("student_feedback"))

def student_profile(request):
    student_obj = Students.objects.get(admin=request.user.id)
    attendance_total = AttendanceReport.objects.filter(student_id=student_obj).count()
    course = Classes.objects.get(id=student_obj.class_id.id)
    user=CustomUser.objects.get(id=request.user.id)
    student=Students.objects.get(admin=user)
    subs_HK1 = SubjectsTeacher.objects.filter(student_id = student_obj, term='1').all()
    subs_HK2 = SubjectsTeacher.objects.filter(student_id = student_obj, term='2').all()
    total = 0
    cnt = 0
    for sub in subs_HK2:
        if(sub.avg_y != None):
            total+=float(sub.avg_y)
            cnt+=1
    if(cnt>0):
        total = total/cnt
    else:
        total ='-'
    return render(request,"Students/student_profile.html",{"user":user,"student":student,"total_attendance":attendance_total, "course":course,
                                                           'subs_HK1':subs_HK1,'subs_HK2':subs_HK2,'total':total}, )
#
def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.save()
            messages.success(request, "Đã Cập Nhật Hồ Sơ")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(request, "Lỗi! Không Cập Nhật Được Hồ Sơ")
            return HttpResponseRedirect(reverse("student_profile"))

@csrf_exempt
def student_fcmtoken_save(request):
    token=request.POST.get("token")
    try:
        student=Students.objects.get(admin=request.user.id)
        student.fcm_token=token
        student.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def student_all_notification(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)

    student1=Students.objects.get(admin=request.user.id)
    notifications=NotificationStudent.objects.filter(student_id=student1.id)
    return render(request,"Students/all_notification.html",{"user":user,"student":student,"notifications":notifications})

def student_view_result(request):
    return HttpResponse("student_view_result")
    # user = CustomUser.objects.get(id=request.user.id)
    # student = Students.objects.get(admin=user)
    #
    # student1=Students.objects.get(admin=request.user.id)
    # studentresult=StudentResult.objects.filter(student_id=student1.id)
    # return render(request,"student_template/student_result.html",{"user":user,"student":student,"studentresult":studentresult})


def home_private_result(request):
    student = Students.objects.get(admin=request.user)
    if Subjects.objects.filter(name="Toán", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Toán", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Toán", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Toán", alf_user=request.user, term='2')
        f1.save()
    #physics
    if Subjects.objects.filter(name="Vật Lí", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Vật Lí", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Vật Lí", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Vật Lí", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="Hoá Học", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Hoá Học", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Hoá Học", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Hoá Học", alf_user=request.user, term='2')
        f1.save()

    if Subjects.objects.filter(name="Sinh Học", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Sinh Học", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Sinh Học", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Sinh Học", alf_user=request.user, term='2')
        f1.save()

    if Subjects.objects.filter(name="Lịch Sử", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Lịch Sử", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Lịch Sử", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Lịch Sử", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="Địa Lí", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Địa Lí", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Địa Lí", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Địa Lí", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="GDCD", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="GDCD", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="GDCD", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="GDCD", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="Tin Học", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Tin Học", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Tin Học", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Tin Học", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="Công Nghệ", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Công Nghệ", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Công Nghệ", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Công Nghệ", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="Thể Dục", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Thể Dục", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Thể Dục", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Thể Dục", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="GDQP", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="GDQP", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="GDQP", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="GDQP", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="Ngoại Ngữ", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Ngoại Ngữ", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Ngoại Ngữ", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Ngoại Ngữ", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="Ngữ Văn", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Ngữ Văn", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Ngữ Văn", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Ngữ Văn", alf_user=request.user, term='2')
        f1.save()
    if Subjects.objects.filter(name="Môn Chuyên", alf_user=request.user, term='1').all().count() == 0:
        f1 = Subjects(name="Môn Chuyên", alf_user=request.user, term='1')
        f1.save()
    if Subjects.objects.filter(name="Môn Chuyên", alf_user=request.user, term='2').all().count() == 0:
        f1 = Subjects(name="Môn Chuyên", alf_user=request.user, term='2')
        f1.save()
    if aim.objects.filter(alf_user=request.user).all().count() == 0:
        a = aim(alf_user=request.user)
        a.save()
    hk1_maths = Subjects.objects.get(name="Toán", alf_user=request.user, term='1')
    hk2_maths = Subjects.objects.get(name="Toán", alf_user=request.user, term='2')
    hk1_physics = Subjects.objects.get(name="Vật Lí", alf_user=request.user, term='1')
    hk2_physics = Subjects.objects.get(name="Vật Lí", alf_user=request.user, term='2')
    hk1_chemis = Subjects.objects.get(name="Hoá Học", alf_user=request.user, term='1')
    hk2_chemis = Subjects.objects.get(name="Hoá Học", alf_user=request.user, term='2')
    hk1_bio = Subjects.objects.get(name="Sinh Học", alf_user=request.user, term='1')
    hk2_bio = Subjects.objects.get(name="Sinh Học", alf_user=request.user, term='2')
    hk1_history = Subjects.objects.get(name="Lịch Sử", alf_user=request.user, term='1')
    hk2_history = Subjects.objects.get(name="Lịch Sử", alf_user=request.user, term='2')
    hk1_geo = Subjects.objects.get(name="Địa Lí", alf_user=request.user, term='1')
    hk2_geo = Subjects.objects.get(name="Địa Lí", alf_user=request.user, term='2')
    hk1_GDCD = Subjects.objects.get(name="GDCD", alf_user=request.user, term='1')
    hk2_GDCD = Subjects.objects.get(name="GDCD", alf_user=request.user, term='2')
    hk1_tech = Subjects.objects.get(name="Công Nghệ", alf_user=request.user, term='1')
    hk2_tech = Subjects.objects.get(name="Công Nghệ", alf_user=request.user, term='2')
    hk1_computer = Subjects.objects.get(name="Tin Học", alf_user=request.user, term='1')
    hk2_computer = Subjects.objects.get(name="Tin Học", alf_user=request.user, term='2')
    hk1_languages = Subjects.objects.get(name="Ngoại Ngữ", alf_user=request.user, term='1')
    hk2_languages = Subjects.objects.get(name="Ngoại Ngữ", alf_user=request.user, term='2')
    hk1_major = Subjects.objects.get(name="Môn Chuyên", alf_user=request.user, term='1')
    hk2_major = Subjects.objects.get(name="Môn Chuyên", alf_user=request.user, term='2')
    hk1_liters = Subjects.objects.get(name="Ngữ Văn", alf_user=request.user, term='1')
    hk2_liters = Subjects.objects.get(name="Ngữ Văn", alf_user=request.user, term='2')
    hk1_DE = Subjects.objects.get(name="GDQP", alf_user=request.user, term='1')
    hk2_DE = Subjects.objects.get(name="GDQP", alf_user=request.user, term='2')
    hk1_PE= Subjects.objects.get(name="Thể Dục", alf_user=request.user, term='1')
    hk2_PE = Subjects.objects.get(name="Thể Dục", alf_user=request.user, term='2')
    tar = get_object_or_404(aim,alf_user=request.user)
    if(hk1_maths.avg != None and hk2_maths.avg != None):
        avg_maths = round((hk1_maths.avg+hk2_maths.avg*2)/3,2)
    else:
        avg_maths = None
    if (hk1_physics.avg != None and hk2_physics.avg != None):
        avg_physics = round((hk1_physics.avg + hk2_physics.avg * 2) / 3, 2)
    else:
        avg_physics = None
    if (hk1_chemis.avg != None and hk2_chemis.avg != None):
        avg_chemis = round((hk1_chemis.avg + hk2_chemis.avg * 2) / 3, 2)
    else:
        avg_chemis = None
    if (hk1_bio.avg != None and hk2_bio.avg != None):
        avg_bio = round((hk1_bio.avg + hk2_bio.avg * 2) / 3, 2)
    else:
        avg_bio = None
    if (hk1_history.avg != None and hk2_history.avg != None):
        avg_history = round((hk1_history.avg + hk2_history.avg * 2) / 3, 2)
    else:
        avg_history = None
    if (hk1_geo.avg != None and hk2_geo.avg != None):
        avg_geo = round((hk1_geo.avg + hk2_geo.avg * 2) / 3, 2)
    else:
        avg_geo = None
    if (hk1_GDCD.avg != None and hk2_GDCD.avg != None):
        avg_GDCD = round((hk1_GDCD.avg + hk2_GDCD.avg * 2) / 3, 2)
    else:
        avg_GDCD = None
    if (hk1_liters.avg != None and hk2_liters.avg != None):
        avg_liters = round((hk1_liters.avg + hk2_liters.avg * 2) / 3, 2)
    else:
        avg_liters = None
    if (hk1_PE.avg != None and hk2_PE.avg != None):
        avg_PE = round((hk1_PE.avg + hk2_PE.avg * 2) / 3, 2)
    else:
        avg_PE = None
    if (hk1_DE.avg != None and hk2_DE.avg != None):
        avg_DE = round((hk1_DE.avg + hk2_DE.avg * 2) / 3, 2)
    else:
        avg_DE = None
    if (hk1_tech.avg != None and hk2_tech.avg != None):
        avg_tech = round((hk1_tech.avg + hk2_tech.avg * 2) / 3, 2)
    else:
        avg_tech = None
    if (hk1_computer.avg != None and hk2_computer.avg != None):
        avg_computer = round((hk1_computer.avg + hk2_computer.avg * 2) / 3, 2)
    else:
        avg_computer = None
    if (hk1_languages.avg != None and hk2_languages.avg != None):
        avg_languages = round((hk1_languages.avg + hk2_languages.avg * 2) / 3, 2)
    else:
        avg_languages = None
    if (hk1_major.avg != None and hk2_major.avg != None):
        avg_major = round((hk1_major.avg + hk2_major.avg * 2) / 3, 2)
    else:
        avg_major = None
    #HK1
    context = {'student': student, 'hk1_physics': hk1_physics, 'hk2_physics': hk2_physics,
               'hk1_maths':hk1_maths,'hk2_maths':hk2_maths,'hk1_chemis':hk1_chemis,
               'hk2_chemis':hk2_chemis,'hk1_bio':hk1_bio,'hk2_bio':hk2_bio,'hk1_history':hk1_history,
               'hk2_history':hk2_history,'hk1_geo':hk1_geo,'hk2_geo':hk2_geo,'hk1_GDCD':hk1_GDCD,
               'hk2_GDCD':hk2_GDCD,'hk1_tech':hk1_tech,'hk2_tech':hk2_tech,'hk1_computer':hk1_computer,
               'hk2_computer':hk2_computer,'hk1_languages':hk1_languages,'hk2_languages':hk2_languages,
               'hk1_major':hk1_major,'hk2_major':hk2_major,'hk1_liters':hk1_liters,'hk2_liters':hk2_liters,
               'hk1_DE':hk1_DE,'hk2_DE':hk2_DE,'hk1_PE':hk1_PE,'hk2_PE':hk2_PE,'tar':tar,
               'avg_maths':avg_maths,'avg_physics':avg_physics,'avg_chemis':avg_chemis,'avg_bio':avg_bio,
               'avg_history':avg_history,'avg_geo':avg_geo,'avg_GDCD':avg_GDCD,'avg_liters':avg_liters,'avg_PE':avg_PE,
               'avg_DE':avg_DE,'avg_tech':avg_tech,'avg_computer':avg_computer,'avg_languages':avg_languages,'avg_major':avg_major}
    return render(request, "Students/student_private_result.html",context)

def run_set(name, value, user):
    if value == 'None':
        return
    a = Subjects.objects.get(name=name, alf_user=user, term='1')
    a.target = value
    a.save()
    b = Subjects.objects.get(name=name, alf_user=user, term='2')
    b.target = value
    b.save()
    return

def target_set(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        cnt = 0
        total = 0
        maths = request.POST.get("maths")
        if maths != 'None':
            total = total + float(maths)
            cnt =cnt + 1
        physics = request.POST.get("physics")
        if physics != 'None':
            total = total + float(physics)
            cnt =cnt + 1
        chemis = request.POST.get("chemis")
        if chemis != 'None':
            total = total + float(chemis)
            cnt =cnt + 1
        bio = request.POST.get("bio")
        if bio != 'None':
            total = total + float(bio)
            cnt =cnt + 1
        computer = request.POST.get("computer")
        if computer != 'None':
            total = total + float(computer)
            cnt =cnt + 1
        tech = request.POST.get("tech")
        if tech != 'None':
            total = total + float(tech)
            cnt =cnt + 1
        liters = request.POST.get("liters")
        if liters != 'None':
            total = total + float(liters)
            cnt =cnt + 1
        history = request.POST.get("history")
        if history != 'None':
            total = total + float(history)
            cnt =cnt + 1
        geo = request.POST.get("geo")
        if geo != 'None':
            total = total + float(geo)
            cnt =cnt + 1
        PE = request.POST.get("PE")
        if PE != 'None':
            total = total + float(PE)
            cnt =cnt + 1
        DE = request.POST.get("DE")
        if DE != 'None':
            total = total + float(DE)
            cnt =cnt + 1
        languages = request.POST.get("languages")
        if languages != 'None':
            total = total + float(languages)
            cnt =cnt + 1
        GDCD = request.POST.get("GDCD")
        if GDCD != 'None':
            total = total + float(GDCD)
            cnt =cnt + 1
        major = request.POST.get("major")
        if major != 'None':
            total = total + float(major)
            cnt =cnt + 1
        try:
            run_set("Toán", maths, request.user)
            run_set("Vật Lí", physics, request.user)
            run_set("Hoá Học", chemis, request.user)
            run_set("Sinh Học", bio, request.user)
            run_set("Lịch Sử", history, request.user)
            run_set("Địa Lí", geo, request.user)
            run_set("GDCD", GDCD, request.user)
            run_set("Tin Học", computer, request.user)
            run_set("Công Nghệ", tech, request.user)
            run_set("Thể Dục", PE, request.user)
            run_set("GDQP", DE, request.user)
            run_set("Ngữ Văn", liters, request.user)
            run_set("Ngoại Ngữ", languages, request.user)
            run_set("Môn Chuyên", major, request.user)
            print(total)
            print(cnt)
            if aim.objects.filter(alf_user=request.user).all().count() == 0:
                a = aim(alf_user=request.user)
                a.save()
            a = aim.objects.get(alf_user=request.user)
            tar = round(total/cnt,2)
            if(tar>=9):
                a.Mod = 9
                m="9+"
            elif(tar>=8):
                a.Mod = "8"
                m = "8+"
            elif (tar >= 7):
                a.Mod = "7"
                m = "7+"
            else:
                a.Mod = 6.5
                m = "6.5+"
            a.save()
            messages.success(request,'Đã Cài Đặt Thành Công! Và mục tiêu trung bình của bạn là:'+m)
            return HttpResponseRedirect(reverse("student_private_result"))
        except:
            messages.error(request, "Lỗi!")
            return HttpResponseRedirect(reverse("student_private_result"))
def update_mark_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        sub = request.POST.get("sub_name_get")
        term = request.POST.get("term_get")

        m1 = request.POST.get("m1")
        m2 = request.POST.get("m2")
        m3 = request.POST.get("m3")
        m4 = request.POST.get("m4")
        t1 = request.POST.get("t1")
        final = request.POST.get("final")
        sub = Subjects.objects.get(name=sub, alf_user=request.user, term=term)
        total = 0
        cnt = 0
        if(m1 != ''):
            sub.m1 = m1
            total = total + float(m1)
            cnt+=1
        if (m2 != ''):
            sub.m2 = m2
            total = total + float(m2)
            cnt += 1
        if (m3 != ''):
            sub.m3 = m3
            total = total + float(m3)
            cnt += 1
        if (m4 != ''):
            sub.m4 = m4
            total = total + float(m4)
            cnt += 1
        if (t1 != ''):
            sub.t1 = t1
            total = total + float(t1)*2
            cnt += 2
        if (final != ''):
            sub.final = final
            total = total + float(final)*3
            cnt += 3
        sub.save()
        if(cnt != 0):
            sub.avg = round(total/cnt,2)
            sub.save()
        subjects = Subjects.objects.filter(alf_user=request.user, term=term).all()
        total = 0
        cnt = 0
        for subject in subjects:
            if (subject.avg != None):
                total = total + float(subject.avg)
                cnt += 1
        print(cnt)
        if (cnt != 0):
            tar = aim.objects.get(alf_user=request.user)
            tar.total = round(total / cnt, 2)
            tar.save()
        messages.success(request,"Đã Nhập Điểm " + sub.name + " Thành Công!")
        return HttpResponseRedirect(reverse("student_private_result"))
@csrf_exempt
@csrf_exempt
def get_private_result(request):
    term = request.POST.get("term")
    target = request.POST.get("target")
    student = Students.objects.get(admin=request.user)
    print(type(term))
    #--------------Physiscs-----------------#
    physics = Subjects.objects.get(name="Vật Lí", alf_user=request.user, term=term)
    physics_hk1=Subjects.objects.get(name="Vật Lí", alf_user=request.user, term="1")
    count_physics = 0
    total_physics = 0
    check_physics = 0
    list_physics = []
    list_physics.append(physics.m1)
    list_physics.append(physics.m2)
    list_physics.append(physics.m3)
    list_physics.append(physics.m4)
    for v in list_physics:
        if v is not None:
            total_physics += v
            count_physics += 1
        if v is None:
            check_physics += 1
    if physics.t1 is not None:
        total_physics += physics.t1 * 2
        count_physics += 2
    if physics.final is not None:
        total_physics += physics.final * 3
        count_physics += 3
    tar = physics.target
    if term=="2":
        if physics_hk1.avg is None:
            physics_hk1.avg = 0
            physics_hk1.save()
        tar = (physics.target*3 -physics_hk1.avg)/2
        tar = round(tar,2)
        if tar >10:
            tar=10.0
    print(check_physics)
    print(count_physics)
    if check_physics == 4:
        physics.message="Vật Lí: điểm số đầu tiên đạt tối thiểu " + str(tar)
        physics.save()
    if check_physics!=0 and physics.t1 is None and physics.final is None and count_physics!=0:
        print("ok")
        tmp1 = tar * (count_physics + 1)
        tmp2 = tar * (count_physics + 2)
        n1 = tmp1 - total_physics
        n2 = (tmp2 - total_physics) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        physics.message='Vật Lí: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        physics.save()
    if check_physics !=0 and physics.t1 is not None and physics.final is None:
        tmp1 = tar * (count_physics + 1)
        tmp2 = tar * (count_physics + 3)
        n1 = tmp1 - total_physics
        n1 = round(n1, 2)
        n2 = (tmp2 - total_physics) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        physics.message='Vật Lí: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        physics.save()
    if physics.final is None and check_physics == 0 and physics.t1 is not None:
        tmp1 = tar * (count_physics + 3)
        n1 = (tmp1 - total_physics) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        physics.message= 'Vật Lí: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        physics.save()
    #----------------MATH------------------#
    math = Subjects.objects.get(name="Toán", alf_user=request.user, term=term)
    math_hk1 = Subjects.objects.get(name="Toán", alf_user=request.user, term="1")
    count_math = 0
    total_math  = 0
    check_math = 0
    list_math = []
    list_math.append(math.m1)
    list_math.append(math.m2)
    list_math.append(math.m3)
    list_math.append(math.m4)
    for v in list_math:
        if v is not None:
            total_math += v
            count_math += 1
        if v is None:
            check_math += 1
    if math.t1 is not None:
        total_math += math.t1 * 2
        count_math += 2
    if math.final is not None:
        total_math += math.final * 3
        count_math += 3
    tar = math.target
    if term == "2":
        if math_hk1.avg is None:
            math_hk1.avg = 0
            math_hk1.save()
        tar = (math.target * 3 - math_hk1.avg) / 2
        tar = round(tar, 2)
    if check_math == 4:
        math.message= "Toán: điểm số đầu tiên đạt tối thiểu  " + str(tar)
        math.save()
    if check_math != 0 and math.t1 is None and math.final is None and count_math!=0:
        tmp1 = tar * (count_math + 1)
        tmp2 = tar * (count_math + 2)
        n1 = tmp1 - total_math
        n2 = (tmp2 - total_math) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        math.message='Toán: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        math.save()
    if check_math != 0 and math.t1 is not None and math.final is None:
        tmp1 = tar * (count_math + 1)
        tmp2 = tar * (count_math + 3)
        n1 = tmp1 - total_math
        n1 = round(n1, 2)
        n2 = (tmp2 - total_math) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        math.message ='Toán: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        math.save()
    if math.final is None and check_math == 0 and math.t1 is not None:
        tmp1 = tar * (count_math + 3)
        n1 = (tmp1 - total_math) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        math.message='Toán: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        math.save()
    #------------------chemistry----------#
    chemis = Subjects.objects.get(name="Hoá Học", alf_user=request.user, term=term)
    chemis_hk1=Subjects.objects.get(name="Hoá Học", alf_user=request.user, term="1")
    count_chemis = 0
    total_chemis = 0
    check_chemis = 0
    list_chemis = []
    list_chemis.append(chemis.m1)
    list_chemis.append(chemis.m2)
    list_chemis.append(chemis.m3)
    list_chemis.append(chemis.m4)
    for v in list_chemis:
        if v is not None:
            total_chemis += v
            count_chemis += 1
        if v is None:
            check_chemis+=1
    if chemis.t1 is not None:
        total_chemis += chemis.t1 * 2
        count_chemis += 2
    if chemis.final is not None:
        total_chemis += chemis.final * 3
        count_chemis += 3
    tar = chemis.target
    if term == "2":
        if chemis_hk1.avg is None:
            chemis_hk1.avg = 0
            chemis_hk1.save()
        tar = (chemis.target * 3 - chemis_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_chemis == 4:
        chemis.message="Hóa: điểm số đầu tiên đạt tối thiểu " + str(tar)
        chemis.save()
    if check_chemis != 0 and chemis.t1 is None and chemis.final is None and count_chemis!=0:
        tmp1 = tar * (count_chemis + 1)
        tmp2 = tar * (count_chemis + 2)
        n1 = tmp1 - total_chemis
        n2 = (tmp2 - total_chemis) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        chemis.message= 'Hóa: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        chemis.save()
    if check_chemis != 0 and chemis.t1 is not None and chemis.final is None:
        tmp1 = tar * (count_chemis + 1)
        tmp2 = tar * (count_chemis + 3)
        n1 = tmp1 - total_chemis
        n1 = round(n1, 2)
        n2 = (tmp2 - total_chemis) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        chemis.message='Hóa: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        chemis.save()
    if chemis.final is None and check_chemis == 0 and chemis.t1 is not None:
        tmp1 = tar * (count_chemis + 3)
        n1 = (tmp1 - total_chemis) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        chemis.message='Hóa: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        chemis.save()
    #---------------Bio----------------#
    bio = Subjects.objects.get(name="Sinh Học", alf_user=request.user, term=term)
    bio_hk1 = Subjects.objects.get(name="Hoá Học", alf_user=request.user, term="1")
    count_bio = 0
    total_bio = 0
    check_bio = 0
    list_bio = []
    list_bio.append(bio.m1)
    list_bio.append(bio.m2)
    list_bio.append(bio.m3)
    list_bio.append(bio.m4)
    for v in list_bio:
        if v is not None:
            total_bio += v
            count_bio += 1
        if v is None:
            check_bio += 1
    if bio.t1 is not None:
        total_bio += bio.t1 * 2
        count_bio += 2
    if bio.final is not None:
        total_bio += bio.final * 3
        count_bio += 3
    tar = bio.target
    print(bio_hk1.avg)
    print("bio")
    if term == "2":
        if bio_hk1.avg is None:
            bio_hk1.avg = 0
            bio_hk1.save()
        tar = (bio.target * 3 - bio_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_bio == 4:
        bio.message="Sinh Học: điểm số đầu tiên đạt tối thiểu " + str(tar)
        bio.save()
    if check_bio != 0 and bio.t1 is None and bio.final is None and count_bio != 0:
        tmp1 = tar * (count_bio + 1)
        tmp2 = tar * (count_bio + 2)
        n1 = tmp1 - total_bio
        n2 = (tmp2 - total_bio) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        bio.message='Sinh Học: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        bio.save()
    if check_bio != 0 and bio.t1 is not None and bio.final is None:
        tmp1 = tar * (count_bio + 1)
        tmp2 = tar * (count_bio + 3)
        n1 = tmp1 - total_bio
        n1 = round(n1, 2)
        n2 = (tmp2 - total_bio) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        bio.message='Sinh Học: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        bio.save()
    if bio.final is None and check_bio == 0 and bio.t1 is not None:
        tmp1 = tar * (count_bio + 3)
        n1 = (tmp1 - total_bio) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        bio.message='Sinh học: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        bio.save()
    #--------------------HISTORY--------------#
    ls=Subjects.objects.get(name="Lịch Sử", alf_user=request.user, term=term)
    ls_hk1 = Subjects.objects.get(name="Lịch Sử", alf_user=request.user, term="1")
    count_ls = 0
    total_ls = 0
    check_ls = 0
    list_ls = []
    list_ls.append(ls.m1)
    list_ls.append(ls.m2)
    list_ls.append(ls.m3)
    list_ls.append(ls.m4)
    for v in list_ls:
        if v is not None:
            total_ls += v
            count_ls += 1
        if v is None:
            check_ls += 1
    if ls.t1 is not None:
        total_ls += ls.t1 * 2
        count_ls += 2
    if ls.final is not None:
        total_ls += ls.final * 3
        count_ls += 3
    tar = ls.target
    if term == "2":
        if ls_hk1.avg is None:
            ls_hk1.avg = 0
            ls_hk1.save()
        tar = (ls.target * 3 - ls_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_ls == 4:
        ls.message="Lịch Sử: điểm số đầu tiên đạt tối thiểu " + str(tar)
        ls.save()
    if check_ls != 0 and ls.t1 is None and ls.final is None and count_ls != 0:
        tmp1 = tar * (count_ls + 1)
        tmp2 = tar * (count_ls + 2)
        n1 = tmp1 - total_ls
        n2 = (tmp2 - total_ls) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        ls.message='Lịch Sử: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        ls.save()
    if check_ls != 0 and ls.t1 is not None and ls.final is None:
        tmp1 = tar * (count_ls + 1)
        tmp2 = tar * (count_ls + 3)
        n1 = tmp1 - total_ls
        n1 = round(n1, 2)
        n2 = (tmp2 - total_ls) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        ls.message='Lịch Sử: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        ls.save()
    if ls.final is None and check_ls == 0 and ls.t1 is not None:
        tmp1 = tar * (count_ls + 3)
        n1 = (tmp1 - total_ls) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        ls.message='Lịch Sử: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        ls.save()
    #---------------GEOGRAPHY--------------#
    geo = Subjects.objects.get(name="Địa Lí", alf_user=request.user, term=term)
    geo_hk1 = Subjects.objects.get(name="Địa Lí", alf_user=request.user, term="1")
    count_geo = 0
    total_geo = 0
    check_geo = 0
    list_geo = []
    list_geo.append(geo.m1)
    list_geo.append(geo.m2)
    list_geo.append(geo.m3)
    list_geo.append(geo.m4)
    for v in list_geo:
        if v is not None:
            total_geo += v
            count_geo += 1
        if v is None:
            check_geo += 1
    if geo.t1 is not None:
        total_geo += geo.t1 * 2
        count_geo += 2
    if geo.final is not None:
        total_geo += geo.final * 3
        count_geo += 3
    tar = geo.target
    if term == "2":
        if geo_hk1.avg is None:
            geo_hk1.avg = 0
            geo_hk1.save()
        tar = (geo.target * 3 - geo_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_geo == 4:
        geo.message="Địa Lí: điểm số đầu tiên đạt tối thiểu " + str(tar)
        geo.save()
    if check_geo != 0 and geo.t1 is None and geo.final is None and count_geo != 0:
        tmp1 = tar * (count_geo + 1)
        tmp2 = tar * (count_geo + 2)
        n1 = tmp1 - total_geo
        n2 = (tmp2 - total_geo) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        geo.message='Địa Lí: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        geo.save()
    if check_geo != 0 and geo.t1 is not None and geo.final is None:
        tmp1 = tar * (count_geo + 1)
        tmp2 = tar * (count_geo + 3)
        n1 = tmp1 - total_geo
        n1 = round(n1, 2)
        n2 = (tmp2 - total_geo) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        geo.message='Địa Lí: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        geo.save()
    if geo.final is None and check_geo == 0 and geo.t1 is not None:
        tmp1 = tar * (count_geo + 3)
        n1 = (tmp1 - total_geo) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        geo.message='Địa Lí: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        geo.save()
    #----------------EDU------------------#
    edu = Subjects.objects.get(name="GDCD", alf_user=request.user, term=term)
    edu_hk1 = Subjects.objects.get(name="GDCD", alf_user=request.user, term="1")
    count_edu = 0
    total_edu = 0
    check_edu = 0
    list_edu = []
    list_edu.append(edu.m1)
    list_edu.append(edu.m2)
    list_edu.append(edu.m3)
    list_edu.append(edu.m4)
    for v in list_edu:
        if v is not None:
            total_edu += v
            count_edu += 1
        if v is None:
            check_edu += 1
    if edu.t1 is not None:
        total_edu += edu.t1 * 2
        count_edu += 2
    if edu.final is not None:
        total_edu += edu.final * 3
        count_edu += 3
    tar = edu.target
    if term == "2":
        if edu_hk1.avg is None:
            edu_hk1.avg = 0
            edu_hk1.save()
        tar = (edu.target * 3 - edu_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_edu == 4:
        edu.message="GDCD: điểm số đầu tiên đạt tối thiểu " + str(tar)
        edu.save()
    if check_edu != 0 and edu.t1 is None and edu.final is None and count_edu != 0:
        tmp1 = tar * (count_edu + 1)
        tmp2 = tar * (count_edu + 2)
        n1 = tmp1 - total_edu
        n2 = (tmp2 - total_edu) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        edu.message='GDCD: 15p kế tiếp cần đạt tối thiểu: ' + w1+ ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        edu.save()
    if check_edu != 0 and edu.t1 is not None and edu.final is None:
        tmp1 = tar * (count_edu + 1)
        tmp2 = tar * (count_edu + 3)
        n1 = tmp1 - total_edu
        n1 = round(n1, 2)
        n2 = (tmp2 - total_edu) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        edu.message='GDCD: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        edu.save()
    if edu.final is None and check_edu == 0 and edu.t1 is not None:
        tmp1 = tar * (count_edu + 3)
        n1 = (tmp1 - total_edu) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        edu.message='GDCD: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        edu.save()
    #-------------Literature---------#
    liter = Subjects.objects.get(name="Ngữ Văn", alf_user=request.user, term=term)
    liter_hk1 = Subjects.objects.get(name="Ngữ Văn", alf_user=request.user, term="1")
    count_liter = 0
    total_liter = 0
    check_liter = 0
    list_liter = []
    list_liter.append(liter.m1)
    list_liter.append(liter.m2)
    list_liter.append(liter.m3)
    list_liter.append(liter.m4)
    for v in list_liter:
        if v is not None:
            total_liter += v
            count_liter += 1
        if v is None:
            check_liter += 1
    if liter.t1 is not None:
        total_liter += liter.t1 * 2
        count_liter += 2
    if liter.final is not None:
        total_liter += liter.final * 3
        count_liter += 3
    tar = liter.target
    if term == "2":
        if liter_hk1.avg is None:
            liter_hk1.avg = 0
            liter_hk1.save()
        tar = (liter.target * 3 - liter_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_liter == 4:
        liter.message="Ngữ Văn: điểm số đầu tiên đạt tối thiểu " + str(tar)
        liter.save()
    if check_liter != 0 and liter.t1 is None and liter.final is None and count_liter != 0:
        tmp1 = tar * (count_liter + 1)
        tmp2 = tar * (count_liter + 2)
        n1 = tmp1 - total_liter
        n2 = (tmp2 - total_liter) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        liter.message='Ngữ Văn: 15p kế tiếp cần đạt tối thiểu: ' + w1+ ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        liter.save()
    if check_liter != 0 and liter.t1 is not None and liter.final is None:
        tmp1 = tar * (count_liter + 1)
        tmp2 = tar * (count_liter + 3)
        n1 = tmp1 - total_liter
        n1 = round(n1, 2)
        n2 = (tmp2 - total_liter) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        liter.message='Ngữ Văn: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        liter.save()
    if liter.final is None and check_liter == 0 and liter.t1 is not None:
        tmp1 = tar * (count_liter + 3)
        n1 = (tmp1 - total_liter) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        liter.message='Ngữ Văn: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        liter.save()
    #------------------IT--------------#
    it = Subjects.objects.get(name="Tin Học", alf_user=request.user, term=term)
    it_hk1 = Subjects.objects.get(name="Tin Học", alf_user=request.user, term="1")
    count_it = 0
    total_it = 0
    check_it = 0
    list_it = []
    list_it.append(it.m1)
    list_it.append(it.m2)
    list_it.append(it.m3)
    list_it.append(it.m4)
    for v in list_it:
        if v is not None:
            total_it += v
            count_it += 1
        if v is None:
            check_it += 1
    if it.t1 is not None:
        total_it += it.t1 * 2
        count_it += 2
    if it.final is not None:
        total_it += it.final * 3
        count_it += 3
    tar = it.target
    if term == "2":
        if it_hk1.avg is None:
            it_hk1.avg = 0
            it_hk1.save()
        tar = (it.target * 3 - it_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_it == 4:
        it.message="Tin Học: điểm số đầu tiên đạt tối thiểu " + str(tar)
        it.save()
    if check_it != 0 and it.t1 is None and it.final is None and count_it != 0:
        tmp1 = tar * (count_it + 1)
        tmp2 = tar * (count_it + 2)
        n1 = tmp1 - total_it
        n2 = (tmp2 - total_it) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        it.message='Tin Học: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        it.save()
    if check_it != 0 and it.t1 is not None and it.final is None:
        tmp1 = tar * (count_it + 1)
        tmp2 = tar * (count_it + 3)
        n1 = tmp1 - total_it
        n1 = round(n1, 2)
        n2 = (tmp2 - total_it) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        it.message='Tin Học: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        it.save()
    if it.final is None and check_it == 0 and it.t1 is not None:
        tmp1 = tar * (count_it + 3)
        n1 = (tmp1 - total_it) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        it.message='Tin Học: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        it.save()
    #--------------------------CN-----------#
    cn = Subjects.objects.get(name="Công Nghệ", alf_user=request.user, term=term)
    cn_hk1 = Subjects.objects.get(name="Công Nghệ", alf_user=request.user, term="1")
    count_cn = 0
    total_cn = 0
    check_cn = 0
    list_cn = []
    list_cn.append(cn.m1)
    list_cn.append(cn.m2)
    list_cn.append(cn.m3)
    list_cn.append(cn.m4)
    for v in list_cn:
        if v is not None:
            total_cn += v
            count_cn += 1
        if v is None:
            check_cn += 1
    if cn.t1 is not None:
        total_cn += cn.t1 * 2
        count_cn += 2
    if cn.final is not None:
        total_cn += cn.final * 3
        count_cn += 3
    tar = cn.target
    if term == "2":
        if cn_hk1.avg is None:
            cn_hk1.avg = 0
            cn_hk1.save()
        tar = (cn.target * 3 - cn_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_cn == 4:
        cn.message="Công Nghệ: điểm số đầu tiên đạt tối thiểu " + str(tar)
        cn.save()
    if check_cn != 0 and cn.t1 is None and cn.final is None and count_cn != 0:
        tmp1 = tar * (count_cn + 1)
        tmp2 = tar * (count_cn + 2)
        n1 = tmp1 - total_cn
        n2 = (tmp2 - total_cn) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        cn.message='Công Nghệ: 15p kế tiếp cần đạt tối thiểu: ' + w1+ ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        cn.save()
    if check_cn != 0 and cn.t1 is not None and cn.final is None:
        tmp1 = tar * (count_cn + 1)
        tmp2 = tar * (count_cn + 3)
        n1 = tmp1 - total_cn
        n1 = round(n1, 2)
        n2 = (tmp2 - total_cn) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        cn.message='Công Nghệ: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        cn.save()
    if cn.final is None and check_cn == 0 and cn.t1 is not None:
        tmp1 = tar * (count_cn + 3)
        n1 = (tmp1 - total_cn) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        cn.message='Công Nghệ: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        cn.save()
    #--------------EXERCISE--------#
    td = Subjects.objects.get(name="Thể Dục", alf_user=request.user, term=term)
    td_hk1 = Subjects.objects.get(name="Thể Dục", alf_user=request.user, term="1")
    count_td = 0
    total_td = 0
    check_td = 0
    list_td = []
    list_td.append(td.m1)
    list_td.append(td.m2)
    list_td.append(td.m3)
    list_td.append(td.m4)
    for v in list_td:
        if v is not None:
            total_td += v
            count_td += 1
        if v is None:
            check_td += 1
    if td.t1 is not None:
        total_td += td.t1 * 2
        count_td += 2
    if td.final is not None:
        total_td += td.final * 3
        count_td += 3
    tar = td.target
    if term == "2":
        if td_hk1.avg is None:
            td_hk1.avg = 0
            td_hk1.save()
        tar = (td.target * 3 - td_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_td == 4:
        td.message="Thể Dục: điểm số đầu tiên đạt tối thiểu " + str(tar)
        td.save()
    if check_td != 0 and td.t1 is None and td.final is None and count_td != 0:
        tmp1 = tar * (count_td + 1)
        tmp2 = tar * (count_td + 2)
        n1 = tmp1 - total_td
        n2 = (tmp2 - total_td) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        td.message='Thể Dục: 15p kế tiếp cần đạt tối thiểu: ' + w1+ ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        td.save()
    if check_td != 0 and td.t1 is not None and td.final is None:
        tmp1 = tar * (count_td + 1)
        tmp2 = tar * (count_td + 3)
        n1 = tmp1 - total_td
        n1 = round(n1, 2)
        n2 = (tmp2 - total_td) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        td.message='Thể Dục: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        td.save()
    if td.final is None and check_td == 0 and td.t1 is not None:
        tmp1 = tar * (count_td + 3)
        n1 = (tmp1 - total_td) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        td.message='Thể Dục: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        td.save()
    #----------------GDQP-------#
    de = Subjects.objects.get(name="GDQP", alf_user=request.user, term=term)
    de_hk1 = Subjects.objects.get(name="GDQP", alf_user=request.user, term="1")
    count_de = 0
    total_de = 0
    check_de = 0
    list_de = []
    list_de.append(de.m1)
    list_de.append(de.m2)
    list_de.append(de.m3)
    list_de.append(de.m4)
    for v in list_de:
        if v is not None:
            total_de += v
            count_de += 1
        if v is None:
            check_de += 1
    if de.t1 is not None:
        total_de += de.t1 * 2
        count_de += 2
    if de.final is not None:
        total_de += de.final * 3
        count_de += 3
    tar = de.target
    if term == "2":
        if de_hk1.avg is None:
            de_hk1.avg = 0
            de_hk1.save()
        tar = (de.target * 3 - de_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_de == 4:
        de.message="GDQP: điểm số đầu tiên đạt tối thiểu " + str(tar)
        de.save()
    if check_de != 0 and de.t1 is None and de.final is None and count_de != 0:
        tmp1 = tar * (count_de + 1)
        tmp2 = tar * (count_de + 2)
        n1 = tmp1 - total_de
        n2 = (tmp2 - total_de) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        de.message='GDQP: 15p kế tiếp cần đạt tối thiểu: ' + w1+ ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        de.save()
    if check_de != 0 and de.t1 is not None and de.final is None:
        tmp1 = tar * (count_de + 1)
        tmp2 = tar * (count_de + 3)
        n1 = tmp1 - total_de
        n1 = round(n1, 2)
        n2 = (tmp2 - total_de) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        td.message='GDQP: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        td.save()
    if de.final is None and check_de == 0 and de.t1 is not None:
        tmp1 = tar * (count_de + 3)
        n1 = (tmp1 - total_de) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        td.message='GDQP: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        td.save()
    #---------------language--------#
    lang = Subjects.objects.get(name="Ngoại Ngữ", alf_user=request.user, term=term)
    lang_hk1 = Subjects.objects.get(name="Ngoại Ngữ", alf_user=request.user, term="1")
    count_lang = 0
    total_lang = 0
    check_lang = 0
    list_lang = []
    list_lang.append(lang.m1)
    list_lang.append(lang.m2)
    list_lang.append(lang.m3)
    list_lang.append(lang.m4)
    for v in list_lang:
        if v is not None:
            total_lang += v
            count_lang += 1
        if v is None:
            check_lang += 1
    if lang.t1 is not None:
        total_lang += lang.t1 * 2
        count_lang += 2
    if lang.final is not None:
        total_lang += lang.final * 3
        count_lang += 3
    tar = lang.target
    if term == "2":
        if lang_hk1.avg is None:
            lang_hk1.avg = 0
            lang_hk1.save()
        tar = (lang.target * 3 - lang_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_lang == 4:
        lang.message="Ngoại Ngữ: điểm số đầu tiên đạt tối thiểu " + str(tar)
        lang.save()
    if check_lang != 0 and lang.t1 is None and lang.final is None and count_lang != 0:
        tmp1 = tar * (count_lang + 1)
        tmp2 = tar * (count_lang + 2)
        n1 = tmp1 - total_lang
        n2 = (tmp2 - total_lang) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        lang.message='Ngoại Ngữ: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        lang.save()
    if check_lang != 0 and lang.t1 is not None and lang.final is None:
        tmp1 = tar * (count_lang + 1)
        tmp2 = tar * (count_lang + 3)
        n1 = tmp1 - total_lang
        n1 = round(n1, 2)
        n2 = (tmp2 - total_lang) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        lang.message='Ngoại Ngữ: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        lang.save()
    if lang.final is None and check_lang == 0 and lang.t1 is not None:
        tmp1 = tar * (count_lang + 3)
        n1 = (tmp1 - total_lang) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        lang.message='Ngoại Ngữ: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        lang.save()
    #--------------MAJOR--------------#
    major = Subjects.objects.get(name="Môn Chuyên", alf_user=request.user, term=term)
    major_hk1 = Subjects.objects.get(name="Môn Chuyên", alf_user=request.user, term="1")
    count_major = 0
    total_major = 0
    check_major = 0
    list_major = []
    list_major.append(major.m1)
    list_major.append(major.m2)
    list_major.append(major.m3)
    list_major.append(major.m4)
    for v in list_major:
        if v is not None:
            total_major += v
            count_major += 1
        if v is None:
            check_major += 1
    if major.t1 is not None:
        total_major += major.t1 * 2
        count_major += 2
    if major.final is not None:
        total_major += major.final * 3
        count_major += 3
    tar = major.target
    if term == "2":
        if major_hk1.avg is None:
            major_hk1.avg = 0
            major_hk1.save()
        tar = (major.target * 3 - major_hk1.avg) / 2
        tar = round(tar, 2)
        if tar > 10:
            tar = 10.0
    if check_major == 4:
        major.message="Môn Chuyên: " + str(tar)
        major.save()
    if check_major != 0 and major.t1 is None and major.final is None and count_major != 0:
        tmp1 = tar * (count_major + 1)
        tmp2 = tar * (count_major + 2)
        n1 = tmp1 - total_major
        n2 = (tmp2 - total_major) / 2
        n1 = round(n1, 2)
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        major.message='Môn Chuyên: 15p kế tiếp cần đạt tối thiểu: ' + w1+ ' | 1 tiết đạt tối thiểu: ' + w2 + ' ' + st
        major.save()
    if check_major != 0 and major.t1 is not None and major.final is None:
        tmp1 = tar * (count_major + 1)
        tmp2 = tar * (count_major + 3)
        n1 = tmp1 - total_major
        n1 = round(n1, 2)
        n2 = (tmp2 - total_major) / 3
        n2 = round(n2, 2)
        w1 = str(n1)
        w2 = str(n2)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        if n2 > 10:
            w2 = '10'
            st = " và cần cải thiện điểm số"
        major.message='Môn Chuyên: 15p kế tiếp cần đạt tối thiểu: ' + w1 + ' | điểm thi đạt tối thiểu: ' + w2 + ' ' + st
        major.save()
    if major.final is None and check_major == 0 and major.t1 is not None:
        tmp1 = tar * (count_major + 3)
        n1 = (tmp1 - total_major) / 3
        n1 = round(n1, 2)
        w1 = str(n1)
        st = ""
        if n1 > 10:
            w1 = '10'
            st = "và cần cải thiện điểm số"
        major.message='Môn Chuyên: điểm thi cần đạt tối thiểu: ' + w1 + ' ' + st
        major.save()
    return HttpResponse(term)    #--------------Physiscs-----------------#

    return HttpResponse(term)
# --------------------------------Subject-------------------------------#

def exam_list(request):
    student = Students.objects.get(admin=request.user.id)
    exams = Exam.objects.filter(class_id=student.class_id).all()
    now_time = datetime.now()
    t = now_time.time()
    now = now_time.date()
    warning = -1
    exams_info = []
    for exam in exams:
        if (Exam_student.objects.filter(student=student, exam=exam).all().count() == 0):
            stn_exam = Exam_student(student=student, exam=exam, is_active=-1)
            stn_exam.save()
        else:
            stn_exam = Exam_student.objects.get(student=student, exam=exam)
        per = 0
        if(stn_exam.sum>0):
            per = stn_exam.sum/10*100

        exams_info.append({'exam':exam,'stn_exam':stn_exam,'per':per})
    return render(request, "Students/exam_list.html",
                  {'exams_info': exams_info,'now':now,'time':t,'stn_id':student.id,'warning':warning})

def start_exam(request,exam_id,stn_id):
    student = Students.objects.get(id=stn_id)
    exam = Exam.objects.get(id=exam_id)

    if(Exam_student.objects.filter(student=student, exam=exam).all().count()  == 0):
        stn_exam = Exam_student(student=student, exam=exam, is_active=-1)
        stn_exam.save()
    else:
        stn_exam = Exam_student.objects.get(student=student, exam=exam)

    if (stn_exam.finish == True):
        return HttpResponseRedirect(reverse("finish_exam", kwargs={'exam_id': exam_id}))

    now_time = datetime.now()
    now = now_time.date()
    if(now == exam.date):
        t = now_time.time()
        if(t < exam.end):
            duration = datetime.combine(date.min, exam.end) - datetime.combine(date.min, t)
            d = duration.seconds
        else:
            exam.is_active = False
            d=0
    else:
        exam.is_active = False
        d = 0

    for i in range(int(exam.number_q)):
        i = i+1
        if(Answer_student.objects.filter(exam=stn_exam, ques_num =i).all().count()==0):
            ans = Answer_student(exam=stn_exam, ques_num =i)
            ans.save()
    ques = Answer_student.objects.filter(exam=stn_exam)

    return render(request, "Students/start_exam.html",
                  {'exam_id': exam_id,'stn_exam':stn_exam,'d':d,'ques':ques,'exam':exam})

def finish_exam(request, exam_id):

    exam = Exam.objects.get(id=exam_id)
    student = Students.objects.get(admin=request.user.id)
    stn_exam = Exam_student.objects.get(student=student, exam=exam)
    per =0
    list_ans = []
    if (stn_exam.sum > 0):
        per = stn_exam.sum / 10 * 100

    for i in range(int(exam.number_q)):
        i = i + 1
        stn_ans = Answer_student.objects.get(exam=stn_exam, ques_num=i)
        res = Answer.objects.get(ques_num=i, ques=exam)
        list_ans.append({'stt': i, 'ans': stn_ans.stn_ans_TN,'bool':stn_ans.bool,'res':res.is_true})

    return render(request, "Students/finish_exam.html",
                  {'stn_exam': stn_exam, 'exam':exam,'list_ans':list_ans,'per':per,'student':student})

@csrf_exempt
def change_warning(request):
    cnt=request.POST.get("cnt")
    id = request.POST.get("id")
    stn_exam = Exam_student.objects.get(id=id)
    stn_exam.is_active = cnt
    stn_exam.save()
    return HttpResponse(cnt)

def save_answer_student(request, exam_id):
    d = 0
    exam = Exam.objects.get(id=exam_id)
    student = Students.objects.get(admin=request.user.id)
    stn_exam = Exam_student.objects.get(student=student, exam=exam)

    if(stn_exam.finish == True):
        return HttpResponseRedirect(reverse("finish_exam", kwargs={'exam_id': exam_id}))
    timeleft = request.POST.get("timel")
    hour = int(int(timeleft)/3600)
    min = int((int(timeleft)%3600)/60)
    sec = int((int(timeleft)%3600)%60)
    if(hour > 0):
        stn_exam.time_finish = str(hour) + " giờ "
    if (min > 0):
        stn_exam.time_finish = str(min) + " phút "
    if (sec > 0):
        stn_exam.time_finish = str(sec) + " giây "
    stn_exam.save()
    for i in range(int(exam.number_q)):
        i = i + 1
        ans = request.POST.get(str(i))
        res = Answer.objects.get(ques_num=i, ques=exam)
        stn_ans = Answer_student.objects.get(exam=stn_exam, ques_num=i)
        if(exam.form == "TN"):
            stn_ans.stn_ans_TN = ans
            if(ans == res.is_true):
                stn_ans.bool=True
                stn_exam.sum+=round(res.mark,2)
            stn_ans.save()
    stn_id = student.id
    stn_exam.finish = True
    stn_exam.save()
    return HttpResponseRedirect(reverse("finish_exam", kwargs={'exam_id': exam_id}))

