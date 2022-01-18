# -*- coding: utf-8 -*-
import os
import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
import re

#folder_path='./dataset/COVID-19'
#filename="./dataset/COVID-19_sentence.txt"
#folder_path='./dataset/MIS-C'
#filename="./dataset/MIS-C_sentence.txt"
folder_path='./dataset/Endometriosis'
filename="./dataset/Endometriosis_sentence.txt"


fp=open(filename, "w",encoding="utf-8")

files= os.listdir(folder_path)


for file in files:
    print('read '+ file)
    f = open(folder_path+'/'+file, 'r',encoding="utf-8")
    read_words = f.read()
    
    read_words = read_words.encode('utf-8').decode('utf-8')
    regex = re.compile(r'[\n\r\t\']')
    read_words = regex.sub("", read_words)
    read_words = read_words.encode('ascii', 'ignore')
    
    read_words = ' '.join(str(read_words).split())
    
    sentences = sent_tokenize(read_words)
    
    for sentence in sentences:
        #print(sentence)
        if len(sentence) > 1:
            fp.write(sentence)
            #fp.write('\n')