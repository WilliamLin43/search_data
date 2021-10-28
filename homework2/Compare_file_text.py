# -*- coding: utf-8 -*-
import sys
import os
import time
import xml.etree.ElementTree as ET
from PyQt5.QtGui import (QImage,QPixmap,QIcon,QFont)
from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton, 
                             QHBoxLayout, QVBoxLayout, qApp, QApplication, 
                             QLabel, QAction, QFileDialog, QComboBox,QStyle,QLineEdit,QTextEdit)

class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self) .__init__(parent)
        
        self.setGeometry(200, 150, 1200, 700)   #windows position and size
        layout = QVBoxLayout ()
        
        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('File 1: ')
        self.nameLabel1.setGeometry(10,50,1200,50)  

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('File 2: ')
        self.nameLabel2.setGeometry(10,100,1200,50)

        self.openfile1 = QPushButton ('Select Files', self)
        self.openfile1.setGeometry(50, 150, 200, 50)   #按鈕起始位置，按鈕大小
        self.openfile1.clicked.connect (self.open)     #連接

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Compare result: ')
        self.nameLabel3.setGeometry(300,150,600,50) 


        self.textEdit1 = QTextEdit(self)
        self.textEdit1.setGeometry(10,220,550,400)        

        self.textEdit2 = QTextEdit(self)
        self.textEdit2.setGeometry(600,220,550,400)     


        exitAction = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton),'&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')        
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        
        Open_File=QAction(self.style().standardIcon(QStyle.SP_DialogOpenButton),'&Open Image File', self)
        Open_File.setStatusTip('Open Image File')
        Open_File.triggered.connect(self.open)
        
        menubar = self.menuBar()
        fileMenu9 = menubar.addMenu('&Exit')
        fileMenu9.addAction(exitAction) 
        
        self.statusBar()
        self.setLayout (layout)
        self.setWindowTitle ('Compare two file')
        self.setWindowIcon(QIcon('icon.png')) #program icon


    def open(self):    #Open file
        File, _  = QFileDialog.getOpenFileName(self, 'Open File', './', '*.xml')
        if File != '':
            Text = 'File 1: '+str(File)
            self.nameLabel1.setText(Text)            
            self.file1 = File
            print(self.file1)

        File, _  = QFileDialog.getOpenFileName(self, 'Open File', './', '*.xml')
        if File != '':
            Text = 'File 2: '+ str(File)
            print(Text)
            self.nameLabel2.setText(Text)
            self.file2 = File
            print(self.file2)
 
        filename = str(self.file1)
        tree = ET.parse(filename)
        root = tree.getroot()
        self.TEXTAbstract1=''
        for AbstractText in root.iter('AbstractText'):
            self.TEXTAbstract1 = str(self.TEXTAbstract1) + str(AbstractText.text)
        self.textEdit1.append(str(self.TEXTAbstract1))

        filename = str(self.file2)
        tree = ET.parse(filename)
        root = tree.getroot()
        self.TEXTAbstract2=''
        for AbstractText in root.iter('AbstractText'):
            self.TEXTAbstract2 = str(self.TEXTAbstract2) + str(AbstractText.text)
        self.textEdit2.append(str(self.TEXTAbstract2))
        
        if len(self.TEXTAbstract1) <= len(self.TEXTAbstract2):
            for i in range(len(self.TEXTAbstract1)):
                if self.TEXTAbstract1[i] != self.TEXTAbstract2[i]:
                    self.TEXTCompare = False
                else:
                    self.TEXTCompare = True
            print(self.TEXTCompare)
        else:
            for i in range(len(self.TEXTAbstract2)):
                if self.TEXTAbstract1[i] != self.TEXTAbstract2[i]:
                    self.TEXTCompare = False
                else:
                    self.TEXTCompare = True
            print(self.TEXTCompare)
        
        if self.TEXTCompare == True:
            Text = 'Compare result: True'
            self.nameLabel3.setText(Text)
            self.nameLabel3.setStyleSheet("background-color: green")
        else:
            Text = 'Compare result: False'
            self.nameLabel3.setText(Text)
            self.nameLabel3.setStyleSheet("background-color: red")
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
        