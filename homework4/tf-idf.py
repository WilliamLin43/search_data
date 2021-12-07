# -*- coding: utf-8 -*-
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import os
import math

stopword = stopwords.words('english')

folder_path='./dataset1'
files= os.listdir(folder_path)
document=0
counts=0
words=[]
wordcount ={}
df_word = []
df={}

for file in files:
    #print('read '+ file)
    f = open(folder_path+'/'+file, 'r',encoding="utf-8")
    read_words = f.read()
    read_words1= re.sub(r'[^\w\s]','',read_words.replace('/', ' '))
    Words_List=word_tokenize(read_words1.lower())#變小寫
    document +=1
    for word in Words_List:
        if not word in stopword and len(word) > 1:
            counts+=1
        if not word in words and not word in stopword and len(word) > 1:            
            words.append(word)
        if not word in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

        if word in stopword: continue
        elif not word in df_word:
            df_word.append(word)
            df[word] = 0
       

'''    
for word in words:
    print(str(word) +':'+ str(wordcount[word]))
'''
counter_list = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
    
#for i in
print('total words:' +str(counts)) 
print('words not in stopword: '+str(len(words)))#單詞數


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

#print(counter_list[:])
tf=[]
tf_list ={}
idf=[]
tf_idf={}



for i in range(len(words)):
    word_tf=(wordcount[words[i]])/counts
    tf.append((word_tf))
    tf_list[words[i]] = word_tf
    word_idf=math.log10(document/df[words[i]])
    #print(words[i] +':' + str(df[words[i]]))
    idf.append(int(word_idf))
    tf_idf[words[i]]=word_tf*word_idf
tf_idf_counter_list = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)


print('Top 20 tf-idf word:')

for i in range(20):
    print(tf_idf_counter_list[i:i+1])

tf_counter_list = sorted(tf_list.items(), key=lambda x: x[1], reverse=True)
print('Top 20 tf word:')

for i in range(20):
    print(tf_counter_list[i:i+1])
    

fp = open('./sentences_data1/sentence.txt', "r",encoding="utf-8")
line = fp.readline()

line_tf_idf =[]
line_tf_idf_rank = {}
x=0

## 用 while 逐行讀取檔案內容，直至檔案結尾
while line:
    #print(line)
    
    line = fp.readline()
    line_word = re.sub(r'[^\w\s]','',line.replace('/', ' '))
    line_word1=word_tokenize(line_word.lower())#變小寫
    line_tf_idf.append(0)
    linewordcount =0 
    for i in range(len(line_word1)):
        if not line_word1[i] in stopword and len(line_word1[i]) > 1: 
            #print(line_word1[i])
            linewordcount+=1
            line_tf_idf[x] = line_tf_idf[x] + tf_idf[line_word1[i]]
    if linewordcount >=1:
        line_tf_idf[x] = line_tf_idf[x] / linewordcount
    else:
        line_tf_idf[x] = 0
    #print('sentence:' + str(x))
    #print('line tf idf: '+ str(line_tf_idf[x]))
    line_tf_idf_rank[x] = line_tf_idf[x]
    x+=1

fp.close()

line_tf_idf_list = sorted(line_tf_idf_rank.items(), key=lambda x: x[1], reverse=True)

rank_line_list =[]

for i in range(5):
    #print(line_tf_idf_list[i:i+1])
    rank_line_list.append(line_tf_idf_list[i:i+1]) 

print('Top 5 tf-idf line with randed:')
for i in range(len(rank_line_list)):
    print(str(rank_line_list[i]))

rank_line_list1 =[]
rank_line_list2 = []

for i in range(len(rank_line_list)):
    rank_line_list1.append(str(rank_line_list[i]).split(',', 1)[0][2:])
    rank_line_list2.append(str(rank_line_list[i]).split(',', 1)[1][:-2])

#print(str(rank_line_list1))
    #print(str(rank_line_list1[0][2:]))





print('Top 5 tf-idf sentence:')

for i in range(len(rank_line_list1)):
    #print(rank_line_list1[i])
    fp = open('./sentences_data1/sentence.txt', "r",encoding="utf-8")
    line = fp.readline()
    k=0
    while line:
        line = fp.readline()
        if int(rank_line_list1[i]) == k:
            print('line '+ str(k) +' : '+str(rank_line_list2[i]) +' , '+ str(line))
        k+=1

    fp.close    
    