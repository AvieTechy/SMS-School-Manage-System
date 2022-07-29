from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ChoiceField
from requests import session

from .models import Classes, SessionYearModel, Students, Teachers


#from .Subject_models import physics_stn,maths_stn, chemis_stn, bio_stn, history_stn, geo_stn, GDCD_stn, liters_stn, PE_stn,DE_stn, computer_stn, tech_stn,languages_stn, major_stn


class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass

class DateInput(forms.DateInput):
    input_type = "date"

class AddTeacherForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255,
                             widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password = forms.CharField(label="Mật Khẩu", max_length=255,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="Họ", max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Tên", max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=255,
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    subject_choice = (
        ("Toán", "Toán"),
        ("Lí", "Vật Lí"),
        ("Hoá Học", "Hoá Học"),
        ("Sinh", "Sinh Học"),
        ("Tin Học-Công Nghệ", "Tin Học - Công Nghệ"),
        ("Văn", "Ngữ Văn"),
        ("Sử-Địa-GDCD", "Sử - Địa - GDCD"),
        ("TD-QPAN", "Thể Dục - QPAN"),
        ("Ngoại Ngữ", "Ngoại Ngữ"),
    )

    subject = forms.ChoiceField(label="Tổ Chuyên Môn", choices=subject_choice,
                            widget=forms.Select(attrs={"class": "form-control"}))

    position_choice = (
        ("Hiệu Trưởng", "Hiệu Trưởng"),
        ("Phó Hiệu Trưởng", "Phó Hiệu Trưởng"),
        ("Chủ Tịch Công Đoàn", "Chủ Tịch Công Đoàn"),
        ("Tổ Trưởng", "Tổ Trưởng"),
        ("Kế Toán", "Kế Toán"),
        ("Giáo Viên", "Giáo Viên")
    )

    position = forms.ChoiceField(label="Chức Vụ", choices=position_choice,
                                widget=forms.Select(attrs={"class": "form-control"}))

    address = forms.CharField(label="Địa Chỉ", max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))

    gender_choice = (
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),

    )

    sex = forms.ChoiceField(label="Giới Tính", choices=gender_choice,
                            widget=forms.Select(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Ảnh Hồ Sơ", max_length=255,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))

class SelectYearForm(forms.Form):
    session_list = []
    sessions = SessionYearModel.object.all()
    for ses in sessions:
        small_ses = (ses.id, str(ses.session_start_year) + "   TO  " + str(ses.session_end_year))
        session_list.append(small_ses)


    session_year_id = forms.ChoiceField(label="Niên Khoá", choices=session_list,
                                        widget=forms.Select(attrs={"class": "form-control"}))

class AddStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control","autocomplete":"off"}))
    password=forms.CharField(label="Mật Khẩu",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="Họ",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Tên",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    address=forms.CharField(label="Địa Chỉ",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    course_list=[]
    courses=Classes.objects.all()
    for course in courses:
       small_course=(course.id,course.class_name)
       course_list.append(small_course)

    gender_choice=(
        ("Nam","Nam"),
        ("Nữ","Nữ"),
    )

    classe=forms.ChoiceField(label="Lớp Học",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="Giới Tính",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    #session_year_id=forms.ChoiceField(label="Niên Khoá",choices=session_list,widget=forms.Select(attrs={"class":"form-control"}))
    #profile_pic=forms.FileField(label="Ảnh Hồ Sơ",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))

class EditStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="Họ",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Tên",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Địa Chỉ",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    classes_list=[]
    classes=Classes.objects.all()
    for classe in classes:
        small_course=(classe.id,str(classe.name)+str(classe.subject))
        classes_list.append(small_course)

    session_list = []
    sessions = SessionYearModel.object.all()

    for ses in sessions:
         small_ses = (ses.id, str(ses.session_start_year)+"   TO  "+str(ses.session_end_year))
         session_list.append(small_ses)

    gender_choice=(
        ("Nam","Nam"),
        ("Nữ","Nữ"),
    )

    classe=forms.ChoiceField(label="Khoá (Lớp)",choices=classes_list,widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="Giới Tính",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id=forms.ChoiceField(label="Niên Khoá",choices=session_list,widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Ảnh Hồ Sơ",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)

class Upload(forms.Form):
    file = forms.FileField(label="Tải file đề", max_length=255,
                                  widget=forms.FileInput(attrs={"class": "form-control input-rounded"}))