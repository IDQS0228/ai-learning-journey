# 文件读写
# 模式说明：
# "w"：写模式（覆盖原文件）
#   \n  换行
# "a"：追加模式（在文件末尾添加）
# "r"：读模式（默认）
# "b"：二进制模式（图片、视频等）
# with ... as f     是对文件定义的一个常见形式
    # 使用with，将会在with语句块结束后自动关闭文件，类似最后对文件使用了close()



# 写文件
with open("test.txt", "w" , encoding = "utf-8") as f :
    f.write("你好，AI\n")
    f.write("你好，美好的未来，这是读写文件的第一步")

# 读文件
with open("test.txt" , "r" , encoding = "utf-8") as f:
    for line in f:
        print(line.strip())     #strip()去掉换行符

# 追加模式
with open("test.txt" , "a" , encoding = "utf-8") as f:
    f.write("\n再一次输入")

# 读文件
with open("test.txt" , "r" , encoding = "utf-8") as f:
    for line in f:
        print(line.strip())     #strip()去掉换行符


# 异常处理：try/except/finally
# try ：  语句的开始
# except ：输入错误，若有这个错误将会执行以下的命令 若没填写错误将直接执行
# finally ： 不管是否会出现错误，执行玩try就会执行这个命令
try:
    with open("test2.txt" , "r" ,encoding = "utf-8") as test :
        print("执行的test2被打开")
except FileNotFoundError:
    print("出现错误，打开失败")
finally:
    print("finally被执行")