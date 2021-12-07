# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import math
from sklearn.preprocessing import normalize
import re
import os
import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords


folder_path='./dataset'
files= os.listdir(folder_path)
filename="./sentences_data/top_2_df_sentence.txt"
fs=open(filename, "w",encoding="utf-8")

stopword = stopwords.words('english')
documents=[]
documentname = []
df={}
idf={}
for file in files:
    words = []
    tf = {}
    #print('read '+ file)
    f = open(folder_path+'/'+file, 'r',encoding="utf-8")        
    read_words = f.read()
    read_words= re.sub(r'[^\w\s]','',read_words.replace('/', ' '))
    read_words=read_words.lower()
    documents.append(read_words)
    documentname.append(file)
    Words_List=word_tokenize(read_words.lower())#變小寫
    for word in Words_List:
        if word in stopword: continue
        elif not word in words:
            words.append(word)
            tf[word] = 1
            df[word] = 0
            idf[word] = 0 
    
    for i in range(len(words)):
        for j in range(len(Words_List)):
            if words[i] == Words_List[j]:
                tf[words[i]] +=1
    for word in words:
        tf[word] =tf[word] /len(Words_List)
    
    tf_list = sorted(tf.items(), key=lambda x: x[1], reverse=True)  

    print('Top 10 tf word:')
    for i in range(10):
        print(tf_list[i:i+1])

wordindocumect=0
for file in files:
    #print('read '+ file)
    f = open(folder_path+'/'+file, 'r',encoding="utf-8")
    read_words = f.read()
    read_words1= re.sub(r'[^\w\s]','',read_words.replace('/', ' '))
    Words_List=word_tokenize(read_words1.lower())#變小寫
    for i in range(len(words)):
        for k in range(len(Words_List)):
            if words[i] == Words_List[k]:
                wordindocumect=1
        
        if wordindocumect==1:
            df[words[i]] += 1
            wordindocumect=0


df_list = sorted(df.items(), key=lambda x: x[1], reverse=True)  

print('Top 20 df word:')
for i in range(20):
    print(df_list[i:i+1])

for word in words:
    idf[word] = math.log10(116/df[word])
    
idf_list = sorted(idf.items(), key=lambda x: x[1], reverse=True)  
print('Top 10 idf word:')
for i in range(10):
    print(idf_list[i:i+1])


tf_idf ={}

for file in files:
    words = []
    tf = {}
    #print('read '+ file)
    f = open(folder_path+'/'+file, 'r',encoding="utf-8")        
    read_words = f.read()
    read_words= re.sub(r'[^\w\s]','',read_words.replace('/', ' '))
    read_words=read_words.lower()
    #documents.append(read_words)
    #documentname.append(file)
    Words_List=word_tokenize(read_words.lower())#變小寫
    for word in Words_List:
        if word in stopword: continue
        elif not word in words:
            words.append(word)
            tf[word] = 1
            
             
    
    for i in range(len(words)):
        for j in range(len(Words_List)):
            if words[i] == Words_List[j]:
                tf[words[i]] +=1
    for word in words:
        tf[word] =tf[word] /len(Words_List)
    
    for word in words:
        tf_idf[word] = tf[word] * idf[word]
        
    tf_idf_list = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)  
    print(str(file)+' Top 20 tf*idf word:')
    for i in range(20):
        print(tf_idf_list[i:i+1])

    line_tf_idf =[]
    line_tf_idf_rank = {}
    x=0
    
    fp = open(folder_path+'/'+file, 'r',encoding="utf-8")
    read_words = fp.readline()
    lines = sent_tokenize(read_words)

    
    for line in lines:
        #print(line)
        
        #line = fp.readline()
        line_word = re.sub(r'[^\w\s]','',line.replace('/', ' '))
        line_word1=word_tokenize(line_word.lower())#變小寫
        line_tf_idf.append(0)
        linewordcount =0 
        for i in range(len(line_word1)):
            if not line_word1[i] in stopword and len(line_word1[i]) > 1: 
                #print(line_word1[i])
                linewordcount+=1
                line_tf_idf[x] = line_tf_idf[x] + df[line_word1[i]]
        if linewordcount >=1:
            line_tf_idf[x] = line_tf_idf[x] / linewordcount
        else:
            line_tf_idf[x] = 0
        #print('sentence:' + str(x))
        #print('line tf idf: '+ str(line_tf_idf[x]))
        line_tf_idf_rank[x] = line_tf_idf[x]
        x+=1
    line_tf_idf_list = sorted(line_tf_idf_rank.items(), key=lambda x: x[1], reverse=True)

    

    #for i in range(2):
        #print(line_tf_idf_list[i:i+1])
        #rank_line_list.append(line_tf_idf_list[i:i+1]) 
    
    #print('Top 5 tf-idf line with ranked:')
    #for i in range(len(rank_line_list)):
        #print(str(rank_line_list[i]))
    top =2
    label = list(map(lambda x: x[0], line_tf_idf_list[:top]))
    value = list(map(lambda y: y[1], line_tf_idf_list[:top]))
    print('Top '+str(top)+' tf-idf line with ranked:')
    for i in range(len(label)):
        print(str(label[i])+','+str(value[i]))
    
    fp.close()
    
    #rank_line_list1 =list(map(lambda x: x[0], line_tf_idf_list[:3]))
    #rank_line_list2 =list(map(lambda x: x[1], line_tf_idf_list[:3]))
    
    #for i in range(len(rank_line_list)):
    #    rank_line_list1.append(str(rank_line_list[i]).split(',', 1)[0][2:])
    #    rank_line_list2.append(str(rank_line_list[i]).split(',', 1)[1][:-2])
    
    #print(str(rank_line_list1))
    #print(str(rank_line_list2))
    
    
    
    
    
    print('Top '+str(top)+' tf-idf sentence:')
    
    for i in range(len(label)):
        #print(rank_line_list1[i])
        fp = open(folder_path+'/'+file, 'r',encoding="utf-8")
        read_words = fp.readline()
        line = sent_tokenize(read_words)
        k=0
        for j in range(len(line)):            
            if int(label[i]) == k:
                print('line '+ str(k) +' : '+str(value[i]) +' , '+ str(line[j]))
                #fs.write(str(file)+',line'+ str(k) +','+str(value[i]) +','+ str(line[j])+'\n')
                fs.write(str(line[j])+'\n')
            k+=1
    
        fp.close    
    

