# -*- coding: utf-8 -*-
#coding:utf-8

_author_ = "william"
_time_  = "2021.10.7"

import pandas as pd
from bottle import template
import webbrowser


    
def show_html(filename,keyword):
    html_string='<html><head><h1>Search XML and Json Files</h1></head><title>Search result</title><body>'
    fp = pd.read_csv(filename)#read data
    check_filename = fp["File Name"]
    Characters1 = fp["Characters1(without \)"]
    Characters2 = fp["Characters2(without \ n)"]
    Word1 = fp["Words1(re)"]
    Word2 = fp["Words2(nltk)"]
    Lines = fp["Lines"]
    Sentences = fp["Sentences"]
    Keyword_sentences_mateches = fp["Keyword sentences mateches"]
    
    
    for i in range(len(check_filename)):
        print(check_filename[i])
        html_string = html_string + '<h2>File Name: ' + str(check_filename[i])
        html_string = html_string + '</h2><p>The number of characters 1 (without \) in string are :' + str(Characters1[i])
        html_string = html_string + '</p><p>The number of characters 2 (without \ n) in string are :' + str(Characters2[i])
        html_string = html_string + '</p><p>The number of Word 1 (re) in string are :' + str(Word1[i])
        html_string = html_string + '</p><p>The number of Word 2 (nltk) in string are :' + str(Word2[i])
        html_string = html_string + '</p><p>The number of lines in string are :' + str(Lines[i])
        html_string = html_string + '</p><p>The number of Sentences in string are :' + str(Sentences[i])
        html_string = html_string + '</p><p>The number of Keyword sentences mateches in string are :' +str(Keyword_sentences_mateches[i])+'</p>'
        f = open(str(str(check_filename[i]+'.txt.txt')), 'r',encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            html_string = html_string + '<p>' + str(line.casefold().replace(keyword,'<font color="red"><b>'+keyword+'</b></font>')) +'</p>'
        html_string = html_string + '<a href=./'+str(check_filename[i])+'.txt>Link text file</a>'
    
    html_string = html_string +  '</body></html>'
   
    
    with open("search_result.html",'wb') as f:
        f.write(html_string.encode('utf-8'))
    
    
    webbrowser.open("search_result.html")

if __name__ == '__main__':
    filename = 'Search_log_20211009114825.csv'
    keyword = 'system'
    show_html(filename,keyword)