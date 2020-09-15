from rest_framework import serializers
from .models import PlaceType,PlaceInformation,PlaceLine,CheckedUser
from SystemUser.models import SystemUser
from SystemUser.serializers import SystemUserSerializer

class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)



class PlaceTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=PlaceType
        fields="__all__"

class CheckedUserSerializer(serializers.ModelSerializer):
    user=RelatedFieldAlternative(queryset=SystemUser.objects.all(),serializer=SystemUserSerializer)
    class Meta:
        model=CheckedUser
        fields='__all__'
    depth=1

class PlaceLineSerializer(serializers.ModelSerializer):

    checkedUser=CheckedUserSerializer(many=True)
    
    class Meta:
        model=PlaceLine
        fields='__all__'

class PlaceInformationSerializer(serializers.ModelSerializer):

    placeId=serializers.IntegerField(required=False)
    placeType=RelatedFieldAlternative(queryset=PlaceType.objects.all(),serializer=PlaceTypeSerializer)
    placeLine=RelatedFieldAlternative(queryset=PlaceLine.objects.all(),serializer=PlaceLineSerializer)
    
   
    class Meta:
        model=PlaceInformation
        fields=['placeId','placeName','placeAddress','placeLongitude','placeLatitude','placeType','placeLine','owner']
    
    depth=2
    read_only_fields=('placeType','placeLine','owner')



