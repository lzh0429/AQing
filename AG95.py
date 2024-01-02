import serial
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
import time

def create_modbus_master(port):
    # 创建并配置串口对象
    serial_port = serial.Serial(port=port, baudrate=115200, bytesize=8, parity='N', stopbits=1, xonxoff=0)
    
    # 创建并配置RTU主机对象
    master = modbus_rtu.RtuMaster(serial_port)
    master.set_timeout(2.0)
    
    return master
    

def write_single_register(master, device_id, register_address, output_value):
        # 发送写入指令
    master.execute(device_id, cst.WRITE_SINGLE_REGISTER, register_address, output_value=output_value)
        # 读取当前值
    response = master.execute(device_id, cst.READ_HOLDING_REGISTERS, register_address, 1)



if __name__ == '__main__':
    # 使用示例
    serial_port = '/dev/ttyUSB0'
    modbus_master = create_modbus_master(serial_port)
    write_single_register(modbus_master, device_id=0x01, register_address=0x0103, output_value=1000)
    time.sleep(1)
    write_single_register(modbus_master, device_id=0x01, register_address=0x0103, output_value=0)



 