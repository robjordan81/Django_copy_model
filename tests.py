from django.test import TestCase

from .models import User,Project,Revision,Data,DataExtra

from rest_framework.test import APIRequestFactory
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import DataSerializer

# Create your tests here.

class UserTest (TestCase):
    def setUp(self):
        User.objects.create(
            name='Rob Jordan')
        #Project.objects.create(
        #    name_project='test_project')
        
        Revision.objects.create(
            rev = 0,
            name_project='test_project')
        revision = Revision.objects.get(id=1)        

        Data.objects.create(
            revision=revision,
            name_data="data1",
            data_item=1)  
        Data.objects.create(
            revision=revision,
            name_data="data2",
            data_item=2)  
        data = Data.objects.get(id=1)
        
        DataExtra.objects.create(
            revision=revision,
            data=data,
            name_data_ex="data1ex",
            data_item_ex=1) 
        
        #print (revision.data_set.all())
        #print ("duplicating")
        revision.duplicate()
        #print (Revision.objects.all())
        #print (Data.objects.all())
        #print (DataExtra.objects.all()) 
        #print (Project.objects.all())
        

        
        
    def testrev(self):
        rev_obj = Revision.objects.get(id=1)        
        self.assertEqual(rev_obj.rev,0)
        self.assertEqual(rev_obj.name_project,'test_project')
        
        rev_obj = Revision.objects.get(id=2)
        self.assertEqual(rev_obj.rev,1)
        
        proj_obj = Project.objects.get(id=1)
        self.assertEqual(proj_obj.name_project,'test_project')
        proj_obj = Project.objects.get(id=2)
        self.assertEqual(proj_obj.name_project,'test_project')
        
    def testapi(self):
        factory = APIRequestFactory()
        response = factory.get('/api/1')
        pk = Revision.objects.last().pk
        print(pk)
        #response = self.client.get('/api/'+ str(pk))
        #response = self.client.get('/api/0')

        #print(Response(serializer.data))
        print("response")
        print(response)
        #self.assertEqual(response, '{"revision":0}')
        