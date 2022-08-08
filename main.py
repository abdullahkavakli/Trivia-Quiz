from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from css import get_css
import time
import pyodbc 
global data
import random
    
def choose_random():
    global data
    cursor = connection.cursor()
    cursor.execute('SELECT top 5 * FROM tbl_question order by newid()')
    data=[]

    for row in cursor:
        data.append(row)        

def choose_scores():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tbl_score order by score')
    scores_data=[]

    for row in cursor:
        scores_data.append(row)


class Ui_Form(object):


    def __init__(self):
        super().__init__()
        self.name=""
        self.score=0
        self.order=0
        self.QUESTION_NUMBER=5#total question to ask is tis number-
        self.answer_order=[2,3,4,5]
        random.shuffle(self.answer_order)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(622, 473)
        css_string=get_css()
        Form.setStyleSheet(css_string)
        self.stacked_widget = QtWidgets.QStackedWidget(Form)
        self.stacked_widget.setGeometry(QtCore.QRect(20, 30, 571, 411))
        self.stacked_widget.setAutoFillBackground(False)
        self.stacked_widget.setObjectName("stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.start = QtWidgets.QPushButton(self.page)
        self.start.setGeometry(QtCore.QRect(370, 240, 110, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.main_label = QtWidgets.QLabel(self.page)
        self.main_label.setGeometry(QtCore.QRect(50, 40, 441, 131))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.main_label.setFont(font)
        self.main_label.setWordWrap(True)
        self.main_label.setObjectName("main_label")
        self.scores = QtWidgets.QPushButton(self.page)
        self.scores.setGeometry(QtCore.QRect(370, 300, 110, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.scores.setFont(font)
        self.scores.setObjectName("scores")
        self.stacked_widget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.lineEdit = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit.setGeometry(QtCore.QRect(210, 120, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")

        self.cont = QtWidgets.QPushButton(self.page_4)
        self.cont.setGeometry(QtCore.QRect(370, 240, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.cont.setFont(font)
        self.cont.setObjectName("cont")

        self.name_label = QtWidgets.QLabel(self.page_4)
        self.name_label.setGeometry(QtCore.QRect(10, 130, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.stacked_widget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.soru = QtWidgets.QLabel(self.page_2)
        self.soru.setGeometry(QtCore.QRect(20, 20, 521, 111))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.soru.setFont(font)
        self.soru.setScaledContents(False)
        self.soru.setWordWrap(True)
        self.soru.setObjectName("soru")

        self.qa = QtWidgets.QPushButton(self.page_2)
        self.qa.setGeometry(QtCore.QRect(30, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.qa.setFont(font)
        self.qa.setObjectName("qa")

        self.qb = QtWidgets.QPushButton(self.page_2)
        self.qb.setGeometry(QtCore.QRect(30, 200, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.qb.setFont(font)
        self.qb.setObjectName("qb")        

        self.qc = QtWidgets.QPushButton(self.page_2)
        self.qc.setGeometry(QtCore.QRect(30, 270, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.qc.setFont(font)
        self.qc.setObjectName("qc")

        self.qd = QtWidgets.QPushButton(self.page_2)
        self.qd.setGeometry(QtCore.QRect(30, 340, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.qd.setFont(font)
        self.qd.setObjectName("qd")

        self.c1 = QtWidgets.QLabel(self.page_2)
        self.c1.setGeometry(QtCore.QRect(100, 130, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.c1.setFont(font)
        self.c1.setObjectName("c1")

        self.c2 = QtWidgets.QLabel(self.page_2)
        self.c2.setGeometry(QtCore.QRect(100, 200, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.c2.setFont(font)
        self.c2.setObjectName("c2")

        self.c3 = QtWidgets.QLabel(self.page_2)
        self.c3.setGeometry(QtCore.QRect(100, 270, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.c3.setFont(font)
        self.c3.setObjectName("c3")

        self.c4 = QtWidgets.QLabel(self.page_2)
        self.c4.setGeometry(QtCore.QRect(100, 340, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.c4.setFont(font)
        self.c4.setObjectName("c4")

        self.stacked_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.sore_label = QtWidgets.QLabel(self.page_3)
        self.sore_label.setGeometry(QtCore.QRect(70, 50, 341, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.sore_label.setFont(font)
        self.sore_label.setObjectName("sore_label")
        self.back_from_your_score = QtWidgets.QPushButton(self.page_3)
        self.back_from_your_score.setGeometry(QtCore.QRect(420, 260, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.back_from_your_score.setFont(font)
        self.back_from_your_score.setObjectName("back_from_your_score")
        self.stacked_widget.addWidget(self.page_3)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")

        self.tableWidget = QtWidgets.QTableWidget(self.page_5)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 301, 381))
        self.tableWidget.setAutoScrollMargin(19)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.setHorizontalHeaderLabels(('Name','Score'))
        

        self.back_from_scores = QtWidgets.QPushButton(self.page_5)
        self.back_from_scores.setGeometry(QtCore.QRect(470, 300, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.back_from_scores.setFont(font)
        self.back_from_scores.setObjectName("back_from_scores")
        self.stacked_widget.addWidget(self.page_5)
        # self.update_table(Form)

        self.retranslateUi(Form)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.start.clicked.connect(lambda x : self.pass_to_your_name(Form))
        self.cont.clicked.connect(lambda x : self.check_name_line_edit(Form))
        self.qa.clicked.connect(lambda x : self.change_question_or_pass_to_your_score(Form,1))
        self.qb.clicked.connect(lambda x : self.change_question_or_pass_to_your_score(Form,2))
        self.qc.clicked.connect(lambda x : self.change_question_or_pass_to_your_score(Form,3))
        self.qd.clicked.connect(lambda x : self.change_question_or_pass_to_your_score(Form,4))
        self.back_from_your_score.clicked.connect(lambda x : self.pass_to_main(Form))
        self.back_from_scores.clicked.connect(lambda x : self.pass_to_main(Form))
        self.scores.clicked.connect(lambda x : self.pass_to_scores(Form))



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Trivia Quiz"))
        self.start.setText(_translate("Form", "Start"))
        self.cont.setText(_translate("Form", "Continue"))
        self.main_label.setText(_translate("Form", "Trivia Quiz"))
        self.scores.setText(_translate("Form", "Scores"))
        self.lineEdit.setText(_translate("Form", ""))
        self.name_label.setText(_translate("Form", "Your Name:"))
        self.soru.setText(_translate("Form", "3.sayfa"))
        self.qa.setText(_translate("Form", "A"))
        self.qb.setText(_translate("Form", "B"))
        self.qc.setText(_translate("Form", "C"))
        self.qd.setText(_translate("Form", "D"))        
        self.c1.setText(_translate("Form", "cvp1"))
        self.c2.setText(_translate("Form", "cvp2"))
        self.c3.setText(_translate("Form", "cvp3"))
        self.c4.setText(_translate("Form", "cvp4"))
        self.sore_label.setText(_translate("Form", "Your Score: "))
        self.back_from_your_score.setText(_translate("Form", "Back"))
        self.back_from_scores.setText(_translate("Form", "Back"))
        



    def retranslateQA(self, Form):
        global data
        _translate = QtCore.QCoreApplication.translate       

        self.soru.setText(_translate("MainWindow",   str(data[self.order][1])))
        self.c1.setText(_translate("MainWindow", str(data[self.order][self.answer_order[0]])))
        self.c2.setText(_translate("MainWindow", str(data[self.order][self.answer_order[1]])))        
        self.c3.setText(_translate("MainWindow", str(data[self.order][self.answer_order[2]])))
        self.c4.setText(_translate("MainWindow", str(data[self.order][self.answer_order[3]])))
        



    def retranslateYourScore(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.sore_label.setText(_translate("Form", f"Your Score:{self.score}"))



    def retranslateLineEdit(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setText(_translate("Form", ""))
        

    def set_to_default(self):
        self.score=0
        self.name=""
        self.order=0

    def pass_to_main(self,Form):
        self.stacked_widget.setCurrentIndex(0)

    def pass_to_qa(self,Form):
        self.stacked_widget.setCurrentIndex(2)
        self.retranslateQA(Form)


    def pass_to_your_score(self,Form):
        self.stacked_widget.setCurrentIndex(3)
        self.retranslateYourScore(Form)
        self.save_them_to_database(Form)
        self.set_to_default()
        choose_random()
        

    def pass_to_your_name(self, Form):
        self.stacked_widget.setCurrentIndex(1)
    
    def save_them_to_database(self, Form):
        """saves score and name to db"""
        
        cursor = connection.cursor()
        scores_belog_to_that_name=[]

        cursor.execute('select count(score) from tbl_score  where name=? group by name',self.name)

        for row in cursor:
            scores_belog_to_that_name.append(row)

        if len(scores_belog_to_that_name)==1:
            cursor.execute('update tbl_score set score=? where name=?',self.score,self.name)
            cursor.commit()
        else:
            cursor.execute('insert into tbl_score values(?,?)',self.name,self.score)
            cursor.commit()

    def pass_to_scores(self,Form):
        try:
            choose_scores()
            self.stacked_widget.setCurrentIndex(4)
            self.update_table(Form)
        except:
            print("Please connect Database")


    def update_table(self,Form):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM tbl_score order by score desc')

        table_items=[]

        for row in cursor:
            table_items.append(row)

        self.tableWidget.setRowCount(len( table_items))

        for i in range(len( table_items)):
            self.tableWidget.setItem(i,0,QTableWidgetItem(table_items[i][0]))
            self.tableWidget.setItem(i,1,QTableWidgetItem(str(table_items[i][1])))
          


    def change_question_or_pass_to_your_score(self,Form,choice):
        self.change_score(choice)
        if (self.order<self.QUESTION_NUMBER-1):    
            self.order+=1          
            random.shuffle(self.answer_order)
            self.retranslateQA(Form)
        else:
            self.pass_to_your_score(Form)


    def check_name_line_edit(self,Form):
        if self.lineEdit.text()!="":
            self.get_text_and_pass_to_qa(Form)
    

    def get_text_and_pass_to_qa(self,Form):
            self.name=self.lineEdit.text()
            self.retranslateLineEdit(Form)            
            self.pass_to_qa(Form)
            self.retranslateQA(Form)

    def change_score(self,choice):        
        true_answer_index=self.which_index_is_true()
        if true_answer_index==choice:
            self.score+=20 
        

    def which_index_is_true(self):
        for i in range(4):
            if str(data[self.order][5])== str(data[self.order][self.answer_order[i]]):
                return i+1


if __name__ == "__main__":
    
    import sys   
           
    try:
        connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=DESKTOP-1IRMV7Q;"
                            "Database=TriviaQuiz;"
                            "Trusted_Connection=yes;")
        
        choose_random()
    except:
        print("Please connect Database, for now data was set to default")


    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
    
    
