from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .push_notification import _send_fcm_message

# for firebase initialization
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate(settings.GOOGLE_CREDENTIAL_SERVICE_ACCOUNT_JSON)
initialize_app = firebase_admin.initialize_app(cred)


def index(request):
    """
    Sends the VAPID key to the index.html.
    By using that key, JS snippet generates a device specific token and prints that to the console.
    
    :param request: HTTP Request

    :return: HTTP Response
    """
    # key pair under web configuration
    vapid_key = settings.PUBLIC_VAPID_KEY
    context = {}
    context['vapid_key'] = vapid_key
    return render(request , 'index.html', context)


def send(request, fcm_notification_device_key):
    """
    Gets the fcm_notification_device_key and sends the fcm message to a specific device.
    
    :param fcm_notification_device_key: firebase app token for specific device
    :type fcm_notification_device_key: str

    :return: HTTP Response
    """
    device_registration  = [
        fcm_notification_device_key
    ]
    fcm_response = _send_fcm_message(device_token = fcm_notification_device_key)
    if fcm_response.status_code == 200:
        return HttpResponse("Noticiation Sent Successfully!")
    else:
        return HttpResponse("Please verify device specific token and Try again :)")


def showFirebaseJS(request):
    """
    It's a module name needed by google firebase to authenticate and send the device specific tokens. Without this module, firebase cannot initialize the app and send the tokens.
    It returns a module of content_type as "text/javascript".
    
    :param request: HTTP request

    :return: HTTP Response
    """
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

    return HttpResponse(data, content_type="text/javascript")