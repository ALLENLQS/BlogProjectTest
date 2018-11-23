#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : ALLEN
# @Time    : 2018/11/1 22:49
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from app01.views import *

urlpatterns = [
    url(r'^$', index),
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