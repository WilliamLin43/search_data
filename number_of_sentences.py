# -*- coding: utf-8 -*-
import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text


def get_sentences(file,keyword):
    
    tempfile = './'+str(file)+'.txt'
    f = open(tempfile, 'r',encoding="utf-8")
    read_words = f.read()
    #print(read_words)
    
    #read_words = 'A Turning machine is a device that manipulates symbols on a strip of tape according to a table of rules. Despite its simplicity, a Turing machine can be adapted to simulate the logic of any computer algorithm, and is particularly useful in explaining the functions of a CPU inside a computer. The "Turing" machine was described by Alan Turing in 1936, who called it an "a(utomatic)-machine". The Turing machine is not intended as a practical computing technology, but rather as a hypothetical device representing a computing machine. Turing machines help computer scientists understand the limits of mechaniacl computation.'
    
    sentences = sent_tokenize(read_words)
    #print(sentences)
    
    print('Number of sentences by nltk: ' + str(len(sentences)))
    
    tokens = word_tokenize(read_words)
    print('Number of word by nltk: ' + str(len(tokens)))
    #print(tokens)
    print('Keyword of sentences: '+str(keyword))
    textList = Text(tokens)
    textList.concordance(keyword)
    
    position =''
    keyword_sentences = ''
    
    for i in range(len(read_words)):
        if keyword.casefold() == read_words[i:(i+len(keyword))].casefold():
            print('position:' + str(i))
            position = position + ',' + str(i)
            cut = 20
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
    
    return len(sentences),len(tokens),position,keyword_sentences


if __name__ == '__main__':
    file = './test1.xml'
    keyword = 'test'
    get_sentences(file,keyword)