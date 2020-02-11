import subprocess
import sys, serial, time, threading

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, QTimer


label_data = []

subprocess_list = []


def kill_process():
    for proc in psutil.process_iter():
        if any(procstr in proc.name() for procstr in
               ['serial_data.exe', 'serial_data.exe', 'serial_data.exe', 'serial_data.exe']):
            print(f'Killing {proc.name()}')
            proc.kill()


class Ui_Form(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()
        self.data10 = QtWidgets.QLabel()
        self.data9 = QtWidgets.QLabel()
        self.data8 = QtWidgets.QLabel()
        self.data7 = QtWidgets.QLabel()
        self.data6 = QtWidgets.QLabel()
        self.data5 = QtWidgets.QLabel()
        self.data4 = QtWidgets.QLabel()
        self.data3 = QtWidgets.QLabel()
        self.data2 = QtWidgets.QLabel()
        self.data1 = QtWidgets.QLabel()
        Form = QtWidgets.QWidget()
        self.setupUi(Form)

        self.timer = QTimer()


    def setupUi(self, Form):
        self.setObjectName("Form")
        self.resize(960, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 941, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_20.addWidget(self.label_13, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_20, 7, 5, 1, 1)
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout.addLayout(self.gridLayout_23, 0, 3, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout.addLayout(self.gridLayout_10, 0, 6, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_19.addWidget(self.label_12, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_19, 7, 4, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addLayout(self.gridLayout_2, 1, 7, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_17.addWidget(self.label_10, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_17, 7, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout.addLayout(self.gridLayout_4, 0, 7, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout.addLayout(self.gridLayout_13, 1, 4, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_16.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_16, 7, 1, 1, 1)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout.addLayout(self.gridLayout_22, 0, 2, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout.addLayout(self.gridLayout_21, 0, 1, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 7, 6, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 7, 0, 1, 1)
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout.addLayout(self.gridLayout_25, 0, 5, 1, 1)
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout.addLayout(self.gridLayout_24, 0, 4, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout.addLayout(self.gridLayout_14, 1, 3, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout.addLayout(self.gridLayout_15, 1, 2, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.start_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start_btn.setObjectName("start_btn")
        self.gridLayout_11.addWidget(self.start_btn, 0, 0, 1, 1)
        self.start_btn.clicked.connect(self.start_click)
        self.gridLayout.addLayout(self.gridLayout_11, 1, 1, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_18.addWidget(self.label_11, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_18, 7, 3, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout.addLayout(self.gridLayout_12, 1, 5, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 7, 7, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout.addLayout(self.gridLayout_9, 1, 6, 1, 1)
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.gridLayout.addLayout(self.gridLayout_27, 2, 2, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_30 = QtWidgets.QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.gridLayout.addLayout(self.gridLayout_30, 3, 2, 1, 1)
        self.gridLayout_31 = QtWidgets.QGridLayout()
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.gridLayout.addLayout(self.gridLayout_31, 2, 1, 1, 1)
        self.gridLayout_32 = QtWidgets.QGridLayout()
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.gridLayout.addLayout(self.gridLayout_32, 3, 1, 1, 1)
        self.gridLayout_36 = QtWidgets.QGridLayout()
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_36.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_36, 6, 0, 1, 1)
        self.gridLayout_37 = QtWidgets.QGridLayout()
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_37.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_37, 5, 0, 1, 1)
        self.gridLayout_38 = QtWidgets.QGridLayout()
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_38.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_38, 4, 0, 1, 1)
        self.gridLayout_39 = QtWidgets.QGridLayout()
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_39.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_39, 3, 0, 1, 1)
        self.gridLayout_40 = QtWidgets.QGridLayout()
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_40.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_40, 2, 0, 1, 1)
        self.gridLayout_41 = QtWidgets.QGridLayout()
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.gridLayout.addLayout(self.gridLayout_41, 2, 3, 1, 1)
        self.gridLayout_42 = QtWidgets.QGridLayout()
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.gridLayout.addLayout(self.gridLayout_42, 3, 3, 1, 1)
        self.gridLayout_49 = QtWidgets.QGridLayout()
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.gridLayout.addLayout(self.gridLayout_49, 6, 7, 1, 1)
        self.gridLayout_50 = QtWidgets.QGridLayout()
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.gridLayout.addLayout(self.gridLayout_50, 5, 7, 1, 1)
        self.gridLayout_57 = QtWidgets.QGridLayout()
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.gridLayout.addLayout(self.gridLayout_57, 3, 7, 1, 1)
        self.gridLayout_58 = QtWidgets.QGridLayout()
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.gridLayout.addLayout(self.gridLayout_58, 3, 6, 1, 1)
        self.gridLayout_59 = QtWidgets.QGridLayout()
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.gridLayout.addLayout(self.gridLayout_59, 4, 7, 1, 1)
        self.gridLayout_60 = QtWidgets.QGridLayout()
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.gridLayout.addLayout(self.gridLayout_60, 2, 7, 1, 1)
        self.gridLayout_61 = QtWidgets.QGridLayout()
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.gridLayout.addLayout(self.gridLayout_61, 2, 6, 1, 1)
        self.gridLayout_62 = QtWidgets.QGridLayout()
        self.gridLayout_62.setObjectName("gridLayout_62")
        self.gridLayout.addLayout(self.gridLayout_62, 2, 5, 1, 1)
        self.gridLayout_63 = QtWidgets.QGridLayout()
        self.gridLayout_63.setObjectName("gridLayout_63")
        self.gridLayout.addLayout(self.gridLayout_63, 3, 5, 1, 1)
        self.gridLayout_64 = QtWidgets.QGridLayout()
        self.gridLayout_64.setObjectName("gridLayout_64")
        self.gridLayout.addLayout(self.gridLayout_64, 3, 4, 1, 1)
        self.gridLayout_65 = QtWidgets.QGridLayout()
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.gridLayout.addLayout(self.gridLayout_65, 2, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_33 = QtWidgets.QGridLayout()
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.data1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data1.setText("")
        self.data1.setObjectName("data1")
        self.data1.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_33.addWidget(self.data1, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_33)
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.data2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data2.setText("")
        self.data2.setObjectName("data2")
        self.data2.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_29.addWidget(self.data2, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_29)
        self.gridLayout_68 = QtWidgets.QGridLayout()
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.data3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data3.setText("")
        self.data3.setObjectName("data3")
        self.data3.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_68.addWidget(self.data3, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_68)
        self.gridLayout_67 = QtWidgets.QGridLayout()
        self.gridLayout_67.setObjectName("gridLayout_67")
        self.data4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data4.setText("")
        self.data4.setObjectName("data4")
        self.data4.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_67.addWidget(self.data4, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_67)
        self.gridLayout_66 = QtWidgets.QGridLayout()
        self.gridLayout_66.setObjectName("gridLayout_66")
        self.data5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data5.setText("")
        self.data5.setObjectName("data5")
        self.data5.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_66.addWidget(self.data5, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_66)
        self.gridLayout_56 = QtWidgets.QGridLayout()
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.data6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data6.setText("")
        self.data6.setObjectName("data6")
        self.data6.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_56.addWidget(self.data6, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_56)
        self.gridLayout_69 = QtWidgets.QGridLayout()
        self.gridLayout_69.setObjectName("gridLayout_69")
        self.data7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data7.setText("")
        self.data7.setObjectName("data7")
        self.data7.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_69.addWidget(self.data7, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_69)
        self.gridLayout_54 = QtWidgets.QGridLayout()
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.data8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data8.setText("")
        self.data8.setObjectName("data8")
        self.data8.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_54.addWidget(self.data8, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_54)
        self.gridLayout_55 = QtWidgets.QGridLayout()
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.data9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data9.setText("")
        self.data9.setObjectName("data9")
        self.data9.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_55.addWidget(self.data9, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_55)
        self.gridLayout_43 = QtWidgets.QGridLayout()
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.data10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.data10.setText("")
        self.data10.setObjectName("data10")
        self.data10.setStyleSheet("background-color: #6B9ABF")
        self.gridLayout_43.addWidget(self.data10, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_43)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_34 = QtWidgets.QGridLayout()
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.verticalLayout.addLayout(self.gridLayout_34)
        self.gridLayout_28 = QtWidgets.QGridLayout()
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.finger = QtWidgets.QLabel(self.gridLayoutWidget)
        self.finger.setText("")
        self.finger.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.finger.setObjectName("finger")
        self.gridLayout_28.addWidget(self.finger, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_28)
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.touch_panel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.touch_panel.setText("")
        self.touch_panel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.touch_panel.setObjectName("touch_panel")
        self.gridLayout_26.addWidget(self.touch_panel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_26)
        self.gridLayout.addLayout(self.verticalLayout, 5, 1, 2, 6)

        self.retranslateUi(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("serial", "serial"))
        self.start_btn.setText(_translate("Form", "start"))

        self.serial_state = {"data1": self.data1}
        self.serial_state["data2"] = self.data2
        self.serial_state["data3"] = self.data3
        self.serial_state["data4"] = self.data4
        self.serial_state["data5"] = self.data5
        self.serial_state["data6"] = self.data6
        self.serial_state["data7"] = self.data7
        self.serial_state["data8"] = self.data8
        self.serial_state["data9"] = self.data9
        self.serial_state["data10"] = self.data10

    def start_click(self):

        reply = QtWidgets.QMessageBox.question(self, "serial", "터치 센서를 확인하겠습니까?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            subprocess_list.append(subprocess.Popen('python serial_data.py', shell=True))
            self.watcher = QtCore.QFileSystemWatcher(self)
            self.watcher.addPath("./serial_data.txt")
            self.watcher.fileChanged.connect(self.label_change)

    def label_change(self, path):
        with open(path, 'r') as f:
            serial_txt = f.read().split(",")
            for i in range(10):
                if serial_txt[i] == "1":
                    self.serial_state["data"+str(i+1)].setStyleSheet("background-color: red")
                elif serial_txt[i] == "0":
                    self.serial_state["data"+str(i+1)].setStyleSheet("background-color: #6B9ABF")

                if serial_txt[0] == "1":
                    self.finger.setText("엄지")
                    if serial_txt[1] == "1":
                        self.finger.setText("엄지와 검지")
                        if serial_txt[4] == "1" or serial_txt[5] == "1":
                            self.finger.setText("엄지-검지-중지")
                            if serial_txt[7] == "1" or serial_txt[8] == "1":
                                self.finger.setText("엄지-검지-중지-약지")
                                if serial_txt[9] == "1":
                                    self.finger.setText("엄지-검지-중지-약지-새끼")
                            elif serial_txt[9] == "1":
                                self.finger.setText("엄지-검지-중지-새끼")
                        elif serial_txt[7] == "1" or serial_txt[8] == "1":
                            self.finger.setText("엄지-검지-약지")
                            if serial_txt[9] == "1":
                                self.finger.setText("엄지-검지-약지-새끼")
                        elif serial_txt[9] == "1":
                            self.finger.setText("엄지-검지-새끼")
                    elif serial_txt[4] == "1" or serial_txt[5] == "1":
                        self.finger.setText("엄지와 중지")
                        if serial_txt[7] == "1" or serial_txt[8] == "1":
                            self.finger.setText("엄지-중지-약지")
                            if serial_txt[9] == "1":
                                self.finger.setText("엄지-중지-약지-새끼")
                        elif serial_txt[9] == "1":
                            self.finger.setText("엄지-중지-새끼")
                    elif serial_txt[7] == "1" or serial_txt[8] == "1":
                        self.finger.setText("엄지와 약지")
                        if serial_txt[9] == "1":
                            self.finger.setText("엄지-약지-새끼")
                    elif serial_txt[9] == "1":
                        self.finger.setText("엄지와 새끼")
                elif serial_txt[1] == "1":
                    self.finger.setText("검지")
                    if serial_txt[4] == "1" or serial_txt[5] == "1":
                        self.finger.setText("검지와 중지")
                        if serial_txt[7] == "1" or serial_txt[8] == "1":
                            self.finger.setText("검지-중지-약지")
                            if serial_txt[9] == "1":
                                self.finger.setText("검지-중지-약지-새끼")
                        elif serial_txt[9] == "1":
                            self.finger.setText("검지-중지-새끼")
                    elif serial_txt[7] == "1" or serial_txt[8] == "1":
                        self.finger.setText("검지와 약지")
                        if serial_txt[9] == "1":
                            self.finger.setText("검지-약지-새끼")
                    elif serial_txt[9] == "1":
                        self.finger.setText("검지와 새끼")
                elif serial_txt[4] == "1" or serial_txt[5] == "1":
                    self.finger.setText("중지")
                    if serial_txt[7] == "1" or serial_txt[8] == "1":
                        self.finger.setText("중지와 약지")
                        if serial_txt[9] == "1":
                            self.finger.setText("중지-약지-새끼")
                    elif serial_txt[9] == "1":
                        self.finger.setText("중지와 새끼")
                elif serial_txt[7] == "1" or serial_txt[8] == "1":
                    self.finger.setText("약지")
                    if serial_txt[9] == "1":
                        self.finger.setText("약지와 새끼")
                elif serial_txt[9] == "1":
                    self.finger.setText("새끼")
                else:
                    self.finger.setText("")

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Quit', "프로그램을 종료하시겠습니까?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            kill_process()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
