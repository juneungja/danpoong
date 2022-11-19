# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import APIView, permission_classes
from .models import *
from .serializers import *
from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAdminUser
from django.core.mail.message import EmailMessage
from danpoong import settings
from rest_framework.permissions import AllowAny
import sys
FROM_EMAIL = settings.EMAIL_HOST_USER




# Create your views here.
# @api_view(['GET'])
# def helloAPI(request):
#     return Response("hello world!")


# class MessageListCreateView(ListCreateAPIView):
#     serializer_class = MessageSerializer
#     queryset = Message.objects.all() 

# class MessageList(APIView):
    
#     def get(self, request):
#         messages = Message.objects.all()
#         #여러 개의 객체를 serialization하기 위해 many=true로 설정한다
#         serializer = MessageSerializer(messages, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# # admin사이트에서 등록한 단어를 랜덤으로 get
# @api_view(['GET'])
# def ManyWord(request, id):
#     totalCategory = Category.objects.all()
#     randomCategory = random.sample(list(totalCategory), id)
#     serializer = WordSerializer(randomCategory, many=True)
#     return Response(serializer.data)

class TextCreate(generics.ListCreateAPIView):
    serializer_class = TextSerializer
    queryset = Message.objects.all()

class CategoryCreate(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    lookup_field ='id'
    
    
    
# 메일보내기 위한 view
class ContactView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        c=1
        while c!=0:
            id=1
            serializer = ContactSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            # smtp사용해서 메일보내는 코드
                subject = "["+serializer.data['name']+"]의 문의" # 메일 제목
                queryset = Contact.objects.get(pk=id)
                emailaddress = queryset
                to = [emailaddress] # 문의 내용을 보낼 메일 주소, 리스트 형식
                message = serializer.data['comment'] # 메일 내용
                EmailMessage(subject=subject, body=message, to=to).send() # 메일 보내기
                return Response(serializer.data, status=201)
            ++id
            if id == sys.getsizeof(emailaddress):
                c=0
            return Response(serializer.errors, status=400)
    
    
