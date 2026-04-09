from django.db import models


class Appointment(models.Model):
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.department} ({self.date})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="doctors/")
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name
