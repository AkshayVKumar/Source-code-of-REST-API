from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    #test the API View
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        #returns the list of APIView Features
        an_apiview=[
            'Used HTTP methods as function (get,post,path,put,delete)',
            'It is similar to the django api view',
            'Gives You the most control over application logic',
            'is mapped manually to url'
        ]
        return Response({'message': 'Hello','an_apiview':an_apiview})
        
    def post(self,request):
        #create a hello message with our name
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        #Handle updating and object
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        #Handle a parial update of an objects
        """Put will modify the entire object or updates the entire object
        Patch will modify the specified indtance in an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        #handles and deletes the specified object
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    #Test Api ViewSet
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        #returns the hello message
        a_viewset=[
            'users actions such as (create,update,partial_update,retrive,destroy)',
            'automatically maps the urls using routers'
            'provides the functionality with less code'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
    
    def create(self,request):
        #create a new hello method
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status='HTTP_400_BAD_REQUEST')
    
    def retrive(self,request,pk=None):
        #retrives the specified object or gets the specified object
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        #updates the specified object
        return Response({'http_method':request.data})
    
    def partial_update(self,request,pk=None):
        #updates the specified data in an object
        return Response({'http_method':'patch'})

    def destroy(self,request,pk=None):
        #deletes the specified object
        return Response({'http_method':'delete'})