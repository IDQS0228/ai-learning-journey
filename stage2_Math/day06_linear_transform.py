import numpy as np
import matplotlib.pyplot as plt
import math

def scale_matrix(sx,sy):
    """生成二维缩放矩阵"""
    return np.array([[sx,0],
                     [0,sy]])

def rotate_matrix(angle_deg):
    """输入角度，生成逆时针旋转矩阵"""
    theta = math.radians(angle_deg)
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([[c,-s],
                     [s,c]])

# ---------------------- 2. 基础点定义 ----------------------
# 原始坐标点 (1,1)
p = np.array([[1], [1]])
print("原始坐标点 p:\n", p)

# 2.1 单独缩放变换
Ms = scale_matrix(2,0.5)
p_scale = Ms @ p
print("\n缩放矩阵：\n", Ms)
print("缩放后坐标：\n", p_scale)

# 2.2 单独旋转变换 90度
Mr = rotate_matrix(90)
p_rot = Mr @ p
print("\n90度旋转矩阵：\n", Mr)
print("旋转后坐标：\n", p_rot)

# ---------------------- 3. 先缩放、再旋转 复合变换 ----------------------
Ms2 = scale_matrix(2,2)
Mr45 = rotate_matrix(45)
M_total = Mr45 @ Ms2
p_combine = M_total @ p
print("\n复合变换总矩阵(先缩放后旋转)：\n", M_total)
print("复合变换后坐标：\n", p_combine)

# ---------------------- 4. Matplotlib 可视化绘图 ----------------------
# 1.全局设置：解决中文显示 + 负号显示问题
plt.rcParams["font.family"] = "SimHei"  # 黑体
plt.rcParams["axes.unicode_minus"] = False      # 开启中文字体后，负号（如 -10、-50）会变成方框乱码；这行代码关闭 Unicode 负号渲染，让负数符号正常显示
plt.figure(figsize=(8,8))
# 绘制原点坐标
plt.axhline(y=0 , color='k', lw = 1)
plt.axvline(x=0 , color='k', lw = 1)
# 提取坐标值
ox,oy = float(p[0]),float(p[1])
sx,sy = float(p_scale[0]),float(p_scale[1])
cx, cy = float(p_combine[0]), float(p_combine[1])

# 绘制原始点、缩放点、复合变换点
plt.scatter(ox,oy,color="red",s=80,label="原始点 (1,1)")
plt.scatter(sx, sy, color="blue", s=80, label="仅缩放")
plt.scatter(cx, cy, color="green", s=80, label="先缩放再旋转")

# 连线辅助观察
plt.plot([0,ox],[0,oy],"r--")
plt.plot([0, sx], [0, sy], "b--")
plt.plot([0, cx], [0, cy], "g--")

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
