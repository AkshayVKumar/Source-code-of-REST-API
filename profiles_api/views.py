from rest_framework.views import APIView
from rest_framework.views import Response

class HelloApiView(APIView):
    #test the API View

    def get(self,request,format=None):
        #returns the list of APIView Features
        an_apiview=[
            'Used HTTP methods as function (get,post,path,put,delete)',
            'It is similar to the django api view',
            'Gives You the most control over application logic',
            'is mapped manually to url'
        ]
        return Response({'message': 'Hello','an_apiview':an_apiview})
        
