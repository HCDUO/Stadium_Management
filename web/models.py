from django.db import models

# Create your models here.

from django.db import models

"""
    创建如下几个表的字段
"""


class customer(models.Model):
    # 手机 unique=True 该字段唯一，为主键
    mobile = models.CharField('手机', primary_key=True, max_length=20)
    # 姓名 字符串 最大长度20 不为空
    name = models.CharField('姓名', max_length=20)
    # 年龄 整数 null=False, 表示该字段不能为空
    age = models.IntegerField('年龄', null=True)
    # 性别 布尔类型 默认True: 男生 False:女生
    sex = models.BooleanField('性别', default=True, null=True)

    class Meta:
        db_table = 'customer'


class court(models.Model):
    # 球场编号
    id = models.IntegerField('编号', primary_key=True)
    # 球场位置
    location = models.CharField('位置', max_length=20)
    # 时间采用左端点包含后边一小时
    # 球场当天运营开始时间
    service_start_time = models.IntegerField('开始时间', null=False)
    # 球场当天运营结束时间
    service_end_time = models.IntegerField('结束时间', null=False)

    class Meta:
        db_table = 'court'


class administrator(models.Model):
    # 管理人员编号
    id = models.IntegerField('编号', primary_key=True)
    # 姓名 字符串 最大长度20 不为空
    name = models.CharField('姓名', max_length=20, null=False)
    # 年龄 整数 null=False, 表示该字段不能为空
    age = models.IntegerField('年龄', null=True)
    # 性别 布尔类型 默认True: 男生 False:女生
    sex = models.BooleanField('性别', null=True)
    # 手机
    mobile = models.CharField('手机', max_length=20, null=False)

    class Meta:
        db_table = 'administrator'


# 预定表单
class status(models.Model):
    # 每一条记录是1h
    # 自增主键防重复
    # 球场编号
    court_id = models.IntegerField('球场编号')
    # 管理人员编号
    administrator_id = models.IntegerField('管理人员编号')
    # 预定人员手机号
    customer = models.CharField('预定人员手机号', max_length=20)
    # 被占用年份
    occupy_year = models.IntegerField('开始年份', null=True)
    # 被占用月份
    occupy_month = models.IntegerField('开始月份', null=True)
    # 被占用日期
    occupy_date = models.IntegerField('开始日期', null=True)
    # 被占用时间
    occupy_hour = models.IntegerField('开始时间', null=True)
    class Meta:
        db_table = 'status'