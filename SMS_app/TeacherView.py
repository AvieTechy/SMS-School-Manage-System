import json
from datetime import datetime
from uuid import uuid4

from django.contrib import messages
from django.core import serializers
from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage, default_storage
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import SelectYearForm, Upload
from .models import SessionYearModel, Students, Attendance, AttendanceReport, \
    LeaveReportTeacher, Teachers, FeedBackTeacher, CustomUser, Classes, NotificationTeacher, OnlineClassRoom, \
    SubjectsTeacher, LessonTimeSet, \
    Timetable, Exam, Answer, Exam_student

list_mor= []
list_aft= []
def set_list():
    for i in range(35):
        list_mor.append("")
    for i in range(21):
        list_aft.append("")
    return
def create_timetable_mor(teacher_id, class_id):
    teacher = CustomUser.objects.get(id=teacher_id)
    classe = Classes.objects.get(id=class_id)
    i=0
    #time = Timetable.objects.filter(teacher = teacher, class_id=classe).all()
    t=Timetable.objects.filter(teacher=teacher, class_id=classe, name='l1_2').all()
    if (t.count()>0):
        t =Timetable.objects.get(teacher=teacher, class_id=classe, name='l1_2')
        list_mor[i]=t
    i+=1
    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l1_3').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l1_3')
        list_mor[i]=t
    i += 1
    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l1_4').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l1_4')
        list_mor[i]=t
    i += 1
    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l1_5').all()
    if(t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l1_5')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l1_6').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l1_6')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l1_7').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l1_7')
        list_mor[i]=t
    i += 1
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l2_2').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l2_2')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l2_3').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l2_3')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l2_4').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l2_4')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l2_5').all()
    if(t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l2_5')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l2_6').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l2_6')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l2_7').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l2_7')
        list_mor[i]=t
    i += 1
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l3_2').all()

    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l3_2')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l3_3').all()
    if (t.count()>0):

        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l3_3')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l3_4').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l3_4')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l3_5').all()
    if(t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l3_5')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l3_6').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l3_6')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l3_7').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l3_7')
        list_mor[i]=t
    i += 1
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l4_2').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l4_2')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l4_3').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l4_3')
        list_mor[i]=t
    i += 1
    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l4_4').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l4_4')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l4_5').all()
    if(t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l4_5')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l4_6').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l4_6')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l4_7').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l4_7')
        list_mor[i]=t
    i += 1
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l5_2').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l5_2')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l5_3').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l5_3')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l5_4').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l5_4')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l5_5').all()
    if(t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l5_5')
        list_mor[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l5_6').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l5_6')
        list_mor[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l5_7').all()
    if (t.count()>0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l5_7')
        list_mor[i]=t
    i += 1


    return list_mor
def create_timetable_aft(teacher_id, class_id):
    teacher = CustomUser.objects.get(id=teacher_id)
    classe = Classes.objects.get(id=class_id)
    # time = Timetable.objects.filter(teacher = teacher, class_id=classe).all()
    i = 0
    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l6_2').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l6_2')
        list_aft[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l6_3').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l6_3')
        list_aft[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l6_4').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l6_4')
        list_aft[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l6_5').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l6_5')
        list_aft[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l6_6').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l6_6')
        list_aft[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l6_7').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l6_7')
        list_aft[i]=t
    i += 1
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l7_2').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l7_2')
        list_aft[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l7_3').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l7_3')
        list_aft[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l7_4').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l7_4')
        list_aft[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l7_5').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l7_5')
        list_aft[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l7_6').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l7_6')
        list_aft[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l7_7').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l7_7')
        list_aft[i]=t
    i += 1
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l8_2').all()

    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l8_2')
        list_aft[i]=t
    i += 1

    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l8_3').all()
    if (t.count() > 0):

        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l8_3')
        list_aft[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l8_4').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l8_4')
        list_aft[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l8_5').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l8_5')
        list_aft[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l8_6').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l8_6')
        list_aft[i]=t
    i += 1


    t = Timetable.objects.filter(teacher=teacher, class_id=classe, name='l8_7').all()
    if (t.count() > 0):
        t = Timetable.objects.get(teacher=teacher, class_id=classe, name='l8_7')
        list_aft[i]=t
    i += 1

    return list_aft
def teacher_home(request,session):
    #For Fetch All Student Under Staff
    user = CustomUser.objects.get(id=request.user.id)
    teacher = Teachers.objects.get(admin=user)
    Session = SessionYearModel.object.get(id=session)
    if(Classes.objects.filter(GVCN=request.user.id, year=Session).all().count()>0):
        CN=Classes.objects.get(GVCN=request.user.id, year=Session).class_name
    else:
        CN = "-"
    lts_mor = LessonTimeSet.objects.filter(session=Session, time="mor").all()
    lts_aft = LessonTimeSet.objects.filter(session=Session, time="aft").all()
    classes_cnt = 0
    timetable_mor = []
    timetable_aft = []
    set_list()
    if(teacher.major == "Toán"):
        classes = Classes.objects.filter(year=Session,maths_name_id=request.user.id).all()
        class_list = []

        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id,classe.id)
            timetable_aft = create_timetable_aft(request.user.id,classe.id)
        classes_cnt = Classes.objects.filter(year=Session,maths_name_id=request.user.id).count()
    if (teacher.major == "Lí"):
        classes = Classes.objects.filter(year=Session, physics_name_id=request.user.id).all()
        class_list = []
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)
        classes_cnt = Classes.objects.filter(year=Session, physics_name_id=request.user.id).count()
    if (teacher.major == "Hoá Học"):
        classes = Classes.objects.filter(year=Session, chemis_name_id=request.user.id).all()
        class_list = []
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)
        classes_cnt = Classes.objects.filter(year=Session, chemis_name_id=request.user.id).count()
    if (teacher.major == "Sinh"):
        classes = Classes.objects.filter(year=Session, bio_name_id=request.user.id).all()
        class_list = []
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)
        classes_cnt = Classes.objects.filter(year=Session, bio_name_id=request.user.id).count()
    if (teacher.major == "Tin Học-Công Nghệ"):
        class_list = []
        classes = Classes.objects.filter(year=Session, computer_name_id=request.user.id).all()
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)

        classes = Classes.objects.filter(year=Session, tech_name_id=request.user.id).all()
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)

        classes_cnt = Classes.objects.filter(year=Session, computer_name_id=request.user.id).count()+Classes.objects.filter(year=Session, tech_name_id=request.user.id).count()

    if (teacher.major == "Văn"):
        classes = Classes.objects.filter(year=Session, liters_name_id=request.user.id).all()
        class_list = []
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)
        classes_cnt = Classes.objects.filter(year=Session, liters_name_id=request.user.id).count()
    if (teacher.major == "Sử-Địa-GDCD"):
        class_list = []
        classes = Classes.objects.filter(year=Session, history_name_id=request.user.id).all()
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)

        classes = Classes.objects.filter(year=Session, geo_name_id=request.user.id).all()
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)

        classes = Classes.objects.filter(year=Session, GDCD_name_id=request.user.id).all()
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)

        classes_cnt = Classes.objects.filter(year=Session, history_name_id=request.user.id).count()+Classes.objects.filter(year=Session, geo_name_id=request.user.id).count()+Classes.objects.filter(year=Session, GDCD_name_id=request.user.id).count()

    if (teacher.major == "TD-QPAN"):
        class_list = []
        classes = Classes.objects.filter(year=Session, PE_name_id=request.user.id).all()
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)
        classes = Classes.objects.filter(year=Session, DE_name_id=request.user.id).all()
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)

        classes_cnt = Classes.objects.filter(year=Session, PE_name_id=request.user.id).count()+Classes.objects.filter(year=Session, DE_name_id=request.user.id).count()
    if (teacher.major == "Ngoại Ngữ"):
        classes = Classes.objects.filter(year=Session, languages_name_id=request.user.id).all()
        class_list = []
        for classe in classes:
            class_list.append(classe.id)
            timetable_mor = create_timetable_mor(request.user.id, classe.id)
            timetable_aft = create_timetable_aft(request.user.id, classe.id)
        classes_cnt = Classes.objects.filter(year=Session, languages_name_id=request.user.id).count()


    return render(request,"Teachers/teacher_home.html",{"classes_cnt":classes_cnt, "CN":CN, "id":session,
                                                        'lts_mor':lts_mor,'lts_aft':lts_aft,"timetable_aft":timetable_aft, 'timetable_mor':timetable_mor})

