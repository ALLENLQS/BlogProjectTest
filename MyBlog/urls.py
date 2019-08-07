"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from app01.views import *

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    path('admin/',admin.site.urls),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^app01/', include('app01.urls')),
    url(r'^$',index),
    url(r'^index/', index),
    url(r'^myArticle/', myArticle),
    url(r'^myArticle_v1/', myArticle_v1),
    url(r'^myPicture/', myPicture),
    url(r'^aboutMe/', aboutMe),
    url(r'^connectMe/', connectMe),
    url(r'^connectMe/(?P<year>\d{4})', connectMe),
    url(r'^api/', Api.as_view()),
    url(r'^aboutMe1/',aboutMe1),
    url(r'^example/',example),

]

urlpatterns += [
    url(r'^vuejsExample/',vuejsExample),
    url(r'^vuePageData/',vuePageData),
    url(r'^vuePageData_v1/',vuePageData_v1),
]
