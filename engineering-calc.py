```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Engineering-calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 749)
        MainWindow.setMinimumSize(QtCore.QSize(472, 749))
        MainWindow.setMaximumSize(QtCore.QSize(472, 749))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 471, 743))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.toolButton_4 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("4", 1))
        self.toolButton_4.setGeometry(QtCore.QRect(10, 400, 91, 91))
        self.toolButton_4.setObjectName("toolButton_4")
        self.pushButton = QtWidgets.QPushButton(self.tab, clicked = lambda: self.operator_it("^", 1))
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 93, 51))
        self.pushButton.setObjectName("pushButton")
        self.toolButton_11 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("0", 1))
        self.toolButton_11.setGeometry(QtCore.QRect(120, 620, 91, 91))
        self.toolButton_11.setObjectName("toolButton_11")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab, clicked = lambda: self.math_it(1))
        self.pushButton_4.setGeometry(QtCore.QRect(340, 220, 93, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.toolButton_16 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.operator_it("+", 1))
        self.toolButton_16.setGeometry(QtCore.QRect(340, 620, 91, 91))
        self.toolButton_16.setObjectName("toolButton_16")
        self.toolButton = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("1", 1))
        self.toolButton.setGeometry(QtCore.QRect(10, 290, 91, 91))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_3 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("3", 1))
        self.toolButton_3.setGeometry(QtCore.QRect(230, 290, 91, 91))
        self.toolButton_3.setObjectName("toolButton_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 421, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.toolButton_10 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.operator_it("%", 1))
        self.toolButton_10.setGeometry(QtCore.QRect(10, 620, 91, 91))
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_15 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.operator_it("-", 1))
        self.toolButton_15.setGeometry(QtCore.QRect(340, 510, 91, 91))
        self.toolButton_15.setObjectName("toolButton_15")
        self.toolButton_14 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.operator_it("x", 1))
        self.toolButton_14.setGeometry(QtCore.QRect(340, 400, 91, 91))
        self.toolButton_14.setObjectName("toolButton_14")
        self.toolButton_7 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("7", 1))
        self.toolButton_7.setGeometry(QtCore.QRect(10, 510, 91, 91))
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_9 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("9", 1))
        self.toolButton_9.setGeometry(QtCore.QRect(230, 510, 91, 91))
        self.toolButton_9.setObjectName("toolButton_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab, clicked = lambda: self.remove_it(1))
        self.pushButton_3.setGeometry(QtCore.QRect(230, 220, 93, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.toolButton_5 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("5", 1))
        self.toolButton_5.setGeometry(QtCore.QRect(120, 400, 91, 91))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("2", 1))
        self.toolButton_2.setGeometry(QtCore.QRect(120, 290, 91, 91))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_13 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.operator_it("/", 1))
        self.toolButton_13.setGeometry(QtCore.QRect(340, 290, 91, 91))
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton_6 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("6", 1))
        self.toolButton_6.setGeometry(QtCore.QRect(230, 400, 91, 91))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_8 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.press_it("8", 1))
        self.toolButton_8.setGeometry(QtCore.QRect(120, 510, 91, 91))
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_12 = QtWidgets.QToolButton(self.tab, clicked = lambda: self.dot_it(1))
        self.toolButton_12.setGeometry(QtCore.QRect(230, 620, 91, 91))
        self.toolButton_12.setObjectName("toolButton_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab, clicked = lambda: self.press_it("c", 1))
        self.pushButton_2.setGeometry(QtCore.QRect(120, 220, 93, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 421, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.toolButton_17 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("1", 2))
        self.toolButton_17.setGeometry(QtCore.QRect(90, 440, 71, 61))
        self.toolButton_17.setObjectName("toolButton_17")
        self.toolButton_18 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("2", 2))
        self.toolButton_18.setGeometry(QtCore.QRect(180, 440, 71, 61))
        self.toolButton_18.setObjectName("toolButton_18")
        self.toolButton_19 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("3", 2))
        self.toolButton_19.setGeometry(QtCore.QRect(270, 440, 71, 61))
        self.toolButton_19.setObjectName("toolButton_19")
        self.toolButton_20 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("4", 2))
        self.toolButton_20.setGeometry(QtCore.QRect(90, 510, 71, 61))
        self.toolButton_20.setObjectName("toolButton_20")
        self.toolButton_21 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("5", 2))
        self.toolButton_21.setGeometry(QtCore.QRect(180, 510, 71, 61))
        self.toolButton_21.setObjectName("toolButton_21")
        self.toolButton_22 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("6", 2))
        self.toolButton_22.setGeometry(QtCore.QRect(270, 510, 71, 61))
        self.toolButton_22.setObjectName("toolButton_22")
        self.toolButton_23 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("7", 2))
        self.toolButton_23.setGeometry(QtCore.QRect(90, 580, 71, 61))
        self.toolButton_23.setObjectName("toolButton_23")
        self.toolButton_24 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("8", 2))
        self.toolButton_24.setGeometry(QtCore.QRect(180, 580, 71, 61))
        self.toolButton_24.setObjectName("toolButton_24")
        self.toolButton_25 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("9", 2))
        self.toolButton_25.setGeometry(QtCore.QRect(270, 580, 71, 61))
        self.toolButton_25.setObjectName("toolButton_25")
        self.toolButton_26 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("0", 2))
        self.toolButton_26.setGeometry(QtCore.QRect(180, 650, 71, 61))
        self.toolButton_26.setObjectName("toolButton_26")
        self.toolButton_27 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.dot_it(2))
        self.toolButton_27.setGeometry(QtCore.QRect(270, 650, 71, 61))
        self.toolButton_27.setObjectName("toolButton_27")
        self.toolButton_28 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.operator_it("%", 2))
        self.toolButton_28.setGeometry(QtCore.QRect(90, 650, 71, 61))
        self.toolButton_28.setObjectName("toolButton_28")
        self.toolButton_29 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.operator_it("/", 2))
        self.toolButton_29.setGeometry(QtCore.QRect(360, 440, 71, 61))
        self.toolButton_29.setObjectName("toolButton_29")
        self.toolButton_30 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.operator_it("x", 2))
        self.toolButton_30.setGeometry(QtCore.QRect(360, 510, 71, 61))
        self.toolButton_30.setObjectName("toolButton_30")
        self.toolButton_31 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.operator_it("-", 2))
        self.toolButton_31.setGeometry(QtCore.QRect(360, 580, 71, 61))
        self.toolButton_31.setObjectName("toolButton_31")
        self.toolButton_32 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.operator_it("+", 2))
        self.toolButton_32.setGeometry(QtCore.QRect(360, 650, 71, 61))
        self.toolButton_32.setObjectName("toolButton_32")
        self.toolButton_33 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.math_it(2))
        self.toolButton_33.setGeometry(QtCore.QRect(360, 210, 71, 61))
        self.toolButton_33.setObjectName("toolButton_33")
        self.toolButton_34 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.remove_it(2))
        self.toolButton_34.setGeometry(QtCore.QRect(270, 210, 71, 61))
        self.toolButton_34.setObjectName("toolButton_34")
        self.toolButton_35 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.press_it("c", 2))
        self.toolButton_35.setGeometry(QtCore.QRect(180, 210, 71, 61))
        self.toolButton_35.setObjectName("toolButton_35")
        self.toolButton_36 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.operator_it("^", 2))
        self.toolButton_36.setGeometry(QtCore.QRect(90, 210, 71, 61))
        self.toolButton_36.setObjectName("toolButton_36")
        self.toolButton_37 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.pi_it())
        self.toolButton_37.setGeometry(QtCore.QRect(90, 290, 71, 61))
        self.toolButton_37.setObjectName("toolButton_37")
        self.toolButton_40 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.fact_it())
        self.toolButton_40.setGeometry(QtCore.QRect(360, 360, 71, 61))
        self.toolButton_40.setObjectName("toolButton_40")
        self.toolButton_41 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.log_it())
        self.toolButton_41.setGeometry(QtCore.QRect(270, 360, 71, 61))
        self.toolButton_41.setObjectName("toolButton_41")
        self.toolButton_42 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.cot_it())
        self.toolButton_42.setGeometry(QtCore.QRect(10, 360, 61, 61))
        self.toolButton_42.setObjectName("toolButton_42")
        self.toolButton_43 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.sin_it())
        self.toolButton_43.setGeometry(QtCore.QRect(10, 440, 61, 61))
        self.toolButton_43.setObjectName("toolButton_43")
        self.toolButton_44 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.cos_it())
        self.toolButton_44.setGeometry(QtCore.QRect(10, 510, 61, 61))
        self.toolButton_44.setObjectName("toolButton_44")
        self.toolButton_45 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_45.setGeometry(QtCore.QRect(10, 210, 61, 61))
        self.toolButton_45.setObjectName("toolButton_45")
        self.toolButton_38 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.abs_it())
        self.toolButton_38.setGeometry(QtCore.QRect(360, 290, 71, 61))
        self.toolButton_38.setObjectName("toolButton_38")
        self.toolButton_39 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.one_on_it())
        self.toolButton_39.setGeometry(QtCore.QRect(270, 290, 71, 61))
        self.toolButton_39.setObjectName("toolButton_39")
        self.toolButton_46 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.sec_it())
        self.toolButton_46.setGeometry(QtCore.QRect(10, 580, 61, 61))
        self.toolButton_46.setObjectName("toolButton_46")
        self.toolButton_47 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.csc_it())
        self.toolButton_47.setGeometry(QtCore.QRect(10, 650, 61, 61))
        self.toolButton_47.setObjectName("toolButton_47")
        self.toolButton_48 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.tan_it())
        self.toolButton_48.setGeometry(QtCore.QRect(10, 290, 61, 61))
        self.toolButton_48.setObjectName("toolButton_48")
        self.toolButton_49 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.open_it())
        self.toolButton_49.setGeometry(QtCore.QRect(90, 360, 71, 61))
        self.toolButton_49.setObjectName("toolButton_49")
        self.toolButton_50 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.close_it())
        self.toolButton_50.setGeometry(QtCore.QRect(180, 360, 71, 61))
        self.toolButton_50.setObjectName("toolButton_50")
        self.toolButton_51 = QtWidgets.QToolButton(self.tab_2, clicked = lambda: self.sqrt_it())
        self.toolButton_51.setGeometry(QtCore.QRect(180, 290, 71, 61))
        self.toolButton_51.setObjectName("toolButton_51")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def math_it(self, tab):
        if tab == 1 :
            screen = self.label.text()
            s1 = screen.replace("^", "**")
            s2 = s1.replace("%", "/100*")
            s3 = s2.replace("x", "*")
            try:
                answer = eval(s3)
                self.label.setText(str(answer))
            except:
                self.label.setText("Error")
        elif tab == 2 :
            screen = self.label_2.text()
            s1 = screen.replace("^", "**")
            s2 = s1.replace("%", "/100*")
            s3 = s2.replace("x", "*")
            x = len(s3) - 1
            if s3[x] == "+" or s3[x] == "-" or s3[x] == "/" or s3[x] == "x" or s3[x] == "^" or s3[x] == "%" or s3[x] == "(" :
                s3 += "0"
            countO = countC = 0
            for l in screen :
                if l == "(" :
                    countO += 1
                elif l == ")" :
                    countC += 1 
            if countO > countC :
                s3 += (countO - countC) * ")"
            try:
                answer = eval(s3)
                self.label_2.setText(str(answer))
            except:
                self.label_2.setText("Error")
        
    def open_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        x = len(screen) - 1
        if screen[x] == "+" or screen[x] == "-" or screen[x] == "/" or screen[x] == "x" or screen[x] == "^" or screen[x] == "%" or screen[x] == "(" :
            self.label_2.setText(f'{screen}{"("}')
        else :
            self.label_2.setText(f'{screen}{"x("}')

    def close_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        countO = countC = 0
        for l in screen :
            if l == "(" :
                countO += 1
            elif l == ")" :
                countC += 1
        if countO > countC :
            if screen[len(screen)-1] == "(" :
                self.label_2.setText(f'{screen}{"0)"}')
            elif screen[len(screen)-1] == '+' or screen[len(screen)-1] == '-' or screen[len(screen)-1] == 'x' or screen[len(screen)-1] == '/' or screen[len(screen)-1] == '%' or screen[len(screen)-1] == '^' :
                screen = screen[:-1]
                self.label_2.setText(f'{screen}{")"}')
            else :
                self.label_2.setText(f'{screen}{")"}')
        else :
            self.label_2.setText(screen)
    
    def sin_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.sin(math.radians(" + screen[index+1:] + "))"
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def cos_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.cos(math.radians(" + screen[index+1:] + "))"
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def tan_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.tan(math.radians(" + screen[index+1:] + "))"
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def cot_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "1 / math.tan(math.radians(" + screen[index+1:] + "))"
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def sec_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.cos(math.radians(" + screen[index+1:] + "))"
            answer = eval(string)
            answer = 1 / answer
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def csc_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.sin(math.radians(" + screen[index+1:] + "))"
            answer = eval(string)
            answer = 1 / answer
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")
    
    def abs_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        if screen[index] == '-' :
            screen = screen[:index] + "+" + screen[index+1:]
        self.label_2.setText(screen)

    def log_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.log10(" + screen[index+1:] + ")"
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def sqrt_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.sqrt(" + screen[index+1:] + ")"
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def one_on_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "1/" + screen[index+1:]
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def fact_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.factorial(" + screen[index+1:] + ")"
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")

    def pi_it(self):
        screen = self.label_2.text()
        if screen == "Error" :
            screen = "0"
        index = 0
        for i in range(0, len(screen)) :
            if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                index = i 
        try :
            if index == 0 :
                index = -1
            string = "math.pi"
            answer = eval(string)
            answer = "{}".format(answer)
            screen = screen[:index+1] + answer
            self.label_2.setText(screen)
        except :
            self.label_2.setText("Error")
    
    def operator_it(self, pressed, tab):
        if tab == 1 :
            screen = self.label.text()
            if screen == "Error" :
                screen = '0'
            if screen[-1] != '+' and screen[-1] != '-' and screen[-1] != 'x' and screen[-1] != '/' and screen[-1] != '^' and screen[-1] != '%' :
                self.label.setText(f'{screen}{pressed}')
            else :
                screen = screen[:-1]
                self.label.setText(f'{screen}{pressed}')
        elif tab == 2 :
            screen = self.label_2.text()
            if screen == "Error" :
                screen = '0'
            if screen[-1] == "(" :
                self.label_2.setText(f'{screen}{"0"}{pressed}')
            elif screen[-1] != '+' and screen[-1] != '-' and screen[-1] != 'x' and screen[-1] != '/' and screen[-1] != '^' and screen[-1] != '%' :
                self.label_2.setText(f'{screen}{pressed}')
            else :
                screen = screen[:-1]
                self.label_2.setText(f'{screen}{pressed}')
    
    def remove_it(self, tab):
        if tab == 1 :
            screen = self.label.text()
            if screen == "Error" :
                screen = '0'
            else :
                screen = screen[:-1]
            if len(screen) == 0 :
                screen = '0'
            self.label.setText(screen)
        elif tab == 2 :
            screen = self.label_2.text()
            if screen == "Error" :
                screen = '0'
            else :
                screen = screen[:-1]
            if len(screen) == 0 :
                screen = '0'
            self.label_2.setText(screen)
    
    def dot_it(self, tab):
        if tab == 1 :
            screen = self.label.text()
            if screen == "Error" :
                screen = "0"
            index = 0
            flag = True
            for i in range(0, len(screen)) :
                if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                    index = i 
            for i in range(index+1, len(screen)) :
                if screen[i] == "." :
                    flag = False
                    break
            if flag == True:
                self.label.setText(f'{screen}.')
        elif tab == 2 :
            screen = self.label_2.text()
            if screen == "Error" :
                screen = "0"
            index = 0
            flag = True
            for i in range(0, len(screen)) :
                if screen[i] == "+" or screen[i] == "-" or screen[i] == "x" or screen[i] == "/" or screen[i] == "^" or screen[i] == "%" :
                    index = i 
            for i in range(index+1, len(screen)) :
                if screen[i] == "." :
                    flag = False
                    break
            if flag == True:
                self.label_2.setText(f'{screen}.')
    
    def press_it(self, pressed, tab):
        if tab == 1 :
            screen = self.label.text()
            if(pressed=='c') or screen == "Error":
                self.label.setText('0')
            else :
                if(self.label.text()=='0'):
                    self.label.setText("")
                self.label.setText(f'{self.label.text()}{pressed}')
        elif tab == 2 :
            screen = self.label_2.text()
            if(pressed=='c') or screen == "Error":
                self.label_2.setText('0')
            else :
                if(self.label_2.text()=='0'):
                    self.label_2.setText("")
                if screen[len(screen)-1] == ")" :
                    self.label_2.setText(f'{self.label_2.text()}{"x"}{pressed}')
                else :
                    self.label_2.setText(f'{self.label_2.text()}{pressed}')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Engineering-Calculator"))
        self.toolButton_4.setText(_translate("MainWindow", "4"))
        self.toolButton_4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton.setText(_translate("MainWindow", "^"))
        self.pushButton.setShortcut(_translate("MainWindow", "^"))
        self.toolButton_11.setText(_translate("MainWindow", "0"))
        self.toolButton_11.setShortcut(_translate("MainWindow", "0"))
        self.pushButton_4.setText(_translate("MainWindow", "="))
        self.pushButton_4.setShortcut(_translate("MainWindow", "Enter"))
        self.toolButton_16.setText(_translate("MainWindow", "+"))
        self.toolButton_16.setShortcut(_translate("MainWindow", "+"))
        self.toolButton.setText(_translate("MainWindow", "1"))
        self.toolButton.setShortcut(_translate("MainWindow", "1"))
        self.toolButton_3.setText(_translate("MainWindow", "3"))
        self.toolButton_3.setShortcut(_translate("MainWindow", "3"))
        self.label.setText(_translate("MainWindow", "0"))
        self.toolButton_10.setText(_translate("MainWindow", "%"))
        self.toolButton_10.setShortcut(_translate("MainWindow", "%"))
        self.toolButton_15.setText(_translate("MainWindow", "-"))
        self.toolButton_15.setShortcut(_translate("MainWindow", "-"))
        self.toolButton_14.setText(_translate("MainWindow", "x"))
        self.toolButton_14.setShortcut(_translate("MainWindow", "*"))
        self.toolButton_7.setText(_translate("MainWindow", "7"))
        self.toolButton_7.setShortcut(_translate("MainWindow", "7"))
        self.toolButton_9.setText(_translate("MainWindow", "9"))
        self.toolButton_9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_3.setText(_translate("MainWindow", "Backspace"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Backspace"))
        self.toolButton_5.setText(_translate("MainWindow", "5"))
        self.toolButton_5.setShortcut(_translate("MainWindow", "5"))
        self.toolButton_2.setText(_translate("MainWindow", "2"))
        self.toolButton_2.setShortcut(_translate("MainWindow", "2"))
        self.toolButton_13.setText(_translate("MainWindow", "/"))
        self.toolButton_13.setShortcut(_translate("MainWindow", "/"))
        self.toolButton_6.setText(_translate("MainWindow", "6"))
        self.toolButton_6.setShortcut(_translate("MainWindow", "6"))
        self.toolButton_8.setText(_translate("MainWindow", "8"))
        self.toolButton_8.setShortcut(_translate("MainWindow", "8"))
        self.toolButton_12.setText(_translate("MainWindow", "."))
        self.toolButton_12.setShortcut(_translate("MainWindow", "."))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Del"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "simple"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.toolButton_17.setText(_translate("MainWindow", "1"))
        self.toolButton_17.setShortcut(_translate("MainWindow", "1"))
        self.toolButton_18.setText(_translate("MainWindow", "2"))
        self.toolButton_18.setShortcut(_translate("MainWindow", "2"))
        self.toolButton_19.setText(_translate("MainWindow", "3"))
        self.toolButton_19.setShortcut(_translate("MainWindow", "3"))
        self.toolButton_20.setText(_translate("MainWindow", "4"))
        self.toolButton_20.setShortcut(_translate("MainWindow", "4"))
        self.toolButton_21.setText(_translate("MainWindow", "5"))
        self.toolButton_21.setShortcut(_translate("MainWindow", "5"))
        self.toolButton_22.setText(_translate("MainWindow", "6"))
        self.toolButton_22.setShortcut(_translate("MainWindow", "6"))
        self.toolButton_23.setText(_translate("MainWindow", "7"))
        self.toolButton_23.setShortcut(_translate("MainWindow", "7"))
        self.toolButton_24.setText(_translate("MainWindow", "8"))
        self.toolButton_24.setShortcut(_translate("MainWindow", "8"))
        self.toolButton_25.setText(_translate("MainWindow", "9"))
        self.toolButton_25.setShortcut(_translate("MainWindow", "9"))
        self.toolButton_26.setText(_translate("MainWindow", "0"))
        self.toolButton_26.setShortcut(_translate("MainWindow", "0"))
        self.toolButton_27.setText(_translate("MainWindow", "."))
        self.toolButton_27.setShortcut(_translate("MainWindow", "."))
        self.toolButton_28.setText(_translate("MainWindow", "%"))
        self.toolButton_28.setShortcut(_translate("MainWindow", "%"))
        self.toolButton_29.setText(_translate("MainWindow", "/"))
        self.toolButton_29.setShortcut(_translate("MainWindow", "/"))
        self.toolButton_30.setText(_translate("MainWindow", "x"))
        self.toolButton_30.setShortcut(_translate("MainWindow", "*"))
        self.toolButton_31.setText(_translate("MainWindow", "-"))
        self.toolButton_31.setShortcut(_translate("MainWindow", "-"))
        self.toolButton_32.setText(_translate("MainWindow", "+"))
        self.toolButton_32.setShortcut(_translate("MainWindow", "+"))
        self.toolButton_33.setText(_translate("MainWindow", "="))
        self.toolButton_33.setShortcut(_translate("MainWindow", "Enter"))
        self.toolButton_34.setText(_translate("MainWindow", "Backspace"))
        self.toolButton_34.setShortcut(_translate("MainWindow", "Backspace"))
        self.toolButton_35.setText(_translate("MainWindow", "Clear"))
        self.toolButton_35.setShortcut(_translate("MainWindow", "Del"))
        self.toolButton_36.setText(_translate("MainWindow", "^"))
        self.toolButton_36.setShortcut(_translate("MainWindow", "^"))
        self.toolButton_37.setText(_translate("MainWindow", "pi"))
        self.toolButton_37.setShortcut(_translate("MainWindow", "P"))
        self.toolButton_40.setText(_translate("MainWindow", "n!"))
        self.toolButton_40.setShortcut(_translate("MainWindow", "!"))
        self.toolButton_41.setText(_translate("MainWindow", "log"))
        self.toolButton_41.setShortcut(_translate("MainWindow", "L"))
        self.toolButton_42.setText(_translate("MainWindow", "cot"))
        self.toolButton_43.setText(_translate("MainWindow", "sin"))
        self.toolButton_44.setText(_translate("MainWindow", "cos"))
        self.toolButton_45.setText(_translate("MainWindow", "DEG"))
        self.toolButton_38.setText(_translate("MainWindow", "|x|"))
        self.toolButton_39.setText(_translate("MainWindow", "1/x"))
        self.toolButton_46.setText(_translate("MainWindow", "sec"))
        self.toolButton_47.setText(_translate("MainWindow", "csc"))
        self.toolButton_48.setText(_translate("MainWindow", "tan"))
        self.toolButton_49.setText(_translate("MainWindow", "("))
        self.toolButton_49.setShortcut(_translate("MainWindow", "("))
        self.toolButton_50.setText(_translate("MainWindow", ")"))
        self.toolButton_50.setShortcut(_translate("MainWindow", ")"))
        self.toolButton_51.setText(_translate("MainWindow", "sqrt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "engineering"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
```
