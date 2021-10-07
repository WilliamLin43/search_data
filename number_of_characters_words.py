# -*- coding: utf-8 -*-
import re

def get_words_and_Characters(file,keyword):
    
    tempfile = './'+str(file)+'.txt'
    f = open(tempfile, 'r',encoding="utf-8")
    read_words = f.read()
    #print(read_words)
    #read_words = "this is test "
     
    # original string
    #print("The original string is : " + read_words)
     
    # using regex (findall()) function
    res = re.findall(r'\w+', read_words)    
    #print(res)
    
    
    for i in range(len(res)):
        if str(res[i]).lower() == str(keyword).lower():            
            print('found keyword position:'+str(i))

    
    words = len(res)    
    Characters = len(read_words)
    
    total_Characters = len(re.findall(r'.+', read_words))
    
    lines = 0
    lines += read_words.count('\n')


    # total no of words
    print("The number of words in string are : " + str(words))
    print("The number of characters in string are : ", str(Characters))
    print("The number of characters in string are : ", str(total_Characters))
    print("The number of lines in string are : ", str(lines))
    
    
    
    return Characters,words,lines



if __name__ == '__main__':
    Query_dir='./test_file'
    file = 'test1.xml'
    keyword = 'system'
    get_words_and_Characters(file,keyword)