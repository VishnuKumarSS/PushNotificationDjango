import pdb
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.conf import settings

# for 
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(settings.GOOGLE_CREDENTIAL_SERVICE_ACCOUNT_JSON)
initialize_app = firebase_admin.initialize_app(cred)

def index(request):
    # key pair under web configuration
    vapid_key = settings.PUBLIC_VAPID_KEY
    context = {}
    context['vapid_key'] = vapid_key
    return render(request , 'index.html', context)


def send(request, fcm_notification_device_key):
    device_registration  = [
        fcm_notification_device_key
    ]
    # send_notification(device_registration , 'This is the Message Title' , 'This is the Message Body', 'This is the Message Subtitle')
    
    return HttpResponse("Sent ")


def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyCdpoBmMRTJ8jaW3b4J48o2Z9-Ex70eTJE",' \
         '        authDomain: "my-first-project-a9467.firebaseapp.com",' \
         '        projectId: "my-first-project-a9467",' \
         '        storageBucket: "my-first-project-a9467.appspot.com",' \
         '        messagingSenderId: "31043981576",' \
         '        appId: "1:31043981576:web:005d48ca56960e67fddcbd",' \
         '        measurementId: "G-EF7KXQC5MR"' \
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