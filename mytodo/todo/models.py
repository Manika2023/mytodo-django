from django.db import models

# Create your models here.
class Todo(models.Model):
     datesubmiited=models.DateField(auto_now_add=True,null=True,blank=True)
     title=models.CharField(max_length=300)
     description=models.TextField()
     completed=models.BooleanField(default=False)

     def __str__(self):
          return self.title