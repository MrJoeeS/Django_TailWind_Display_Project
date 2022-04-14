To get access to the API you may need to create a superuser. 
Create a superuser with the command below to gain access. Make the password: password123
The API uses the below login. The the login credentials were hardcoded in since this will not go into production.

Run the command in command prompt at (download_location)\DjangoTailWindDisplayProject\mysite
python manage.py createsuperuser --email admin@example.com --username admin

After the above step in the same directery run 
python manage.py runserver
This will start the server. 

If you want to run tailwind, in a differnt terminal run 
python manage.py tailwind start

This also needs to be ran in the location (download_location)\DjangoTailWindDisplayProject\mysite

The site where the data is located is http://localhost:8000/home/
The API Root is located at http://localhost:8000/

All HTMLs are located at mysite\theme\templates
The code that pulls the data for the graphs is located at mysite\templatetags\test_script.py
The API endpoints is located at mysite\practice_project\views.py
The models for the APIs is located at mysite\practice_project\models.py