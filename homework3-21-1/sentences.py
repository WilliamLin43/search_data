# -*- coding: utf-8 -*-
import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text


f = open('./dataset/dailymail.txt', 'r',encoding="utf-8")
read_words = f.read()
    
sentences = sent_tokenize(read_words)

filename="./dataset/dailymail_sentence.txt"
fp=open(filename, "a",encoding="utf-8")

for sentence in sentences:
    print(sentence)
    if len(sentence) > 1:
        fp.write(sentence)
        fp.write('\n')