from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from django.contrib.auth.models import User
#3rd apps field

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"Host"),(2,"Teacher"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class SessionYearModel(models.Model):
    id=models.AutoField(primary_key=True)
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    object=models.Manager()

class AdminHost(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Teachers(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, null=True)
    position = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    profile_pic = models.FileField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects=models.Manager()

class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    class_name=models.CharField(max_length=225)
    name = models.IntegerField()
    subject = models.CharField(max_length=225)
    year = models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    ss = models.IntegerField(null=True)
    GVCN = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    maths_name = models.CharField(max_length=255, blank=True, null=True)
    physics_name = models.CharField(max_length=255, blank=True, null=True)
    chemis_name = models.CharField(max_length=255, blank=True, null=True)
    bio_name = models.CharField(max_length=255, blank=True, null=True)
    history_name = models.CharField(max_length=255, blank=True, null=True)
    geo_name = models.CharField(max_length=255, blank=True, null=True)
    GDCD_name = models.CharField(max_length=255, blank=True, null=True)
    liters_name = models.CharField(max_length=255, blank=True, null=True)
    PE_name = models.CharField(max_length=255, blank=True, null=True)
    DE_name = models.CharField(max_length=255, blank=True, null=True)
    languages_name = models.CharField(max_length=255, blank=True, null=True)
    major_name = models.CharField(max_length=255, blank=True, null=True)
    tech_name = models.CharField(max_length=255, blank=True, null=True)
    computer_name = models.CharField(max_length=255, blank=True, null=True)
    maths_name_id = models.CharField(max_length=255, blank=True, null=True)
    physics_name_id = models.CharField(max_length=255, blank=True, null=True)
    chemis_name_id = models.CharField(max_length=255, blank=True, null=True)
    bio_name_id = models.CharField(max_length=255, blank=True, null=True)
    history_name_id = models.CharField(max_length=255, blank=True, null=True)
    geo_name_id = models.CharField(max_length=255, blank=True, null=True)
    GDCD_name_id = models.CharField(max_length=255, blank=True, null=True)
    liters_name_id = models.CharField(max_length=255, blank=True, null=True)
    PE_name_id = models.CharField(max_length=255, blank=True, null=True)
    DE_name_id = models.CharField(max_length=255, blank=True, null=True)
    languages_name_id = models.CharField(max_length=255, blank=True, null=True)
    major_name_id = models.CharField(max_length=255, blank=True, null=True)
    tech_name_id = models.CharField(max_length=255, blank=True, null=True)
    computer_name_id = models.CharField(max_length=255, blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.class_name)

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    profile_pic=models.FileField(blank=True, null=True)
    address=models.TextField()
    class_id=models.ForeignKey(Classes,on_delete=models.DO_NOTHING)
    session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects = models.Manager()

    def __str__(self):
        return str(self.admin)


class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportTeacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackTeacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationTeacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    GVMB_id = models.ForeignKey(Teachers,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes,on_delete=models.CASCADE)
    attendance_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class LessonTimeSet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    session = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    objects = models.Manager()

class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, null=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)

class StudentResult(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    subject_exam_marks=models.FloatField(default=0)
    subject_assignment_marks=models.FloatField(default=0)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

class OnlineClassRoom(models.Model):
    id=models.AutoField(primary_key=True)
    room_name=models.CharField(max_length=255)
    room_pwd=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    session_years=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    started_by=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


   # ---------------------------------------- Subject Begin ----------------------------------- #

class SubjectsTeacher(models.Model):
    name = models.CharField(max_length=225)
    m1 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], )
    m2 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], )
    m3 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], )
    m4 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], )
    t1 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], )
    final = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], )
    term = models.CharField(default='', max_length=3)
    avg = models.FloatField(blank=True, null=True)
    avg_y = models.FloatField(blank=True, null=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    publish = models.BooleanField(default=False)
    objects = models.Manager()


   # ---------------------------------------- Subject End ----------------------------------- #


   # ------------------------------------ Create profile user ------------------------------- #

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHost.objects.create(admin=instance)
        if instance.user_type==2:
            Teachers.objects.create(admin=instance,address="",profile_pic="",gender="",major="",position="")
        if instance.user_type==3:
            Students.objects.create(admin=instance,class_id=Classes.objects.get(id=1),session_year_id=SessionYearModel.object.get(id=1),address="",profile_pic="",gender="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhost.save()
    if instance.user_type==2:
        instance.teachers.save()
    if instance.user_type==3:
        instance.students.save()


class aim(models.Model):
    Mod = models.FloatField(max_length=225,blank=True, null=True)
    alf_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    objects = models.Manager()

class Subjects(models.Model):
    name = models.CharField(max_length=225)
    m1 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],)
    m2 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],)
    m3 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],)
    m4 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],)
    t1 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],)
    final = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],)
    avg = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    target = models.FloatField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    alf_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    term = models.CharField(default='', max_length=3)
    objects = models.Manager()

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=225)
    mul = models.CharField(max_length=225)
    form = models.CharField(max_length=225, default="TN")
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    sub = models.CharField(max_length=225)
    year = models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    number_q = models.IntegerField()
    file = models.FileField()

class Answer(models.Model):
    is_true = models.CharField(max_length=255, blank=True, null=True)
    ques_num = models.IntegerField()
    mark = models.FloatField()
    ques = models.ForeignKey(Exam,on_delete=models.CASCADE)

class Exam_student(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=0)
    sum = models.FloatField(blank=True, null=True, default=0)
    finish = models.BooleanField(default=False)
    time_finish = models.CharField(max_length=255, blank=True, null=True)
class Answer_student(models.Model):
    ques_num = models.IntegerField()
    exam = models.ForeignKey(Exam_student, on_delete=models.CASCADE)
    stn_ans_TN = models.CharField(max_length=255, blank=True, null=True)
    stn_ans_TL = models.TextField(max_length=255, blank=True, null=True)
    bool = models.BooleanField(default=False)