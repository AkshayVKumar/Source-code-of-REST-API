from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    #serialized a name field for testing or APIView
    name=serializers.CharField(max_length=10)