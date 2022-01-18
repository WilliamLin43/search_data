# -*- coding: utf-8 -*-
import os
from gensim.models import Word2Vec

def n_most_similar():
    words_input = input("Enter a word or words separated with spaces : ")
    words = words_input.lower().split()
    while len(words_input) == 0:
        print("\n You must enter a word!\n")
        words_input = input("Enter a word or words separated with spaces : ")
        words = words_input.lower().split()
    for i in range(0, len(words)):
        while (words[i] not in model1.wv):
            print("\n The word" + words[i]  + " does not exist in vocabulary!\n")
            words[i] = input("Enter a word instead which is included in vocabulary : ").lower()
    n = input("How many similar words to search for : ")
    while (not n.isdigit() or len(n) == 0 or int(n) == 0):
            print("\n You must enter an integer!\n")
            n = input("How many similar words to search for : ")
    n = int(n)
    #print(n)
    
    for i in range(len(words)):
        print("\n The most similar word to " , words[i] , " : \n")
        for j in range(n):
            print(str(model1.wv.most_similar(positive = words[i], topn = n)[j][0])+" "+str(round(model1.wv.most_similar(positive = words[i], topn = n)[j][1], PRECISION)))

def find_similar_word(words,MODEL1,n):
    filepath = './'+words+'_word2vec-skipgram-trained.model'
    if os.path.isfile(filepath):
        MODEL1 = words+'_word2vec-skipgram-trained.model'        
    else:
        MODEL1 = 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model'
    
    model1 = Word2Vec.load(MODEL1)
    
    n = int(n)
    similar_words = []
    similar_Score = []
    words = words.lower()
    print("\n The most similar word to " , words , " : \n")
    for j in range(n):
        print(str(model1.wv.most_similar(positive = words, topn = n)[j][0])+" "+str(round(model1.wv.most_similar(positive = words, topn = n)[j][1], 4)))
        similar_words.append(model1.wv.most_similar(positive = words, topn = n)[j][0])
        similar_Score.append(round(model1.wv.most_similar(positive = words, topn = n)[j][1], 4))
    return similar_words,similar_Score
        
    
   
            

if __name__ == '__main__':
    MODEL1 = "COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model"
    PRECISION = 4    
    print("Loading "+str(MODEL1)+" trained model\n")
    model1 = Word2Vec.load(MODEL1)
    print(str(MODEL1)+" trained model loaded\n")
    #n_most_similar()
    words =['COVID-19']
    n = 5
    similar_words,similar_Score = find_similar_word(words,MODEL1,n)
