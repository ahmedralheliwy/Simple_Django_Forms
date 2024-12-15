from django.db import models

# Create your models here.
class Sign_Up(models.Model):
    username=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    checkbox=models.BooleanField(verbose_name='Policies',null=True)

    def __str__(self):
        return self.username if self.username else "unnamed"
    