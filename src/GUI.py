import numpy as np
import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window_widget(QDockWidget):
	def __init__(self):
		super().__init__()
		# self.setObjectName("WindowWidget")
		self.setWindowTitle('Window Widget')
		self.setWidget(QWidget())
		self.layout=QVBoxLayout()
		self.widget().setLayout(self.layout)
		#self.layout.addWidget(QLabel('Window Widget'))

class text_box(QTextEdit):
	def __init__(self):
		super().__init__()
		self.setObjectName("text_box")
		self.setAcceptRichText(False)
		self.setLineWrapMode(QTextEdit.NoWrap)
	def cursorPositionChanged(self):
		print('Cursor Position:',self.textCursor().position())

class text_area(QWidget):
	def __init__(self,name="text_area"):
		super().__init__()
		self.layout=QVBoxLayout()
		self.setLayout(self.layout)
		self.text_box=QTextEdit()
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