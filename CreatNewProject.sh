pip install virtualenv
virtualenv -p python3 env
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
env/scripts/activate
pip install django
django-admin 
django-admin startproject MyFirstProject 
cd MyFirstProject
python manage.py runserver