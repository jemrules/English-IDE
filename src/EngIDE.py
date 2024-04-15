import numpy as np
import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from html import escape
from syntax_handle import colorize
rust=False
try:
    import english_rs as Ers
    rust=True
except ImportError:
    rust=False
    print("Rust end not compiled!")

def rgb_txt(text,rgb):
    return "<span style='color:rgb({R},{G},{B})'>{txt}</span>".format(R=rgb[0],G=rgb[1],B=rgb[2],txt=escape(text))
def css_txt(text,css):
    return "<span style='{css}'>{txt}</span>".format(css=css,txt=escape(text))

class window_widget(QDockWidget):
    def __init__(self):
        super().__init__()
        # self.setObjectName("WindowWidget")
        self.setWindowTitle('Window Widget')
        self.setWidget(QWidget())
        self.layout=QVBoxLayout()
        self.widget().setLayout(self.layout)
        # self.layout.addWidget(QLabel('Window Widget'))
class text_box(QTextEdit):
    def __init__(self):
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
    def __init__(self,name="text_area"):
        super().__init__()
        self.layout=QVBoxLayout()
        # self.setObjectName("test")
        self.setLayout(self.layout)
        self.text_box=text_box()
        self.layout.addWidget(self.text_box)

class suggestion_area(QWidget):
    def __init__(self):
        super().__init__()
        # self.setObjectName("SuggestionArea")
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(QLabel('Suggestion Area'))

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GUI')
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(QWidget())
        self.layout=QVBoxLayout()
        self.centralWidget().setLayout(self.layout)
        self.text_areas=QTabWidget()
        self.text_areas.setObjectName("text_areas")
        self.layout.addWidget(self.text_areas)
        self.text_areas.addTab(text_area('tab_1'),'Tab 1')
        self.text_areas.addTab(text_area('tab_2'),'Tab 2')
app=QApplication(sys.argv)
f=open("style.css","r")
app.setStyleSheet(f.read())
print(f.read())
f.close()
a=GUI()
# Align to top
a.show()
sys.exit(app.exec_())