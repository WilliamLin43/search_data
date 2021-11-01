# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import time
from termcolor import colored, cprint
import sys
import webbrowser

def check_edit_distance(filename,keyword,edit_distance):
    
 
    print(filename)
    
    f = open(filename, 'r',encoding="utf-8")
    read_words = f.read()
    #print(read_words)
    
    #全部轉成小寫
    #read_words = read_words.lower()
    #keyword = keyword.lower()
    
    result = word_tokenize(read_words)
    position =''
    tempfile = time.strftime("%Y%m%d%H%M%S", time.localtime())


    html_string='<html><head><h1>Search keyword Files</h1></head><title>Search result</title><body>'
    html_string = html_string + '<h2>File Name: ' + str(filename) +'</h2>'
    html_string = html_string + '<p>'

    j=0
    
    for word in result:
        ed = nltk.edit_distance(keyword, word)
        
        if ed < edit_distance:
            print(word, ed)
            position = position +','+ str(j)
            html_string = html_string + '<font color="red"><b> ' + str(word)+'</b></font>'
        else:
            html_string = html_string + ' ' + str(word)
        
        j += 1
        
    html_string = html_string +  '</p></body></html>'
    with open("search_result"+str(tempfile)+".html",'wb') as f:
        f.write(html_string.encode('utf-8'))
    
    
    webbrowser.open("search_result"+str(tempfile)+".html")
    
    position = position[1:]
    print(position)

    
    return position


if __name__ == '__main__':
    filename = './Data_PubMed/COVID-19_100.txt'
    keyword = 'COVID-19'
    edit_distance = 3

    check_edit_distance(filename,keyword,edit_distance)