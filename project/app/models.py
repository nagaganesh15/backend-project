from django.db import models

class User(models.Model):
    username=models.CharField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField()
    # profileimage=models.ImageField(upload_to='profileimage/', null=True, blank=True)
    profileimage = models.ImageField(upload_to='profile_images/', null=True, blank=True,default='default/defaultprofileimage.jpeg')
    memoryscore=models.IntegerField(default=0)
    memoryproof=models.ImageField(upload_to='memoryproofs/',default='default/defaultprofileimage.jpeg',null=True, blank=True)
    stonescore=models.IntegerField(default=0)
    stoneproof=models.ImageField(upload_to='stoneproofs/',default='default/defaultprofileimage.jpeg',null=True, blank=True)
    guessscore=models.IntegerField(default=0)
    guessproof=models.ImageField(upload_to='guessproofs/',default='default/defaultprofileimage.jpeg',null=True, blank=True)
    waterscore=models.IntegerField(default=0)
    waterproof=models.ImageField(upload_to='waterproofs/',default='default/defaultprofileimage.jpeg',null=True, blank=True)
    brickscore=models.IntegerField(default=0)
    brickproof=models.ImageField(upload_to='brickproofs/',default='default/defaultprofileimage.jpeg',null=True, blank=True)

    def __str__(self):
        return self.username

class Memorygame(models.Model):
    profileimage=models.ImageField()
    profilename=models.CharField()
    memoryscore=models.IntegerField()
    memoryproof = models.ImageField(upload_to='memoryproofs/')

    def __str__(self):
        return self.profilename

# Create your models here.
