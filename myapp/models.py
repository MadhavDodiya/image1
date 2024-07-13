from django.db import models

# Create your models here.
class imageupload(models.Model):
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image')
    
    def __str__(self):
        return self.name