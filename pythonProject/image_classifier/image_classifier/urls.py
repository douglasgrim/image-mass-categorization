"""
URL configuration for image_classifier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path


from django.contrib import admin
from django.urls import path

from website.views import welcome, date, about
from meetings.views import detail, rooms_list, roomdetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path('date', date),
    path('home', welcome, name="home"),
    path('', welcome, name="homebase"),
    path('about', about),
    path('meetings/<int:id>', detail, name="detail"),
    path('rooms', rooms_list, name="rooms_list"),
    path('rooms/<int:id>', roomdetail, name="roomdetail")
]
