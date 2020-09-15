from django.db import models

# Create your models here.
class UserType(models.Model):

    typeId=models.AutoField(primary_key=True)
    typeName=models.CharField( max_length=50,null=False)    



    def __int__(self):
        return self.typeId


class SystemUser(models.Model):

    userId=models.AutoField(primary_key=True)
    name=  models.CharField( max_length=50)
    phoneNumber=models.CharField( max_length=50, unique=True)
    password=models.CharField(max_length=60)
    

    def __int__(self):
        return self.userId

class UserPermission(models.Model):
    
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(SystemUser, related_name='permission',on_delete=models.CASCADE)
    userType=models.ForeignKey(UserType,related_name='type',on_delete=models.CASCADE)
    def __int__(self):
        return self.id