import datetime

import web.models
from web.models import customer, administrator, status, court
from django.http import HttpResponse


def customer_insert(request):
    mobile = request.GET.get('mobile')
    name = request.GET.get('name')
    age = request.GET.get('age')
    sex = request.GET.get('sex')
    try:
        customer.objects.get(mobile=mobile)
    except web.models.customer.DoesNotExist:
        cust = customer(mobile=mobile, name=name,
                        age=age, sex=sex)
        cust.save()
        return HttpResponse("顾客" + mobile + "插入成功")
    return HttpResponse("顾客" + mobile + "已存在")


def customer_select(request):
    sel = request.GET.get('mobile')
    sql = f"select * from customer where mobile='{sel}'"
    # django 执行原生的sql语句
    result = customer.objects.raw(sql)

    # result = customer.objects.filter(mobile=request.GET.get('mobile'))
    """
    result为<class 'django.db.models.query.QuerySet'>的对象
    需要进行数据处理
    """
    arr = []
    for i in result:
        content = {'手机': i.mobile, '姓名': i.name, '年龄': i.age, '性别': i.sex}
        arr.append(content)
    print(arr)
    print(type(arr))
    return HttpResponse(arr)


def customer_modify(request):
    try:
        cust = customer.objects.get(mobile=request.GET.get('mobile'))
    except web.models.customer.DoesNotExist:
        return HttpResponse("不存在此人，无法修改！")
    if request.GET.get('name'):
        cust.name = request.GET.get('name')
    if request.GET.get('age'):
        cust.age = request.GET.get('age')
    if request.GET.get('sex'):
        cust.sex = request.GET.get('sex')
    cust.save()
    mp = {'手机': cust.mobile, '姓名': cust.name, '年龄': cust.age, '性别': cust.sex}
    arr = [mp]
    return HttpResponse(arr)


def customer_delete(request):
    mobile = request.GET.get('mobile')
    try:
        cust = customer.objects.get(mobile=mobile)
        cust.delete()
    except web.models.customer.DoesNotExist:
        return HttpResponse(mobile + "查无此人！")
    return HttpResponse(mobile + "删除成功！")


def administrator_insert(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    age = request.GET.get('age')
    sex = request.GET.get('sex')
    mobile = request.GET.get('mobile')
    try:
        administrator.objects.get(id=id)
    except web.models.administrator.DoesNotExist:
        admin = administrator(id=id, mobile=mobile, name=name,
                              age=age, sex=sex)
        admin.save()
        return HttpResponse("管理人员" + id + "插入成功")
    return HttpResponse("管理人员" + id + "已存在")


def administrator_select(request):
    sel = request.GET.get('id')
    sql = f"select * from administrator where id='{sel}'"
    # django 执行原生的sql语句
    result = administrator.objects.raw(sql)
    arr = []
    for i in result:
        content = {'编号': i.id, '姓名': i.name, '年龄': i.age, '性别': i.sex, '手机': i.mobile}
        arr.append(content)
    print(arr)
    print(type(arr))
    return HttpResponse(arr)


def administrator_modify(request):
    try:
        admin = administrator.objects.get(id=request.GET.get('id'))
    except web.models.administrator.DoesNotExist:
        return HttpResponse("不存在此人，无法修改！")
    if request.GET.get('name'):
        admin.name = request.GET.get('name')
    if request.GET.get('age'):
        admin.age = request.GET.get('age')
    if request.GET.get('sex'):
        admin.sex = request.GET.get('sex')
    if request.GET.get('mobile'):
        admin.mobile = request.GET.get('mobile')
    admin.save()
    mp = {'编号': admin.id, '姓名': admin.name, '年龄': admin.age, '性别': admin.sex, '手机': admin.mobile}
    arr = [mp]
    return HttpResponse(arr)


def administrator_delete(request):
    id = request.GET.get('id')
    try:
        admin = administrator.objects.get(id=id)
        admin.delete()
    except web.models.administrator.DoesNotExist:
        return HttpResponse(id + "查无此人！")
    return HttpResponse(id + "删除成功！")


def court_insert(request):
    id = request.GET.get('id')
    location = request.GET.get('location')
    service_start_time = request.GET.get('start')
    service_end_time = request.GET.get('end')
    try:
        crt = court.objects.get(id=id)
    except court.DoesNotExist:
        crt = court(id=id, location=location, service_start_time=service_start_time, service_end_time=service_end_time)
        crt.save()
        return HttpResponse(
            [{'球场编号': id, '位置': location, '开始运营时间': service_start_time, '结束运营时间': service_end_time}])
    return HttpResponse(id + '已存在')


def court_select(request):
    sel = request.GET.get('id')
    sql = f"select * from court where id='{sel}'"
    # django 执行原生的sql语句
    result = court.objects.raw(sql)
    arr = []
    for i in result:
        content = {'球场编号': i.id, '球场位置': i.location, '运营开始时间': i.service_start_time,
                   '运营结束时间': i.service_end_time}
        arr.append(content)
    print(arr)
    print(type(arr))
    return HttpResponse(arr)


def court_modify(request):
    try:
        crt = court.objects.get(id=request.GET.get('id'))
    except web.models.customer.DoesNotExist:
        return HttpResponse("不存在此场，无法修改！")
    if request.GET.get('location'):
        crt.location = request.GET.get('location')
    if request.GET.get('start'):
        crt.service_start_time = request.GET.get('start')
    if request.GET.get('end'):
        crt.service_end_time = request.GET.get('end')
    crt.save()
    arr = [{'编号': crt.id, '位置': crt.location, '运营开始时间': crt.service_start_time,
            '运营结束时间': crt.service_end_time}]
    return HttpResponse(arr)


def court_delete(request):
    id = request.GET.get('id')
    try:
        crt = court.objects.get(id=id)
        crt.delete()
    except court.DoesNotExist:
        return HttpResponse(id + "查无此场！")
    return HttpResponse(id + "删除成功！")


def status_display(request):
    #展示某年某月某日的球场安排情况
    time = request.GET.get('time').split('-')
    time = [int(i) for i in time]
    sql = f'select * from status where ' \
          f'occupy_year={time[0]} and' \
          f'occupy_month={time[1]} and' \
          f'occupy_date={time[2]}'

    return

def status_insert(request):
    id = request.GET.get('id')
    customer = request.GET.get('customer')
    administrator = request.GET.get('admin')
    #时间格式：2022-1-4-9(表示2022年1月4号9点-10点时间段)
    #年，月，日，时
    start = request.GET.get('start').split('-')
    start = [int(i) for i in start]
    end = request.GET.get('end').split('-')
    end = [int(i) for i in end]
    sql = 'select * from status where '

    return  HttpResponse(start)