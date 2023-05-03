from rest_framework import serializers
from .models import Data, UploadImageTest
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['revision','name_data','data_item']
        
        
        #https://stackoverflow.com/questions/28036404/django-rest-framework-upload-image-the-submitted-data-was-not-a-file
   
        
        
        
class ImageSerializer(serializers.ModelSerializer):
    #file = Base64ImageField(
    #    max_length=None, use_url=True,
    #)
    
    class Meta:
        model = UploadImageTest
        #fields = ['name', 'file']
        fields = ['file']
        #fields = "__all__"