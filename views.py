#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

try:
    from utils.CustomBaseView import MyListCreateView, MyRetrieveUpdateAPIView
    from utils.permissions import CustomAddPermission
except:
    from rest_framework.generics import ListCreateAPIView as MyListCreateView, \
        RetrieveUpdateAPIView as MyRetrieveUpdateAPIView
    from rest_framework.permissions import BasePermission as CustomAddPermission

from .models import CRUDEvent, LoginEvent, RequestEvent
from .serializers import CRUDEventSerializer, LoginEventSerializer, RequestEventSerializer


class CRUDEventFilter(filters.FilterSet):
    creator = filters.CharFilter(field_name='user__first_name', lookup_expr='icontains')
    event_type = filters.CharFilter(lookup_expr='icontains')
    app_name = filters.CharFilter(field_name='content_type__app_label', lookup_expr='icontains')
    object_id = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(field_name='object_json_repr', lookup_expr='icontains')
    start_date = filters.DateFilter(field_name='datetime__date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='datetime__date', lookup_expr='lte')


class CRUDEventListView(MyListCreateView):
    """
    操作日志 - 列表和创建接口
    """
    queryset = CRUDEvent.objects.order_by("-datetime")
    serializer_class = CRUDEventSerializer
    permission_classes = (IsAuthenticated, CustomAddPermission)
    permission_codes = {
        "GET": "crudevent-list",
    }

    # 使用过滤器
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CRUDEventFilter


class CRUDEventDetailView(MyRetrieveUpdateAPIView):
    """
    操作日志 - 列表和创建接口
    """
    queryset = CRUDEvent.objects.all()
    serializer_class = CRUDEventSerializer
    permission_classes = (IsAuthenticated, CustomAddPermission)
    permission_codes = {
        "GET": "crudevent-detail",
    }


class LoginEventListView(MyListCreateView):
    """
    操作日志 - 列表和创建接口
    """
    queryset = LoginEvent.objects.order_by("-datetime")
    serializer_class = LoginEventSerializer
    permission_classes = (IsAuthenticated, CustomAddPermission)
    permission_codes = {
        "GET": "loginevent-list",
    }

    # 使用过滤器
    filter_backends = (filters.DjangoFilterBackend,)


class LoginEventDetailView(MyRetrieveUpdateAPIView):
    """
    操作日志 - 列表和创建接口
    """
    queryset = LoginEvent.objects.all()
    serializer_class = LoginEventSerializer
    permission_classes = (IsAuthenticated, CustomAddPermission)
    permission_codes = {
        "GET": "loginevent-detail",
    }

class RequestEventListView(MyListCreateView):
    """
    操作日志 - 列表和创建接口
    """
    queryset = RequestEvent.objects.order_by("-datetime")
    serializer_class = RequestEventSerializer
    permission_classes = (IsAuthenticated, CustomAddPermission)
    permission_codes = {
        "GET": "requestevent-list",
    }

    # 使用过滤器
    filter_backends = (filters.DjangoFilterBackend,)


class RequestEventDetailView(MyRetrieveUpdateAPIView):
    """
    操作日志 - 列表和创建接口
    """
    queryset = RequestEvent.objects.all()
    serializer_class = RequestEventSerializer
    permission_classes = (IsAuthenticated, CustomAddPermission)
    permission_codes = {
        "GET": "requestevent-detail",
    }
