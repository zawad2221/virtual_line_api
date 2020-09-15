from rest_framework import serializers
from SystemUser.models import SystemUser

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model=SystemUser
        fields=['name','phoneNumber','password']

    def save(self):
        systemUser= SystemUser(
            name=self.validated_data['name'],
            phoneNumber=self.validated_data['phoneNumber'],
            password=self.validated_data['password']
        )
        