def select_year_teacher(request):
    session_list = SessionYearModel.object.all()
    return render(request,"Teachers/select_year_teacher.html",{"session_list":session_list})

def select_year_teacher_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        session = request.POST.get("session")
        try:
            return HttpResponseRedirect(reverse("teacher_home", kwargs={"session": session}))
        except:
            messages.error(request, "Lỗi!")
            return HttpResponseRedirect(reverse("select_year_teacher"))

def teacher_take_attendance(request,session):
    Session = SessionYearModel.object.get(id=session)
    class_list = []
    classes = Classes.objects.filter(year=Session, maths_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, physics_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, chemis_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, bio_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, history_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, geo_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, GDCD_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, PE_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, DE_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, computer_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, tech_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, languages_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, major_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, liters_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    session_years=SessionYearModel.object.all()
    return render(request,"Teachers/teacher_take_attendance.html",{"class_list":class_list,"session_years":session_years,'id':session})

@csrf_exempt
def get_students(request):
    class_id=request.POST.get("classe")
    print(class_id)
    classe=Classes.objects.get(id=class_id)
    students=Students.objects.filter(class_id=classe.id)
    list_data=[]

    for student in students:
        data_small={"id":student.admin.id,"name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_attendance_data(request):
    student_ids=request.POST.get("student_ids")
    class_id=request.POST.get("class_id")
    attendance_date=request.POST.get("attendance_date")
      #subject_model=Subjects.objects.get(id=subject_id)
    classe = Classes.objects.get(id=class_id)
    print(classe)
    json_sstudent=json.loads(student_ids)
    #print(data[0]['id'])

    try:
        user = CustomUser.objects.get(id=request.user.id)
        teacher = Teachers.objects.get(admin=user)
        print(user)
        print(attendance_date)


        attendance=Attendance(GVMB_id=teacher,attendance_date=attendance_date,class_id=classe)
        print("save")
        attendance.save()
        print("save")
        print(attendance)
        for stud in json_sstudent:
             student=Students.objects.get(admin=stud['id'])
             attendance_report=AttendanceReport(student_id=student,attendance_id=attendance,status=stud['status'])

             attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Lỗi")

def teacher_update_attendance(request,session):
    Session = SessionYearModel.object.get(id=session)
    class_list = []
    classes = Classes.objects.filter(year=Session, maths_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, physics_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, chemis_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, bio_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, history_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, geo_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, GDCD_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, PE_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, DE_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, computer_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, tech_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, languages_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, major_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, liters_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    return render(request,"Teachers/teacher_update_attendance.html",{"class_list":class_list,'id':session})

@csrf_exempt
def get_attendance_dates(request):
    classe=request.POST.get("classe")
    classe_obj=Classes.objects.get(id=classe)
    attendance=Attendance.objects.filter(class_id=classe_obj,GVMB_id=request.user.teachers)
    attendance_obj=[]
    for attendance_single in attendance:
        data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date)}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj),safe=False)

