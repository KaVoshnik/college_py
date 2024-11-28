from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 50, 300, 30))
        self.input_amount.setObjectName("input_amount")

        self.comboBox_from = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_from.setGeometry(QtCore.QRect(50, 100, 140, 30))
        self.comboBox_from.setObjectName("comboBox_from")

        self.comboBox_to = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_to.setGeometry(QtCore.QRect(210, 100, 140, 30))
        self.comboBox_to.setObjectName("comboBox_to")

        self.btn_convert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convert.setGeometry(QtCore.QRect(50, 150, 300, 30))
        self.btn_convert.setObjectName("btn_convert")

        self.btn_swap = QtWidgets.QPushButton(self.centralwidget)
        self.btn_swap.setGeometry(QtCore.QRect(50, 200, 300, 30))
        self.btn_swap.setObjectName("btn_swap")

        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(50, 250, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Converter"))
        self.input_amount.setPlaceholderText(_translate("MainWindow", "Enter amount"))
        self.btn_convert.setText(_translate("MainWindow", "Convert"))
        self.btn_swap.setText(_translate("MainWindow", "Swap"))
        self.label_result.setText(_translate("MainWindow", "Result:"))
