from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null= True,blank=True)
    # participants = 
    Updated_at = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    #host =

class Room(models.Model):
    host =  topic =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic =  models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null= True,blank=True)
    # participants = 
    Updated_at = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    #host = 
# class Project(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(max_length=200)
#     id = models.CharField(max_length=200)
#     technology = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='images/')
#     link = models.URLField(max_length=200)

#     def __str__(self):
#         return self.title



class Message(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Updated_at = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)