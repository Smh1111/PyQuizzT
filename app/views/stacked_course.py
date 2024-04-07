from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget, QStackedWidget, QMainWindow)

from PySide6 import QtCore, QtGui, QtWidgets
import requests
from views.course_list import Course_list
from views.lesson_quiz_list import Lesson_Quiz_list
from views.quiz_page import QuizPage
from views.quiz_correct_answer_list import Quiz_correct_answer_list
from views.quiz_wrong_answer_list import Quiz_wrong_answer_list
from views.quiz_answer_list import Quiz_answer_list
from views.update_lesson import EditLessonForm
from views.add_quiz_question import QuizQuestion
from views.module_list import Module_list
from views.show_test_case import Show_Test_Case

class Stacked_Course(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setupUi(self)
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 551)
        
        font1 = QFont()
        font1.setPointSize(20)
        
        self.stacked = QStackedWidget(Form)
        self.stacked.setObjectName(u"stackedWidget")
        self.stacked.setGeometry(QRect(0, 0, 811, 541))
        
        ###################################### 0
        self.course_list = Course_list(self.username)
        self.stacked.addWidget(self.course_list)
        
        for button in self.course_list.buttons:
            button.clicked.connect(self.go_to_module)
        
        self.course_list.enroll_btn.clicked.connect(self.enroll_course)
        
        ##########################################1
        
        self.lq_list = Lesson_Quiz_list()
        self.stacked.addWidget(self.lq_list)
        
        self.lq_list.return_2.clicked.connect(self.go_to_module)
        
        for button in self.lq_list.quiz_buttons:
            button.clicked.connect(self.go_to_quiz)
        
        ########################################2
        self.quiz = QuizPage()
        self.stacked.addWidget(self.quiz)
        
        self.text_case = []
        self.answer = []
        
        self.quiz.nav_bar.back_button.clicked.connect(self.go_to_lesson_quiz)
        
        self.quiz.nav_bar.send_button.clicked.connect(self.go_to_answer)
        
        #################################### 3
        self.show_ans = Quiz_answer_list()
        self.stacked.addWidget(self.show_ans)
        
        self.show_ans.next.clicked.connect(self.go_to_lesson_quiz)
        self.show_ans.go_back.clicked.connect(self.go_to_quiz)
        
        for button in self.show_ans.buttons:
            button.clicked.connect(self.go_to_show_test_case)
        
        #################################### 4
        self.module_list = Module_list()
        self.stacked.addWidget(self.module_list)
        
        for button in self.module_list.buttons:
            button.clicked.connect(self.go_to_lesson_quiz)
        
        self.module_list.return_2.clicked.connect(self.go_to_course)
        ###################################### 5
        self.show_test_case = Show_Test_Case()
        self.stacked.addWidget(self.show_test_case)
        
        self.show_test_case.go_back.clicked.connect(self.go_to_answer)
        ######################################
        QMetaObject.connectSlotsByName(Form)
    
    def go_to_course(self):
        self.stacked.setCurrentIndex(0)
    
    def go_to_lesson_quiz(self):
        self.stacked.setCurrentIndex(1)
        
    def go_to_quiz(self):
        self.stacked.setCurrentIndex(2)
    
    def go_to_answer(self):
        self.stacked.setCurrentIndex(3)
        
    def go_to_module(self):
        self.stacked.setCurrentIndex(4)
        
    def go_to_show_test_case(self):
        self.stacked.setCurrentIndex(5)
    
    def go_to_lesson(self):
        pass
    
    def enroll_course(self):
        if self.course_list.lineEdit.text() != '' :
            response = requests.post("http://127.0.0.1:8000/api/enroll", params={"courseCode": self.course_list.lineEdit.text(), "username": self.username})

            # Check if the request was successful
            if response.status_code == 200:
                # Print the response message
                if response.json()["success"]:
                    self.course_list.gridLayout.removeItem(self.course_list.verticalSpacer)
                    button = QPushButton(self.course_list.scrollAreaWidgetContents)
                    self.course_list.gridLayout.addWidget(button, self.course_list.index, 0, 1, 1)
                    course_name = self.getCourseName(self.course_list.lineEdit.text()).strip('"')
                    button.setText(course_name)
                    self.course_list.buttons.append(button)
                    button.clicked.connect(self.go_to_module)
                    
                    label = QLabel(self.course_list.scrollAreaWidgetContents)
                    label.setObjectName(f"label_{self.course_list.index+1}")
                    label.setText(QCoreApplication.translate("Form", u"Complete?", None))
                    
                    self.course_list.lineEdit.clear()

                    self.course_list.gridLayout.addWidget(label, self.course_list.index, 1, 1, 1)
                    
                    # print(QPushButton(self.course_list.scrollAreaWidgetContents))
                    delete = QPushButton(self.course_list.scrollAreaWidgetContents)
                    delete.setObjectName(f"delete_{self.course_list.index + 1}")
                    delete.setText('Leave')
                    self.course_list.delete_buttons[delete]  = self.course_list.index
                    delete.clicked.connect(self.course_list.delete_course)
                    self.course_list.gridLayout.addWidget(delete, self.course_list.index, 2, 1, 1)
                    
                    self.course_list.index += 1

                    self.course_list.gridLayout.addItem(self.course_list.verticalSpacer, self.course_list.index, 0, 1, 1)
            else:
                # Print an error message if the request failed
                print("Error:", response.text)

            self.course_list.lineEdit.clear()

    def getCourseName(self, courseCode):
        response = requests.get(f"http://127.0.0.1:8000/course/getCourseName/{courseCode}")
        if response.status_code == 200:
            return response.text
        return None