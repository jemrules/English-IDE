import numpy as np
import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from html import escape
from syntax_handle import colorize
from english_rs.english_rs import autocorrect
# rust=False
# try:
#     import english_rs as Ers
#     rust=True
# except ImportError:
#     rust=False
#     print("Rust end not compiled!")

def rgb_txt(text,rgb):
    return "<span style='color:rgb({R},{G},{B})'>{txt}</span>".format(R=rgb[0],G=rgb[1],B=rgb[2],txt=escape(text))
def css_txt(text,css):
    return "<span style='{css}'>{txt}</span>".format(css=css,txt=escape(text))

class window_widget(QDockWidget):
    def __init__(self,p=None):
        super().__init__()
        # self.setObjectName("WindowWidget")
        self.setWindowTitle('Window Widget')
        self.setWidget(QWidget())
        self.layout=QVBoxLayout()
        self.widget().setLayout(self.layout)
        # self.layout.addWidget(QLabel('Window Widget'))
class text_box(QTextEdit):
    def __init__(self,p=None):
        super().__init__()
        self.setAcceptRichText(False)
        self.setObjectName("text_box")
        self.textChanged.connect(self.update_text)
        self.cursorPositionChanged.connect(self.cursor_pos_update)
        self.disableChange=0
        self.currentPos=1
        self.last=""
        self.setLineWrapMode(QTextEdit.NoWrap)
    def update_text(self):
        if self.disableChange>0:
            self.disableChange-=1
            return
        self.disableChange=3
        self.currentPos=self.textCursor().position()
        colorized=colorize(self.toPlainText(),self.currentPos)
        if self.last==colorized[0]:
            return
        self.setHtml(colorized[0])
        self.last=colorized[0]
        cursor=self.textCursor()
        cursor.setPosition(self.currentPos+colorized[1])
        self.setTextCursor(cursor)
    def cursor_pos_update(self):
        self.update_text()

class text_area(QWidget):
    def __init__(self,name="text_area",p=None):
        super().__init__()
        self.layout=QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        # self.setObjectName("test")
        self.setLayout(self.layout)
        self.text_box=text_box()
        self.text_box.cursorPositionChanged.connect(self.move_c)
        self.cursorBox=suggestion_area(p=p)
        self.layout.addWidget(self.text_box)
        self.p=p
    def move_c(self):
        # print(self.text_box.cursorRect())
        WPos=(0,0)
        WindApp=None
        inst=QApplication.instance()
        for x in inst.allWidgets():
            if isinstance(x,QMainWindow):
                WindApp=x
                WPos=(x.pos().x(),x.pos().y())
        self.cursorBox.move(self.text_box.cursorRect().x()+WPos[0]+20,self.text_box.cursorRect().y()+WPos[1]+self.sizeHint().height()//2-10)
        self.cursorBox.show()
        self.cursorBox.UpdateText(self.text_box.toPlainText())
        WindApp.activateWindow()

    #     self.text_box.cursorPositionChanged.connect(self.move_c)
    # def move_c(self):
    #     self.setFixedSize(200,500)
    #     self.move(50,500)

class suggestion_area(QDialog):
    def __init__(self,p=None):
        super().__init__()
        self.setObjectName("suggestion_area")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.NonModal)
        #self.setWindowFlags()
        self.layout=QVBoxLayout()
        self.Label=QLabel("Suggestions")
        self.layout.addWidget(self.Label)
        self.p=p
        self.txt=""
        self.setLayout(self.layout)
    def UpdateText(self,txt):
        self.txt=txt
        if len(txt.split())>0:
            suggestions=autocorrect(txt.split()[len(txt.split())-1])
            print(txt.split()[len(txt.split())-1])
            print(suggestions)
            #self.Label.setText(suggestions[0])
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GUI')
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(QWidget())
        self.setObjectName("GUI")
        self.layout=QVBoxLayout()
        self.centralWidget().setLayout(self.layout)
        self.text_areas=QTabWidget()
        self.text_areas.setObjectName("text_areas")
        self.layout.addWidget(self.text_areas)
        self.text_areas.addTab(text_area('tab_1',p=self),'Tab 1')
        self.text_areas.addTab(text_area('tab_2',p=self),'Tab 2')
    def closeEvent(self,a):
        inst=QApplication.instance()
        for x in inst.allWidgets():
            if isinstance(x,QDialog):
                x.reject()
app=QApplication(sys.argv)
f=open("style.css","r")
app.setStyleSheet(f.read())
print(f.read())
f.close()
a=GUI()
# Align to top
a.show()
sys.exit(app.exec_())