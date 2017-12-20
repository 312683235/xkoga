"""HHHHH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from he import views
from django.views.static import serve
from HHHHH.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/', views.Index.as_view(),name='index'),
    url(r'^register/', views.Register.as_view(),name='register'),
    url(r'^registerverif/', views.RegisterVerif.as_view(),name='registerverif'),
    url(r'^sendemail/', views.SendEmail.as_view(),name='sendemail'),
    url(r'^base/', views.Base.as_view(),name='base'),
    url(r'^login/', views.LoginView.as_view(),name='login'),
    url(r'^userinfo/', views.Userinfo.as_view(),name='userinfo'),
    url(r'^edit-(\w+)/', views.Edit.as_view()),
    url(r'^logout/', views.Logout.as_view(),name='logout'),
    url(r'^publish/', views.Publish.as_view(),name='publish'),
    url(r'^consultation/', views.Consultation.as_view(),name='consultation'),
    url(r'^server-(\d+)/', views.Server.as_view(),name='server'),
    url(r'^serverlist/', views.ServerList.as_view(),name='serverlist'),
    url(r'^consultation-(\d+)/', views.Consultation.as_view(),name='consultation'),
    url(r'^consultationlist/', views.ConsultationList.as_view(),name='consultationlist'),
    url(r'^comment/', views.Comment.as_view()),
    url(r'^mechanismlist-(\d+)/', views.Mechanism.as_view()),
    url(r'^mechanismlist/', views.MechanismList.as_view(),name='mechanismlist'),
    url(r'^publiclist/', views.PublicList.as_view(),name='publiclist'),
    url(r'^public-(\d+)/', views.Public.as_view(),name='public'),
    #上传文件处理
    url(r'^uploads/(?P<path>.*)$', serve,{'document_root':MEDIA_ROOT}),
]