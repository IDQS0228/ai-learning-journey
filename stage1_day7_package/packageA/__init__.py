print("init被调用了")

#在被当作包时调用，记得用from .来相对引用包里的模块
from .import pa_tool


pa_tool.minus(2,1)

print("包里的隐藏1")
if __name__ == "__main__":
    print("包里的隐藏2")