@csrf_exempt
def get_attendance_student(request):
    attendance_date=request.POST.get("attendance_date")
    attendance=Attendance.objects.get(id=attendance_date)

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
    list_data=[]

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_updateattendance_data(request):
    student_ids=request.POST.get("student_ids")
    attendance_date=request.POST.get("attendance_date")
    print(attendance_date)
    attendance=Attendance.objects.get(id=attendance_date)

    json_sstudent=json.loads(student_ids)
    try:
        for stud in json_sstudent:
             student=Students.objects.get(admin=stud['id'])
             attendance_report=AttendanceReport.objects.get(student_id=student,attendance_id=attendance)
             attendance_report.status=stud['status']
             attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Lỗi")

def teacher_apply_leave(request,session):
    teacher_obj = Teachers.objects.get(admin=request.user.id)
    leave_data=LeaveReportTeacher.objects.filter(teacher_id=teacher_obj)
    return render(request,"Teachers/teacher_apply_leave.html",{"leave_data":leave_data,'id':session})

def teacher_apply_leave_save(request,session):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("teacher_apply_leave" ,kwargs={'session':session}))
    else:
        leave_date=request.POST.get("leave_date")
        leave_msg=request.POST.get("leave_msg")

        teacher_obj=Teachers.objects.get(admin=request.user.id)
        try:
            leave_report=LeaveReportTeacher(teacher_id=teacher_obj,leave_date=leave_date,leave_message=leave_msg,leave_status=0)
            leave_report.save()
            messages.success(request, "Đã Gửi Thành Công")
            return HttpResponseRedirect(reverse("teacher_apply_leave",kwargs={'session':session}))
        except:
            messages.error(request, "Lỗi! Không Gửi Được")
            return HttpResponseRedirect(reverse("teacher_apply_leave",kwargs={'session':session}))


