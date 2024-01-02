import urx

robot = urx.Robot("192.168.1.102")

try:
    # 获取机器人当前姿势
    pose_vector = robot.getl()
    # 输出姿势坐标
    print("X:", pose_vector[0])
    print("Y:", pose_vector[1])
    print("Z:", pose_vector[2])
    print("RX:", pose_vector[3])
    print("RY:", pose_vector[4])
    print("RZ:", pose_vector[5])
    print("{:.6f}, {:.6f}, {:.6f}, {:.3f}, {:.3f}, {:.3f}".format(pose_vector[0], pose_vector[1], \
    pose_vector[2], pose_vector[3], pose_vector[4], pose_vector[5]))
finally:
    # 关闭与机器人的连接
    robot.close()
