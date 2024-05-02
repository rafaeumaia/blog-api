from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

apps_urlpatterns = [
    path('post/', include('apps.post.urls')),
]
