# Form implementation generated from reading ui file 'register_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class RegisterWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(950, 600)
        self.login_button = QtWidgets.QPushButton(parent=RegisterWindow)
        self.login_button.setGeometry(QtCore.QRect(350, 420, 271, 24))
        self.login_button.setObjectName("login_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=RegisterWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 120, 271, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.frame = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.username_label = QtWidgets.QLabel(parent=self.frame)
        self.username_label.setGeometry(QtCore.QRect(0, 0, 111, 16))
        self.username_label.setObjectName("username_label")
        self.username_input = QtWidgets.QLineEdit(parent=self.frame)
        self.username_input.setGeometry(QtCore.QRect(0, 20, 271, 21))
        self.username_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.password_label = QtWidgets.QLabel(parent=self.frame_2)
        self.password_label.setGeometry(QtCore.QRect(0, 0, 49, 16))
        self.password_label.setObjectName("password_label")
        self.password_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.password_input.setGeometry(QtCore.QRect(0, 20, 271, 21))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.confirm_label = QtWidgets.QLabel(parent=self.frame_3)
        self.confirm_label.setGeometry(QtCore.QRect(0, 0, 131, 16))
        self.confirm_label.setObjectName("confirm_label")
        self.confirm_input = QtWidgets.QLineEdit(parent=self.frame_3)
        self.confirm_input.setGeometry(QtCore.QRect(0, 20, 271, 21))
        self.confirm_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_input.setObjectName("confirm_input")
        self.verticalLayout.addWidget(self.frame_3)
        self.register_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.register_button.setObjectName("register_button")
        self.verticalLayout.addWidget(self.register_button)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Register"))
        self.login_button.setText(_translate("RegisterWindow", "Already have an account? Login"))
        self.title.setText(_translate("RegisterWindow", "Create an account"))
        self.username_label.setText(_translate("RegisterWindow", "Username"))
        self.password_label.setText(_translate("RegisterWindow", "Password"))
        self.confirm_label.setText(_translate("RegisterWindow", "Confirm Password"))
        self.register_button.setText(_translate("RegisterWindow", "Register"))
