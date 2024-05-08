import numpy as np
import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from html import escape
from syntax_handle import colorize
from english_rs.english_rs import autocorrect, compare_words
import threading
# rust=False
# try:
#     import english_rs as Ers
#     rust=True
# except ImportError:
#     rust=False
#     print("Rust end not compiled!")

# https://www.sketchengine.eu/english-word-list/

print("\n".join([str(y) for y in compare_words("hello","hello")]))

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
        self.disableChange=2
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
        self.setObjectName("test LABEL")
        self.setLayout(self.layout)
        self.text_box=text_box()
        self.text_box.cursorPositionChanged.connect(self.move_c)
        self.cursorBox=suggestion_area(p=p)
        self.layout.addWidget(self.text_box)
        self.p=p
    def mouseMoved(self,event):
        print(self.text_box.textCursor().document())
        self.cursorBox.setVisible(False)
    def move_c(self):
        # print(self.text_box.cursorRect())
        WPos=(0,0)
        WindApp=None
        inst=QApplication.instance()
        for x in inst.allWidgets():
            if isinstance(x,QMainWindow):
                WindApp=x
                WPos=(x.pos().x(),x.pos().y())
            if isinstance(x, text_area) and x!=self:
                x.cursorBox.setVisible(False)
        self.cursorBox.setGeometry(self.text_box.cursorRect().x()+WPos[0]+20,self.text_box.cursorRect().y()+WPos[1]+self.sizeHint().height()//2-10,115,56)
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
        self.ACThread = threading.Thread(target=self.ACTh, args=(self.txt,))
        self.ACThread.start()
        # inst=QApplication.instance()
        # for x in inst.allWidgets():
        #     if isinstance(x,QMainWindow ):
        #         x.mouseMoveEvent.connect(self.mouseClicked)
        self.suggestions=[]
        self.lastWord=""
        self.setLayout(self.layout)
    def ACTh(self,x):
        #print("in",x)
        self.suggestions=autocorrect(x)
    def UpdateText(self,txt):
        #print("--",self.size().width(),self.size().height())
        #print(txt)
        self.txt=txt.lower()
        if len(txt.split())>0:
            if not self.ACThread.is_alive() and self.lastWord!=txt.split()[len(txt.split())-1]:
                self.ACThread.join()
                self.ACThread = threading.Thread(target=self.ACTh, args=(self.txt.split()[len(txt.split())-1],))
                self.ACThread.start()
                self.lastWord=txt.split()[len(self.txt.split())-1]
            #print(self.suggestions[:20],self.lastWord==self.txt.split()[len(txt.split())-1])
            #print(txt.split()[len(txt.split())-1])
            #print(suggestions)
            minimum=0
            maximum=0
            for x in self.suggestions[:20]:
                if x[1]>maximum:
                    maximum=x[1]
                if x[1]<minimum:
                    minimum=x[1]
            maximum-=minimum
            self.Label.setText("<br/>".join([rgb_txt(("> " if x[1]/maximum<=0.5 else "")+str(x[0]),(255*x[1]/maximum*0.8,255,255*x[1]/maximum*0.8)) for x in self.suggestions[:20] if x[1]/maximum<=0.75]))
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
        self.text_areas.addTab(window_widget(text_area('tab_1',p=self)),'Tab 1')
        self.text_areas.addTab(window_widget(text_area('tab_2',p=self)),'Tab 2')
        self.setMouseTracking(True)
    def closeEvent(self,a):
        inst=QApplication.instance()
        for x in inst.allWidgets():
            if isinstance(x,QDialog):
                x.reject()
    # def mouseMoveEvent(self,event):
    #     inst=QApplication.instance()
    #     for x in inst.allWidgets():
    #         if isinstance(x,QWidget):
    #             try:
    #                 x.mouseMoved(event)
    #             except Exception as err:
    #                 pass
app=QApplication(sys.argv)
f=open("style.css","r")
app.setStyleSheet(f.read())
print(f.read())
f.close()
a=GUI()
# Align to top
a.show()
sys.exit(app.exec_())