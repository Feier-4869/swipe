import random


import requests
from django.http import JsonResponse

from swiper.worker.tasks import celery_app
from swiper.user import config, error




def gen_code(num):
    start=10**(num-1)
    end=10**num-1

    return random.randint(start,end)


def render_json(code=0,data=None):
    return JsonResponse({'code':code,'data':data})

@celery_app.task
def send_sms_celery(phone):
    code = gen_code(6)
    param = {
        'sid': config.YZX_SID,
        'token': config.YZX_TOKEN,
        'appleid': config.YZX_APP_ID,
        'param': code,
        'mobile': phone,

    }
    res = requests.post(config.YZX_URL, json=param)
    print(res.json())
    # ４返回响应
    if res['code'] == '000000':
        return render_json(data='发送验证码成功')
    else:
        return render_json(error.SMS_ERROR, '发送验证码失败')


