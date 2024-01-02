import urx
import math
import time
from  AG95 import write_single_register,create_modbus_master


serial_port = '/dev/ttyUSB0'
modbus_master = create_modbus_master(serial_port)
rob = urx.Robot("192.168.1.102")  

write_single_register(modbus_master, device_id=0x01, register_address=0x0301, output_value=1)
#初始化夹爪
write_single_register(modbus_master, device_id=0x01, register_address=0x0100, output_value=1)
time.sleep(2)
write_single_register(modbus_master, device_id=0x01, register_address=0x0101, output_value=80)
joint_angles_degrees_1 = [42.78,-75.13,53.99,-74.39,-90.77,-0.35]
joint_angles_degrees_2 = [90.03,-75.13,53.99,-74.39,-90.77,-0.35]
# 使用math.radians函数将它们转换为弧度
joint_angles_radians_1 = [math.radians(angle) for angle in joint_angles_degrees_1]
joint_angles_radians_2 = [math.radians(angle) for angle in joint_angles_degrees_2]
try:
    rob.movej(joint_angles_radians_1, 0.5, 1,wait=True)
    write_single_register(modbus_master, device_id=0x01, register_address=0x0103, output_value=700)
    time.sleep(2)
    rob.movel((-0.198459, -0.332746, 0.04, -1.227, -2.833, 0.127), 0.5, 1, wait=True)
    write_single_register(modbus_master, device_id=0x01, register_address=0x0103, output_value=0)
    time.sleep(2)
    rob.movej(joint_angles_radians_1, 0.5, 1,wait=True)
    rob.movej(joint_angles_radians_2, 0.5, 1,wait=True)
    rob.movel((0.109605, -0.373747, 0.04, 0.012, -3.127, 0.084), 0.5, 1, wait=True)
    write_single_register(modbus_master, device_id=0x01, register_address=0x0103, output_value=1000)
    time.sleep(2)
    rob.movej(joint_angles_radians_2, 0.5, 1,wait=True)
    write_single_register(modbus_master, device_id=0x01, register_address=0x0103, output_value=0)
    

finally:
    rob.close()