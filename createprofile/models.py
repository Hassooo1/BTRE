from django.db import models
# Create your models here.
class CreateProfile(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    dob = models.DateField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.name