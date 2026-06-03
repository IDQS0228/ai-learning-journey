# 模块 (.py 文件)= 单个脚本      文件名 = 模块名
# 包 = 装多个模块的文件夹       文件夹 + 文件夹内必须有 init.py = 包


# 导入模块以及调用模块的四个方法
# 导入同文件夹的整个的模块    import 模块名
import tool
# 调用模块的方法
print(tool.add(1,2))
print(tool.get_code())

# 从模块导入指定函数
from tool import add,get_code
# 调用模块的方法
print(add(3,4))
print(get_code())

# 导入后起别名（解决重名、名字太长）
import tool as t
# 调用模块的方法
print(t.add(5,6))
print(t.get_code())

#全部导入（不推荐，容易变量覆盖）
#from tool import *

#导入包
import packageA