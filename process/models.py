from django.db import models

class RegistrationModel(models.Model):
    rno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    otp = models.IntegerField()
    doj = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100,default="pending")

class IndustriesModel(models.Model):
    ino = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

class ProfileModel(models.Model):
    pno = models.AutoField(primary_key=True)
    person = models.OneToOneField(RegistrationModel,on_delete=models.CASCADE)
    education = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="user_images/")
    resume = models.FileField(upload_to="user_resumes/")
    itype = models.ForeignKey(IndustriesModel,on_delete=models.CASCADE)
