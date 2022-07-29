"""SMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''''
from django.contrib import admin
from django.urls import path
urlpatterns = [
    #home
    path('admin/', admin.site.urls),
]

'''
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from SMS import settings
from SMS_app import views,HostView, StudentView, TeacherView

urlpatterns = [
    #home

    path('admin/', admin.site.urls),
    path('broteam/',views.Broteam),
    path('',views.ShowMainPage,name="show_main"),
    path('SMS/login',views.ShowLoginPage,name="show_login"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_select_year',HostView.admin_select_year,name="admin_select_year"),
    path('select_session',HostView.select_year,name="select_session"),
    path('select_session_save',HostView.select_year_save,name="select_session_save"),
    path('admin_home/<str:session>',HostView.admin_home,name="admin_home"),
    #check
    path('check_email_exist', HostView.check_email_exist,name="check_email_exist"),
    path('check_username_exist', HostView.check_username_exist,name="check_username_exist"),
    #add
    path('<str:session>/add_student', HostView.add_student,name="add_student"),
    path('<str:session>/add_student_save', HostView.add_student_save,name="add_student_save"),
    path('<str:session>/add_class', HostView.add_class,name="add_class"),
    path('<str:session>/add_class_save', HostView.add_class_save,name="add_class_save"),
    path('add_session_save', HostView.add_session_save,name="add_session_save"),
    path('add_teacher', HostView.add_teacher,name="add_teacher"),
    #path('add_MajorFields', HostView.MajorFields,name="add_MajorFields"),
    path('add_teacher_save',HostView.add_teacher_save,name="add_teacher_save"),
    #manage
    path('<str:session>/manage_student', HostView.manage_student,name="manage_student"),
    path('<str:session>/manage_class', HostView.manage_class,name="manage_class"),
    #path('manage_teacher', HostView.manage_teacher,name="manage_teacher"),
    path('<str:session>/manage_teacher_in_session', HostView.manage_teacher_in_session,name="manage_teacher_in_session"),
    path('manage_session', HostView.manage_session,name="manage_session"),
    path('division_teacher_save', HostView.division_teacher_save,name="division_teacher_save"),
    path('<str:session>/timetable_division_save', HostView.timetable_division_save,name="timetable_division_save"),
    path('<str:session>/lession_time_set', HostView.lession_time_set,name="lession_time_set"),
    path('<str:session>/lession_time_set_save', HostView.lession_time_set_save,name="lession_time_set_save"),
    path('get_class_divide', HostView.get_class_divide,name="get_class_divide"),

    # edit
    path('<str:session>/edit_student/<str:student_id>', HostView.edit_student,name="edit_student"),
    path('<str:session>/edit_student_save/<str:student_id>', HostView.edit_student_save,name="edit_student_save"),
    path('<str:session>/edit_class/<str:class_id>', HostView.edit_class,name="edit_class"),
    path('<str:session>/edit_class_save/<str:class_id>', HostView.edit_class_save,name="edit_class_save"),
    path('<str:session>/edit_teacher/<str:teacher_id>', HostView.edit_teacher,name="edit_teacher"),
    path('<str:session>/edit_teacher_save', HostView.edit_teacher_save,name="edit_teacher_save"),
    #logout
    path('logout_user', views.logout_user,name="logout"),
    path('get_class', HostView.get_class,name="get_class"),


    path('<str:session>/student_feedback_message', HostView.student_feedback_message,name="student_feedback_message"),
    path('student_feedback_message_replied', HostView.student_feedback_message_replied,name="student_feedback_message_replied"),
    path('<str:session>/teacher_feedback_message', HostView.teacher_feedback_message,name="teacher_feedback_message"),
    path('teacher_feedback_message_replied', HostView.teacher_feedback_message_replied,name="teacher_feedback_message_replied"),
    path('<str:session>/student_leave_view', HostView.student_leave_view,name="student_leave_view"),
    path('<str:session>/teacher_leave_view', HostView.teacher_leave_view,name="teacher_leave_view"),
    path('<str:session>/student_approve_leave/<str:leave_id>', HostView.student_approve_leave,name="student_approve_leave"),
    path('<str:session>/student_disapprove_leave/<str:leave_id>', HostView.student_disapprove_leave,name="student_disapprove_leave"),
    path('<str:session>/teacher_disapprove_leave/<str:leave_id>', HostView.teacher_disapprove_leave,name="teacher_disapprove_leave"),
    path('<str:session>/teacher_approve_leave/<str:leave_id>', HostView.teacher_approve_leave,name="teacher_approve_leave"),
    path('<str:session>/admin_profile', HostView.admin_profile,name="admin_profile"),
    path('<str:session>/admin_profile_save', HostView.admin_profile_save,name="admin_profile_save"),
    path('<str:session>/admin_send_notification_teacher', HostView.admin_send_notification_teacher,name="admin_send_notification_teacher"),
    path('<str:session>/admin_send_notification_student', HostView.admin_send_notification_student,name="admin_send_notification_student"),
    path('send_student_notification', HostView.send_student_notification,name="send_student_notification"),
    path('send_teacher_notification', HostView.send_teacher_notification,name="send_teacher_notification"),

         #     Teacher URL Path
    path('select_session_teacher',TeacherView.select_year_teacher,name="select_session_teacher"),
    path('select_session_teacher_save',TeacherView.select_year_teacher_save,name="select_session_teacher_save"),
    path('teacher_home/<str:session>', TeacherView.teacher_home, name="teacher_home"),
    path('<str:session>/fetch_student_result', TeacherView.fetch_student_result, name="fetch_student_result"),

    path('<str:session>/teacher_take_attendance', TeacherView.teacher_take_attendance, name="teacher_take_attendance"),
    path('<str:session>/teacher_update_attendance', TeacherView.teacher_update_attendance, name="teacher_update_attendance"),
    path('get_students', TeacherView.get_students, name="get_students"),
    path('get_attendance_dates', TeacherView.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student', TeacherView.get_attendance_student, name="get_attendance_student"),
    path('save_attendance_data', TeacherView.save_attendance_data, name="save_attendance_data"),
    path('save_updateattendance_data', TeacherView.save_updateattendance_data, name="save_updateattendance_data"),
    path('<str:session>/teacher_apply_leave', TeacherView.teacher_apply_leave, name="teacher_apply_leave"),
    path('<str:session>/teacher_apply_leave_save', TeacherView.teacher_apply_leave_save, name="teacher_apply_leave_save"),
    path('<str:session>/teacher_feedback', TeacherView.teacher_feedback, name="teacher_feedback"),
    path('<str:session>/teacher_feedback_save', TeacherView.teacher_feedback_save, name="teacher_feedback_save"),
    path('<str:session>/teacher_profile', TeacherView.teacher_profile, name="teacher_profile"),
    path('<str:session>/teacher_profile_save', TeacherView.teacher_profile_save, name="teacher_profile_save"),
    path('staff_fcmtoken_save', TeacherView.staff_fcmtoken_save, name="staff_fcmtoken_save"),
    path('<str:session>/teacher_all_notification', TeacherView.teacher_all_notification, name="teacher_all_notification"),
    path('<str:session>/teacher_add_result', TeacherView.teacher_add_result, name="teacher_add_result"),
    path('<str:session>/save_student_result/<int:class_id>/<str:term>', TeacherView.save_student_result, name="save_student_result"),
    path('<str:session>/start_live_classroom',TeacherView.start_live_classroom, name="start_live_classroom"),
    path('<str:session>/start_live_classroom_process',TeacherView.start_live_classroom_process, name="start_live_classroom_process"),
    path('<str:session>/exam',TeacherView.exam, name="exam"),
    path('<str:session>/create_exam',TeacherView.create_exam, name="create_exam"),
    path('<str:session>/create_answer/<str:num_q>/<str:id>',TeacherView.create_answer, name="create_answer"),
    path('<str:session>/create_answer_save/<str:num_q>/<str:id>',TeacherView.create_answer_save, name="create_answer_save"),
    path('<str:session>/show_info/<str:id>',TeacherView.show_info, name="show_info"),
    path('turn_publish',TeacherView.turn_publish, name="turn_publish"),

                   #Student Path
    path('student_private_result', StudentView.home_private_result, name="student_private_result"),
    #path('hk<str:term>/<str:student_id>/<str:Class>', StudentView.hk1, name="hk1"),
    path('get_private_result', StudentView.get_private_result, name="get_private_result"),
    path('update_mark_save', StudentView.update_mark_save, name="update_mark_save"),
    path('student_home', StudentView.student_home, name="student_home"),
    path('student_view_attendance', StudentView.student_view_attendance, name="student_view_attendance"),
    #path('student_view_attendance', StudentView.personal_result_home, name="personal_result_home"),
    path('student_view_attendance_post', StudentView.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave', StudentView.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', StudentView.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', StudentView.student_feedback, name="student_feedback"),
    path('student_feedback_save', StudentView.student_feedback_save, name="student_feedback_save"),
    path('student_profile', StudentView.student_profile, name="student_profile"),
    path('student_profile_save', StudentView.student_profile_save, name="student_profile_save"),
    path('student_fcmtoken_save', StudentView.student_fcmtoken_save, name="student_fcmtoken_save"),
    path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js"),
    path('student_all_notification',StudentView.student_all_notification,name="student_all_notification"),
    path('student_view_result',StudentView.student_view_result,name="student_view_result"),
    path('join_class_room/<str:subject_name>/<int:class_id>',StudentView.join_class_room,name="join_class_room"),
    path('node_modules/canvas-designer/widget.html',TeacherView.returnHtmlWidget,name="returnHtmlWidget"),
    path('target_set',StudentView.target_set,name="target_set"),
    path('exam_list',StudentView.exam_list,name="exam_list"),
    path('start_exam/<str:exam_id>/<int:stn_id>',StudentView.start_exam,name="start_exam"),
    path('change_warning',StudentView.change_warning,name="change_warning"),
    path('save_answer_student/<str:exam_id>',StudentView.save_answer_student,name="save_answer_student"),
    path('finish_exam/<str:exam_id>',StudentView.finish_exam,name="finish_exam"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
