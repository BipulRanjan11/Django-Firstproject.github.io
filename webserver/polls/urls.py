from django.urls import path
from .import views
urlpatterns=[
    path('home/',views.index),
    path('detail/<int:question_id>/',views.detail),
    path('results/<int:question_id>/',views.results),
    path('vote/<int:question_id>/',views.vote)

]