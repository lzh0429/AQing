import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

def control_io_voltage(ip, port, io_address, voltage_value):
    # 创建 Modbus 客户端
    master = modbus_tcp.TcpMaster(host=ip, port=port)
    master.set_timeout(1.0)
    
    # UR3 Modbus 设备地址，默认为 1
    device_address = 1
    
    try:
        # 写入数据到指定的 Modbus 寄存器，这里假设控制 I/O 口输出电压的寄存器地址为 23
        master.execute(device_address, cst.WRITE_SINGLE_REGISTER, io_address, output_value=voltage_value)
        print(f"成功设置 I/O 口输出电压为 {voltage_value}")
    except Exception as e:
        print(f"写入数据时发生错误: {e}")
    finally:
        # 断开与控制器的连接
        master.close()

if __name__ == '__main__':
    # 设置 UR3 控制器的 IP 地址和 Modbus 端口号
    controller_ip = '192.168.1.102'
    controller_port = 502
    
    # 设置要控制的 I/O 口地址和输出电压值
    io_address = 20
    output_voltage = 0

    control_io_voltage(controller_ip, controller_port, io_address, output_voltage)
'''
    io_address = 16 #模拟输出analog_out[0]
    output_voltage = 32767  #(0-65535),32765=5v,65535=10v

    io_address1 = 17 
    output_voltage1 = 1 #模拟输出analog_out[0]1为电压,0为电流
    io_address2 = 18 #模拟输出analog_out[1]
    output_voltage2 = 32767
    io_address3 = 19
    output_voltage3 = 1
    # 调用函数进行控制
    control_io_voltage(controller_ip, controller_port, io_address1, output_voltage1)
    control_io_voltage(controller_ip, controller_port, io_address, output_voltage)
    control_io_voltage(controller_ip, controller_port, io_address3, output_voltage3)
    control_io_voltage(controller_ip, controller_port, io_address2, output_voltage2)
'''