def teacher_feedback(request,session):
    teacher_id=Teachers.objects.get(admin=request.user.id)
    feedback_data=FeedBackTeacher.objects.filter(teacher_id=teacher_id)
    return render(request,"Teachers/teacher_feedback.html",{"feedback_data":feedback_data,'id':session})

def teacher_feedback_save(request,session):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("teacher_feedback", kwargs={'session':session}))
    else:
        feedback_msg=request.POST.get("feedback_msg")

        teacher_obj=Teachers.objects.get(admin=request.user.id)
        try:
            feedback=FeedBackTeacher(teacher_id=teacher_obj,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request, "Đã Gửi Thành Công")
            return HttpResponseRedirect(reverse("teacher_feedback",kwargs={'session':session}))
        except:
            messages.error(request, "Lỗi! Không Gửi Được")
            return HttpResponseRedirect(reverse("teacher_feedback",kwargs={'session':session}))

def teacher_profile(request,session):

    user=CustomUser.objects.get(id=request.user.id)
    teacher=Teachers.objects.get(admin=user)
    return render(request,"Teachers/teacher_profile.html",{"user":user,"teacher":teacher, 'id':session})

def teacher_profile_save(request,session):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("teacher_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        phone = request.POST.get("phone")
        address=request.POST.get("address")
        password=request.POST.get("password")

        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            teacher=Teachers.objects.get(admin=customuser.id)
            teacher.address=address
            teacher.phone = phone
            teacher.save()
            messages.success(request, "Đã Cập Nhật Hồ Sơ")
            return HttpResponseRedirect(reverse("teacher_profile",kwargs={'session':session}))
        except:
            messages.error(request, "Lỗi! Không Cập Nhật được Hồ Sơ ")
            return HttpResponseRedirect(reverse("teacher_profile",kwargs={'session':session}))

@csrf_exempt
def staff_fcmtoken_save(request):
    return HttpResponse("ok")

    # token=request.POST.get("token")
    # try:
    #     teacher=Teachers.objects.get(admin=request.user.id)
    #     teacher.fcm_token=token
    #     teacher.save()
    #     return HttpResponse("True")
    # except:
    #     return HttpResponse("False")

def teacher_all_notification(request,session):
    teacher=Teachers.objects.get(admin=request.user.id)
    notifications=NotificationTeacher.objects.filter(teacher_id=teacher.id)
    return render(request,"Teachers/all_notification.html",{"notifications":notifications,'id':session})
def check_subject(id,class_id,Session):
    class_obj = Classes.objects.get(id=class_id, year=Session)
    if (str(class_obj.maths_name_id) == str(id)):
        subject = "Toán"
    elif (str(class_obj.physics_name_id) == str(id)):
        subject = "Vật Lí"
    elif (str(class_obj.chemis_name_id) == str(id)):
        subject = "Hoá Học"
    elif (str(class_obj.bio_name_id) == str(id)):
        subject = "Sinh Học"
    elif (str(class_obj.history_name_id) == str(id)):
        subject = "Lịch Sử"
    elif (str(class_obj.geo_name_id) == str(id)):
        subject = "Địa Lí"
    elif (str(class_obj.GDCD_name_id) == str(id)):
        subject = "GDCD"
    elif (str(class_obj.liters_name_id) == str(id)):
        subject = "Ngữ Văn"
    elif (str(class_obj.PE_name_id) == str(id)):
        subject = "Thể Dục"
    elif (str(class_obj.DE_name_id) == str(id)):
        subject = "GDQP"
    elif (str(class_obj.languages_name_id) == str(id)):
        subject = "Ngoại Ngữ"
    elif (str(class_obj.computer_name_id) == str(id)):
        subject = "Tin Học"
    elif (str(class_obj.tech_name_id) == str(id)):
        subject = "Công Nghệ"
    else:
        subject = "Môn Chuyên"
    return subject
def teacher_add_result(request,session):
    teacher = Teachers.objects.get(admin=request.user.id)
    Session = SessionYearModel.object.get(id=session)
    class_list = []
    classes = Classes.objects.filter(year=Session, maths_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, physics_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, chemis_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, bio_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, history_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, geo_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, GDCD_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, PE_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, DE_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, computer_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, tech_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, languages_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, major_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, liters_name_id=request.user.id).all()
    for classe in classes:
        class_list.append(classe)
    return render(request,"Teachers/teacher_add_result.html",{'classes':class_list,'id':session,'teacher':teacher})
def fetch_student_result(request,session):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("teacher_add_result",kwargs={'session':session}))
    else:
        classe_id = request.POST.get('classe')
        students = Students.objects.filter(class_id=classe_id)
        classe = Classes.objects.get(id=classe_id)
        Session = SessionYearModel.object.get(id=session)
        sub = check_subject(request.user.id,classe_id,Session)
        students = Students.objects.filter(class_id=classe)
        subjects = SubjectsTeacher.objects.filter(name=sub, class_id=classe, term="1").all()
        subject_hk1_m1 = []
        subject_hk2 = []
        for student in students:
            subs = SubjectsTeacher.objects.get(name=sub, class_id=classe, term="1", student_id=student)
            name = str(student.admin.first_name)+" "+str(student.admin.last_name)
            avg_hk1 = subs.avg
            subject_hk1_m1.append({'name':name,'m1':subs.m1,'m2':subs.m2,'m3':subs.m3,'m4':subs.m4,'t1':subs.t1,'final':subs.final,'avg':subs.avg,'stn_id':student.id})
            subs = SubjectsTeacher.objects.get(name=sub, class_id=classe, term="2", student_id=student)
            if(avg_hk1 != None and subs.avg != None):
                avg_y = (avg_hk1+subs.avg*2)/3
            else:
                avg_y = None
            subs.avg_y = avg_y
            subs.save()
            subject_hk2.append(
                {'name': name, 'm1': subs.m1, 'm2': subs.m2, 'm3': subs.m3, 'm4': subs.m4, 't1': subs.t1,
                 'final': subs.final,'avg':subs.avg,'stn_id':student.id,'avg_y':avg_y})

        return render(request,"Teachers/fetch_student_result.html",{'id':session,'students':students,'classe':classe,
                                                                    'subject_hk1_m1':subject_hk1_m1,
                                                                    'subjects':subjects,'subject_hk2':subject_hk2})


