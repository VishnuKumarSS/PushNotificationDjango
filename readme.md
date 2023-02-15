pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Go to the home page of the server, copy the <Key> from the server.
Then navigate to the send/<Key>/

The push notification will be sent!