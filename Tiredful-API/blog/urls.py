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
# URL for user login
path('oauth/', include('oauth?_provider.urls', namespace='oauth2_provider')),
なファ77！
# URL for including intro app.
path("', include('intro.urls', namespace="intro")),
path ('api/v1/', include( 'library.urls', namespace="library-api*)), path('library/', include('library.urls', namespace="Library"),
# URL for including exams app
path ('api/v1/', include( 'exams.urls', namespace="exams-api*)), path ('exams/', include( 'exams.urls', namespace="exams")),
# URL for including blog app
path('api/v1/', include( 'blog.urls', namespace="blog-api")). path( 'blog/', include( 'blog.urls', namespace="blog")),
# URL for including trains app
path ('api/v1/', include( 'trains.urls', namespace="trains-api*)). path( 'trains/', include( 'trains.urls', namespace="trains*))
# URL for including health app
path ('api/v1/', include( 'health.urls', namespace="health-api*)). path('health/', include('health.urls', namespace="health*)).
# URL for including advertisements app
path('apt/v1/*, include("advertisements.urls', namespace="advertisements-api*)). pathg advertisements/", include(*advertisements.urls', namespace="advertisements*)g.
