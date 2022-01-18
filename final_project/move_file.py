# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize
import re
import os
import shutil


def search_file(Keyword):

    folder_path='./dataset_all'
    files= os.listdir(folder_path)
    wordindocumect =0
    folder_path1 = './dataset/'+Keyword
    
    if os.path.isdir(folder_path1):
        print('remove folder & files')
        shutil.rmtree(folder_path1)
        os.mkdir(folder_path1)
    else:
        os.mkdir(folder_path1)
    
    for file in files:
        #print('read '+ file)
        f = open(folder_path+'/'+file, 'r',encoding="utf-8")
        read_words = f.read()
        #read_words1= re.sub(r'[^\w\s]','',read_words.replace('/', ' '))
        read_words1 = re.sub(r'^\w\s',' ',str(read_words))
        #Words_List = word_tokenize(read_words1)
        Words_List=word_tokenize(read_words1.lower())#變小寫
        
        for i in range(len(Words_List)):
            if Words_List[i] == Keyword.lower():
                wordindocumect=1
        
        if wordindocumect==1:
            wordindocumect=0
            print(str(folder_path)+'/'+str(file))
            shutil.copyfile(folder_path+'/'+file, './dataset/'+ str(Keyword)+'/'+file)

if __name__ == '__main__':
    Keyword ='COVID-19'
    #Keyword ='MIS-C'
    #Keyword ='Endometriosis'
    search_file(Keyword)
    