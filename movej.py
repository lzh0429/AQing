import urx
import math
import time

# 创建一个机器人对象
rob = urx.Robot("192.168.1.102")  # 请将IP地址替换为您的机器人的IP地址

# 假设你有一个以度为单位的关节角度列表
joint_angles_degrees_1 = [-0.29, -90.15, 88.35, -49.40, -0.73, 359.63]
# 使用math.radians函数将它们转换为弧度
joint_angles_radians_1 = [math.radians(angle) for angle in joint_angles_degrees_1]
try:
    # 移动到第一个位置
    rob.movej(joint_angles_radians_1, 1, 2,wait=True)  # 这些是关节的目标位置
   # time.sleep(2)
finally:
    # 确保在结束时关闭机器人的连接
    rob.close()
    