from rest_framework import serializers
from .models import SystemUser,UserPermission,UserType

class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserType
        fields = ['typeId','typeName']

class RegistrationUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SystemUser
        fields = ['userId','name','phoneNumber','password']


class UserPermissionSerializer(serializers.ModelSerializer):
    
    userType=UserTypeSerializer(many=False,read_only=True)
    
    class Meta:
        model = UserPermission
        fields = ['id','user','userType']

class SystemUserSerializer(serializers.ModelSerializer):

    permission=UserPermissionSerializer(many=True,read_only=True)
    #permission=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    #userId=serializers.IntegerField(required=False)
   
    #userType=serializers.PrimaryKeyRelatedField(queryset=UserType.objects.all(), many=True)
    
    class Meta:
        model = SystemUser
        fields = ['userId','name','phoneNumber','permission']
        # depth=2