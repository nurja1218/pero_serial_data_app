import subprocess
import sys, serial, time, threading

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QIcon

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
        Form = QtWidgets.QWidget()
        self.setupUi(Form)

        self.timer = QTimer()

    def setupUi(self, Form):
        self.setObjectName("serial")
        self.resize(900, 600)
        self.setFixedSize(900, 600)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.setFont(font)
        self.setStyleSheet("background-color: white;")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 881, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout.addLayout(self.gridLayout_24, 19, 32, 1, 1)
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout.addLayout(self.gridLayout_25, 10, 32, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout.addLayout(self.gridLayout_15, 8, 32, 1, 1)
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout.addLayout(self.gridLayout_26, 21, 32, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout.addLayout(self.gridLayout_10, 6, 32, 1, 1)
        self.gridLayout_28 = QtWidgets.QGridLayout()
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.gridLayout.addLayout(self.gridLayout_28, 2, 32, 1, 1)
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout.addLayout(self.gridLayout_23, 23, 32, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout.addLayout(self.gridLayout_16, 13, 32, 1, 1)
        self.gridLayout_33 = QtWidgets.QGridLayout()
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.gridLayout.addLayout(self.gridLayout_33, 0, 2, 1, 1)
        self.gridLayout_41 = QtWidgets.QGridLayout()
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.gridLayout.addLayout(self.gridLayout_41, 0, 30, 1, 1)
        self.gridLayout_30 = QtWidgets.QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.gridLayout.addLayout(self.gridLayout_30, 0, 1, 1, 1)
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.gridLayout.addLayout(self.gridLayout_29, 24, 32, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout.addLayout(self.gridLayout_14, 14, 32, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout.addLayout(self.gridLayout_8, 18, 32, 1, 1)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout.addLayout(self.gridLayout_22, 20, 32, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout.addLayout(self.gridLayout_20, 16, 32, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout.addLayout(self.gridLayout_19, 12, 32, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout.addLayout(self.gridLayout_9, 22, 32, 1, 1)
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.gridLayout.addLayout(self.gridLayout_27, 4, 32, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout.addLayout(self.gridLayout_12, 9, 32, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout.addLayout(self.gridLayout_11, 7, 32, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout.addLayout(self.gridLayout_13, 15, 32, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout.addLayout(self.gridLayout_17, 11, 32, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout.addLayout(self.gridLayout_18, 17, 32, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout.addLayout(self.gridLayout_21, 5, 32, 1, 1)
        self.gridLayout_45 = QtWidgets.QGridLayout()
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.gridLayout.addLayout(self.gridLayout_45, 0, 5, 1, 1)
        self.gridLayout_36 = QtWidgets.QGridLayout()
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.gridLayout.addLayout(self.gridLayout_36, 0, 28, 1, 1)
        self.gridLayout_35 = QtWidgets.QGridLayout()
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.gridLayout.addLayout(self.gridLayout_35, 0, 3, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_39 = QtWidgets.QGridLayout()
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.gridLayout.addLayout(self.gridLayout_39, 0, 26, 1, 1)
        self.gridLayout_48 = QtWidgets.QGridLayout()
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.gridLayout.addLayout(self.gridLayout_48, 0, 7, 1, 1)
        self.gridLayout_50 = QtWidgets.QGridLayout()
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.gridLayout.addLayout(self.gridLayout_50, 0, 21, 1, 1)
        self.gridLayout_58 = QtWidgets.QGridLayout()
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.gridLayout.addLayout(self.gridLayout_58, 0, 25, 1, 1)
        self.gridLayout_57 = QtWidgets.QGridLayout()
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.gridLayout.addLayout(self.gridLayout_57, 0, 22, 1, 1)
        self.gridLayout_38 = QtWidgets.QGridLayout()
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.gridLayout.addLayout(self.gridLayout_38, 0, 8, 1, 1)
        self.gridLayout_54 = QtWidgets.QGridLayout()
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.gridLayout.addLayout(self.gridLayout_54, 0, 24, 1, 1)
        self.gridLayout_43 = QtWidgets.QGridLayout()
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.gridLayout.addLayout(self.gridLayout_43, 0, 20, 1, 1)
        self.gridLayout_59 = QtWidgets.QGridLayout()
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.gridLayout.addLayout(self.gridLayout_59, 0, 14, 1, 1)
        self.gridLayout_37 = QtWidgets.QGridLayout()
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.gridLayout.addLayout(self.gridLayout_37, 0, 17, 1, 1)
        self.gridLayout_40 = QtWidgets.QGridLayout()
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.gridLayout.addLayout(self.gridLayout_40, 0, 19, 1, 1)
        self.gridLayout_46 = QtWidgets.QGridLayout()
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.gridLayout.addLayout(self.gridLayout_46, 0, 10, 1, 1)
        self.gridLayout_31 = QtWidgets.QGridLayout()
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.gridLayout.addLayout(self.gridLayout_31, 0, 16, 1, 1)
        self.gridLayout_42 = QtWidgets.QGridLayout()
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.gridLayout.addLayout(self.gridLayout_42, 0, 15, 1, 1)
        self.gridLayout_51 = QtWidgets.QGridLayout()
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.gridLayout.addLayout(self.gridLayout_51, 0, 11, 1, 1)
        self.gridLayout_32 = QtWidgets.QGridLayout()
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.gridLayout.addLayout(self.gridLayout_32, 0, 9, 1, 1)
        self.gridLayout_56 = QtWidgets.QGridLayout()
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.gridLayout.addLayout(self.gridLayout_56, 0, 12, 1, 1)
        self.gridLayout_53 = QtWidgets.QGridLayout()
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.gridLayout.addLayout(self.gridLayout_53, 0, 23, 1, 1)
        self.gridLayout_49 = QtWidgets.QGridLayout()
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.gridLayout.addLayout(self.gridLayout_49, 0, 13, 1, 1)
        self.gridLayout_60 = QtWidgets.QGridLayout()
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.gridLayout.addLayout(self.gridLayout_60, 0, 27, 1, 1)
        self.gridLayout_34 = QtWidgets.QGridLayout()
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.gridLayout.addLayout(self.gridLayout_34, 0, 18, 1, 1)
        self.gridLayout_55 = QtWidgets.QGridLayout()
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.gridLayout.addLayout(self.gridLayout_55, 0, 6, 1, 1)
        self.gridLayout_52 = QtWidgets.QGridLayout()
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.gridLayout.addLayout(self.gridLayout_52, 0, 4, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addLayout(self.gridLayout_3, 0, 32, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout.addLayout(self.gridLayout_4, 1, 32, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addLayout(self.gridLayout_2, 25, 32, 1, 1)
        self.gridLayout_62 = QtWidgets.QGridLayout()
        self.gridLayout_62.setObjectName("gridLayout_62")
        self.gridLayout.addLayout(self.gridLayout_62, 0, 29, 1, 1)
        self.gridLayout_63 = QtWidgets.QGridLayout()
        self.gridLayout_63.setObjectName("gridLayout_63")
        self.gridLayout.addLayout(self.gridLayout_63, 3, 32, 1, 1)
        self.gridLayout_47 = QtWidgets.QGridLayout()
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.logo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.gridLayout_47.addWidget(self.logo, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_47, 1, 26, 3, 5)
        self.gridLayout_152 = QtWidgets.QGridLayout()
        self.gridLayout_152.setObjectName("gridLayout_152")
        self.gridLayout.addLayout(self.gridLayout_152, 1, 21, 3, 5)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(24)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 1, 1, 3, 20)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_61 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.touch_5 = QtWidgets.QLabel(self.groupBox)
        self.touch_5.setText("")
        self.touch_5.setObjectName("touch_5")
        self.gridLayout_5.addWidget(self.touch_5, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_5, 2, 15, 5, 3)
        self.gridLayout_130 = QtWidgets.QGridLayout()
        self.gridLayout_130.setObjectName("gridLayout_130")
        self.ch_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_4.setFont(font)
        self.ch_4.setStyleSheet("color: #a9a9a9;")
        self.ch_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_4.setObjectName("ch_4")
        self.gridLayout_130.addWidget(self.ch_4, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_130, 7, 12, 2, 3)
        self.gridLayout_129 = QtWidgets.QGridLayout()
        self.gridLayout_129.setObjectName("gridLayout_129")
        self.touch_6 = QtWidgets.QLabel(self.groupBox)
        self.touch_6.setText("")
        self.touch_6.setObjectName("touch_6")
        self.gridLayout_129.addWidget(self.touch_6, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_129, 2, 18, 5, 3)
        self.gridLayout_131 = QtWidgets.QGridLayout()
        self.gridLayout_131.setObjectName("gridLayout_131")
        self.ch_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_5.setFont(font)
        self.ch_5.setStyleSheet("color: #a9a9a9;")
        self.ch_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_5.setObjectName("ch_5")
        self.gridLayout_131.addWidget(self.ch_5, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_131, 7, 15, 2, 3)
        self.gridLayout_136 = QtWidgets.QGridLayout()
        self.gridLayout_136.setObjectName("gridLayout_136")
        self.ch_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_8.setFont(font)
        self.ch_8.setStyleSheet("color: #a9a9a9;")
        self.ch_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_8.setObjectName("ch_8")
        self.gridLayout_136.addWidget(self.ch_8, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_136, 7, 24, 2, 3)
        self.gridLayout_134 = QtWidgets.QGridLayout()
        self.gridLayout_134.setObjectName("gridLayout_134")
        self.ch_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_7.setFont(font)
        self.ch_7.setStyleSheet("color: #a9a9a9;")
        self.ch_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_7.setObjectName("ch_7")
        self.gridLayout_134.addWidget(self.ch_7, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_134, 7, 21, 2, 3)
        self.gridLayout_132 = QtWidgets.QGridLayout()
        self.gridLayout_132.setObjectName("gridLayout_132")
        self.ch_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_6.setFont(font)
        self.ch_6.setStyleSheet("color: #a9a9a9;")
        self.ch_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_6.setObjectName("ch_6")
        self.gridLayout_132.addWidget(self.ch_6, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_132, 7, 18, 2, 3)
        self.gridLayout_123 = QtWidgets.QGridLayout()
        self.gridLayout_123.setObjectName("gridLayout_123")
        self.touch_2 = QtWidgets.QLabel(self.groupBox)
        self.touch_2.setText("")
        self.touch_2.setObjectName("touch_2")
        self.gridLayout_123.addWidget(self.touch_2, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_123, 2, 6, 5, 3)
        self.gridLayout_139 = QtWidgets.QGridLayout()
        self.gridLayout_139.setObjectName("gridLayout_139")
        self.touch_10 = QtWidgets.QLabel(self.groupBox)
        self.touch_10.setText("")
        self.touch_10.setObjectName("touch_10")
        self.gridLayout_139.addWidget(self.touch_10, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_139, 2, 30, 5, 3)
        self.gridLayout_124 = QtWidgets.QGridLayout()
        self.gridLayout_124.setObjectName("gridLayout_124")
        self.touch_3 = QtWidgets.QLabel(self.groupBox)
        self.touch_3.setText("")
        self.touch_3.setObjectName("touch_3")
        self.gridLayout_124.addWidget(self.touch_3, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_124, 2, 9, 5, 3)
        self.gridLayout_140 = QtWidgets.QGridLayout()
        self.gridLayout_140.setObjectName("gridLayout_140")
        self.ch_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_10.setFont(font)
        self.ch_10.setStyleSheet("color: #a9a9a9;")
        self.ch_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_10.setObjectName("ch_10")
        self.gridLayout_140.addWidget(self.ch_10, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_140, 7, 30, 2, 3)
        self.gridLayout_133 = QtWidgets.QGridLayout()
        self.gridLayout_133.setObjectName("gridLayout_133")
        self.touch_7 = QtWidgets.QLabel(self.groupBox)
        self.touch_7.setText("")
        self.touch_7.setObjectName("touch_7")
        self.gridLayout_133.addWidget(self.touch_7, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_133, 2, 21, 5, 3)
        self.gridLayout_126 = QtWidgets.QGridLayout()
        self.gridLayout_126.setObjectName("gridLayout_126")
        self.ch_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_2.setFont(font)
        self.ch_2.setStyleSheet("color: #a9a9a9;")
        self.ch_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_2.setObjectName("ch_2")
        self.gridLayout_126.addWidget(self.ch_2, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_126, 7, 6, 2, 3)
        self.gridLayout_137 = QtWidgets.QGridLayout()
        self.gridLayout_137.setObjectName("gridLayout_137")
        self.touch_9 = QtWidgets.QLabel(self.groupBox)
        self.touch_9.setText("")
        self.touch_9.setObjectName("touch_9")
        self.gridLayout_137.addWidget(self.touch_9, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_137, 2, 27, 5, 3)
        self.gridLayout_128 = QtWidgets.QGridLayout()
        self.gridLayout_128.setObjectName("gridLayout_128")
        self.touch_4 = QtWidgets.QLabel(self.groupBox)
        self.touch_4.setText("")
        self.touch_4.setObjectName("touch_4")
        self.gridLayout_128.addWidget(self.touch_4, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_128, 2, 12, 5, 3)
        self.gridLayout_66 = QtWidgets.QGridLayout()
        self.gridLayout_66.setObjectName("gridLayout_66")
        self.gridLayout_61.addLayout(self.gridLayout_66, 21, 33, 1, 1)
        self.gridLayout_81 = QtWidgets.QGridLayout()
        self.gridLayout_81.setObjectName("gridLayout_81")
        self.gridLayout_61.addLayout(self.gridLayout_81, 8, 33, 1, 1)
        self.gridLayout_73 = QtWidgets.QGridLayout()
        self.gridLayout_73.setObjectName("gridLayout_73")
        self.gridLayout_61.addLayout(self.gridLayout_73, 4, 33, 1, 1)
        self.gridLayout_77 = QtWidgets.QGridLayout()
        self.gridLayout_77.setObjectName("gridLayout_77")
        self.gridLayout_61.addLayout(self.gridLayout_77, 5, 33, 1, 1)
        self.gridLayout_88 = QtWidgets.QGridLayout()
        self.gridLayout_88.setObjectName("gridLayout_88")
        self.gridLayout_61.addLayout(self.gridLayout_88, 20, 33, 1, 1)
        self.gridLayout_75 = QtWidgets.QGridLayout()
        self.gridLayout_75.setObjectName("gridLayout_75")
        self.gridLayout_61.addLayout(self.gridLayout_75, 16, 33, 1, 1)
        self.gridLayout_67 = QtWidgets.QGridLayout()
        self.gridLayout_67.setObjectName("gridLayout_67")
        self.gridLayout_61.addLayout(self.gridLayout_67, 0, 33, 1, 1)
        self.gridLayout_138 = QtWidgets.QGridLayout()
        self.gridLayout_138.setObjectName("gridLayout_138")
        self.ch_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_9.setFont(font)
        self.ch_9.setStyleSheet("color: #a9a9a9;")
        self.ch_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_9.setObjectName("ch_9")
        self.gridLayout_138.addWidget(self.ch_9, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_138, 7, 27, 2, 3)
        self.gridLayout_70 = QtWidgets.QGridLayout()
        self.gridLayout_70.setObjectName("gridLayout_70")
        self.gridLayout_61.addLayout(self.gridLayout_70, 7, 33, 1, 1)
        self.gridLayout_83 = QtWidgets.QGridLayout()
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.gridLayout_61.addLayout(self.gridLayout_83, 19, 33, 1, 1)
        self.gridLayout_74 = QtWidgets.QGridLayout()
        self.gridLayout_74.setObjectName("gridLayout_74")
        self.gridLayout_61.addLayout(self.gridLayout_74, 17, 33, 1, 1)
        self.gridLayout_87 = QtWidgets.QGridLayout()
        self.gridLayout_87.setObjectName("gridLayout_87")
        self.gridLayout_61.addLayout(self.gridLayout_87, 11, 33, 1, 1)
        self.gridLayout_86 = QtWidgets.QGridLayout()
        self.gridLayout_86.setObjectName("gridLayout_86")
        self.gridLayout_61.addLayout(self.gridLayout_86, 9, 33, 1, 1)
        self.gridLayout_78 = QtWidgets.QGridLayout()
        self.gridLayout_78.setObjectName("gridLayout_78")
        self.gridLayout_61.addLayout(self.gridLayout_78, 15, 33, 1, 1)
        self.gridLayout_80 = QtWidgets.QGridLayout()
        self.gridLayout_80.setObjectName("gridLayout_80")
        self.gridLayout_61.addLayout(self.gridLayout_80, 13, 33, 1, 1)
        self.gridLayout_76 = QtWidgets.QGridLayout()
        self.gridLayout_76.setObjectName("gridLayout_76")
        self.gridLayout_61.addLayout(self.gridLayout_76, 3, 33, 1, 1)
        self.gridLayout_127 = QtWidgets.QGridLayout()
        self.gridLayout_127.setObjectName("gridLayout_127")
        self.ch_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_3.setFont(font)
        self.ch_3.setStyleSheet("color: #a9a9a9;")
        self.ch_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_3.setObjectName("ch_3")
        self.gridLayout_127.addWidget(self.ch_3, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_127, 7, 9, 2, 3)
        self.gridLayout_79 = QtWidgets.QGridLayout()
        self.gridLayout_79.setObjectName("gridLayout_79")
        self.gridLayout_61.addLayout(self.gridLayout_79, 6, 33, 1, 1)
        self.gridLayout_82 = QtWidgets.QGridLayout()
        self.gridLayout_82.setObjectName("gridLayout_82")
        self.gridLayout_61.addLayout(self.gridLayout_82, 10, 33, 1, 1)
        self.gridLayout_84 = QtWidgets.QGridLayout()
        self.gridLayout_84.setObjectName("gridLayout_84")
        self.gridLayout_61.addLayout(self.gridLayout_84, 12, 33, 1, 1)
        self.gridLayout_72 = QtWidgets.QGridLayout()
        self.gridLayout_72.setObjectName("gridLayout_72")
        self.gridLayout_61.addLayout(self.gridLayout_72, 18, 33, 1, 1)
        self.gridLayout_68 = QtWidgets.QGridLayout()
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.gridLayout_61.addLayout(self.gridLayout_68, 1, 33, 1, 1)
        self.gridLayout_71 = QtWidgets.QGridLayout()
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.gridLayout_61.addLayout(self.gridLayout_71, 14, 33, 1, 1)
        self.gridLayout_85 = QtWidgets.QGridLayout()
        self.gridLayout_85.setObjectName("gridLayout_85")
        self.gridLayout_61.addLayout(self.gridLayout_85, 2, 33, 1, 1)
        self.gridLayout_89 = QtWidgets.QGridLayout()
        self.gridLayout_89.setObjectName("gridLayout_89")
        self.gridLayout_61.addLayout(self.gridLayout_89, 9, 0, 1, 1)
        self.gridLayout_135 = QtWidgets.QGridLayout()
        self.gridLayout_135.setObjectName("gridLayout_135")
        self.touch_8 = QtWidgets.QLabel(self.groupBox)
        self.touch_8.setText("")
        self.touch_8.setObjectName("touch_8")
        self.gridLayout_135.addWidget(self.touch_8, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_135, 2, 24, 5, 3)
        self.gridLayout_91 = QtWidgets.QGridLayout()
        self.gridLayout_91.setObjectName("gridLayout_91")
        self.gridLayout_61.addLayout(self.gridLayout_91, 9, 19, 1, 1)
        self.gridLayout_95 = QtWidgets.QGridLayout()
        self.gridLayout_95.setObjectName("gridLayout_95")
        self.gridLayout_61.addLayout(self.gridLayout_95, 9, 29, 1, 1)
        self.gridLayout_99 = QtWidgets.QGridLayout()
        self.gridLayout_99.setObjectName("gridLayout_99")
        self.gridLayout_61.addLayout(self.gridLayout_99, 9, 22, 1, 1)
        self.gridLayout_119 = QtWidgets.QGridLayout()
        self.gridLayout_119.setObjectName("gridLayout_119")
        self.gridLayout_61.addLayout(self.gridLayout_119, 9, 32, 1, 1)
        self.gridLayout_92 = QtWidgets.QGridLayout()
        self.gridLayout_92.setObjectName("gridLayout_92")
        self.gridLayout_61.addLayout(self.gridLayout_92, 9, 6, 1, 1)
        self.gridLayout_115 = QtWidgets.QGridLayout()
        self.gridLayout_115.setObjectName("gridLayout_115")
        self.gridLayout_61.addLayout(self.gridLayout_115, 9, 7, 1, 1)
        self.gridLayout_112 = QtWidgets.QGridLayout()
        self.gridLayout_112.setObjectName("gridLayout_112")
        self.gridLayout_61.addLayout(self.gridLayout_112, 9, 16, 1, 1)
        self.gridLayout_104 = QtWidgets.QGridLayout()
        self.gridLayout_104.setObjectName("gridLayout_104")
        self.gridLayout_61.addLayout(self.gridLayout_104, 9, 10, 1, 1)
        self.gridLayout_118 = QtWidgets.QGridLayout()
        self.gridLayout_118.setObjectName("gridLayout_118")
        self.gridLayout_61.addLayout(self.gridLayout_118, 9, 13, 1, 1)
        self.gridLayout_107 = QtWidgets.QGridLayout()
        self.gridLayout_107.setObjectName("gridLayout_107")
        self.gridLayout_61.addLayout(self.gridLayout_107, 9, 15, 1, 1)
        self.gridLayout_97 = QtWidgets.QGridLayout()
        self.gridLayout_97.setObjectName("gridLayout_97")
        self.gridLayout_61.addLayout(self.gridLayout_97, 9, 27, 1, 1)
        self.gridLayout_69 = QtWidgets.QGridLayout()
        self.gridLayout_69.setObjectName("gridLayout_69")
        self.gridLayout_61.addLayout(self.gridLayout_69, 9, 9, 1, 1)
        self.gridLayout_96 = QtWidgets.QGridLayout()
        self.gridLayout_96.setObjectName("gridLayout_96")
        self.gridLayout_61.addLayout(self.gridLayout_96, 9, 1, 1, 1)
        self.gridLayout_106 = QtWidgets.QGridLayout()
        self.gridLayout_106.setObjectName("gridLayout_106")
        self.gridLayout_61.addLayout(self.gridLayout_106, 9, 3, 1, 1)
        self.gridLayout_110 = QtWidgets.QGridLayout()
        self.gridLayout_110.setObjectName("gridLayout_110")
        self.gridLayout_61.addLayout(self.gridLayout_110, 9, 8, 1, 1)
        self.gridLayout_111 = QtWidgets.QGridLayout()
        self.gridLayout_111.setObjectName("gridLayout_111")
        self.gridLayout_61.addLayout(self.gridLayout_111, 9, 24, 1, 1)
        self.gridLayout_109 = QtWidgets.QGridLayout()
        self.gridLayout_109.setObjectName("gridLayout_109")
        self.gridLayout_61.addLayout(self.gridLayout_109, 9, 23, 1, 1)
        self.gridLayout_108 = QtWidgets.QGridLayout()
        self.gridLayout_108.setObjectName("gridLayout_108")
        self.gridLayout_61.addLayout(self.gridLayout_108, 9, 18, 1, 1)
        self.gridLayout_100 = QtWidgets.QGridLayout()
        self.gridLayout_100.setObjectName("gridLayout_100")
        self.gridLayout_61.addLayout(self.gridLayout_100, 9, 17, 1, 1)
        self.gridLayout_113 = QtWidgets.QGridLayout()
        self.gridLayout_113.setObjectName("gridLayout_113")
        self.gridLayout_61.addLayout(self.gridLayout_113, 9, 31, 1, 1)
        self.gridLayout_114 = QtWidgets.QGridLayout()
        self.gridLayout_114.setObjectName("gridLayout_114")
        self.gridLayout_61.addLayout(self.gridLayout_114, 9, 14, 1, 1)
        self.gridLayout_90 = QtWidgets.QGridLayout()
        self.gridLayout_90.setObjectName("gridLayout_90")
        self.gridLayout_61.addLayout(self.gridLayout_90, 9, 11, 1, 1)
        self.gridLayout_101 = QtWidgets.QGridLayout()
        self.gridLayout_101.setObjectName("gridLayout_101")
        self.gridLayout_61.addLayout(self.gridLayout_101, 9, 12, 1, 1)
        self.gridLayout_93 = QtWidgets.QGridLayout()
        self.gridLayout_93.setObjectName("gridLayout_93")
        self.gridLayout_61.addLayout(self.gridLayout_93, 9, 25, 1, 1)
        self.gridLayout_102 = QtWidgets.QGridLayout()
        self.gridLayout_102.setObjectName("gridLayout_102")
        self.gridLayout_61.addLayout(self.gridLayout_102, 9, 28, 1, 1)
        self.gridLayout_98 = QtWidgets.QGridLayout()
        self.gridLayout_98.setObjectName("gridLayout_98")
        self.gridLayout_61.addLayout(self.gridLayout_98, 9, 5, 1, 1)
        self.gridLayout_94 = QtWidgets.QGridLayout()
        self.gridLayout_94.setObjectName("gridLayout_94")
        self.gridLayout_61.addLayout(self.gridLayout_94, 9, 4, 1, 1)
        self.gridLayout_116 = QtWidgets.QGridLayout()
        self.gridLayout_116.setObjectName("gridLayout_116")
        self.gridLayout_61.addLayout(self.gridLayout_116, 9, 26, 1, 1)
        self.gridLayout_103 = QtWidgets.QGridLayout()
        self.gridLayout_103.setObjectName("gridLayout_103")
        self.gridLayout_61.addLayout(self.gridLayout_103, 9, 20, 1, 1)
        self.gridLayout_117 = QtWidgets.QGridLayout()
        self.gridLayout_117.setObjectName("gridLayout_117")
        self.gridLayout_61.addLayout(self.gridLayout_117, 9, 30, 1, 1)
        self.gridLayout_105 = QtWidgets.QGridLayout()
        self.gridLayout_105.setObjectName("gridLayout_105")
        self.gridLayout_61.addLayout(self.gridLayout_105, 9, 21, 1, 1)
        self.gridLayout_143 = QtWidgets.QGridLayout()
        self.gridLayout_143.setObjectName("gridLayout_143")
        self.gridLayout_61.addLayout(self.gridLayout_143, 9, 2, 1, 1)
        self.gridLayout_122 = QtWidgets.QGridLayout()
        self.gridLayout_122.setObjectName("gridLayout_122")
        self.touch_1 = QtWidgets.QLabel(self.groupBox)
        self.touch_1.setText("")
        self.touch_1.setObjectName("touch_1")
        self.gridLayout_122.addWidget(self.touch_1, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_122, 2, 1, 5, 5)
        self.gridLayout_125 = QtWidgets.QGridLayout()
        self.gridLayout_125.setObjectName("gridLayout_125")
        self.ch_1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.ch_1.setFont(font)
        self.ch_1.setStyleSheet("color: #a9a9a9;")
        self.ch_1.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ch_1.setObjectName("ch_1")
        self.gridLayout_125.addWidget(self.ch_1, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_125, 7, 1, 2, 5)
        self.gridLayout_120 = QtWidgets.QGridLayout()
        self.gridLayout_120.setObjectName("gridLayout_120")
        self.des_touch = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.des_touch.setFont(font)
        self.des_touch.setObjectName("des_touch")
        self.gridLayout_120.addWidget(self.des_touch, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_120, 0, 0, 2, 33)
        self.gridLayout_144 = QtWidgets.QGridLayout()
        self.gridLayout_144.setObjectName("gridLayout_144")
        self.finger_1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(14)
        self.finger_1.setFont(font)
        self.finger_1.setObjectName("finger_1")
        self.gridLayout_144.addWidget(self.finger_1, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_144, 12, 1, 2, 8)
        self.gridLayout_121 = QtWidgets.QGridLayout()
        self.gridLayout_121.setObjectName("gridLayout_121")
        self.finger_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(14)
        self.finger_2.setFont(font)
        self.finger_2.setObjectName("finger_2")
        self.gridLayout_121.addWidget(self.finger_2, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_121, 14, 1, 2, 8)
        self.gridLayout_142 = QtWidgets.QGridLayout()
        self.gridLayout_142.setObjectName("gridLayout_142")
        self.finger_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(14)
        self.finger_3.setFont(font)
        self.finger_3.setObjectName("finger_3")
        self.gridLayout_142.addWidget(self.finger_3, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_142, 16, 1, 2, 8)
        self.gridLayout_145 = QtWidgets.QGridLayout()
        self.gridLayout_145.setObjectName("gridLayout_145")
        self.finger_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(14)
        self.finger_4.setFont(font)
        self.finger_4.setObjectName("finger_4")
        self.gridLayout_145.addWidget(self.finger_4, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_145, 18, 1, 2, 8)
        self.gridLayout_146 = QtWidgets.QGridLayout()
        self.gridLayout_146.setObjectName("gridLayout_146")
        self.finger_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(14)
        self.finger_5.setFont(font)
        self.finger_5.setObjectName("finger_5")
        self.gridLayout_146.addWidget(self.finger_5, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_146, 20, 1, 2, 8)
        self.gridLayout_147 = QtWidgets.QGridLayout()
        self.gridLayout_147.setObjectName("gridLayout_147")
        self.fin_position_1 = QtWidgets.QLabel(self.groupBox)
        self.fin_position_1.setText("")
        self.fin_position_1.setObjectName("fin_position_1")
        self.gridLayout_147.addWidget(self.fin_position_1, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_147, 16, 11, 4, 4)
        self.gridLayout_148 = QtWidgets.QGridLayout()
        self.gridLayout_148.setObjectName("gridLayout_148")
        self.fin_position_2 = QtWidgets.QLabel(self.groupBox)
        self.fin_position_2.setText("")
        self.fin_position_2.setObjectName("fin_position_2")
        self.gridLayout_148.addWidget(self.fin_position_2, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_148, 14, 15, 4, 4)
        self.gridLayout_149 = QtWidgets.QGridLayout()
        self.gridLayout_149.setObjectName("gridLayout_149")
        self.fin_position_3 = QtWidgets.QLabel(self.groupBox)
        self.fin_position_3.setText("")
        self.fin_position_3.setObjectName("fin_position_3")
        self.gridLayout_149.addWidget(self.fin_position_3, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_149, 14, 19, 4, 4)
        self.gridLayout_150 = QtWidgets.QGridLayout()
        self.gridLayout_150.setObjectName("gridLayout_150")
        self.fin_position_4 = QtWidgets.QLabel(self.groupBox)
        self.fin_position_4.setText("")
        self.fin_position_4.setObjectName("fin_position_4")
        self.gridLayout_150.addWidget(self.fin_position_4, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_150, 14, 23, 4, 4)
        self.gridLayout_151 = QtWidgets.QGridLayout()
        self.gridLayout_151.setObjectName("gridLayout_151")
        self.fin_position_5 = QtWidgets.QLabel(self.groupBox)
        self.fin_position_5.setText("")
        self.fin_position_5.setObjectName("fin_position_5")
        self.gridLayout_151.addWidget(self.fin_position_5, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_151, 14, 27, 4, 4)
        self.gridLayout_141 = QtWidgets.QGridLayout()
        self.gridLayout_141.setObjectName("gridLayout_141")
        self.des_finger_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        self.des_finger_4.setFont(font)
        self.des_finger_4.setObjectName("des_finger_4")
        self.gridLayout_141.addWidget(self.des_finger_4, 0, 0, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_141, 10, 0, 2, 27)
        self.gridLayout_44 = QtWidgets.QGridLayout()
        self.gridLayout_44.setObjectName("gridLayout_44")

        self.serial_scan = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(8)
        self.serial_scan.setFont(font)
        self.serial_scan.setObjectName("serial_scan")
        self.gridLayout_44.addWidget(self.serial_scan, 0, 0, 1, 1)
        self.serial_scan.clicked.connect(self.btn_click)

        self.gridLayout_61.addLayout(self.gridLayout_44, 10, 27, 2, 6)
        self.gridLayout.addWidget(self.groupBox, 4, 1, 21, 30)

        self.retranslateUi(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("pero", "pero"))
        self.setWindowIcon(QIcon("./img_frame/palmcat_title.png"))
        self.label.setText(_translate("serial", "<html><head/><body><p><span style=\" color:#a9a9a9;\">PERO</span> touch test tool</p></body></html>"))
        self.ch_4.setText(_translate("serial", "CH.4"))
        self.ch_5.setText(_translate("serial", "CH.5"))
        self.ch_8.setText(_translate("serial", "CH.8"))
        self.ch_7.setText(_translate("serial", "CH.7"))
        self.ch_6.setText(_translate("serial", "CH.6"))
        self.ch_10.setText(_translate("serial", "CH.10"))
        self.ch_2.setText(_translate("serial", "CH.2"))
        self.ch_9.setText(_translate("serial", "CH.9"))
        self.ch_3.setText(_translate("serial", "CH.3"))
        self.ch_1.setText(_translate("serial", "CH.1"))
        self.des_touch.setText(_translate("serial", "<html><head/><body><p>Touch recognition / Palm Side part <span style=\" font-size:8pt; color:#a9a9a9;\">터치센서에서 인식된 터치패널</span></p></body></html>"))
        self.finger_1.setText(_translate("serial", ""))
        self.finger_2.setText(_translate("serial", ""))
        self.finger_3.setText(_translate("serial", ""))
        self.finger_4.setText(_translate("serial", ""))
        self.finger_5.setText(_translate("serial", ""))
        self.des_finger_4.setText(_translate("serial", "<html><head/><body><p>Finger recognition / <span style=\" font-size:8pt; color:#a9a9a9;\">PERO가 감지한 손가락</span></p></body></html>"))
        self.serial_scan.setText(_translate("serial", "Serial Data Scan"))

        # 터치패널 객체 dictionary화
        self.touch_panel = {"touch1": self.touch_1, "touch2": self.touch_2, "touch3": self.touch_3,
                            "touch4": self.touch_4,
                            "touch5": self.touch_5, "touch6": self.touch_6, "touch7": self.touch_7,
                            "touch8": self.touch_8,
                            "touch9": self.touch_9, "touch10": self.touch_10}
        # 터치손가락 이미지 객체 dictionary화
        self.fin_touch_position = {"fin_tp1": self.fin_position_1, "fin_tp2": self.fin_position_2,
                                   "fin_tp3": self.fin_position_3,
                                   "fin_tp4": self.fin_position_4, "fin_tp5": self.fin_position_5}
        # 터치손가락 텍스트 객체 dictionary화
        self.fin_txt = {"fin_txt1": self.finger_1, "fin_txt2": self.finger_2,
                        "fin_txt3": self.finger_3, "fin_txt4": self.finger_4,
                        "fin_txt5": self.finger_5}

        palmcat_logo = QPixmap("./img_frame/logo.png")
        palmcat_logo = palmcat_logo.scaledToHeight(60)
        self.logo.setPixmap(QPixmap(palmcat_logo))

        # 터치패드 이미지
        self.touch_off = QPixmap("./img_frame/finger_off.png")
        self.touch_off = self.touch_off.scaledToHeight(90)
        self.touch_on = QPixmap("./img_frame/finger_on.png")
        self.touch_on = self.touch_on.scaledToHeight(90)
        # 터치패드 엄지 이미지
        self.touch_thumb_off = QPixmap("./img_frame/thumb_off.png")
        self.touch_thumb_off = self.touch_thumb_off.scaledToHeight(90)
        self.touch_thumb_on = QPixmap("./img_frame/thumb_on.png")
        self.touch_thumb_on = self.touch_thumb_on.scaledToHeight(90)
        # 손가락 터치 이미지
        self.fin_tp_off = QPixmap("./img_frame/touch_off.png")
        self.fin_tp_off = self.fin_tp_off.scaledToHeight(77)
        self.fin_tp_on = QPixmap("./img_frame/touch_on.png")
        self.fin_tp_on = self.fin_tp_on.scaledToHeight(77)

        # 초기 off 이미지 삽입
        for i in range(10):
            if i == 0:
                self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_thumb_off)
                self.touch_panel["touch" + str(i + 1)].setAlignment(QtCore.Qt.AlignCenter)
            else:
                self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_off)
                self.touch_panel["touch" + str(i + 1)].setAlignment(QtCore.Qt.AlignCenter)

        for i in range(5):
            self.fin_touch_position["fin_tp" + str(i + 1)].setPixmap(self.fin_tp_off)
            self.fin_touch_position["fin_tp" + str(i + 1)].setAlignment(QtCore.Qt.AlignCenter)

    def btn_click(self):

        reply = QtWidgets.QMessageBox.question(self, "serial", "터치 센서를 확인하겠습니까?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        # btn클릭하고 뜬 message를 yes
        if reply == QtWidgets.QMessageBox.Yes:
            # serial data 읽는 파일 실행
            subprocess_list.append(subprocess.Popen('serial_data.exe', shell=True))
            # serial_data.txt파일의 변화가 생길때마다 label_change함수를 실행
            self.watcher = QtCore.QFileSystemWatcher(self)
            self.watcher.addPath("./serial_data.txt")
            self.watcher.fileChanged.connect(self.label_change)

    # serial_data.txt파일 변화가 생기면 실행
    def label_change(self, path):
        # serial_data.txt 파일 읽어서 text_data에 저장
        with open(path, 'r') as f:
            text_data = f.read()
            # txt파일에 disconnection이 write되었다면(연결이 끊어져있다면)
            if text_data == "disconnection":
                print(text_data)
                # subprocess죽이고 txt변화 읽는 path 지우기
                kill_process()
                self.watcher.removePath(path)
                reply = QtWidgets.QMessageBox.question(self, "serial", "연결에 문제가 생겼습니다.\n다시 연결하고 시도해주세요.", QtWidgets.QMessageBox.Ok)
                # serial_data를 삭제
                # 터치패널 off 이미지
                for i in range(10):
                    if i == 0:
                        self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_thumb_off)
                    else:
                        self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_off)

                # 손가락 터치 위치 off 이미지
                for i in range(5):
                    self.fin_touch_position["fin_tp" + str(i + 1)].setPixmap(self.fin_tp_off)

                # 누른 손가락 text 지우기
                for i in range(5):
                    self.fin_txt["fin_txt" + str(i + 1)].setText("")
            # txt파일에 data error 즉, 들어오는 데이터에 이상이 생겼다면
            elif text_data == "data_error":
                print(text_data)
                # serial data를 그만 읽고 위젯 모든 객체 초기화
                kill_process()
                self.watcher.removePath(path)
                reply = QtWidgets.QMessageBox.question(self, "serial", "데이터에 문제가 생겼습니다.\n연결을 끊었다가 다시 연결하고 시도해주세요.", QtWidgets.QMessageBox.Ok)
                for i in range(10):
                    if i == 0:
                        self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_thumb_off)
                    else:
                        self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_off)

                for i in range(5):
                    self.fin_touch_position["fin_tp" + str(i + 1)].setPixmap(self.fin_tp_off)
                for i in range(5):
                    self.fin_txt["fin_txt" + str(i + 1)].setText("")
            # txt파일에 serial data가 들어온다면
            else:
                # serial_txt에 list로 터치패널 값을 저장
                serial_txt = text_data.split(",")

                for i in range(10):
                    # serial data가 1인 패널은 on 이미지로
                    if i == 0:
                        if serial_txt[i] == "1":
                            self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_thumb_on)
                        elif serial_txt[i] == "0":
                            self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_thumb_off)
                    else:
                        if serial_txt[i] == "1":
                            self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_on)
                        elif serial_txt[i] == "0":
                            self.touch_panel["touch" + str(i + 1)].setPixmap(self.touch_off)
                    # thumb를 터치했을때
                    if serial_txt[0] == "1":
                        # serial data값을 표기하기 전에 이전에 입력된 데이터를 없애줌
                        for a in range(5):
                            self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                        for a in range(5):
                            self.fin_txt["fin_txt" + str(a + 1)].setText("")
                        # 어떤 손가락을 눌렀는지 text와 이미지로 표현
                        self.finger_1.setText("Thumb")
                        self.fin_position_1.setPixmap(self.fin_tp_on)
                        if serial_txt[1] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_1.setText("Thumb")
                            self.finger_2.setText("Index")
                            self.fin_position_1.setPixmap(self.fin_tp_on)
                            self.fin_position_2.setPixmap(self.fin_tp_on)
                            #############################
                            if serial_txt[4] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_1.setText("Thumb")
                                self.finger_2.setText("Index")
                                self.finger_3.setText("Middle")
                                self.fin_position_1.setPixmap(self.fin_tp_on)
                                self.fin_position_2.setPixmap(self.fin_tp_on)
                                self.fin_position_3.setPixmap(self.fin_tp_on)
                                if serial_txt[6] == "1":
                                    for a in range(5):
                                        self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                    for a in range(5):
                                        self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                    self.finger_1.setText("Thumb")
                                    self.finger_2.setText("Index")
                                    self.finger_3.setText("Middle")
                                    self.finger_4.setText("Ring")
                                    self.fin_position_1.setPixmap(self.fin_tp_on)
                                    self.fin_position_2.setPixmap(self.fin_tp_on)
                                    self.fin_position_3.setPixmap(self.fin_tp_on)
                                    self.fin_position_4.setPixmap(self.fin_tp_on)
                                    if serial_txt[9] == "1":
                                        for a in range(5):
                                            self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                        for a in range(5):
                                            self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                        self.finger_1.setText("Thumb")
                                        self.finger_2.setText("Index")
                                        self.finger_3.setText("Middle")
                                        self.finger_4.setText("Ring")
                                        self.finger_5.setText("Pinky")
                                        self.fin_position_1.setPixmap(self.fin_tp_on)
                                        self.fin_position_2.setPixmap(self.fin_tp_on)
                                        self.fin_position_3.setPixmap(self.fin_tp_on)
                                        self.fin_position_4.setPixmap(self.fin_tp_on)
                                        self.fin_position_5.setPixmap(self.fin_tp_on)
                                elif serial_txt[9] == "1":
                                    for a in range(5):
                                        self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                    for a in range(5):
                                        self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                    self.finger_1.setText("Thumb")
                                    self.finger_2.setText("Index")
                                    self.finger_3.setText("Middle")
                                    self.finger_5.setText("Pinky")
                                    self.fin_position_1.setPixmap(self.fin_tp_on)
                                    self.fin_position_2.setPixmap(self.fin_tp_on)
                                    self.fin_position_3.setPixmap(self.fin_tp_on)
                                    self.fin_position_5.setPixmap(self.fin_tp_on)
                            elif serial_txt[6] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_1.setText("Thumb")
                                self.finger_2.setText("Index")
                                self.finger_4.setText("Ring")
                                self.fin_position_1.setPixmap(self.fin_tp_on)
                                self.fin_position_2.setPixmap(self.fin_tp_on)
                                self.fin_position_4.setPixmap(self.fin_tp_on)
                                if serial_txt[9] == "1":
                                    for a in range(5):
                                        self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                    for a in range(5):
                                        self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                    self.finger_1.setText("Thumb")
                                    self.finger_2.setText("Index")
                                    self.finger_4.setText("Ring")
                                    self.finger_5.setText("Pinky")
                                    self.fin_position_1.setPixmap(self.fin_tp_on)
                                    self.fin_position_2.setPixmap(self.fin_tp_on)
                                    self.fin_position_4.setPixmap(self.fin_tp_on)
                                    self.fin_position_5.setPixmap(self.fin_tp_on)
                            elif serial_txt[9] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_1.setText("Thumb")
                                self.finger_2.setText("Index")
                                self.finger_5.setText("Pinky")
                                self.fin_position_1.setPixmap(self.fin_tp_on)
                                self.fin_position_2.setPixmap(self.fin_tp_on)
                                self.fin_position_5.setPixmap(self.fin_tp_on)
                        elif serial_txt[4] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_1.setText("Thumb")
                            self.finger_3.setText("Middle")
                            self.fin_position_1.setPixmap(self.fin_tp_on)
                            self.fin_position_3.setPixmap(self.fin_tp_on)
                            if serial_txt[6] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_1.setText("Thumb")
                                self.finger_3.setText("Middle")
                                self.finger_4.setText("Ring")
                                self.fin_position_1.setPixmap(self.fin_tp_on)
                                self.fin_position_3.setPixmap(self.fin_tp_on)
                                self.fin_position_4.setPixmap(self.fin_tp_on)
                                if serial_txt[9] == "1":
                                    for a in range(5):
                                        self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                    for a in range(5):
                                        self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                    self.finger_1.setText("Thumb")
                                    self.finger_3.setText("Middle")
                                    self.finger_4.setText("Ring")
                                    self.finger_5.setText("Pinky")
                                    self.fin_position_1.setPixmap(self.fin_tp_on)
                                    self.fin_position_3.setPixmap(self.fin_tp_on)
                                    self.fin_position_4.setPixmap(self.fin_tp_on)
                                    self.fin_position_5.setPixmap(self.fin_tp_on)
                            elif serial_txt[9] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_1.setText("Thumb")
                                self.finger_3.setText("Middle")
                                self.finger_5.setText("Pinky")
                                self.fin_position_1.setPixmap(self.fin_tp_on)
                                self.fin_position_3.setPixmap(self.fin_tp_on)
                                self.fin_position_5.setPixmap(self.fin_tp_on)
                        elif serial_txt[6] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_1.setText("Thumb")
                            self.finger_4.setText("Ring")
                            self.fin_position_1.setPixmap(self.fin_tp_on)
                            self.fin_position_4.setPixmap(self.fin_tp_on)
                            if serial_txt[9] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_1.setText("Thumb")
                                self.finger_4.setText("Ring")
                                self.finger_5.setText("Pinky")
                                self.fin_position_1.setPixmap(self.fin_tp_on)
                                self.fin_position_4.setPixmap(self.fin_tp_on)
                                self.fin_position_5.setPixmap(self.fin_tp_on)
                        elif serial_txt[9] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_1.setText("Thumb")
                            self.finger_5.setText("Pinky")
                            self.fin_position_1.setPixmap(self.fin_tp_on)
                            self.fin_position_5.setPixmap(self.fin_tp_on)
                    elif serial_txt[1] == "1":
                        for a in range(5):
                            self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                        for a in range(5):
                            self.fin_txt["fin_txt" + str(a + 1)].setText("")

                        self.finger_2.setText("Index")
                        self.fin_position_2.setPixmap(self.fin_tp_on)
                        if serial_txt[4] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_2.setText("Index")
                            self.finger_3.setText("Middle")
                            self.fin_position_2.setPixmap(self.fin_tp_on)
                            self.fin_position_3.setPixmap(self.fin_tp_on)
                            if serial_txt[6] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_2.setText("Index")
                                self.finger_3.setText("Middle")
                                self.finger_4.setText("Ring")
                                self.fin_position_2.setPixmap(self.fin_tp_on)
                                self.fin_position_3.setPixmap(self.fin_tp_on)
                                self.fin_position_4.setPixmap(self.fin_tp_on)
                                if serial_txt[9] == "1":
                                    for a in range(5):
                                        self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                    for a in range(5):
                                        self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                    self.finger_2.setText("Index")
                                    self.finger_3.setText("Middle")
                                    self.finger_4.setText("Ring")
                                    self.finger_5.setText("Pinky")
                                    self.fin_position_2.setPixmap(self.fin_tp_on)
                                    self.fin_position_3.setPixmap(self.fin_tp_on)
                                    self.fin_position_4.setPixmap(self.fin_tp_on)
                                    self.fin_position_5.setPixmap(self.fin_tp_on)
                            elif serial_txt[9] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_2.setText("Index")
                                self.finger_3.setText("Middle")
                                self.finger_5.setText("Pinky")
                                self.fin_position_2.setPixmap(self.fin_tp_on)
                                self.fin_position_3.setPixmap(self.fin_tp_on)
                                self.fin_position_5.setPixmap(self.fin_tp_on)
                        elif serial_txt[6] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_2.setText("Index")
                            self.finger_4.setText("Ring")
                            self.fin_position_2.setPixmap(self.fin_tp_on)
                            self.fin_position_4.setPixmap(self.fin_tp_on)
                            if serial_txt[9] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_2.setText("Index")
                                self.finger_4.setText("Ring")
                                self.finger_5.setText("Pinky")
                                self.fin_position_2.setPixmap(self.fin_tp_on)
                                self.fin_position_4.setPixmap(self.fin_tp_on)
                                self.fin_position_5.setPixmap(self.fin_tp_on)
                        elif serial_txt[9] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_2.setText("Index")
                            self.finger_5.setText("Pinky")
                            self.fin_position_2.setPixmap(self.fin_tp_on)
                            self.fin_position_5.setPixmap(self.fin_tp_on)
                    elif serial_txt[4] == "1":
                        for a in range(5):
                            self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                        for a in range(5):
                            self.fin_txt["fin_txt" + str(a + 1)].setText("")

                        self.finger_3.setText("Middle")
                        self.fin_position_3.setPixmap(self.fin_tp_on)
                        if serial_txt[6] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_3.setText("Middle")
                            self.finger_4.setText("Ring")
                            self.fin_position_2.setPixmap(self.fin_tp_on)
                            self.fin_position_4.setPixmap(self.fin_tp_on)
                            if serial_txt[9] == "1":
                                for a in range(5):
                                    self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                                for a in range(5):
                                    self.fin_txt["fin_txt" + str(a + 1)].setText("")

                                self.finger_3.setText("Middle")
                                self.finger_4.setText("Ring")
                                self.finger_5.setText("Pinky")
                                self.fin_position_3.setPixmap(self.fin_tp_on)
                                self.fin_position_4.setPixmap(self.fin_tp_on)
                                self.fin_position_5.setPixmap(self.fin_tp_on)
                        elif serial_txt[9] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_3.setText("Middle")
                            self.finger_5.setText("Pinky")
                            self.fin_position_3.setPixmap(self.fin_tp_on)
                            self.fin_position_5.setPixmap(self.fin_tp_on)
                    elif serial_txt[6] == "1":
                        for a in range(5):
                            self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                        for a in range(5):
                            self.fin_txt["fin_txt" + str(a + 1)].setText("")

                        self.finger_4.setText("Ring")
                        self.fin_position_4.setPixmap(self.fin_tp_on)
                        if serial_txt[9] == "1":
                            for a in range(5):
                                self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                            for a in range(5):
                                self.fin_txt["fin_txt" + str(a + 1)].setText("")

                            self.finger_4.setText("Ring")
                            self.finger_5.setText("Pinky")
                            self.fin_position_4.setPixmap(self.fin_tp_on)
                            self.fin_position_5.setPixmap(self.fin_tp_on)
                    elif serial_txt[9] == "1":
                        for a in range(5):
                            self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                        for a in range(5):
                            self.fin_txt["fin_txt" + str(a + 1)].setText("")

                        self.finger_5.setText("Pinky")
                        self.fin_position_5.setPixmap(self.fin_tp_on)
                        #############
                    else:
                        for a in range(5):
                            self.fin_touch_position["fin_tp" + str(a + 1)].setPixmap(self.fin_tp_off)
                        for a in range(5):
                            self.fin_txt["fin_txt" + str(a + 1)].setText("")

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
