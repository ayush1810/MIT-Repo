from django.db import models

# Create your models here.
class Semester(models.Model):
    sem = models.IntegerField(default = 1, unique=True)

    def __str__(self):
        return str(self.sem)

class Branch(models.Model):
    name = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    semester = models.ForeignKey(Semester, models.CASCADE)
    branch_name = models.ForeignKey(Branch,models.CASCADE)
    name = models.CharField(max_length = 255, unique=True)

    def __str__(self):
        return str(self.name)
