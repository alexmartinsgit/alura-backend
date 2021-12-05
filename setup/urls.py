from django.contrib import admin
from django.urls import path
from videos.views import videos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', videos),
]
