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

app_name = 'exams'

from django.urls import path, include
from . import views

urlpatterns = [

    # ex: /exams/
    path('', views.index, name='index'),

    # ex: /exams/score_card>
    path('exams/(?P<score_card>[0-9-=A-Za-z]+)/', views.get_score, name='exams'),
]