def save_student_result(request,session,class_id,term):
    if request.method!='POST':
        messages.error(request,"Lỗi! Không Lưu Được")
        return HttpResponseRedirect('teacher_add_result',kwargs={'session':session})
    classe = Classes.objects.get(id=class_id)
    students = Students.objects.filter(class_id=classe)
    Session = SessionYearModel.object.get(id=session)
    for student in students:
        m1 = str(student.id)+"m1_"+term
        m2 = str(student.id) + "m2_" + term
        m3 = str(student.id) + "m3_" + term
        m4 = str(student.id) + "m4_" + term
        t1 = str(student.id) + "t1_" + term
        final = str(student.id) + "final_" + term
        hs1_1 = request.POST.get(m1)
        hs1_2 = request.POST.get(m2)
        hs1_3 = request.POST.get(m3)
        hs1_4 = request.POST.get(m4)
        hs2 = request.POST.get(t1)
        final = request.POST.get(final)
        print(hs1_1)
        subject = check_subject(request.user.id,class_id,Session)
        s = SubjectsTeacher.objects.get(name=subject, class_id=classe, term=term, student_id=student)
        total =0
        cnt = 0
        if (hs1_1 != '' ):
            s.m1 = hs1_1
            total = total + float(hs1_1)
            cnt+=1
        if (hs1_2 != ''):
            s.m2 = hs1_2
            total = total + float(hs1_2)
            cnt += 1
        if (hs1_3 != ''):
            s.m3 = hs1_3
            total = total + float(hs1_3)
            cnt += 1
        if (hs1_4 != ''):
            s.m4 = hs1_4
            total = total + float(hs1_4)
            cnt += 1
        if (hs2 != ''):
            s.t1 = hs2
            total = total + float(hs2)*2
            cnt += 2
        if (final != ''):
            s.final = final
            total = total + float(final)*3
            cnt += 3
        print(cnt)
        if(cnt!=0):
            s.avg = round(total/cnt,2)
        print(s.avg)
        s.save()
    return HttpResponseRedirect(reverse("teacher_add_result",kwargs={'session':session}))


