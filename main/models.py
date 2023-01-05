from django.db import models
from math import ceil

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
    status = models.CharField(max_length=200, blank=True, null=True)
    average = models.FloatField(default=0)
    get_grants = models.CharField(max_length=3, default="No")

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
                return "excellent"
            elif average >= 75 and average < 90:
                return "good"
            elif average >= 60 and average < 75:
                return "satisfactorily"
            return "expelled"

        if item == "get_grants":
            students = Student.objects.filter(group=self.group)
            if self in students[:ceil(len(students)*4/10)]:
                return "Yes"
            return "No"

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
    value = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.value}"