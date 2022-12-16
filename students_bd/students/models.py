from django.db import models

class Group(models.Model):
    name = models.TextField(max_length=32)
    size = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    name = models.TextField(max_length=32)
    age = models.IntegerField()
    sex = models.TextField(max_length=10)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.name}'