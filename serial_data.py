import serial, time
import serial.tools.list_ports as port_list


def connect_serial():
    time.sleep(2)
    ser_conn = serial.Serial(
        port=serial_port,
        baudrate=115200,
    )
    return ser_conn


def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

try:
    while True:
        time.sleep(0.1)
        serial_port = ""
        # 현재 연결된 usb serial 장치 중 JLink=DK보드의 포트번호를 찾기
        ports = list(port_list.comports())
        for p in ports:
            if "JLink" in str(p):
                serial_port = str(p).split(" ")[0]
            # print(serial_port)

        if serial_port == "":
            # print("DK board don't connect")
            # DK보드가 연결되지 않은 상태이다
            f = open("./serial_data.txt", "w")
            f.write("disconnection")
            f.close()
            raise NotImplementedError
        else:
            # DK보드가 연결되었으므로 serial data를 읽어온다
            # print("DK board connection state")

            ser = connect_serial()

            while True:
                # serial data를 읽을 수 있다면 리스트형식으로 저장
                if ser.readable():
                    res = ser.readline()
                    serial_data = res.decode().split("\n")
                    serial_data = serial_data[0].split(",")
                    # serial_data[0] = serial_data[0][-1]
                    # print(serial_data)

                    errchk = [isNumber(t) for t in serial_data]

                    if errchk == [True, True, True, True, True, True, True, True, True, True]:
                        intlist_flag = 'True'
                    else:
                        intlist_flag = 'False'

                if len(serial_data) == 10 and intlist_flag == 'True':
                    # 하나의 리스트를 한줄로 덮어써서 txt파일에 저장
                    vstr = ""
                    for i in serial_data:
                        vstr = vstr + str(i) + ","
                    vstr = vstr.rstrip(",")
                    f = open("./serial_data.txt", "w")
                    f.writelines(vstr)
                    # print(vstr)
                    f.close()
                else:
                    # print("need reconnect")
                    ser.close()
                    f = open("./serial_data.txt", "w")
                    f.write("data_error")
                    f.close()
                    raise NotImplementedError
            #         break
            # pass
except NotImplementedError:
    # print("re try")
    pass
