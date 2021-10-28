# -*- coding: utf-8 -*-
import re

def get_words_and_Characters(file,keyword):
    
    tempfile = './'+str(file)+'.txt'
    f = open(tempfile, 'r',encoding="utf-8")
    read_words = f.read()
    #print(read_words)

    #read_words = read_words.replace('/',',')  
    
    res = re.split(r'\s+', read_words)    
    
    words = 0
    sentences=0
    
    for i in range(len(res)):
        if len(res[i]) > 0 and res[i] != '-' and res[i] != '–' and res[i] != ',':
            words += 1
            pos=res[i][:-1].find(',')
            
            if int(pos) > 0 and res[i][pos-1:pos].isdigit() != True :
                words += 1
            #print(res[i])
        if res[i][-1:] == '.' or res[i][-1:] == '?' or res[i][-1:] == '!' or res[i][-1:] == '!!!' or res[i][-1:] == '...' or res[i][-1:] == ':':
            sentences += 1
            if i > len(res) and res[i+1][:1].isdigit():
                #print(res[i])
                sentences -= 1
                
    print('check sentences number:'+str(sentences))
    '''
    read_words = read_words.replace('\n','.')    
    sentences_line = re.split(r"[.,...,?,!,!!!,???]", read_words)
    for i in range(len(sentences_line)):
        if len(sentences_line[i]) > 1:
            print(sentences_line[i])
   '''         
        #if str(res[i]).lower() == str(keyword).lower():            
        #    print('found keyword position:'+str(i))

    lines = 0
    lines += read_words.count('\n')
    
    read_words = re.sub(r"\s+", "", read_words)
    #print(read_words)
    
    Characters = len(read_words)
        
    


    # total no of words
    print("The number of words in string are : " + str(words))
    print("The number of characters(without empty) in string are : ", str(Characters))
    print("The number of lines in string are : ", str(lines))
    
    
    
    return Characters,words,lines



if __name__ == '__main__':
    Query_dir='./test_file'
    file = 'test1.xml'
    keyword = 'system'
    get_words_and_Characters(file,keyword)