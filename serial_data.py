import serial, time
import serial.tools.list_ports as port_list


serial_port = ""

ports = list(port_list.comports())
for p in ports:
    if "JLink" in str(p):
        serial_port = str(p).split(" ")[0]
    print(serial_port)

if serial_port == "":
    print("DK board don't connect")
    # DK보드가 연결되지 않은 상태이다
else:
    # DK보드가 연결되었으므로 serial data를 읽어온다
    print("DK board connection state")
    ser = serial.Serial(
        port=serial_port,
        baudrate=115200,
    )

    # initial_time = int(time.time())

    while True:
        # loop_time = int(time.time())

        # serial data를 읽을 수 있다면 리스트형식으로 저장
        if ser.readable():
            res = ser.readline()
            serial_data = res.decode().split("\n")
            serial_data = serial_data[0].split(",")
            serial_data[0] = serial_data[0][-1]
            # print(serial_data)

            # 하나의 리스트를 한줄로 덮어써서 txt파일에 저장
            vstr = ""
            for i in serial_data:
                vstr = vstr + str(i) + ","
            vstr = vstr.rstrip(",")
            f = open("./serial_data.txt", "w")
            f.writelines(vstr)
            f.close()
            print(vstr)

        # if loop_time - initial_time > 3:
        #     print("end")
        #     break
