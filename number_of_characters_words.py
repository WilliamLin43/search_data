# -*- coding: utf-8 -*-
import re

def get_words_and_Characters(file,keyword):
    
    tempfile = './'+str(file)+'.txt'
    f = open(tempfile, 'r',encoding="utf-8")
    read_words = f.read()
    print(read_words)
    #read_words = "this is test "
     
    # original string
    print("The original string is : " + read_words)
     
    # using regex (findall()) function
    res = len(re.findall(r'\w+', read_words))
     
    # total no of words
    print("The number of words in string are : " + str(res))
    print("The number of Characters in string are : ", len(read_words))
    words = res
    Characters = len(read_words)
    
    return Characters,words



if __name__ == '__main__':
    file = './test1.xml'
    keyword = 'test'
    get_words_and_Characters(file,keyword)