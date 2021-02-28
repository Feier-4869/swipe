import re
import requests





from django.http import request, JsonResponse
from django.shortcuts import render
from swiper.user import error, config
from swiper.user.common import render_json,send_sms_celery


# Create your views here.

from .common import gen_code
def send_sms(request):
    # １获取参数

    phone = request.POST.get('phone')

    # ２判断参数
    # 2.1不能为空
    if not all([phone]):
        return render_json({'code': 1000, 'data': '手机号不能为空'})
    # 2.2格式是否正确
    if not re.match(r'^1[3456789]\d{9}$', phone):
        return render_json({'code': 1001, 'data': '手机号格式不正确'})

    # ３异步执行发送短信的任务
    send_sms_celery.delay(phone)

# 登录
def login(request):
    # １．获取参数数据
    phone=request.POST.get('phone')
    code=request.POST.get('code')
    # ２．判断数据
    # 2.1判断验证码是否正确
    
    # 2.2判断手机号码和验证码不能为空
    if not all([phone,code]):
        return JsonResponse(error.PHONE_SMS_NOT_EMPTY,'手机号和密码不能为空')
    # 2.3判断手机格式是否正确
    if not re.match(r'^1[3456789]\d{9}$', phone):
        return JsonResponse(error.PHONE_NOT_FORMAT,'手机号格式不正确')

# ３．处理逻辑
    # ４．返回响应
    