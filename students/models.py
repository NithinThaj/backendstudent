from django.db import models



class Student(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  email = models.EmailField(unique=True)
  street = models.CharField(max_length=255)
  state = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  pincode = models.CharField(max_length=6)
  subjects = models.JSONField(default=list)

  def _str_(self):
    return f"{self.first_name} {self.last_name}"