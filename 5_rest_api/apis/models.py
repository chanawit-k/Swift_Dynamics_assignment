from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    sex = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClassRoom(models.Model):
    year = models.PositiveIntegerField()
    section = models.CharField(max_length=10)
    teachers = models.ManyToManyField(Teacher, related_name='classrooms')

    def __str__(self):
        return f"Year {self.year} Section {self.section}"


class Student(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    sex = models.CharField(max_length=225)
    classroom = models.ForeignKey(ClassRoom, blank=True, null=True, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class School(models.Model):
    name = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    address = models.CharField(max_length=255)
    classrooms = models.ManyToManyField(ClassRoom, blank=True, related_name='schools')

    def __str__(self):
        return self.name
