import serial, time
import serial.tools.list_ports as port_list


def connect_serial(serial_port):
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


def loop_listen():
    try:
        while True:
            time.sleep(0.1)
            serial_port = ""
            ports = list(port_list.comports())
            for p in ports:
                if "JLink" in str(p):
                    serial_port = str(p).split(" ")[0]
            print(serial_port)

            # serial_port = "COM3"

            if serial_port == "":
                f = open("./serial_data.txt", "w")
                f.write("disconnect")
                f.close()
                raise NotImplementedError
            else:
                ser = connect_serial(serial_port)

                while True:
                    if ser.readable():
                        # gyro_axis = ['100', '100', '0']  # 자이로 축값
                        res = ser.readline()
                        res_decode = res.decode("utf-8")
                        line_split = res_decode.replace("\x00", "")
                        serial_data = line_split.split("\n")
                        serial_data = serial_data[0].split(",")
                        # serial_data = gyro_axis + serial_data
                        errchk = [isNumber(t) for t in serial_data]

                        if errchk == [True, True, True, True, True, True, True, True, True, True, True, True, True]:
                            intlist_flag = 'True'
                        else:
                            intlist_flag = 'False'

                    if len(serial_data) == 13 and intlist_flag == 'True':
                        ######################################
                        # 하나의 리스트를 한줄로 덮어써서 txt파일에 저장
                        vstr = ""
                        i = 0
                        for data in serial_data:
                            if i > 2:
                                vstr = vstr + str(data) + ","
                            i = i + 1
                        vstr = vstr.rstrip(",")
                        f = open("./serial_data.txt", "w")
                        f.writelines(vstr)
                        print(vstr)
                        f.close()
                    else:
                        ##################################
                        ser.close()
                        f = open("./serial_data.txt", "w")
                        f.write("data_error")
                        f.close()
                        raise NotImplementedError
    except NotImplementedError:
        pass

loop_listen()
