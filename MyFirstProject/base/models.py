from django.db import models

# Create your models here.



class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null= True,blank=True)
    # participants = 
    Updated_at = models.DateTimeField(auto_now=True)
    created=Models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.name
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