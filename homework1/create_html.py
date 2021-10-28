# -*- coding: utf-8 -*-
#coding:utf-8

_author_ = "william"
_time_  = "2021.10.7"

import pandas as pd
import webbrowser


    
def show_html(filename,keyword):
    html_string='<html><head><h1>Search XML and Json Files</h1></head><title>Search result</title><body>'
    fp = pd.read_csv(filename)#read csv lod data
    check_filename = fp["File Name"]
    Characters1 = fp["Characters1(without empty)"]
    Word1 = fp["Words1(re)"]
    Word2 = fp["Words2(nltk)"]
    Lines = fp["Lines"]
    Sentences = fp["Sentences"]
    Keyword_sentences_mateches = fp["Keyword sentences mateches"]
    
    
    for i in range(len(check_filename)): 
        #print(check_filename[i])
        html_string = html_string + '<h2>File Name: ' + str(check_filename[i])
        html_string = html_string + '</h2><p>The number of characters (without empty) in string are :<font color="blue"><b>' + str(Characters1[i])+'</b></font>'
        html_string = html_string + '</p><p>The number of Word 1 (re) in string are :<font color="blue"><b>' + str(Word1[i])+'</b></font>'
        html_string = html_string + '</p><p>The number of Word 2 (nltk) in string are :<font color="blue"><b>' + str(Word2[i])+'</b></font>'
        html_string = html_string + '</p><p>The number of lines in string are :<font color="blue"><b>' + str(Lines[i])+'</b></font>'
        html_string = html_string + '</p><p>The number of Sentences in string are :<font color="blue"><b>' + str(Sentences[i])+'</b></font>'
        html_string = html_string + '</p><p>The number of Keyword sentences mateches in string are :<font color="blue"><b>' +str(Keyword_sentences_mateches[i])+'</b></font></p>'
        f = open(str(str(check_filename[i]+'.txt.txt')), 'r',encoding="utf-8") # read keyword sentences log file
        lines = f.readlines()
        for line in lines:
            for j in range(len(line)):
                if keyword == line[j:(j+len(keyword))]: #check keyword position                    
                    html_string = html_string + '<p>' + str(line[:j]) + '<font color="red"><b>'+ str(line[j:j+len(keyword)]) +'</b></font>'+ str(line[j+len(keyword):]) +'</p>'
            
        html_string = html_string + '<a href=./'+str(check_filename[i])+'.txt>Link text file</a>'
    
    html_string = html_string +  '</body></html>'
   
    
    with open("search_result.html",'wb') as f:
        f.write(html_string.encode('utf-8'))
    
    
    webbrowser.open("search_result.html")

if __name__ == '__main__':
    filename = 'Search_log_20211009114825.csv'
    keyword = 'system'
    show_html(filename,keyword)