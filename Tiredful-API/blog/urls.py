# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# Copyright (C) 2017-2018 Payatu Software Labs
# This file is part of Tiredful API application

app_name = 'blog'

from django.urls import path, include
from . import views

urlpatterns = [

    # ex: /blog/
    path('', views.index, name='index'),

    # ex: /articles/<article-id>
    path('articles/(?P<article_id>[0-9]+)/', views.article, name='articles'),

    # ex: /approve-article/<article_id>
    path('approve-article/(?P<article_id>[0-9]+)/', views.approve_article, name='approve-article'),

]