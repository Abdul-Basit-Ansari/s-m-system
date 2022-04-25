"""managment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mgsystem import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name='index'),
    path('adddata', views.adddata ,name='adddata'),
    path('editinfo', views.editinfo ,name='editinfo'),
    path('signup', views.signup ,name='signup'),
    path('login', views.userlogin ,name='login'),
    path('logout', views.userlogout ,name='logout'),
    path('datalist', views.datalist ,name='datalist'),
    path('student/<int:sno>', views.student ,name='student'),
    path('report', views.report ,name='report'),
    path('contactus', views.contactus ,name='contactus'),
    path('about', views.about ,name='about'),
    path('isdelete/<int:sno>', views.isdelete ,name='isdelete'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
print(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))
