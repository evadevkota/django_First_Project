from django.db import models

# Create your models here.
#table name - todo
    #column - title(length-100,string),description(length-unlimited,string),status(bool)
class TodoTable(models.Model):
    #class variable
    #char=string
    title= models.CharField(max_length=100)
    description=models.TextField()
    status=models.BooleanField()
