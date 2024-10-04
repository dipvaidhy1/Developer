"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from newblog import views
# For imgs and file feild 
from django.conf import settings
from django.conf.urls.static import static
# optional

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage , name="Homepage"),
    path('home/', views.homePage , name="Homepage"),
    path('blog-detail/<int:id>/', views.DeatailsPage , name="Deatailspage"),
    path('add-post/', views.AddPost , name="add-post"),
    # optional
    # path('blog-detail/<int:id>/', views.blog_detail, name='blog_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
