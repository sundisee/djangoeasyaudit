#!/usr/bin/env python
# encoding: utf-8
import logging

from rest_framework import serializers
from .models import CRUDEvent, LoginEvent, RequestEvent


logger = logging.getLogger('django')


class CRUDEventSerializer(serializers.ModelSerializer):
    """
    CURD事件序列化类 - get(列表, 详情) post(修改, 创建)
    """
    class Meta:
        model = CRUDEvent
        fields = '__all__'


class LoginEventSerializer(serializers.ModelSerializer):
    """
    登录登出序事件列化类 - get(列表, 详情) post(修改, 创建)
    """
    class Meta:
        model = LoginEvent
        fields = '__all__'

class RequestEventSerializer(serializers.ModelSerializer):
    """
    浏览序事件列化类 - get(列表, 详情) post(修改, 创建)
    """
    class Meta:
        model = RequestEvent
        fields = '__all__'
