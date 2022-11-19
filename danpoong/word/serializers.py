from rest_framework import serializers
from .models import *

class TextSerializer(serializers.ModelSerializer):
    # Word모델 데이터가 주어지면 모델안의 애트리뷰트가 JSON데이터로 변환된다
    class Meta:
        model = Message
        fields = '__all__'
        
    def create(self, validated_data):
        data = Message.objects.create(**validated_data)
        return data
   
        
        
class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'
    def create(self, validated_data):
        data = Category.objects.create(**validated_data)
        return data
    
    
#메일 전송을 위한 시리얼
class ContactSerializer(serializers.Serializer):
    
    class Meta:
        model = Contact
        fields = '__all__'