vectorizer = TfidfVectorizer(sublinear_tf=False, stop_words=stopword, token_pattern="(?u)\\b\\w+\\b", smooth_idf=True, norm='l2')
tfidf = vectorizer.fit_transform(documents)


df_tfidf = pd.DataFrame(tfidf.toarray(),columns=vectorizer.get_feature_names(), index=documentname)
print("TFIDF")

df_tfidf.to_csv("output_df_tfidf.csv", index = True)


sentence_list={}
line_name = []


for file in files:
    line_id =0

    #print(df_tfidf.loc[file])
    fp = open(folder_path+'/'+file, 'r',encoding="utf-8") 
    read_words  = fp.readline()
    sentences = sent_tokenize(read_words)
    
    for sentence in sentences:
        line_name.append(str(file[:-4])+','+ str(line_id))
        sentence_list[line_name[line_id]] = 0
        wordcount=0
        if len(sentence) > 1:
            line_word = re.sub(r'[^\w\s]','',sentence.replace('/', ' '))
            #print(sentence)
            line_word1=word_tokenize(line_word.lower())#變小寫
            for k in range(len(line_word1)):
                for i in range(len(df_tfidf.loc[file])):
                    if line_word1[k] == df_tfidf.columns[i]:
                        wordcount +=1
                        #print(str(df_tfidf.columns[i])+ ':'+ str(df_tfidf.loc[file].iloc[i]))
                        sentence_list[line_name[line_id]] = sentence_list[line_name[line_id]] + (df_tfidf.loc[file].iloc[i])
        sentence_list[line_name[line_id]] = sentence_list[line_name[line_id]] / wordcount
        line_id +=1
        wordcount=0
                        
sentence_list_rank = sorted(sentence_list.items(), key=lambda x: x[1], reverse=True)                

top =10
label = list(map(lambda x: x[0], sentence_list_rank[:top]))
value = list(map(lambda y: y[1], sentence_list_rank[:top]))
print('Top '+str(top)+' tf-idf line with ranked:')
for i in range(len(label)):
    print(str(label[i])+','+str(value[i]))

for l in range(len(label)):
    print((label[l].split(','))[0])
    print((label[l].split(','))[1])
    for file in files:
               
        if file[:-4] ==  (label[l].split(','))[0]:
            #print(file[:-4]) 
            fp = open(folder_path+'/'+file, 'r',encoding="utf-8") 
            read_words  = fp.readline()
            sentences = sent_tokenize(read_words)
            n=0
            for sentence in sentences:
                
                if int(str(label[l].split(',')[1])) == n:
                    print(str(file) +',' + str(n) +','+str(sentence))                    
                n+=1
            
    

#print(df_tfidf.columns)


tf_word ={}

for file in files:
    fp = open(folder_path+'/'+file, 'r',encoding="utf-8") 
    #read_words = fp.read()        
    read_words  = fp.readline()
    sentences = sent_tokenize(read_words)
    
    for sentence in sentences:
        #print(sentence)
        if len(sentence) > 1:
            line_word = re.sub(r'[^\w\s]','',sentence.replace('/', ' '))
            #print(sentence)
            line_word1=word_tokenize(line_word.lower())#變小寫
            for k in range(len(line_word1)):
                for j in range(len(words)):
                    if not line_word1[k] in stopword and line_word1[k] in tf_word:
                        tf_word[line_word1[k]] = tf_word[line_word1[k]] + 1
                        #print(line_word1[k])
                    
