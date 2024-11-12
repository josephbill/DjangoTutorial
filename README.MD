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

### AGENDA 
1. Databases 
2. Objects Relationships

### Install an sqlite viewer 
1. go to file -> settings -> plugins on sidebar
2. ctrl + alt + s to open settings 
3. go to installed tab 
4. ensure the plugin Database Tools and SQL is checked 
5. if not present search in marketplace 
6. double click on desired view for db
7. right click to check if database drivers are enabled 
8. If not installed , click to install 
9. right click to get to properties 
10. check the general tab , to ensure sqlite URL is correctly mapped to 
your project 
11. check the schema tab and allow the schema you want or all to visualize
all schemas 
12. Locate the schema , then double click to visualize table for app. 
13. https://www.jetbrains.com/help/pycharm/sqlite.html#connect-to-sqlite-database


### Databases
A database is an organized system for storing , managing and retrieving data in an efficient and organized 
manner 
- Maintain persitency on data. Manipulate the data 

### Database Structure 
Key elements of the structure 
1. Tables : primary structure for organizing data , where data is stored in rows and columns 
2. Columns : Represents specific attributes or props for the items in each row. Each column will
have a data type like text, integer or date ....
3. Primary Key : A unique id for each row , ensuring no row has the same Primary key , making it
easier to access and manage individual records 
4. Foreign Key : A field in one table that links to the primary key of another table , creating 
relationships between the tables 

### Database Types 
Classified by how they store data, the type of relationships they support and the design 

a. Relational Databases (RDBMS)
use tables to store data with predefined relationships between the tables. 
Each table has rows and columns where relationships are established using PK and FK 

examples : MySQL , PostgreSQL , Oracle , SQL server , sqlite

Advantage: High data integrity , SQL support , support for complex queries through SQL joins 

b. NoSQL Databases 
store data in non-tabular forms , which makes them suitable for unstructured , unrelated or semi
structured data 
Document-Oriented sequence : JSON-like documents 

Example : Google Firebase , MongoDB 

c. In-Memory db's : storage happens in main memory rather than disks (RAM) 
Example : Redis 

d. Object-Oriented Databases 
storage of data in objects
example : ObjectDB 

e. Distributed databases 
Data is stored across different locations and interconnected through a network 
Example : Google Spanner , Apache Cassandra 


### Database Attributes and Fields (Columns)
1. Data types : define the kind of data to be stored in each column. (text, integer, date , boolean)
2. Constraint : Rules to be applied to the data to ensure data integrity (NOT NULL, NULL , UNIQUE, length)4
3. Indexes : Special data structures that improve query performance by allowing fast retrieval of rows usings keys columns 
4. Schemas : Describe the structure of the db. includes the tables , 
relationships, views and permission. 

### Database Operations
- CRUD operations : Create , read, update, delete 
- Query : retrieve specific data using SQL : Structured query language 
- Transactions: group operations within single units

### Database Relationships 
Defining how data in different tables relate to one another 
1. One to One : Each row in one table is linked to one row in another table 
2. One to Many : A row in one table can be linked to multiple rows in another
table 
3. Many to Many : Rows in one table are linked multiple rows in another table
, often managed using a join table 

### ORM : Object Relational Mapping 
this is a programming technique allowing us to interact with a relational db using 
oop.
Key usage 
- replaces the need for writing raw SQL queries instead we use the objects to perform
db operations , makes our code cleaner and more maintainable 

Python Flask = SQLAlchemy ORM 
Python Django = Django ORM 

### Django ORM 
Allows interaction with databases using python classes and methods rather than raw SQL. 
Breakdown :
1. Each model class represents a table in the database 
2. Each instance/object of that class will represent a row in the table

### Basic concepts of Django ORM 
1. Model : a python class to represent the table 
2. Querysets : A collection of db rows represented as objects which can be filtered
ordered and manipulated 
3. Migrations : A way to apply db schema changes i.e. creating tables 




