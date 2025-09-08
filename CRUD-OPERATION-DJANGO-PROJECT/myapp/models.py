from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField(unique=True)  # Enforce uniqueness at the database level
    city = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Convert city name to uppercase before saving
        self.city = self.city.upper()
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
