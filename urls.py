#!/usr/bin/env python
# encoding: utf-8
from django.urls import path
from .views import CRUDEventListView, CRUDEventDetailView, \
    LoginEventListView, LoginEventDetailView, RequestEventListView, RequestEventDetailView


urlpatterns = [
    path('crudevent/', CRUDEventListView.as_view(), name='crudevent-list'),
    path('crudevent/<int:pk>/', CRUDEventDetailView.as_view(), name='crudevent-detail'),
    path('loginevent/', LoginEventListView.as_view(), name='loginevent-list'),
    path('loginevent/<int:pk>/', LoginEventDetailView.as_view(), name='loginevent-detail'),
    path('requestevent/', RequestEventListView.as_view(), name='requestevent-list'),
    path('requestevent/<int:pk>/', RequestEventDetailView.as_view(), name='requestevent-detail'),

]