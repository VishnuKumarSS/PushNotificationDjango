`pip install -r requirements.txt`

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Go to the home page of the server, copy the **Device specific firebase app Key** from the console of the browser.
Then navigate to the send/**Paste the key here**/

The push notification will be sent!


To send a Firebase Cloud Message, we have to send a request to the url

[https://fcm.googleapis.com/fcm/send](https://fcm.googleapis.com/fcm/send)

For parameters and it’s usage, We can refer this documentation - [https://firebase.google.com/docs/cloud-messaging/http-server-ref](https://firebase.google.com/docs/cloud-messaging/http-server-ref)

In headers we have to add **Content-Type** and **Authorization,** for that we have to create Firebase account and navigate to the Project settings -> Cloud Messaging, here we have to enable firebase cloud messaging api by activating **Cloud Messaging** in the console.cloud.google.com

Now we should see the server key in the console.firebase.google.com

[https://lh5.googleusercontent.com/WDfn8frOyrYFwQ0R0srvBBM1_hvjRR20bN2VOITnoGZnYql-mIcw_PLs82x1hmQHePJzxfI3JW0d3jzlXRZuoDGUZ0fnOqvTklcF8_-OOHhfRY3QICvWzCxnVi2yyWAV_igRJNSsPisSZCeoCXCPOJk](https://lh5.googleusercontent.com/WDfn8frOyrYFwQ0R0srvBBM1_hvjRR20bN2VOITnoGZnYql-mIcw_PLs82x1hmQHePJzxfI3JW0d3jzlXRZuoDGUZ0fnOqvTklcF8_-OOHhfRY3QICvWzCxnVi2yyWAV_igRJNSsPisSZCeoCXCPOJk)

That **key** will be in the Authorization field of Headers and Content-Type will most probably should be **application/json**.

[https://lh3.googleusercontent.com/3WDpDn3XD7Ohr-AURYs32jXfAxv4NqMJppRE-a0vYjCO-FJ9xsLz8g9l46gKpqFzMH7VZ49glKJy17JlRmzGOw0pEJOuGzzP8Qxv3RUzb6DJTxOfrWVU4KK_6QXhz7XTYwB52WK3WMvINJIvceIaV0g](https://lh3.googleusercontent.com/3WDpDn3XD7Ohr-AURYs32jXfAxv4NqMJppRE-a0vYjCO-FJ9xsLz8g9l46gKpqFzMH7VZ49glKJy17JlRmzGOw0pEJOuGzzP8Qxv3RUzb6DJTxOfrWVU4KK_6QXhz7XTYwB52WK3WMvINJIvceIaV0g)

**Then we can refer this page for SDK instructions**

[https://console.firebase.google.com/project/pushnotification-test-3fa8c/settings/general/android:com.company.pushnotification](https://console.firebase.google.com/project/pushnotification-test-3fa8c/settings/general/android:com.company.pushnotification)

## **Now we have to generate a (device specific permit key), to be used on the body of the payload,**

To generate the **device specific permit keys**, it depends on the platform we are using.

For setting up **android client** we can visit the link below

[https://firebase.google.com/docs/cloud-messaging/android/client](https://firebase.google.com/docs/cloud-messaging/android/client)

We can visit the link below for various platform specific documentation.

[https://firebase.google.com/docs/cloud-messaging](https://firebase.google.com/docs/cloud-messaging)

```json
payload = {

	# we can use "to" for single device notification
	
	# "to": registration_id
	
	"registration_ids" :registration_ids,
	
	"priority" : "high",
	
	"notification" : {
	
	"body" : message_body,
	
	"title" : message_title,
	
	"subtitle": message_subtitle
	
	# "image" : image_link,
	
	# "icon": icon_link,
	
	}
	
}
```

Now we should have that device specific keys. Here, the **registrations_ids** is a **list** of device specific permit keys, if we wanna just send the notification only to a **single** user then we can use **“to” : “<**device specific permit key**>”** also, Or else we should use the **“registration_ids”** field.

And then inside the **notification** key the **message and title** are mandatory, Rest are optional.

[https://lh5.googleusercontent.com/3TeuhfSeJhoLcRXqsaS_MU_OojmyOWOic_K19UIQfCobY1d9reASg8lAIJdiR7A9kODC56eDy3ynAGiGyBWpJ6gqeg22caNULr-qlWYkMgGjDmWZgHF2Rgne3-w_dbIm39a4TwgV-PUmRUMCSDCtPk4](https://lh5.googleusercontent.com/3TeuhfSeJhoLcRXqsaS_MU_OojmyOWOic_K19UIQfCobY1d9reASg8lAIJdiR7A9kODC56eDy3ynAGiGyBWpJ6gqeg22caNULr-qlWYkMgGjDmWZgHF2Rgne3-w_dbIm39a4TwgV-PUmRUMCSDCtPk4)

Now send the request, the user should have received the message now!

We can refer this Youtube Video for this

[Firebase send push notification using postman example.](https://www.youtube.com/watch?v=rQzexLu0eLU&ab_channel=AlimonPito)

We can follow the below links for that,

**https://medium.com/scalereal/push-notifications-through-django-db528c303b91**

Then refer,

**WEB -**

[Firebase Push notification Django | Push notification Django | Learn how to send push notification](https://www.youtube.com/watch?v=RXK3O0ONJv0&ab_channel=CodeKeen)

**ANDROID -**

[https://medium.com/@shamsul.arefin.sajib/how-to-connect-django-and-android-with-firebase-fcm-notifications-71e9aafdd988](https://medium.com/@shamsul.arefin.sajib/how-to-connect-django-and-android-with-firebase-fcm-notifications-71e9aafdd988)

# **Notice messages to users under specific topic (Not our case)**

We can refer this Youtube Video for this

[Firebase send message for multiple devices using postman +flutter example](https://www.youtube.com/watch?v=mCeSgHmVehk&ab_channel=AlimonPito)

Here we are sending the messages to the user’s by categorizing them into Topic names. For that first we have to make that user subscribe to that topic. Then we can do something like this,