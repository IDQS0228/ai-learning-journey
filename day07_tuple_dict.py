#元组：不能改的列表
""" 用 小括号 ()
不能增删改（只读）
索引、查询和列表一样 """

#创建元组
t = (10,20,30)

#查询 [索引]
print(t[0]) #10
print(t[-1]) #30


#字典：带名字的键值对（存信息最方便）
""" 用 大括号 {}
格式：键: 值 （key: value）
键不能重复，值可以随便改 """

#创建字典
student = {
    "name":"小明",
    "age":18,
    "city":"北京"
}

#查字典
print(student["name"])  #小明
print(student["age"])   #18
print(student["city"])  #北京

#增
student["gender"] = "男"
print(student["gender"])    #男

#改
student["age"] = 19
print(student["age"])   #19

#删
del student["city"]
print(student)

