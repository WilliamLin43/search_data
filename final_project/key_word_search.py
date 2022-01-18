# -*- coding: utf-8 -*-
import sys
import os
import time
import webbrowser
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
import re
import numpy as np
from PyQt5.QtGui import (QImage,QPixmap,QIcon,QFont)
from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton, 
                             QHBoxLayout, QVBoxLayout, qApp, QApplication, 
                             QLabel, QAction, QFileDialog, QComboBox,QStyle,QLineEdit,QTextEdit)

from Word2Vec_Search import find_similar_word
from find_tfidf import calculate_tfidf
from show_plot import plot_2D,plot_3D
from KMeans import find_KMeans

class WinForm(QMainWindow):
    def __init__(self, parent=None):
        super(WinForm, self) .__init__(parent)
        
        self.setGeometry(200, 150, 1900, 1300)   #windows position and size
        layout = QVBoxLayout ()
        
        self.nword_Number = 10
        self.Similar_Value = 0
        
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Keyword: ')
        self.nameLabel.setGeometry(10,50,100,50)        
        self.keywordline = QLineEdit(self)
        self.keywordline.setText('COVID-19 MIS-C')
        self.keywordline.setGeometry(110,50,300,50)
        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('find similar word: ')
        self.nameLabel1.setGeometry(450,50,300,50)

        self.nword_label = QLabel(self)
        self.nword_label.setText('10')
        self.nword_label.setGeometry(650,50,100,50)  
        
        #comboBox setting
        self.selectnwordcombo = QComboBox(self)
        for i in range(30):
            self.selectnwordcombo.addItem(str(i+1))
        self.selectnwordcombo.move(700, 60)
        self.selectnwordcombo.adjustSize()
        self.selectnwordcombo.activated[str].connect(self.selectnwordonChanged)
        

        self.Similar_Value_label = QLabel(self)
        self.Similar_Value_label.setFont(QFont("Roman times",10,QFont.Bold))        
        self.Similar_Value_label.setStyleSheet("background-color:yellow")
        self.Similar_Value_label.setText('<font color=red>Similar Value:'+str(self.Similar_Value) +'</font>')
        self.Similar_Value_label.setGeometry(800,50,250,50)  

        self.Search_Word2vec = QPushButton ('Search Word2vec', self)
        self.Search_Word2vec.setStyleSheet("QPushButton{font-size:32px}")
        self.Search_Word2vec.setGeometry(10,110, 300, 100)   #position and size
        self.Search_Word2vec.clicked.connect (self.Start)     #call function

        self.Search_TF_IDF = QPushButton ('Search TF-IDF(W)', self)
        self.Search_TF_IDF.setStyleSheet("QPushButton{font-size:32px}")
        self.Search_TF_IDF.setGeometry(320,110, 300, 100)   #position and size
        self.Search_TF_IDF.clicked.connect (self.TF_IDF)     #call function

        self.Search_TF_IDF_S = QPushButton ('Search TF-IDF(S)', self)
        self.Search_TF_IDF_S.setStyleSheet("QPushButton{font-size:32px}")
        self.Search_TF_IDF_S.setGeometry(630,110, 300, 100)   #position and size
        self.Search_TF_IDF_S.clicked.connect (self.TF_IDF_S)     #call function

        self.Show_Plot = QPushButton ('Show Word2vec', self)
        self.Show_Plot.setStyleSheet("QPushButton{font-size:32px}")
        self.Show_Plot.setGeometry(940,110, 300, 100)   #position and size
        self.Show_Plot.clicked.connect (self.Show_Plot_Run)     #call function

        self.Show_Plot1 = QPushButton ('Show TF-IDF', self)
        self.Show_Plot1.setStyleSheet("QPushButton{font-size:32px}")
        self.Show_Plot1.setGeometry(1250,110, 300, 100)   #position and size
        self.Show_Plot1.clicked.connect (self.Show_Plot_Run1)     #call function        

        self.Show_Plot1 = QPushButton ('Show KMean', self)
        self.Show_Plot1.setStyleSheet("QPushButton{font-size:32px}")
        self.Show_Plot1.setGeometry(1560,110, 300, 100)   #position and size
        self.Show_Plot1.clicked.connect (self.Show_KMean)     #call function        


        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(10,220,1850,1050)
        
        #self.displayLabel = QLabel(self)
        #self.displayLabel.setStyleSheet("background-color:lightgreen")
        #self.displayLabel.setGeometry(1100,50,1000,2000) 

        
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

    def selectnwordonChanged(self, text):
        self.nword_label.setText(text)
        self.nword_Number =int(text)
        #self.nword_label.adjustSize()


    def Word_process(Awords):
        stopword = stopwords.words('english')
        Rwords =[]
        for k in range(len(Awords)):
            if Awords[k] in stopword:
                Awords[k] = ''
                
            if Awords[k] in ['-','－','?','(',')','%','[',']','+','``','"','--','*','&','.','..','#','@','`','~','{','}','$','@','!']:
                Awords[k] = ''
            #去除特殊符號字元
            Awords[k] = Awords[k].replace('~','')
            Awords[k] = Awords[k].replace(',','')
            Awords[k] = Awords[k].replace('!','')
            Awords[k] = Awords[k].replace('@','')
            Awords[k] = Awords[k].replace('#','')
            Awords[k] = Awords[k].replace('$','')
            Awords[k] = Awords[k].replace('%','')
            Awords[k] = Awords[k].replace('^','')
            Awords[k] = Awords[k].replace('&','')
            Awords[k] = Awords[k].replace('*','')
            Awords[k] = Awords[k].replace('(','')
            Awords[k] = Awords[k].replace(')','')
            Awords[k] = Awords[k].replace('!','')
            Awords[k] = Awords[k].replace(':','')
            Awords[k] = Awords[k].replace('+','')
            Awords[k] = Awords[k].replace('=','')
            Awords[k] = Awords[k].replace('=-','')
            Awords[k] = Awords[k].replace(',','')
            Awords[k] = Awords[k].replace("'",'')
            Awords[k] = Awords[k].replace("'s",'')
            Awords[k] = Awords[k].replace('\n','')
            Awords[k] = Awords[k].replace('\r','')        
            Awords[k] = Awords[k].replace(' ','')
            Awords[k] = Awords[k].replace('.','')
        for k in range(len(Awords)):
            if Awords[k] != '':
                Rwords.append(Awords[k])
        return Rwords



    def jaccard_similarity(s1, s2):
        def add_space(s):
            return ' '.join(list(s))
    
        # 將字中間加入空格
        s1, s2 = add_space(s1), add_space(s2)
        # 轉化為TF矩陣
        cv = CountVectorizer(tokenizer=lambda s: s.split())
        corpus = [s1, s2]
        vectors = cv.fit_transform(corpus).toarray()
        # 求交集
        numerator = np.sum(np.min(vectors, axis=0))
        # 求並集
        denominator = np.sum(np.max(vectors, axis=0))
        # 計算傑卡德係數
        return (1.0*numerator/denominator)


    def create_html1(self,tf_idf_sentences):
        
        html_string='<html><head><h1>Search '+ str(self.keywordline.text()) +'</h1></head><title>Search result</title><body>'
        html_string=html_string + '<table style="border:3px #cccccc solid;" cellpadding="10" border="1"><tr><td><b>#</b></td><td><b>Keyword</b></td><td><b>Douument</b></td><td><b>Sentenance</b></td><td><b>Score</b></td>'
        for i in range(len(tf_idf_sentences)):
            html_string=html_string + '<tr>'
            html_string=html_string + '<td><b>'+str(i+1)+'</td>'
            if i < (len(tf_idf_sentences)/2):
                html_string=html_string + '<td><p><font color="blue"><b>'+str(self.words[0])+'</b></font></p></td>'
            else:
                html_string=html_string + '<td><p><font color="blue"><b>'+str(self.words[1])+'</b></font></p></td>'
            for j in range(len(tf_idf_sentences[i])):
                html_string = html_string + '<td><p><font color="red"><b>' + str(tf_idf_sentences[i][j])+'</b></font></p></td>'
            html_string=html_string + '</tr>'
        html_string=html_string + '</tr></table>'
        html_string = html_string +  '</body></html>'
        
        #self.displayLabel.setText(html_string)
        self.textEdit.append(html_string)
   
        with open("search_result.html",'wb') as f:
            f.write(html_string.encode('utf-8'))
        webbrowser.open("search_result.html")


    def create_html2(self,tf_idf_words):
        
        html_string='<html><head><h1>Search '+ str(self.keywordline.text()) +'</h1></head><title>Search result</title><body>'
        html_string=html_string + '<table style="border:3px #cccccc solid;" cellpadding="10" border="1"><tr><td><b>#</b></td><td><b>Keyword</b></td><td><b>TF-IDF</b></td><td><b>Score</b></td>'
        for i in range(len(tf_idf_words)):
            html_string=html_string + '<tr>'
            html_string=html_string + '<td><b>'+str(i+1)+'</b></td>'
            if i < (len(tf_idf_words)/2):
                html_string=html_string + '<td><p><font color="blue"><b>'+str(self.words[0])+'</b></font></p></td>'
            else:
                html_string=html_string + '<td><p><font color="blue"><b>'+str(self.words[1])+'</b></font></p></td>'
            for j in range(len(tf_idf_words[i])):
                html_string = html_string + '<td><p><font color="red"><b>' + str(tf_idf_words[i][j])+'</b></font></p></td>'
            html_string=html_string + '</tr>'
        html_string=html_string + '</tr></table>'
        html_string = html_string +  '</body></html>'
        
        #self.displayLabel.setText(html_string)
        self.textEdit.append(html_string)
   
        with open("search_result2.html",'wb') as f:
            f.write(html_string.encode('utf-8'))
        webbrowser.open("search_result2.html")


    def create_html3(self,similar_words,similar_Score):
        
        html_string='<html><head><h1>Search '+ str(self.keywordline.text()) +'</h1></head><title>Search result</title><body>'
        html_string=html_string + '<table style="border:3px #cccccc solid;" cellpadding="10" border="1"><tr><td><b>#</b></td><td><b>Keyword</b></td><td><b>Word2Vec</b></td><td><b>Score</b></td>'
        #for i in range(int(len(similar_words)/len(self.words))):
        for i in range(len(similar_words)):
            html_string=html_string + '<tr>'
            html_string=html_string + '<td><b>'+str(i+1)+'</b></td>'
            if i < (len(similar_words)/2):
                html_string=html_string + '<td><p><font color="blue"><b>'+str(self.words[0])+'</b></font></p></td>'

            else:
                html_string=html_string + '<td><p><font color="blue"><b>'+str(self.words[1])+'</b></font></p></td>'


            html_string = html_string + '<td><p><font color="red"><b>' + str(similar_words[i])+'</b></font></p></td>'
            html_string = html_string + '<td><p><font color="red"><b>' + str(similar_Score[i])+'</b></font></p></td>'         

            html_string=html_string + '</tr>'
        html_string=html_string + '</tr></table>'
        html_string = html_string +  '</body></html>'
        
        #self.displayLabel.setText(html_string)
        self.textEdit.append(html_string)
   
        with open("search_result2.html",'wb') as f:
            f.write(html_string.encode('utf-8'))
        webbrowser.open("search_result2.html")

        
    def Start(self):
        print("Search ...")
        self.keyword = str(self.keywordline.text())
        self.words = self.keyword.lower().split()
        MODEL1 = "COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model"        
        similar_list =[]
        similar_list_Score=[]
        #similar_word = {}
        for w in self.words:
            if not w in ['and','or']:
                self.textEdit.append(str(w) +' similar words top ' + str(self.nword_Number) )
                similar_words,similar_Score = find_similar_word(w,MODEL1,self.nword_Number)
                for j in range(len(similar_words)):
                    self.textEdit.append(str(similar_words[j])+":"+str(similar_Score[j]))
                    similar_list.append(str(similar_words[j]))
                    similar_list_Score.append(str(similar_Score[j]))
                    #similar_word[str(w)+str(j)] = str(similar_words[j])
        
        words_list =''
        for i in range(len(similar_list)):
            words_list = str(words_list) +', '+ str(similar_list[i])
        word_count = 0
        for i in range(len(similar_list)):
            for j in range(len(similar_list)):                
                if similar_list[i] == similar_list[j]:
                    word_count += 1
        if word_count-len(similar_list) > 0:
            self.textEdit.append("<font color=red>Similar Value= " +str(((word_count-len(similar_list)))/len(similar_list))+"</font>") 
            self.Similar_Value = (word_count-len(similar_list))/len(similar_list)
        else:
            self.textEdit.append("<font color=red>Similar Value= 0.0</font>")
            self.Similar_Value = 0
        
        WinForm.create_html3(self,similar_list,similar_list_Score)
        self.Similar_Value_label.setText('<font color=red>Similar Value:'+str(self.Similar_Value) +'</font>')
        
        
    def TF_IDF(self):
        print("Search ...")
        self.keyword = str(self.keywordline.text())
        self.words = self.keyword.lower().split()

        tf_idf_word =[]
        tf_idf_word2 =[]
        tf_idf_sentences =[]
        for w in self.words:
            if not w in ['and','or']:
                #self.textEdit.append(str(w))
                SEC_R,tf_idf,tf_idf_R2 = calculate_tfidf(w,self.nword_Number)

            if not w in ['and','or']:   
                self.textEdit.append(str(w)+' TFIDF Top '+ str(self.nword_Number))
                for i in range(len(tf_idf)):
                    self.textEdit.append(str(i+1)+' : ' + str(tf_idf[i]))
                    tf_idf_word.append(tf_idf[i])
                    tf_idf_word2.append(tf_idf_R2[i])
                self.textEdit.append(str(w)+' TFIDF Sentences top '+ str(self.nword_Number))
                for i in range(len(SEC_R)):
                    self.textEdit.append(str(i+1)+' : ' + str(SEC_R[i]))
                    tf_idf_sentences.append(SEC_R[i])
        word_count = 0
        for i in range(len(tf_idf_word)):
            for j in range(len(tf_idf_word)):                
                if tf_idf_word[i] == tf_idf_word[j]:
                    word_count += 1
        if word_count-len(tf_idf_word) > 0:
            self.textEdit.append("<font color=red><b>Similar Value= " +str(((word_count-len(tf_idf_word)))/len(tf_idf_word))+"</b></font>")
            self.Similar_Value = (word_count-len(tf_idf_word))/len(tf_idf_word)
        else:
            self.textEdit.append("<font color=red><b>Similar Value= 0.0</b></font>")
            self.Similar_Value = 0
        
        #WinForm.create_html1(self,tf_idf_sentences)
        WinForm.create_html2(self,tf_idf_word2,)
        self.Similar_Value_label.setText('<font color=red><b>Similar Value:'+str(self.Similar_Value) +'</b></font>')

    def TF_IDF_S(self):
        print("Search ...")
        self.keyword = str(self.keywordline.text())
        self.words = self.keyword.lower().split()

        tf_idf_word =[]
        tf_idf_word2 =[]
        tf_idf_sentences =[]
        for w in self.words:
            if not w in ['and','or']:
                #self.textEdit.append(str(w))
                SEC_R,tf_idf,tf_idf_R2 = calculate_tfidf(w,self.nword_Number)

            if not w in ['and','or']:   
                self.textEdit.append(str(w)+' TFIDF Top '+ str(self.nword_Number))
                for i in range(len(tf_idf)):
                    self.textEdit.append(str(i+1)+' : ' + str(tf_idf[i]))
                    tf_idf_word.append(tf_idf[i])
                    tf_idf_word2.append(tf_idf_R2[i])
                self.textEdit.append(str(w)+' TFIDF Sentences top '+ str(self.nword_Number))
                for i in range(len(SEC_R)):
                    self.textEdit.append(str(i+1)+' : ' + str(SEC_R[i]))
                    tf_idf_sentences.append(SEC_R[i])
        word_count = 0
        
        for i in range(len(tf_idf_word)):
            for j in range(len(tf_idf_word)):                
                if tf_idf_word[i] == tf_idf_word[j]:
                    word_count += 1
        if word_count-len(tf_idf_word) > 0:
            self.textEdit.append("Similar Value= " +str(((word_count-len(tf_idf_word)))/len(tf_idf_word)))
            self.Similar_Value = (word_count-len(tf_idf_word))/len(tf_idf_word)
        else:
            self.textEdit.append("Similar Value= 0.0")
            self.Similar_Value = 0
        
        s1 =''
        s2 =''
        for i in range(len(tf_idf_sentences)):
            if i < self.nword_Number:
                s1 = s1 + str(tf_idf_sentences[i][1])
            else:
                s2 = s2 + str(tf_idf_sentences[i][1])
        
        print("s1")
        print(s1)
        print("s2")
        print(s2)
        
        mark_out = re.sub(r'^\w\s',' ',s1.replace('/', ' '))        
        Awords=word_tokenize(mark_out.lower())#變小寫
        s1=WinForm.Word_process(Awords)
        
        mark_out = re.sub(r'^\w\s',' ',s2.replace('/', ' '))        
        Awords=word_tokenize(mark_out.lower())#變小寫
        s2=WinForm.Word_process(Awords)
        
        
        self.Similar_Value = WinForm.jaccard_similarity(s1,s2)
        
        self.textEdit.append("Similar Value= " +str(self.Similar_Value))
        
        
        
        WinForm.create_html1(self,tf_idf_sentences)
        #WinForm.create_html2(self,tf_idf_word2,)
        self.Similar_Value_label.setText('<font color=red>Similar Value:'+str(self.Similar_Value) +'</font>')

    def Show_Plot_Run(self):
            f = open('./word2vec_covid-19.txt', 'r',encoding="utf-8")
            read_words = f.read()
            read_words1 = read_words.encode('utf-8').decode('utf-8')    
            read_words1 = re.sub(r'^\w\s',' ',str(read_words))
            Words_List1=word_tokenize(read_words1.lower())#變小寫
        
            f = open('./word2vec_mis-c.txt', 'r',encoding="utf-8")
            read_words = f.read()
            read_words1 = read_words.encode('utf-8').decode('utf-8')    
            read_words1 = re.sub(r'^\w\s',' ',str(read_words))
            Words_List2=word_tokenize(read_words1.lower())#變小寫
        
            f = open('./word2vec_endometriosis.txt', 'r',encoding="utf-8")
            read_words = f.read()
            read_words1 = read_words.encode('utf-8').decode('utf-8')    
            read_words1 = re.sub(r'^\w\s',' ',str(read_words))
            Words_List3=word_tokenize(read_words1.lower())#變小寫    
        
            f = open('./word2vec_sars-cov-2.txt', 'r',encoding="utf-8")
            read_words = f.read()
            read_words1 = read_words.encode('utf-8').decode('utf-8')    
            read_words1 = re.sub(r'^\w\s',' ',str(read_words))
            Words_List4=word_tokenize(read_words1.lower())#變小寫           
        
            keyword =['COVID-19','MIS-C','Endometriosis','SARS-COV-2']
            #plot_3D(Words_List)
            plot_2D(Words_List1,Words_List2,Words_List3,Words_List4,keyword)
            plot_3D(Words_List1,Words_List2,Words_List3,Words_List4,keyword)
        
    def Show_Plot_Run1(self):
            f = open('./tfidf_covid-19.txt', 'r',encoding="utf-8")
            read_words = f.read()
            read_words1 = read_words.encode('utf-8').decode('utf-8')    
            read_words1 = re.sub(r'^\w\s',' ',str(read_words))
            Words_List1=word_tokenize(read_words1.lower())#變小寫
        
            f = open('./tfidf_mis-c.txt', 'r',encoding="utf-8")
            read_words = f.read()
            read_words1 = read_words.encode('utf-8').decode('utf-8')    
            read_words1 = re.sub(r'^\w\s',' ',str(read_words))
            Words_List2=word_tokenize(read_words1.lower())#變小寫
        
            f = open('./tfidf_endometriosis.txt', 'r',encoding="utf-8")
            read_words = f.read()
            read_words1 = read_words.encode('utf-8').decode('utf-8')    
            read_words1 = re.sub(r'^\w\s',' ',str(read_words))
            Words_List3=word_tokenize(read_words1.lower())#變小寫    
            
            f = open('./tfidf_sars-cov-2.txt', 'r',encoding="utf-8")
            read_words = f.read()
            read_words1 = read_words.encode('utf-8').decode('utf-8')    
            read_words1 = re.sub(r'^\w\s',' ',str(read_words))
            Words_List4=word_tokenize(read_words1.lower())#變小寫    
            
            keyword =['COVID-19','MIS-C','Endometriosis','SARS-COV-2']
            #plot_3D(Words_List)
            plot_2D(Words_List1,Words_List2,Words_List3,Words_List4,keyword)
            plot_3D(Words_List1,Words_List2,Words_List3,Words_List4,keyword)

    def Show_KMean(self):
        find_KMeans(self.nword_Number)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())