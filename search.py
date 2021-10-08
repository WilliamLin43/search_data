# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtGui import (QImage,QPixmap,QIcon,QFont)
from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton, 
                             QHBoxLayout, QVBoxLayout, qApp, QApplication, 
                             QLabel, QAction, QFileDialog, QComboBox,QStyle,QLineEdit,QTextEdit)

import xml_file_read
import json_file_read
import number_of_characters_words
import number_of_sentences


class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self) .__init__(parent)
        
        self.setGeometry(200, 150, 1200, 700)   #windows position and size
        layout = QVBoxLayout ()
        
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Keyword: ')
        self.nameLabel.setGeometry(10,50,100,50)        
        self.keywordline = QLineEdit(self)
        self.keywordline.setText('system')
        self.keywordline.setGeometry(110,50,300,50)        
        
        self.openfolder = QPushButton ('Search directory', self)
        self.openfolder.setStyleSheet("QPushButton{font-size:32px}")
        self.openfolder.setGeometry(10,110, 300, 100)   #position and size
        self.openfolder.clicked.connect (self.Start)     #call function
     
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(10,220,1000,400)        
        
        exitAction = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton),'&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')        
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        
        
        
        menubar = self.menuBar()
        fileMenu9 = menubar.addMenu('&Exit')
        fileMenu9.addAction(exitAction) 
        
        self.statusBar()
        self.setLayout (layout)
        self.setWindowTitle ('Search key word')
        self.setWindowIcon(QIcon('icon.png')) #program icon
        
      

    def checkfile(self):
        if os.path.isdir(self.Query_dir):
            files= os.listdir(self.Query_dir) #get all files
            self.textEdit.append("select and check file")
            print("select and check file")            
            for file in files:
                if not os.path.isdir(file): #Check if not folder, open it                    
                    self.textEdit.append("File name: "+str(file))
                    print("File name:"+str(file))
                    fileformat = file.split('.')
                    #self.textEdit.append("File format:"+str(fileformat[1]))
                    #print("File format:"+str(fileformat[1]))
                    if fileformat[1] == 'xml':
                        xml_file_read.get_xml_file_info(self.Query_dir,file,self.keyword)
                    if fileformat[1] == 'json':
                        json_file_read.get_json_file_info(self.Query_dir,file,self.keyword)
                        
                        
                    self.Characters,self.words,self.lines = number_of_characters_words.get_words_and_Characters(file,self.keyword)
                    self.textEdit.append("Characters number: "+str(self.Characters))
                    self.textEdit.append("Words number: "+str(self.words))
                    self.textEdit.append("Lines number: "+str(self.lines))
                    self.Sentences,self.Position,self.keyword_sentences = number_of_sentences.get_sentences(file,self.keyword)
                    self.textEdit.append("Sentences number: "+str(self.Sentences))
                    self.textEdit.append("Keyword sentences: "+str(self.keyword_sentences.count('\n'))+" matches")
                    self.textEdit.append(str(self.keyword_sentences))                        
                        

                    

    def Start(self):
        print("Search ...")
        self.Query_dir = QFileDialog.getExistingDirectory(self, "Open Directory","./",QFileDialog.ShowDirsOnly|QFileDialog.DontResolveSymlinks);
        self.keyword = str(self.keywordline.text())
        outputdata = 'Key word: ' + self.keywordline.text()        
        self.textEdit.append(str(outputdata))                                                
        print('Key word: ' + self.keywordline.text())     

        outputdata = 'Search directory:' + str(self.Query_dir) 
        self.textEdit.append(str(outputdata))
        print('Search directory:' + str(self.Query_dir))
        self.checkfile()
        

                    
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())