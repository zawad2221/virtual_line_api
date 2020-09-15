from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import SystemUser,UserPermission,UserType
from .serializers import SystemUserSerializer,UserPermissionSerializer,RegistrationUserSerializer,UserTypeSerializer

# Create your views here.

@csrf_exempt
def registration(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        print(data['name'])

        permissionData={

        }
        #permissionData['user']

        serializer= RegistrationUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            permissionUser=SystemUser.objects.get(userId=serializer.data['userId'])
            permissionType=UserType.objects.get(typeId='1')
            permissionSave=UserPermission(user=permissionUser,userType=permissionType)
            permissionSave.save()

            # permissionData['user']=serializer.data['userId']
            # # typeSerializer= UserTypeSerializer(UserType.objects.get(typeId='1'))
            # permissionData['userType']="1"
            # permissionSerializer=UserPermissionSerializer(data=permissionData)
            # if permissionSerializer.is_valid():
            #     permissionSerializer.save()
            responseData={}
            responseData["status"]="successfull"
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def giveUserPermission(user,userType):
    userIn=SystemUser.objects.get(userId=user)
    userTy=UserType.objects.get(typeId=userType)
    permissionSave=UserPermission(user=userIn,userType=userTy)
    permissionSave.save()
    return permissionSave.id

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        print(data['phoneNumber'])
        user = SystemUser.objects.get(phoneNumber=data['phoneNumber'],password=data['password'])
        serializer = SystemUserSerializer(user, many=False)
        if serializer.data['phoneNumber']==data['phoneNumber']:
            # permission=UserPermission.objects.all().filter(user=serializer.data['userId'])
            # permissionSerializer = UserPermissionSerializer(permission, many=True)
            # print(permissionSerializer.data)
            print("login success.....................#######")
            return JsonResponse(serializer.data,safe=False, status=200)
        
