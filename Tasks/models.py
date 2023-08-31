from django.db import models
from django.contrib.auth.models import User 
from .choice import Priority_Choice, Status,Gender,doing
class ToDo(models.Model):
    title = models.CharField(max_length=50,choices=doing)
    status = models.CharField(max_length=10, choices=Status)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10,choices=Priority_Choice)
