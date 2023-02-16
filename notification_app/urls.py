from django.urls import path
from .views import *

urlpatterns = [
    path('' , index),
    path('send-notification/<str:fcm_notification_device_key>' , send_notification),
    path('firebase-messaging-sw.js',showFirebaseJS,name="show_firebase_js"),
]
