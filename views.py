from django.shortcuts import render

from django.views.generic import ListView
from .models import Data,Revision,UploadImageTest

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import DataSerializer,ImageSerializer

import json


# Create your views here.
class test(ListView):
    model = Data
    
class ImageViewSet(APIView):
    parser_classes = [FileUploadParser]
    #parser_classes = [MultiPartParser, FormParser]#,JSONParser]
    #parser_classes = [MultiPartParser]
    #queryset = UploadImageTest.objects.all()
    #serializer_class = ImageSerializer

    def post(self, request, format=None):
        print(request.data)
        #serializer = ImageSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_200_OK)
        #else:
        #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #file_obj = request.data['file']
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
        
        
        
        print(request.data)
        image = UploadImageTest.objects.create(file=file_obj)
        return Response(json.dumps({'message': "Uploaded"}), status=200)

        
        
        
 #       file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
 #       image = UploadImageTest.objects.create(image=file_obj)

 #       data = {
 #           'name': request.data.get('image'),
 #           'image': request.data.get('image'), 
 #           }
 #       serializer = ImageSerializer(data=data)
 #       if serializer.is_valid():
 #           serializer.save()
 #           return Response(serializer.data, status=status.HTTP_201_CREATED)

 #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









        
        # ...
        #return Response(json.dumps({'message': "Uploaded"}), status=200)


    #def post(self, request, *args, **kwargs):
    #    file = request.data['file']
    #    image = UploadImageTest.objects.create(image=file)
    #    return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)



    
class DataListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the data items for given requested user
        '''
        kwarg = self.kwargs['revision']
        datas = Data.objects.last()
        serializer = DataSerializer(datas, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        #kwarg = self.kwarg['revision']
        
        data = {
            'revision': Revision.objects.last(),
            'name_data': request.data.get('name_data'), 
            'data_item': request.data.get('data_item')
        }
        serializer = DataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)