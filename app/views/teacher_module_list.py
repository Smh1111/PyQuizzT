# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'module_list.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget, QStackedWidget, QMainWindow, QLineEdit)

from PySide6 import QtCore, QtGui, QtWidgets

class Teacher_Module_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.module = ['mol1', 'mol2', 'mol3']
        self.cID = "abcdefgh"
        self.module_buttons = []
        self.index = 0
        
        self.edit_buttons = {}
        
        self.delete_buttons = {}   
        
        self.setupUi(self)
        
        
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 551)
        
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 781, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 779, 489))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.courseID = QLabel(Form)
        self.courseID.setText(f"courseID : {self.cID}")
        self.courseID.setGeometry(QRect(200, 520, 300, 24))
        
        # for loop making pushButton and Label
        for _ in range(len(self.module)):
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setObjectName(f"module_{self.index + 1}")
            button.setText(self.module[self.index])
            self.gridLayout.addWidget(button, self.index, 0, 1, 1)
            self.module_buttons.append(button)
            
            edit = QPushButton(self.scrollAreaWidgetContents)
            edit.setObjectName(f"edit_{self.index + 1}")
            edit.setText('Edit')
            self.gridLayout.addWidget(edit, self.index, 1, 1, 1)
            self.edit_buttons[edit] = self.index
            
            delete = QPushButton(self.scrollAreaWidgetContents)
            delete.setObjectName(f"delete_{self.index + 1}")
            delete.setText('Delete')
            self.delete_buttons[delete]  = self.index
            
            # delete.clicked.connect(lambda i = i: self.delete_module(i))
            delete.clicked.connect(self.delete_module)
            
            self.gridLayout.addWidget(delete, self.index, 2, 1, 1)
            self.index += 1
        # makes verticleSpacer
        self.verticalSpacer = QSpacerItem(20, 378, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, self.index, 0, 1, 1)
        
        ############################################

        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.enroll_btn = QPushButton(Form)
        self.enroll_btn.setObjectName(u"enroll_btn")
        self.enroll_btn.setGeometry(QRect(600, 510, 181, 24))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(375, 510, 200, 31))
        
        # self.enroll_btn.clicked.connect(self.enroll_module)
        self.enroll_btn.setText('Add Module')
        
        self.return_2 = QPushButton(Form)
        self.return_2.setObjectName(u"return_2")
        self.return_2.setGeometry(QRect(30, 510, 131, 24))
        self.return_2.setText('Return to ...')

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def delete_module(self):
        sender_button = self.sender()
                
        position = None
        if sender_button in self.delete_buttons:
            position = self.delete_buttons[sender_button]
        
        if position != None:
            for j in range(self.gridLayout.columnCount()):
                item = self.gridLayout.itemAtPosition(position, j)
                # item = self.gridLayout.itemAtPosition(row, j)
                if item:
                    widget = item.widget()
                    self.gridLayout.removeWidget(widget)
                    widget.deleteLater()
            del self.delete_buttons[sender_button]
            # print(self.delete_buttons)