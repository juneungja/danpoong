from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name="word"

urlpatterns = [
    # # path("hello/",helloAPI),
    # path('word/', views.MessageList.as_view()),
    # path("<int:id>/",ManyWord )
     path('category/', CategoryCreate.as_view()),
    path('category/<str:id>', CategoryDetail.as_view()),
    path('', TextCreate.as_view()),
    path('email/',ContactView.as_view() )
]

urlpatterns = format_suffix_patterns(urlpatterns)
