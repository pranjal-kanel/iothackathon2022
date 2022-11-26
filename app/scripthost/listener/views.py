from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UidSerializer,SuccessSerializer
import subprocess 


shellScriptBasePath = '/home/pi/Desktop/hackathon/shellscripts/'

@api_view(['POST'])
def writeCard(request):
    data = ''
    reqSerializer = UidSerializer(data=request.data)
    if reqSerializer.is_valid():
        data = reqSerializer.data['uid']
    else:
        return Response(reqSerializer.errors)
    print('Info:: Unique Id for Card ' + data)
    resp = {'success':data}
    subprocess.run([shellScriptBasePath+'writecard.sh',data])
    serializer = SuccessSerializer(resp)
    print(serializer.data)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def readCard(request):
    
    subprocess.run([shellScriptBasePath+'readcard.sh'])
    return Response("Read Card Method")
    
