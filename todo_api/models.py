from django.db import models

# Create your models here.
# one to many relationship : one users will have many todos
class User(models.Model):
    # username
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Many to many relationship : Task -> tags
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Class task
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # this attribute user will store the user id as a foreign key
    '''
    the user variable below establishes a one to many relationship between 
    a user and a task : a user can have many tasks 
    '''
    user = models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)
    '''
    tags establishes a many to many relationship with tasks. 
    '''
    tags = models.ManyToManyField(Tag,related_name='tasks')

    def __str__(self):
        return self.title
