from django.shortcuts import render
import datetime
import json
import os
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .EmailBackEnd import EmailBackEnd
from .models import CustomUser, SessionYearModel
from SMS import settings

# Create your views here.
def Broteam(request):
    return render(request,"Home/BroTeam.html")

def ShowMainPage(request):
    return render(request,"Home/SMS_Home.html")

def ShowLoginPage(request):
    return render(request, "Home/login.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       # captcha_token=request.POST.get("g-recaptcha-response")
       # cap_url="https://www.google.com/recaptcha/api/siteverify"
       # cap_secret="6LeWtqUZAAAAANlv3se4uw5WAg-p0X61CJjHPxKT"
       # cap_data={"secret":cap_secret,"response":captcha_token}
       # cap_server_response=requests.post(url=cap_url,data=cap_data)
       # cap_json=json.loads(cap_server_response.text)

       # if cap_json['success']==False:
        #    messages.error(request,"Invalid Captcha Try Again")
         #   return HttpResponseRedirect("/")

        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("admin_select_year"))
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("select_session_teacher"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"Lỗi Đăng Nhập! Hãy Kiểm tra lại email & mật khẩu")
            return HttpResponseRedirect("/SMS/login")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "YOUR_API_KEY",' \
         '        authDomain: "FIREBASE_AUTH_URL",' \
         '        databaseURL: "FIREBASE_DATABASE_URL",' \
         '        projectId: "FIREBASE_PROJECT_ID",' \
         '        storageBucket: "FIREBASE_STORAGE_BUCKET_URL",' \
         '        messagingSenderId: "FIREBASE_SENDER_ID",' \
         '        appId: "FIREBASE_APP_ID",' \
         '        measurementId: "FIREBASE_MEASUREMENT_ID"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")
