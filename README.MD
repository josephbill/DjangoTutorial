### DJANGO
- THis is a python web framework (a software framework that simplifies the development of web apps by providing
a structure and common  components (tools and libs to handle common web dev tasks) )

1. routing : mapping url routes to various pages or functionalities
2. Authentication : authorization , identity
3. Database integration and interaction
4. Session Management
5. Form Handling

Examples
Backend Frameworks
1. NodeJS
2. Python (Flask and Django)
3. PHP (Laravel)
4. Ruby on Rails
5. GO (GIN, ECHO)

Frontend Framework
1. React JS
2. Next JS
3. Angular
4. Vue


### A DJANGO WEBSITE
- This typically consists of a single Project , that is then spilt into separates apps
   Instagram (case study)
   - user management : Logging in and out , registering , forgot password
   - media features : upload, edit and display media
   - messaging : send messages

- django apps are structured to separate the logic pieces
- django supports the architecural pattern of MVC.
  - Models : define the data. This is usually the database description and often the base layer to an app.
  - Views : display some or all data and also enable client interaction. HTML AND CSS things
  - Controllers : handles how the database and the views interact
- django recognizes above as an MVT pattern
  - Models : define the data. This is usually the database description and often the base layer to an app.
  - Views : url mapping logic
  - Templates : HTML and CSS ,



### Conclusion:
A django site starts off as a project , and its built up with a number of apps that handle separate functionalities. Each app follows the
MVT pattern.


### Tools to work with django
1. Python - python --version
            python3 --version

2. pip  -  pip install django
3. python -m django --version

### How to create to django projects

python -m django-admin startproject PROJECTNAME

### How to run the django server

- cd projectname
- python manage.py runserver

### How to add an app

- python manage.py startapp todo
- next register the app to the project , in settings.py on project folder
add it to the installed apps list

### How to map models to database tables (applying migrations)
1. Define the model
2. make the migrations ( python manage.py makemigrations )
3. apply the migrations ( python manage.py migrate )