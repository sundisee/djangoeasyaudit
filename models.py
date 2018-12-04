from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class CRUDEvent(models.Model):
    CREATE = 1
    UPDATE = 2
    DELETE = 3
    M2M_CHANGE = 4
    M2M_CHANGE_REV = 5

    TYPES = (
        (CREATE, '新增'),
        (UPDATE, '修改'),
        (DELETE, '删除'),
        (M2M_CHANGE, '多对多关系修改'),
        (M2M_CHANGE_REV, 'Reverse Many-to-Many Change'),
    )

    event_type = models.SmallIntegerField(verbose_name='操作方法', choices=TYPES)
    object_id = models.IntegerField(verbose_name='被操作对象ID',)  # we should try to allow other ID types
    content_type = models.ForeignKey(ContentType, verbose_name='操作模块',  on_delete=models.CASCADE)
    object_repr = models.CharField(verbose_name='模块描述', max_length=255, null=True, blank=True)
    object_json_repr = models.TextField(verbose_name='操作内容', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='操作人',  null=True, blank=True, on_delete=models.SET_NULL)
    user_pk_as_string = models.CharField(max_length=255, null=True, blank=True,
                                         help_text='String version of the user pk')
    datetime = models.DateTimeField(verbose_name='操作时间', auto_now_add=True)

    def is_create(self):
        return self.CREATE == self.event_type

    def is_update(self):
        return self.UPDATE == self.event_type

    def is_delete(self):
        return self.DELETE == self.event_type

    class Meta:
        verbose_name = 'CRUD event'
        verbose_name_plural = 'CRUD events'
        ordering = ['-datetime']
        index_together = ['object_id', 'content_type', ]


class LoginEvent(models.Model):
    LOGIN = 0
    LOGOUT = 1
    FAILED = 2
    TYPES = (
        (LOGIN, 'Login'),
        (LOGOUT, 'Logout'),
        (FAILED, 'Failed login'),
    )
    login_type = models.SmallIntegerField(choices=TYPES)
    username = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    remote_ip = models.CharField(max_length=50, null=True, db_index=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'login event'
        verbose_name_plural = 'login events'
        ordering = ['-datetime']


class RequestEvent(models.Model):
    url = models.CharField(max_length=255, null=False, db_index=True)
    method = models.CharField(max_length=20, null=False, db_index=True)
    query_string = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    remote_ip = models.CharField(max_length=50, null=True, db_index=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'request event'
        verbose_name_plural = 'request events'
        ordering = ['-datetime']