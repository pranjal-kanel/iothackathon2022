from rest_framework import serializers

class SuccessSerializer(serializers.Serializer):
    success = serializers.CharField(max_length=200)
    
class UidSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=200)
