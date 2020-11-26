from django.db import models

__all__ = [
    'Dean',
    'Student',
    'Teacher',
    'Subject',
    'Group',
]


class Dean(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    faculty_title = models.CharField(max_length=100)

    def __str__(self):
        return self.faculty_title


class Student(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    group = models.ForeignKey('mrs.Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.father_name


class Teacher(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.father_name


class Subject(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)


class Group(models.Model):
    course_number = models.IntegerField(default=1)
    dean = models.ForeignKey(Dean, on_delete=models.CASCADE)
    group_number = models.IntegerField(default=1)

    def __str__(self):
        return str(self.dean_id) + str(self.course_number) + str(self.group_number)
