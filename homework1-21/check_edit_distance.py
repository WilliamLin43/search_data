# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import time

def check_edit_distance(filename,keyword,edit_distance):
    
 
    print(filename)
    
    f = open(filename, 'r',encoding="utf-8")
    read_words = f.read()
    #print(read_words)
    
    #全部轉成小寫
    #read_words = read_words.lower()
    #keyword = keyword.lower()
    '''
    result = word_tokenize(read_words)
 
    for word in result:
        ed = nltk.edit_distance(keyword, word)
        if ed < 3:
            print(word, ed)
    
    '''
    
    position =''
    keyword_sentences = ''
    tempfile = time.strftime("%Y%m%d%H%M%S", time.localtime())+'.txt'
    
    for i in range(len(read_words)):
        if nltk.edit_distance(keyword, read_words[i:(i+len(keyword))]) < edit_distance:
            print('position:' + str(i))
            position = position + ',' + str(i)
            cut = 30
            if i > cut and i < len(read_words)-cut:
                print(read_words[i-cut:i+len(keyword)+cut])
                keyword_sentences = keyword_sentences + read_words[i-cut:len(keyword)+i+cut].replace("\n", "") + '\n'
            if i > cut and i > len(read_words)-cut:
               print(read_words[i-cut:])
               keyword_sentences = keyword_sentences + read_words[i-cut:].replace("\n", "") + '\n'
            if i < cut and i < len(read_words)-cut:
                print(read_words[:i+len(keyword)+cut])
                keyword_sentences = keyword_sentences + read_words[:len(keyword)+i+cut].replace("\n", "") + '\n'
            if i < cut and i > len(read_words)-cut:
                print(read_words)
                keyword_sentences = keyword_sentences + read_words.replace("\n", "") + '\n'

    f1 = open(str(tempfile+'.txt'),'w',encoding="utf-8")    
    f1.write(keyword_sentences)
    f1.close
        
    
    return position


if __name__ == '__main__':
    filename = './Data_PubMed/COVID-19_100.txt'
    keyword = 'COVID-19'

    check_edit_distance(filename,keyword)