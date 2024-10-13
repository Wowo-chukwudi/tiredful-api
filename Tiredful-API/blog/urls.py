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

from django.urls import path, include
from . import views

urlpatterns = [

    # ex: /blog/
    path(r'^$', views.index, name='index'),

    # ex: /articles/<article-id>
    path(r'^articles/(?P<article_id>[0-9]+)/$', views.article, name='articles'),

    # ex: /approve-article/<article_id>
    path(r'^approve-article/(?P<article_id>[0-9]+)/$', views.approve_article, name='approve-article'),

]