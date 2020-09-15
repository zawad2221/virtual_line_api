from django.db import models
from SystemUser.models import SystemUser

# Create your models here.

class PlaceType(models.Model):
    placeTypeNames=(
        ("Pharmacy","Pharmacy"),
        ("Super Shop","Super Shop"),
        ("Resturant","Resturant")
    )
    placeTypeId=models.AutoField(primary_key=True)
    placeTypeName=models.CharField(max_length=55,choices=placeTypeNames)

    def __str__(self):
        return self.placeTypeName

class CheckedUser(models.Model):
    checkedId=models.AutoField(primary_key=True)
    user=models.ForeignKey(SystemUser,on_delete=models.CASCADE)
    def __int__(self):
        return self.checkedId

class PlaceLine(models.Model):
    statusChoices = (
        ("close", "close"),
    ("open", "open")
    
)
    lineId=models.AutoField(primary_key=True)
    lineStatus=models.CharField(max_length=11,choices=statusChoices,default=statusChoices[0][0])
    checkedUser=models.ManyToManyField(CheckedUser,blank=True,null=True)

    

    def __int__(self):
        return self.lineId



class PlaceInformation(models.Model):
    placeId=models.AutoField(primary_key=True)
    placeName=models.CharField(max_length=30)
    placeAddress=models.CharField(max_length=38)
    placeType=models.ForeignKey(PlaceType,on_delete=models.CASCADE)
    placeLongitude=models.CharField(max_length=34)
    placeLatitude=models.CharField(max_length=34)
    placeLine=models.ForeignKey(PlaceLine,on_delete=models.CASCADE)
    owner=models.ForeignKey(SystemUser,on_delete=models.CASCADE,default='1')


    def __str__(self):
        return self.placeName
