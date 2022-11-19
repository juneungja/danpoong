from django.db import models


import datetime
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, default=True)
    
    def __str__(self):
        return self.category
    
class Message(models.Model):
    nickname = models.CharField(max_length=10, default=True)
    title = models.CharField(max_length=30, default=True)
    category = models.ForeignKey(Category, verbose_name='카테고리', default=False ,on_delete=models.CASCADE)
    text = models.TextField(default=True)
    email = models.CharField(max_length=30, default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
    
    
#이메일을 보내기 위한 모델

class Contact(models.Model):
    email = models.EmailField()
    comment = models.TextField()
    
    class Meta:
        db_table = 'contact'
        
        def __str__(self):
            return self.email


    