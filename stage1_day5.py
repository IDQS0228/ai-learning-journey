# 学习os 和 sys


# os模块 即操作系统的交互，电脑本体     操作文件和文件夹
import os    # 必须导入，不要用 from os import *

# os.getcwd()               当前工作目录，输出当前文件夹的路径
print(os.getcwd())  #E:\AI-Learning
# os.chdir("文件夹路径")    切换目录
os.chdir("E:\Game") #例子：进入E:\Game
# os.listdir()              列出文件内容
print(os.listdir()) #['InfinityNikki Launcher']
# os.mkdir("文件夹名")      创建文件夹
# os.makedirs("a/b/c")      创建多层文件夹
os.mkdir("test_game_dir")   # 只能建一层，已存在会报错
os.makedirs("test_game_dir2/test1")
# os.rmdir  删除空文件夹
os.rmdir("test_game_dir")
os.rmdir("test_game_dir2/test1")
# os.rmdir("test_game_dir2")

# os.path.exists("test.txt")    判断文件或者文件夹是否存在  返回bool
print(os.path.exists("test_game_dir"))
print(os.path.exists("test_game_dir2"))
# 路径拼接（跨平台，避免手动写斜杠）
path=os.path.join("E:\Game", "test.txt")
print(path)



# sys模块 （Python 解释器交互，程序控制器）
# 获取命令行参数（脚本外部传参）
# 退出程序、获取解释器版本、系统平台
# 动态添加模块搜索路径

import sys

print(sys.argv) #argv,多用于面向命令的工程，它就是一个列表，专门把你在命令行里输入的这些内容存起来，给脚本里的代码用
print(sys.argv[0])    # 脚本名：stage1_day5.py
# print(sys.argv[1])    # 第一个参数：张三

# sys.version 解释器版本（python版本）
print(sys.version)

# sys.platform 系统平台
print(sys.platform)

print(sys.path)  # 列表，Python找模块的顺序
# sys.path.append("E:/my_modules")  # 添加自定义路径


# 退出程序（0=正常，非0=异常）自定义非0状态
# sys.exit(0)
sys.exit("错误：参数不足")  # 异常退出并提示
