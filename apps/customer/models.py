from django.db import models

from common.utils import create_time_stamp


class CustomerModel(models.Model):

    class Meta:
        db_table = 'customer'
        verbose_name = '客户信息 端信息和分数信息'

    client_name = models.CharField(max_length=64, verbose_name='客户端名称')
    score = models.BigIntegerField(verbose_name='分数')

    create_time = models.BigIntegerField(default=create_time_stamp, verbose_name='创建时间')
    update_time = models.BigIntegerField(default=create_time_stamp, verbose_name='更新时间')
