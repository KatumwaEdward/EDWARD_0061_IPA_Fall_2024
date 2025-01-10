#first install python,pip and virtual environment in your system
1. created a virtual environment for the project
    ubuntu - python3 -m venv .venv
    windows - python -m venv .venv
2. activate the virtual environment (ALWAYS ACTIVATE THE VIRTUAL ENVIRONMENT BEFORE START WORKING)
    ubuntu - source .venv/bin/activate
    windows - .venv\Scripts\activate
3. install django && djangorestframework && djoser && django-cors-headers
    ubuntu - pip3 install django djangorestframework djoser django-cors-headers
    windows - pip install django djangorestframework djoser django-cors-headers
4. create a django project
    ubuntu - django-admin startproject final_project
    windows - django-admin startproject final_project
5. create a app for the project
    ubuntu - python3 manage.py startapp api
    windows - python manage.py startapp api
6. run the live server
    ubuntu - python3 manage.py runserver
    windows - python manage.py runserver
7. 