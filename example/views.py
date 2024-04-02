from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Device
from .serializers import DeviceSerializer

@api_view(['GET', 'POST'])

def device_list(request):
    '''GET all devices
       POST new device
    '''
    
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer_device_list = DeviceSerializer(devices, many=True)
        print(serializer_device_list)
        return JsonResponse({'devices': serializer_device_list.data}, safe=False)
    
    if request.method == 'POST':
        serializer_device = DeviceSerializer(data=request.data)
        if serializer_device.is_valid():
            try:
                serializer_device.save()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer_device.data, status=status.HTTP_201_CREATED)
        
# ---
        
@api_view(['DELETE'])

def delete_device(request, id):
    '''GET all devices
       POST new device
    '''

    try:
        device = Device.objects.get(id=id)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    