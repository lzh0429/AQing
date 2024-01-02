import urx
import math

# 连接到机械臂
robot = urx.Robot("192.168.1.102")  # 请将IP地址更改为你的机械臂的IP地址


# 使用movep函数移动机械臂
robot.movep((-0.33827482244661206,-0.11283733946979099, 0.18971154552164504, 2.0611894713970793 ,2.3161965777040208 ,-0.12956983059152163),0.1,0.2)
robot.movep((-0.3383044455894698 ,-0.32880614148970133 ,0.18969929020774454 ,2.0612360458625565 ,2.316104026532056 ,-0.1296214859040601),0.1,0.2)
robot.movep((-0.17392217267343196 ,-0.32882842451028016 ,0.18969654348200798, 2.0612755809495673 ,2.316035275106114 ,-0.12964785345215143),0.1,0.2)

# 断开与机械臂的连接
robot.close()