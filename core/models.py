from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    registered_time = models.TimeField()
    location = models.CharField(max_length=100)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
