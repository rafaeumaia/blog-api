from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('posts', views.PostListCreate.as_view(), name='post-view-create'),
]