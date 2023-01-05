from django.db import models
from math import ceil
from random import randint

class StudentStatus(models.Model):
    value = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.value}"

    @classmethod
    def get_default_status(cls):
        status = cls.objects.get(value="expelled")
        return status

class StudentGetGrants(models.Model):
    value = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.value}"

    @classmethod
    def get_default_getgrants(cls):
        getgrants = cls.objects.get(value="No")
        return getgrants

class Department(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"

class Professor(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"

class Group(models.Model):
    name = models.CharField(max_length=500)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    class Meta:
        ordering = ('-average', 'name')
    name = models.CharField(max_length=500)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(StudentStatus, on_delete=models.CASCADE, default=StudentStatus.get_default_status)
    # status = models.CharField(max_length=500)
    average = models.FloatField(default=0)
    get_grants = models.ForeignKey(StudentGetGrants, on_delete=models.CASCADE, default=StudentGetGrants.get_default_getgrants)
    # get_grants = models.CharField(max_length=500)

    def __getattribute__(self, item):
        if item == "average":
            marks = Mark.objects.filter(student__name=self.name)
            mark_count = marks.count()
            if mark_count:
                return marks.aggregate(models.Sum("value"))['value__sum']/mark_count
            return 0

        if item == "status":
            average = self.average
            if average >= 90 and average <= 100:
                return StudentStatus.objects.get(value="excellent")
            elif average >= 75 and average < 90:
                return StudentStatus.objects.get(value="good")
            elif average >= 60 and average < 75:
                return StudentStatus.objects.get(value="satisfactorily")
            return StudentStatus.objects.get(value="expelled")

        if item == "get_grants":
            students = Student.objects.filter(group=self.group)
            if self in students[:ceil(len(students)*4/10)]:
                return StudentGetGrants.objects.get(value="Yes")
            return StudentGetGrants.objects.get(value="No")

        if item == "department":
            return self.group.department

        return object.__getattribute__(self, item)

    def __str__(self):
        return f"{self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=500)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(default=randint(50, 100))

    def __str__(self):
        return f"{self.value}"
