# -*- coding: utf-8 -*-
import json
import sys
import time
import serial


file = "C:/test_config/serial_info.json"
# PortDevice = sys.argv[1]
# cmd = sys.argv[2]
# timeout = sys.argv[3]
# endsymbol = sys.argv[4]


def serial_send_cmd(PortDevice, cmd, timeout, endsymbol):
    device_Path, baud_Rate, Data_Bits = get_serial_config(PortDevice)
    res = communiate(device_Path, cmd, baud_Rate, timeout, endsymbol)
    #print(res)
    return res


def read_json_config(file):
    with open(file) as json_file:
        config = json.load(json_file)
    return config


def get_serial_config(PortDevice):
    config_data = read_json_config(file)
    unit_data = config_data[PortDevice]
    device_Path = unit_data["devicePath"]
    baud_Rate = unit_data["baudRate"]
    Data_Bits = unit_data["DataBits"]
    return device_Path, baud_Rate, Data_Bits


def communiate(PortName, cmd, BaudRate, timeout, endsymbol):
    cmd += '\r\n'
    ser = serial.Serial(PortName, int(BaudRate), timeout=float(timeout))
    ser.flush()

    trans_cmd = cmd.encode()
    ser.write(trans_cmd)

    # timeout==0 表示只写不读
    if float(timeout) == 0:
        ser.flush()
        ser.close()
        return ''

    _end = endsymbol
    if _end == '0D0A':
        _end = '\r\n'

    reports = ''
    tickbegin = time.time()
    while True:
        tickend = time.time()
        if (tickend - tickbegin) >= float(timeout):
            ser.flush()
            ser.close()
            break

        time.sleep(0.001)
        reports += ser.read(ser.inWaiting()).decode()

        if not endsymbol == 'no endSymble':
            if endsymbol in reports:
                ser.flush()
                ser.close()
                return reports
                break

            if _end in reports:
                ser.flush()
                ser.close()
                return reports
                break


if __name__ == '__main__':
    serial_send_cmd("DUT", "11111", "5", "0D0A")
