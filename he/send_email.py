from he import models
from random import Random
from django.core.mail import send_mail
from HHHHH.settings import EMAIL_FROM

def random_str(strlen=8):
    strs = '0123456789'
    chars = ''
    length = len(strs)-1
    random = Random()
    for i in range(strlen):
        chars += strs[random.randint(0,length)]
    return chars


def send_email_code(email,send_type='register'):
    dbcode = models.Code()
    random_code = random_str(6)
    dbcode.email = email
    dbcode.code = random_code
    dbcode.type = send_type
    dbcode.save()

    send_title = ''
    send_content = ''

    if send_type == 'register':
        send_title = '用户注册验证码'
        send_content = '输入验证码完成注册' + random_code
        status = send_mail(send_title,send_content,EMAIL_FROM,[email])
        if status:
            print('发送成功')



