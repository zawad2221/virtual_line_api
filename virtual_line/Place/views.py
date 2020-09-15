from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import PlaceTypeSerializer,PlaceInformationSerializer,PlaceLineSerializer
from .models import PlaceType,PlaceInformation,PlaceLine,CheckedUser
from SystemUser.models import SystemUser
from SystemUser.views import giveUserPermission

# Create your views here.

@csrf_exempt
def getPlaceType(request):
    if request.method=="GET":
        placeType=PlaceType.objects.all()
        placeTypeSerializer=PlaceTypeSerializer(placeType,many=True)
        return JsonResponse(placeTypeSerializer.data,safe=False,status=200)
    data={
        "response":"failed"
    }
    return JsonResponse(data,safe=False,status=400)

@csrf_exempt
def getAllPlace(request):
    if request.method=="GET":
        print("place info33333333333")
        placeInfo=PlaceInformation.objects.all()
        
        placeSerializer=PlaceInformationSerializer(placeInfo,many=True)
        return JsonResponse(placeSerializer.data,status=200,safe=False)

@csrf_exempt
def getPlaceByOwner(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        ownerPlace=PlaceInformation.objects.filter(owner=data['userId'])
        placeSerializer=PlaceInformationSerializer(ownerPlace,many=True)
        return JsonResponse(placeSerializer.data,status=200,safe=False)

@csrf_exempt
def getPlaceById(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        place=PlaceInformation.objects.get(placeId=data['placeId'])
        placeSerializer=PlaceInformationSerializer(place,many=False)
        return JsonResponse(placeSerializer.data,status=200,safe=False)

        

@csrf_exempt
def addPlace(request):
    if request.method=="POST":
        line=PlaceLine(lineStatus="close")
        line.save()
        
        data=JSONParser().parse(request)
        
        data['placeLine']=line.lineId
        try:
            data['placeType']=data['placeType']['placeTypeId']
        except:
            print("place type dont requred reasign")

        
        placeSerializer=PlaceInformationSerializer(data=data)
        if placeSerializer.is_valid():
            placeSerializer.save()
            giveUserPermission(data['owner'],'2')
            return JsonResponse(placeSerializer.data,status=200)
        return JsonResponse(placeSerializer.errors,status=400)

@csrf_exempt
def changeLineStatus(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        line=PlaceLine.objects.filter(lineId=data['lineId']).update(lineStatus=data['lineStatus'])
        pk=data['lineId']
        del data['lineId']
        # lineSerializer=PlaceLineSerializer(instance=line,data=data)
        # if lineSerializer.is_valid():
        #     lineSerializer.save()
        if data['lineStatus']=='close':
            CheckedUser.objects.filter(placeline__lineId=pk).delete()
        return JsonResponse(data,status=200)

@csrf_exempt
def removeUserFromLine(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        CheckedUser.objects.filter(checkedId=data['checkedId']).delete()
        return JsonResponse({"response":"deleted"},status=200)

@csrf_exempt
def addUserInLine(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        lineId=data['lineId']
        userId=""
        for d in data['checkedUser']:
            userId=d['user']['userId']
        print(lineId,userId)
        user=SystemUser.objects.get(userId=userId)
        checkedUser=CheckedUser(user=user)
        checkedUser.save()
        line=PlaceLine.objects.get(lineId=lineId).checkedUser.add(checkedUser)
        return JsonResponse({"response":"checked"},status=200)