@csrf_exempt
def turn_publish(request):
    term=request.POST.get('term')
    class_id=request.POST.get('classe')
    classe = Classes.objects.get(id=class_id)
    sub = SubjectsTeacher.objects.filter(class_id=classe, term=term, teacher=request.user.id).all()
    for s in sub:
        s.publish = True
        s.save()
    return HttpResponse("True")

def fetch_class_list(Session,id):
    class_list = []
    classes = Classes.objects.filter(year=Session, maths_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, physics_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, chemis_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, bio_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, history_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, geo_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, GDCD_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, PE_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, DE_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, computer_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, tech_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, languages_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, major_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    classes = Classes.objects.filter(year=Session, liters_name_id=id).all()
    for classe in classes:
        class_list.append(classe)
    return class_list

def start_live_classroom(request,session):
    Session = SessionYearModel.object.get(id=session)
    class_list = fetch_class_list(Session,request.user.id)
    return render(request,"Teachers/start_live_classroom.html",{"classes":class_list,"id":session})

def start_live_classroom_process(request,session):
    Session=SessionYearModel.object.get(id=session)
    classe=request.POST.get("classe")
    class_obj=Classes.objects.get(id=classe, year=Session)
    subject = check_subject(request.user.id,classe,Session)
    print(subject)
    print(class_obj)
    checks=OnlineClassRoom.objects.filter(class_id=class_obj, subject=subject, session_years=Session, is_active=True).exists()
    if checks:
        data=OnlineClassRoom.objects.get(class_id=class_obj, subject=subject, session_years=Session, is_active=True)
        room_pwd=data.room_pwd
        roomname=data.room_name
    else:
        room_pwd=datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        roomname=datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        teacher_obj=Teachers.objects.get(admin=request.user.id)
        onlineClass=OnlineClassRoom(room_name=roomname,room_pwd=room_pwd,subject=subject,class_id=class_obj, session_years=Session,started_by=teacher_obj, is_active=True)
        onlineClass.save()

    return render(request,"Teachers/live_class_room_start.html",{"username":request.user.username,"password":room_pwd,"roomid":roomname,"subject":subject,"session_year":Session,"class":class_obj})


def returnHtmlWidget(request):
    return render(request,"widget.html")

def exam(request, session):
    Session = SessionYearModel.object.get(id=session)
    class_list = fetch_class_list(Session, request.user.id)
    teacher = Teachers.objects.get(admin=request.user.id)
    exams = Exam.objects.filter(teacher=teacher,year = Session)
    form = Upload()
    now_time = datetime.now()
    now = now_time.date()
    exams_l = []
    for exam in exams:
        if (now == exam.date or now < exam.date):
            t = now_time.time()
            if (t > exam.end):
                exam.is_active = False
                exam.save()
        else:
            exam.is_active = False
            exam.save()
        if(now < exam.date):
            exam.is_active = True
            exam.save()
    return render(request, "Teachers/exam.html",{'id':session,"classes":class_list,'form':form,'exams':exams})


def create_exam(request, session):
    Session = SessionYearModel.object.get(id=session)
    if request.method!="POST":
        return HttpResponseRedirect(reverse("exam", kwargs={'session':session}))
    else:

        title = request.POST.get('title')
        mul = request.POST.get('mul')
        form1 = request.POST.get('form1')
        date = request.POST.get('date')
        start = request.POST.get('start')
        end = request.POST.get('end')
        number_q = request.POST.get('num_q')
        class_id = request.POST.get('classe')
        classe = Classes.objects.get(id=class_id)
        teacher = Teachers.objects.get(admin=request.user.id)
        sub = check_subject(request.user.id, class_id, Session)
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            file_url = fs.url(filename)
            exam = Exam(
                name = title,
                mul = mul,
                form = form1,
                date = date,
                start = start,
                end = end,
                sub = sub,
                teacher = teacher,
                year = Session,
                class_id = classe,
                number_q = number_q,
                file = file_url)
            exam.save()
            id=exam.id
            print(id)
            print("da save")
            return HttpResponseRedirect(reverse("create_answer",kwargs={'session':session,'num_q':number_q,'id':id}))
        else:
            messages.error(request, "Lỗi! Không Tạo Được")
            return HttpResponseRedirect(reverse("exam", kwargs={'session': session}))

def create_answer(request, session, num_q, id):
    exam = Exam.objects.get(id=id)
    for i in range(int(num_q)):
        i = i+1
        mark = 10 / int(num_q)
        mark = round(mark,2)
        ans = Answer(ques_num =i, ques=exam, mark = mark)
        ans.save()
    ques = Answer.objects.filter(ques=exam)
    return render(request, "Teachers/create_answer.html", {'id': session,'ques':ques,'exam_id':id,'num_q':num_q})

def create_answer_save(request, session, num_q, id):
    exam = Exam.objects.get(id=id)
    if request.method!="POST":
        messages.error(request, "Lỗi! Không Tạo Được")
        return HttpResponseRedirect(reverse("exam", kwargs={'session': session}))
    else:
        for i in range(int(num_q)):
            i = i+1
            ans = request.POST.get(str(i))
            print(i)
            print(ans)
            res = Answer.objects.get(ques_num=i, ques=exam)
            res.is_true = ans
            res.save()
        messages.success(request, "Đã Tạo Thành Công")
        return HttpResponseRedirect(reverse("exam", kwargs={'session': session}))

def show_info(request, session, id):
    exam = Exam.objects.get(id=id)
    num_q = exam.number_q
    list_exam = []
    for i in range(int(num_q)):
        i = i + 1
        res = Answer.objects.get(ques_num=i, ques=exam)
        list_exam.append({'stt':i,'ans':res.is_true})
    stn_exam = Exam_student.objects.filter(exam=exam).all()
    return render(request, "Teachers/show_info.html", {'id': session,'list_exam':list_exam,'exam':exam,'stn_exam':stn_exam})

