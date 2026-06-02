from datetime import datetime , timedelta
import random
import string

# 获取验证码
def get_random():
    true_yzm = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits , k = 6) )# 随机生成6个字符
    print("您的验证码是",true_yzm)
    return true_yzm

# 获取验证码过期时间
def get_overtime():
    overtime = datetime.now() +timedelta(minutes = 5)
    overtime_str = overtime.strftime("%Y-%m-%d %H:%M:%S")
    print("您的验证码过期时间为：",overtime_str)
    return overtime

# 验证码和时间对比
def contrast(overtime , input_yzm , true_yzm ,):
    if datetime.now() > overtime:
        print("验证码输入超时，请重新申请验证码")
        
    elif input_yzm != true_yzm :
        print("验证码错误请重新输入")
        new_input = input()
        contrast(overtime , new_input , true_yzm)
    else:
        print("验证成功")


# 开始
true_yzm = get_random()
overtime = get_overtime()
get_input = input()
contrast(overtime , get_input , true_yzm)
