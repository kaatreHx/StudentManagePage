"""
URL configuration for NewProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Project.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('insert/', insert, name="insert"),
    path('update/<int:id>', update, name="update"),
    path('showList', allData, name="showList"),
    path('student/<int:id>', studentData),
    path('studentDelete/<int:id>', deleteStudent, name="deleteStudent"),
    path('landingPage', renderPage),
    path('searchData', searchData, name="searchData")

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
