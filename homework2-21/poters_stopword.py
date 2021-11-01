# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas as pd
import time
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
import sys
from PyQt5.QtGui import (QImage,QPixmap,QIcon,QFont)
from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton, 
                             QHBoxLayout, QVBoxLayout, qApp, QApplication, 
                             QLabel, QAction, QFileDialog, QComboBox,QStyle,QLineEdit,QTextEdit)

import show_plot
import check_edit_distance_nltk

class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self) .__init__(parent)
        
        self.setGeometry(200, 150, 1200, 800)   #windows position and size
        layout = QVBoxLayout ()
        
        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('Keyword: ')
        self.nameLabel1.setGeometry(10,50,100,50)
        
        self.keywordline = QLineEdit(self)
        self.keywordline.setText('COVID-19')
        self.keywordline.setGeometry(10,100,150,50)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Documents: ')
        self.nameLabel2.setGeometry(180,50,120,50)

        self.documentline = QLineEdit(self)
        self.documentline.setText('500')
        self.documentline.setGeometry(180,100,100,50)        
        
        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Rank from: ')
        self.nameLabel3.setGeometry(300,50,120,50)

        self.rankline1 = QLineEdit(self)
        self.rankline1.setText('30')
        self.rankline1.setGeometry(300,100,100,50)        
        
        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Rank to: ')
        self.nameLabel4.setGeometry(450,50,100,50)

        self.rankline2 = QLineEdit(self)
        self.rankline2.setText('500')
        self.rankline2.setGeometry(450,100,100,50)           

        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Edit distance: ')
        self.nameLabel5.setGeometry(580,50,100,50)

        self.Edit_distance = QLineEdit(self)
        self.Edit_distance.setText('2')
        self.Edit_distance.setGeometry(580,100,100,50)  
        
        
        self.bcheckfile1 = QPushButton ("With Stopword & Porter’s" , self)
        self.bcheckfile1.setStyleSheet("QPushButton{font-size:18px}")
        self.bcheckfile1.setGeometry(10,160, 300, 100)   #position and size
        self.bcheckfile1.clicked.connect (self.Start1)     #call function

        self.bcheckfile2 = QPushButton ("With Stopword" , self)
        self.bcheckfile2.setStyleSheet("QPushButton{font-size:18px}")
        self.bcheckfile2.setGeometry(350,160, 300, 100)   #position and size
        self.bcheckfile2.clicked.connect (self.Start2)     #call function        

        self.bcheckfile3 = QPushButton ("Without Stopword & Porter’s" , self)
        self.bcheckfile3.setStyleSheet("QPushButton{font-size:18px}")
        self.bcheckfile3.setGeometry(700,160, 300, 100)   #position and size
        self.bcheckfile3.clicked.connect (self.Start3)     #call function      


        self.zipfplot1 = QPushButton ("Plot with Stopword & Porter’s" , self)
        self.zipfplot1.setStyleSheet("QPushButton{font-size:18px}")
        self.zipfplot1.setGeometry(10,270, 300, 100)   #position and size
        self.zipfplot1.clicked.connect (self.plot1)     #call function

        self.zipfplot2 = QPushButton ("Plot With Stopword" , self)
        self.zipfplot2.setStyleSheet("QPushButton{font-size:18px}")
        self.zipfplot2.setGeometry(350,270, 300, 100)   #position and size
        self.zipfplot2.clicked.connect (self.plot2)     #call function        

        self.zipfplot3 = QPushButton ("Plot Without Stopword & Porter’s" , self)
        self.zipfplot3.setStyleSheet("QPushButton{font-size:18px}")
        self.zipfplot3.setGeometry(700,270, 300, 100)   #position and size
        self.zipfplot3.clicked.connect (self.plot3)     #call function      


        self.find_keywords1 = QPushButton ("Find keywords" , self)
        self.find_keywords1.setStyleSheet("QPushButton{font-size:18px}")
        self.find_keywords1.setGeometry(10,390, 300, 100)   #position and size
        self.find_keywords1.clicked.connect (self.find_keywords)     #call function   
 

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(310,390,700,400)          


        exitAction = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton),'&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')        
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        

        
        menubar = self.menuBar()
        fileMenu9 = menubar.addMenu('&Exit')
        fileMenu9.addAction(exitAction) 
        
        self.statusBar()
        self.setLayout (layout)
        self.setWindowTitle ('Zipf Distribution')
        self.setWindowIcon(QIcon('icon.png')) #program icon        
        
        
        
        
        
        
        
    def checkfile1(self,file):
        
        print(file)
        
        f = open(file, 'r',encoding="utf-8")
        read_words = f.read()
        #print(read_words)
        
        #全部轉成小寫
        read_words = read_words.lower()
    
        #去除特殊符號
        read_words = read_words.replace('/',' ')
        read_words = read_words.replace('.',' ')
        read_words = read_words.replace('\n','') 
        read_words = read_words.replace('/e/',' ')
        read_words = read_words.replace('(d)',' ')
        read_words = read_words.replace('s)',' ')
        read_words = read_words.replace('?]',' ')
        read_words = read_words.replace('?]',' ')
        read_words = read_words.replace('=-B',' ')
        read_words = read_words.replace('-C',' ')
        
        
        result = word_tokenize(read_words)
        print("Total words:"+str(len(result)))
        
        words = 0
                
        ps = PorterStemmer()
        
        for i in range(len(result)):            
            if len(result[i]) > 0 and result[i] != '-' and result[i] != '–' and result[i] != ',':
                words += 1
                
                #確認是否為數字千分號
                pos=result[i][:-1].find(',')
                #print(pos)            
                if int(pos) > 0 and result[i][pos-1:pos].isdigit() != True :
                    words += 1
                #print(res[i])
            #去除特殊符號字元單一數字
            if result[i] in ['-','－','?','(',')','%','[',']','+','``','"','--','*','&','.','..','#','@','`','~','{','}','$','@','!']:
                result[i] = ''
            #去除特殊符號字元
            result[i] = result[i].replace('~','')
            result[i] = result[i].replace(',','')
            result[i] = result[i].replace('!','')
            result[i] = result[i].replace('@','')
            result[i] = result[i].replace('#','')
            result[i] = result[i].replace('$','')
            result[i] = result[i].replace('%','')
            result[i] = result[i].replace('^','')
            result[i] = result[i].replace('&','')
            result[i] = result[i].replace('*','')
            result[i] = result[i].replace('(','')
            result[i] = result[i].replace(')','')
            result[i] = result[i].replace('!','')
            result[i] = result[i].replace(':','')
            result[i] = result[i].replace('+','')
            result[i] = result[i].replace('=','')
            result[i] = result[i].replace('=-','')
            result[i] = result[i].replace(',','')
            result[i] = result[i].replace("'",'')
            result[i] = result[i].replace("'s",'')
            result[i] = result[i].replace('\n','')
            result[i] = result[i].replace(' ','')
            
            if len(result[i]) > 50:
                result[i] = ''
                
            if len(result[i]) < 2:
                #print(result[i])
                result[i] = ''    
            
            #加入Porter's algorithm
            result[i] = ps.stem(result[i])
            #print(result[i])
            
            #去除Stopwords
            stop_words = set(stopwords.words('english'))
            if result[i] in stop_words:
                #print(result[i])
                result[i] = ''
    
            if len(result[i]) in ['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','the','they','them','their','theirs','themselves','what','with','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']:
                #print(result[i])
                result[i] = ''
                            
            #判斷第一個是字負號或數字及最後一個字是否為數字, 去除數字
            if result[i].isdigit() == True:
                #print(result[i])
                result[i] = ''            
            
            if (result[i][:1].isdigit() == True or result[i][:1]=='-'):
                if result[i][-1:].isdigit() == True or result[i][-1:] ==0:
                    #print(result[i])
                    result[i] = ''
                    
            #確認文字字尾是否帶有符號, 計算句子, 並去除該符號
            if result[i][-1:] in ['.','"','?',':','!',',',';']:
            #if res[i][-1:] == '.' or res[i][-1:] == ',' or res[i][-1:] == '?' or res[i][-1:] == '!' or res[i][-1:] == '!!!' or res[i][-1:] == '...' or res[i][-1:] == ':':
                
                result[i]=result[i][:-1] #去除字尾符號
                
                #確認前一個字是否為數字, 若是則為小數點
                if i > len(result) and result[i+1][:1].isdigit() == True:
                    #print(res[i])
                    result[i] = ''   
        
        for i in range(len(result)):
            #print(result[i])
            #print(self.result_unique)
                
            if result[i] != '' and not result[i] in self.result_unique:
                #print('Add: '+ result[i])            
                self.result_unique.append(result[i])            
                self.word_frequency.append(0)
        
        print('result unique number:'+str(len(self.result_unique)))         

        
        for i in range(len(self.result_unique)):
            #print(self.result_unique[i])
            #print(self.word_frequency[i])
            #print(read_words.count(str(self.result_unique[i])))
            self.word_frequency[i] = int(self.word_frequency[i]) + int(read_words.count(str(self.result_unique[i])))            

    
        #fileName=time.strftime("%Y%m%d%H%M%S", time.localtime())
        fileprint=open("./analysisdata_SP_"+str(file[14:-4])+".csv", "a",encoding="utf-8")
    
        fileprint.write("Words,Frequency\n")
        
        for i in range(len(self.result_unique)):
            if not self.result_unique[i] in [' ','<','>',''] and self.result_unique[i].isdigit() == False and len(self.result_unique[i]) > 1 and self.word_frequency[i] > 0:
                fileprint.write( str(self.result_unique[i]) +',' + str(self.word_frequency[i]) +'\n')   
                #print(str(result_unique[i]) +':'+ str(word_frequency[i]))
        
        return


    def checkfile2(self,file):
        
        print(file)
        
        f = open(file, 'r',encoding="utf-8")
        read_words = f.read()
        #print(read_words)
        
        #全部轉成小寫
        read_words = read_words.lower()
    
        #去除特殊符號
        read_words = read_words.replace('/',' ')
        read_words = read_words.replace('.',' ')
        read_words = read_words.replace('\n','') 
        read_words = read_words.replace('/e/',' ')
        read_words = read_words.replace('(d)',' ')
        read_words = read_words.replace('s)',' ')
        read_words = read_words.replace('?]',' ')
        read_words = read_words.replace('?]',' ')
        read_words = read_words.replace('=-B',' ')
        read_words = read_words.replace('-C',' ')
        
        
        result = word_tokenize(read_words)
        print("Total words:"+str(len(result)))
        
        words = 0
                
        #ps = PorterStemmer()
        
        for i in range(len(result)):            
            if len(result[i]) > 0 and result[i] != '-' and result[i] != '–' and result[i] != ',':
                words += 1
                
                #確認是否為數字千分號
                pos=result[i][:-1].find(',')
                #print(pos)            
                if int(pos) > 0 and result[i][pos-1:pos].isdigit() != True :
                    words += 1
                #print(res[i])
            #去除特殊符號字元單一數字
            if result[i] in ['-','－','?','(',')','%','[',']','+','``','"','--','*','&','.','..','#','@','`','~','{','}','$','@','!']:
                result[i] = ''
            #去除特殊符號字元
            result[i] = result[i].replace('~','')
            result[i] = result[i].replace(',','')
            result[i] = result[i].replace('!','')
            result[i] = result[i].replace('@','')
            result[i] = result[i].replace('#','')
            result[i] = result[i].replace('$','')
            result[i] = result[i].replace('%','')
            result[i] = result[i].replace('^','')
            result[i] = result[i].replace('&','')
            result[i] = result[i].replace('*','')
            result[i] = result[i].replace('(','')
            result[i] = result[i].replace(')','')
            result[i] = result[i].replace('!','')
            result[i] = result[i].replace(':','')
            result[i] = result[i].replace('+','')
            result[i] = result[i].replace('=','')
            result[i] = result[i].replace('=-','')
            result[i] = result[i].replace(',','')
            result[i] = result[i].replace("'",'')
            result[i] = result[i].replace("'s",'')
            result[i] = result[i].replace('\n','')
            result[i] = result[i].replace(' ','')
            
            if len(result[i]) > 50:
                result[i] = ''
                
            if len(result[i]) < 2:
                #print(result[i])
                result[i] = ''    
            
            #加入Porter's algorithm
            #result[i] = ps.stem(result[i])
            #print(result[i])
            
            #去除Stopwords
            stop_words = set(stopwords.words('english'))
            if result[i] in stop_words:
                #print(result[i])
                result[i] = ''
    
            if len(result[i]) in ['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','the','they','them','their','theirs','themselves','what','with','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']:
                #print(result[i])
                result[i] = ''
                            
            #判斷第一個是字負號或數字及最後一個字是否為數字, 去除數字
            if result[i].isdigit() == True:
                #print(result[i])
                result[i] = ''            
            
            if (result[i][:1].isdigit() == True or result[i][:1]=='-'):
                if result[i][-1:].isdigit() == True or result[i][-1:] ==0:
                    #print(result[i])
                    result[i] = ''
                    
            #確認文字字尾是否帶有符號, 計算句子, 並去除該符號
            if result[i][-1:] in ['.','"','?',':','!',',',';']:
            #if res[i][-1:] == '.' or res[i][-1:] == ',' or res[i][-1:] == '?' or res[i][-1:] == '!' or res[i][-1:] == '!!!' or res[i][-1:] == '...' or res[i][-1:] == ':':
                
                result[i]=result[i][:-1] #去除字尾符號
                
                #確認前一個字是否為數字, 若是則為小數點
                if i > len(result) and result[i+1][:1].isdigit() == True:
                    #print(res[i])
                    result[i] = ''   
        
        for i in range(len(result)):
            #print(result[i])
            #print(self.result_unique)
                
            if result[i] != '' and not result[i] in self.result_unique:
                #print('Add: '+ result[i])            
                self.result_unique.append(result[i])            
                self.word_frequency.append(0)
        
        print('result unique number:'+str(len(self.result_unique)))         

        
        for i in range(len(self.result_unique)):
            #print(self.result_unique[i])
            #print(self.word_frequency[i])
            #print(read_words.count(str(self.result_unique[i])))
            self.word_frequency[i] = int(self.word_frequency[i]) + int(read_words.count(str(self.result_unique[i])))            

    
        #fileName=time.strftime("%Y%m%d%H%M%S", time.localtime())
        fileprint=open("./analysisdata_SN_"+str(file[14:-4])+".csv", "a",encoding="utf-8")
    
        fileprint.write("Words,Frequency\n")
        
        for i in range(len(self.result_unique)):
            if not self.result_unique[i] in [' ','<','>',''] and self.result_unique[i].isdigit() == False and len(self.result_unique[i]) > 1 and self.word_frequency[i] > 0:
                fileprint.write( str(self.result_unique[i]) +',' + str(self.word_frequency[i]) +'\n')   
                #print(str(result_unique[i]) +':'+ str(word_frequency[i]))
        
        return    
    

    def checkfile3(self,file):
        
        print(file)
        
        f = open(file, 'r',encoding="utf-8")
        read_words = f.read()
        #print(read_words)
        
        #全部轉成小寫
        read_words = read_words.lower()
    
        #去除特殊符號
        read_words = read_words.replace('/',' ')
        read_words = read_words.replace('.',' ')
        read_words = read_words.replace('\n','') 
        read_words = read_words.replace('/e/',' ')
        read_words = read_words.replace('(d)',' ')
        read_words = read_words.replace('s)',' ')
        read_words = read_words.replace('?]',' ')
        read_words = read_words.replace('?]',' ')
        read_words = read_words.replace('=-B',' ')
        read_words = read_words.replace('-C',' ')
        
        
        result = word_tokenize(read_words)
        print("Total words:"+str(len(result)))
        
        words = 0
                
        #ps = PorterStemmer()
        
        for i in range(len(result)):            
            if len(result[i]) > 0 and result[i] != '-' and result[i] != '–' and result[i] != ',':
                words += 1
                
                #確認是否為數字千分號
                pos=result[i][:-1].find(',')
                #print(pos)            
                if int(pos) > 0 and result[i][pos-1:pos].isdigit() != True :
                    words += 1
                #print(res[i])
            #去除特殊符號字元單一數字
            if result[i] in ['-','－','?','(',')','%','[',']','+','``','"','--','*','&','.','..','#','@','`','~','{','}','$','@','!']:
                result[i] = ''
            #去除特殊符號字元
            result[i] = result[i].replace('~','')
            result[i] = result[i].replace(',','')
            result[i] = result[i].replace('!','')
            result[i] = result[i].replace('@','')
            result[i] = result[i].replace('#','')
            result[i] = result[i].replace('$','')
            result[i] = result[i].replace('%','')
            result[i] = result[i].replace('^','')
            result[i] = result[i].replace('&','')
            result[i] = result[i].replace('*','')
            result[i] = result[i].replace('(','')
            result[i] = result[i].replace(')','')
            result[i] = result[i].replace('!','')
            result[i] = result[i].replace(':','')
            result[i] = result[i].replace('+','')
            result[i] = result[i].replace('=','')
            result[i] = result[i].replace('=-','')
            result[i] = result[i].replace(',','')
            result[i] = result[i].replace("'",'')
            result[i] = result[i].replace("'s",'')
            result[i] = result[i].replace('\n','')
            result[i] = result[i].replace(' ','')
            
            if len(result[i]) > 50:
                result[i] = ''
                
            if len(result[i]) < 2:
                #print(result[i])
                result[i] = ''    
            '''
            #加入Porter's algorithm
            result[i] = ps.stem(result[i])
            #print(result[i])
            '''
            '''
            #去除Stopwords
            stop_words = set(stopwords.words('english'))
            if result[i] in stop_words:
                #print(result[i])
                result[i] = ''
    
            if len(result[i]) in ['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','the','they','them','their','theirs','themselves','what','with','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']:
                #print(result[i])
                result[i] = ''
            '''                
            #判斷第一個是字負號或數字及最後一個字是否為數字, 去除數字
            if result[i].isdigit() == True:
                #print(result[i])
                result[i] = ''            
            
            if (result[i][:1].isdigit() == True or result[i][:1]=='-'):
                if result[i][-1:].isdigit() == True or result[i][-1:] ==0:
                    #print(result[i])
                    result[i] = ''
                    
            #確認文字字尾是否帶有符號, 計算句子, 並去除該符號
            if result[i][-1:] in ['.','"','?',':','!',',',';']:
            #if res[i][-1:] == '.' or res[i][-1:] == ',' or res[i][-1:] == '?' or res[i][-1:] == '!' or res[i][-1:] == '!!!' or res[i][-1:] == '...' or res[i][-1:] == ':':
                
                result[i]=result[i][:-1] #去除字尾符號
                
                #確認前一個字是否為數字, 若是則為小數點
                if i > len(result) and result[i+1][:1].isdigit() == True:
                    #print(res[i])
                    result[i] = ''   
        
        for i in range(len(result)):
            #print(result[i])
            #print(self.result_unique)
                
            if result[i] != '' and not result[i] in self.result_unique:
                #print('Add: '+ result[i])            
                self.result_unique.append(result[i])            
                self.word_frequency.append(0)
        
        print('result unique number:'+str(len(self.result_unique)))         

        
        for i in range(len(self.result_unique)):
            #print(self.result_unique[i])
            #print(self.word_frequency[i])
            #print(read_words.count(str(self.result_unique[i])))
            self.word_frequency[i] = int(self.word_frequency[i]) + int(read_words.count(str(self.result_unique[i])))            

    
        #fileName=time.strftime("%Y%m%d%H%M%S", time.localtime())
        fileprint=open("./analysisdata_NN_"+str(file[14:-4])+".csv", "a",encoding="utf-8")
    
        fileprint.write("Words,Frequency\n")
        
        for i in range(len(self.result_unique)):
            if not self.result_unique[i] in [' ','<','>',''] and self.result_unique[i].isdigit() == False and len(self.result_unique[i]) > 1 and self.word_frequency[i] > 0:
                fileprint.write( str(self.result_unique[i]) +',' + str(self.word_frequency[i]) +'\n')   
                #print(str(result_unique[i]) +':'+ str(word_frequency[i]))
        
        return
    
    
    def Start1(self):

        
        self.result_unique=[]
        self.word_frequency=[]
            
            
        Query_dir='./Data_PubMed'
    
        j=1
        for i in range(500):
            file = 'COVID-19_'+str(j*100)+'.txt'
            filepath= str(Query_dir) +'/'+ str(file)
            self.keyword = 'COVID-19'
            self.checkfile1(filepath)
            j += 1


    def Start2(self):

        
        self.result_unique=[]
        self.word_frequency=[]
            
            
        Query_dir='./Data_PubMed'
    
        j=1
        for i in range(500):
            file = 'COVID-19_'+str(j*100)+'.txt'
            filepath= str(Query_dir) +'/'+ str(file)
            self.keyword = 'COVID-19'
            self.checkfile2(filepath)
            j += 1
            
    def Start3(self):

        
        self.result_unique=[]
        self.word_frequency=[]
            
            
        Query_dir='./Data_PubMed'
    
        j=1
        for i in range(500):
            file = 'COVID-19_'+str(j*100)+'.txt'
            filepath= str(Query_dir) +'/'+ str(file)
            self.keyword = 'COVID-19'
            self.checkfile3(filepath)
            j += 1

    def plot1(self):
        filename="./SP_Data/analysisdata_SP_COVID-19_"+ str(self.documentline.text()) +".csv"
        self.keyword=str(self.keywordline.text())
        Rank1=int(self.rankline1.text())
        Rank2=int(self.rankline2.text())
        ststus='with Stopword remove & Porter’s algorithm'
        show_plot.plot_zipf(filename,ststus,self.keyword,Rank1,Rank2)
        
    def plot2(self):
        filename="./SN_Data/analysisdata_SN_COVID-19_"+ str(self.documentline.text()) +".csv"
        self.keyword=str(self.keywordline.text())
        Rank1=int(self.rankline1.text())
        Rank2=int(self.rankline2.text())
        ststus='with Stopword remove'
        show_plot.plot_zipf(filename,ststus,self.keyword,Rank1,Rank2)

    def plot3(self):
        filename="./NN_Data/analysisdata_NN_COVID-19_"+ str(self.documentline.text()) +".csv"
        self.keyword=str(self.keywordline.text())
        Rank1=int(self.rankline1.text())
        Rank2=int(self.rankline2.text())
        ststus='without Stopword remove & Porter’s algorithm'
        show_plot.plot_zipf(filename,ststus,self.keyword,Rank1,Rank2)

    def find_keywords(self):
        self.keyword=str(self.keywordline.text())
        self.edit_distance = int(self.Edit_distance.text())
        Query_dir='./Data_PubMed'
        documents = int(int(self.documentline.text())/100)
        j=1
        for i in range(documents):
            file = 'COVID-19_'+str(j*100)+'.txt'
            filepath= str(Query_dir) +'/'+ str(file)
            position = check_edit_distance_nltk.check_edit_distance(filepath,self.keyword,self.edit_distance)
            j += 1
            self.textEdit.append("File: "+str(filepath) + " ; found "+ str(self.keyword) +" in position: " +str(position) +'\n')
            print(str(filepath) + " found "+ str(self.keyword) +" in position: " +str(position))
            
            
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
    
