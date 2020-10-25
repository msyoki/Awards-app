from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_pic= models.ImageField(upload_to='profilepic/',null=True)
    name= models.CharField(max_length=70)
    bio= models.TextField()
    email=models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    webimage= models.ImageField(upload_to='webimage/',null=True)
    name= models.CharField(max_length=70)
    description= models.TextField()
    link= models.CharField(max_length=200)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name




