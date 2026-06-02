# datetime 时间 + random 随机数｜实战：带有效期的 4 位验证码工具

# datetime：获取当前年月日时分秒
# timedelta：做时间加减（加几分钟、几天）
from datetime import datetime , timedelta

# 获取现在的时间
now = datetime.now()
print("当前时间：",now)

# 格式化：转成 2026-06-02 23:10:20 字符串
# %Y年 %m月 %d日 %H时 %M分 %S秒 固定写法
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(now_str)

# 时间加减(timedelta())
after5min = now + timedelta(minutes = 5 )
print("五分钟后:",after5min)

# 时间对比
if now < after5min:
    print("验证码没过期")
else:
    print("验证码已过期")



import random   #随机数
import string   # string.digits = 0123456789 # string.ascii_uppercase = 大写 A-Z；ascii_lowercase小写 a-z

# 随机抽取整数 randint(a,b) 随机整数 [a,b]
print(random.randint(0,9))

# choices(序列)：随机抽取1个元素
print(random.choice("ABCDEFG"))

# choices(序列 , k = n)：一次抽取n个
res = random.choices(string.ascii_uppercase + string.digits +string.ascii_lowercase, k = 4)
print(res)

# shuffle(列表)：打乱列表顺序
random.shuffle(res)
print(res)