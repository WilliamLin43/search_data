# -*- coding: utf-8 -*-
import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.manifold import TSNE
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from gensim.models import Word2Vec
from nltk.stem import PorterStemmer
from mpl_toolkits.mplot3d.axes3d import Axes3D
import plotly.express as px



def plot_with_labels(low_dim_embs1, labels1,low_dim_embs2, labels2,low_dim_embs3, labels3,low_dim_embs4, labels4):

    rcParams['font.family'] = ['serif']
    rcParams['font.serif'] = ['Times New Roman']
    rcParams['axes.unicode_minus'] = False
    assert low_dim_embs1.shape[0] >= len(labels1), "More labels than embeddings"
    plt.figure(figsize=(18, 18))  # in inches
    show_word = 5
    labels1 = labels1[:show_word]
    labels2 = labels2[:show_word]
    labels3 = labels3[:show_word]
    labels4 = labels4[:show_word]
    for i, label in enumerate(labels1):
        x, y = low_dim_embs1[i, :]
        plt.scatter(x, y,c="yellow")
        plt.annotate(label,
                 xy=(x, y),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')
    for i, label in enumerate(labels2):
        x, y = low_dim_embs2[i, :]
        plt.scatter(x, y,c="green")
        plt.annotate(label,
                 xy=(x, y),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')

    for i, label in enumerate(labels3):
        x, y = low_dim_embs3[i, :]
        plt.scatter(x, y,c="blue")
        plt.annotate(label,
                 xy=(x, y),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')

    for i, label in enumerate(labels4):
        x, y = low_dim_embs4[i, :]
        plt.scatter(x, y,c="red")
        plt.annotate(label,
                 xy=(x, y),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')


    plt.show()


def plot_2D():
    
    fp = pd.read_csv("./analysisdata2D.csv",encoding="utf-8")#read csv lod data
    df=pd.DataFrame(fp)
    df2 = df.loc[df['Group'] == 1]
    #fig = px.scatter(df, x="X", y="Y", size="Value",color="Value",hover_name="Words")
    #print(df2)
    fig = px.scatter(df, x="X", y="Y", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.show()
    
    fig = px.scatter(df2, x="X", y="Y", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.show()
    

def plot_3D():
    
    fp = pd.read_csv("./analysisdata3D.csv",encoding="utf-8")#read csv lod data
    df=pd.DataFrame(fp)
    df2 = df.loc[df['Group'] == 1]

    fig = px.scatter_3d(df, x="X", y="Y", z="Z", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.show()

    fig = px.scatter_3d(df2, x="X", y="Y", z="Z", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.show()
    


if __name__ == '__main__':
    MODEL1 = "covid_word2vec-cbow-trained.model"
    MODEL2 = "covid_word2vec-skipgram-trained.model"
    MODEL3 = "dysautonomia_word2vec-cbow-trained.model"
    MODEL4 = "dysautonomia_word2vec-skipgram-trained.model"
    MODEL5 = "dailymail_word2vec-cbow-trained.model"
    MODEL6 = "dailymail_word2vec-skipgram-trained.model"
    
    model1 = Word2Vec.load(MODEL1)
    model2 = Word2Vec.load(MODEL2)
    model3 = Word2Vec.load(MODEL3)
    model4 = Word2Vec.load(MODEL4)    
    model5 = Word2Vec.load(MODEL5)
    model6 = Word2Vec.load(MODEL6) 
    tempfile = '../dataset/dailymail_50_sentence.txt'
    f = open(tempfile, 'r')
    read_words = f.read()
    #read_words = read_words.replace('\n', '')
    #list_words = word_tokenize(read_words)
    #print(list_words)
    stop_words = set(stopwords.words('english'))
    
    tokens = word_tokenize(read_words)
    list_words = [w for w in tokens if not w in stopwords.words('english')]
    
    ps = PorterStemmer()
    for i in range(len(list_words)):
        list_words[i] = ps.stem(list_words[i])
        if list_words[i] in ['-','－','?','(',')','%','[',']','+','``','"','--','*','&','.','..','#','@','`','~','{','}','$','@','!']:
                     list_words[i] = ''
        #去除特殊符號字元
        list_words[i] = list_words[i].replace('~','')
        list_words[i] = list_words[i].replace(',','')
        list_words[i] = list_words[i].replace('!','')
        list_words[i] = list_words[i].replace('@','')
        list_words[i] = list_words[i].replace('#','')
        list_words[i] = list_words[i].replace('$','')
        list_words[i] = list_words[i].replace('%','')
        list_words[i] = list_words[i].replace('^','')
        list_words[i] = list_words[i].replace('&','')
        list_words[i] = list_words[i].replace('*','')
        list_words[i] = list_words[i].replace('(','')
        list_words[i] = list_words[i].replace(')','')
        list_words[i] = list_words[i].replace('!','')
        list_words[i] = list_words[i].replace(':','')
        list_words[i] = list_words[i].replace('+','')
        list_words[i] = list_words[i].replace('=','')
        list_words[i] = list_words[i].replace('=-','')
        list_words[i] = list_words[i].replace(',','')
        list_words[i] = list_words[i].replace("'",'')
        list_words[i] = list_words[i].replace("'s",'')
        list_words[i] = list_words[i].replace('\n','')
        list_words[i] = list_words[i].replace(' ','')
    
    list_words2 =[]
    for i in range(len(list_words)):
        if list_words[i] != '':
            list_words2.append(list_words[i]) 
            
    
    print(list_words2)
    
    vector_dim = 100
    vocabs1 = []
    vocabs2 = []
    vocabs3 = []
    vocabs4 = []
    vocabs5 = []
    vocabs6 = []
    tempvocabs1 =[]
    tempvocabs2 =[]
    tempvocabs3 =[]
    tempvocabs4 =[]
    tempvocabs5 =[]
    tempvocabs6 =[]
    embedding1 = np.array([])
    embedding2 = np.array([])
    embedding3 = np.array([])
    embedding4 = np.array([])
    embedding5 = np.array([])
    embedding6 = np.array([])
    words1 = list(model1.wv.key_to_index.keys())
    words2 = list(model2.wv.key_to_index.keys())
    words3 = list(model3.wv.key_to_index.keys())
    words4 = list(model4.wv.key_to_index.keys())
    words5 = list(model5.wv.key_to_index.keys())
    words6 = list(model6.wv.key_to_index.keys())    

    for word in list_words2:
        if word in words1 and not word in vocabs1 and not word in stop_words:
            vocabs1.append(word)
            #print(word)
            #print(len(model1.wv[word]))
            embedding1 = np.append(embedding1, model1.wv[word])
    embedding1 = embedding1.reshape(len(vocabs1), vector_dim)
    #print(embedding1)

    for word in list_words2:
        if word in words2 and not word in vocabs2 and not word in stop_words:
            vocabs2.append(word)
            #print(word)
            #print(len(model.wv[word]))
            embedding2 = np.append(embedding2, model2.wv[word])
    embedding2 = embedding2.reshape(len(vocabs2), vector_dim)

    for word in list_words2:
        if word in words3 and not word in vocabs3 and not word in stop_words:
            vocabs3.append(word)
            #print(word)
            #print(len(model.wv[word]))
            embedding3 = np.append(embedding3, model3.wv[word])
    embedding3 = embedding3.reshape(len(vocabs3), vector_dim)

    for word in list_words2:
        if word in words4 and not word in vocabs4 and not word in stop_words:
            vocabs4.append(word)
            #print(word)
            #print(len(model.wv[word]))
            embedding4 = np.append(embedding4, model4.wv[word])
    embedding4 = embedding4.reshape(len(vocabs4), vector_dim)


    for word in list_words2:
        if word in words5 and not word in vocabs5 and not word in stop_words:
            vocabs5.append(word)
            #print(word)
            #print(len(model.wv[word]))
            embedding5 = np.append(embedding5, model5.wv[word])
    embedding5 = embedding5.reshape(len(vocabs5), vector_dim)

    for word in list_words2:
        if word in words6 and not word in vocabs6 and not word in stop_words:
            vocabs6.append(word)
            #print(word)
            #print(len(model.wv[word]))
            embedding6 = np.append(embedding6, model6.wv[word])
    embedding6 = embedding6.reshape(len(vocabs6), vector_dim)

    #降维
    tsne = TSNE(n_components=3,perplexity=5,n_iter=300,verbose=1,method='exact',init='random')
    low_dim_embedding1 = tsne.fit_transform(embedding1)
    low_dim_embedding2 = tsne.fit_transform(embedding2)
    low_dim_embedding3 = tsne.fit_transform(embedding3)
    low_dim_embedding4 = tsne.fit_transform(embedding4)
    low_dim_embedding5 = tsne.fit_transform(embedding5)
    low_dim_embedding6 = tsne.fit_transform(embedding6)

    fileprint1=open("./analysisdata3D.csv", "w",encoding="utf-8")    
    fileprint1.write("Words,X,Y,Z,Group,Value,Model\n")
    
    group=5     
    for i in range(len(low_dim_embedding1[:,0])):
        fileprint1.write(str(vocabs1[i])+','+ str(low_dim_embedding1[:,0][i])+','+ str(low_dim_embedding1[:,1][i])+','+ str(low_dim_embedding1[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL1)+'\n')
        
    for i in range(len(low_dim_embedding2[:,0])):
        fileprint1.write(str(vocabs2[i])+','+ str(low_dim_embedding2[:,0][i])+','+ str(low_dim_embedding2[:,1][i])+','+ str(low_dim_embedding2[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL2)+'\n')

    for i in range(len(low_dim_embedding3[:,0])):
        fileprint1.write(str(vocabs3[i])+','+ str(low_dim_embedding3[:,0][i])+','+ str(low_dim_embedding3[:,1][i])+','+ str(low_dim_embedding3[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL3)+'\n')

    for i in range(len(low_dim_embedding4[:,0])):
        fileprint1.write(str(vocabs4[i])+','+ str(low_dim_embedding4[:,0][i])+','+ str(low_dim_embedding4[:,1][i])+','+ str(low_dim_embedding4[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL4)+'\n')
    
    for i in range(len(low_dim_embedding5[:,0])):
        fileprint1.write(str(vocabs5[i])+','+ str(low_dim_embedding5[:,0][i])+','+ str(low_dim_embedding5[:,1][i])+','+ str(low_dim_embedding5[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL5)+'\n')
    
    for i in range(len(low_dim_embedding6[:,0])):
        fileprint1.write(str(vocabs6[i])+','+ str(low_dim_embedding6[:,0][i])+','+ str(low_dim_embedding6[:,1][i])+','+ str(low_dim_embedding6[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL6)+'\n')

    plot_3D()

        
    tsne = TSNE(n_components=2,perplexity=5,n_iter=300,verbose=1,method='exact',init='random')
    low_dim_embedding1 = tsne.fit_transform(embedding1)
    low_dim_embedding2 = tsne.fit_transform(embedding2)
    low_dim_embedding3 = tsne.fit_transform(embedding3)
    low_dim_embedding4 = tsne.fit_transform(embedding4)
    low_dim_embedding5 = tsne.fit_transform(embedding5)
    low_dim_embedding6 = tsne.fit_transform(embedding6)

    fileprint1=open("./analysisdata2D.csv", "w",encoding="utf-8")    
    fileprint1.write("Words,X,Y,Group,Value,Model\n")


    group=5     
    for i in range(len(low_dim_embedding1[:,0])):
        fileprint1.write(str(vocabs1[i])+','+ str(low_dim_embedding1[:,0][i])+','+ str(low_dim_embedding1[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL1)+'\n')
        
    for i in range(len(low_dim_embedding2[:,0])):
        fileprint1.write(str(vocabs2[i])+','+ str(low_dim_embedding2[:,0][i])+','+ str(low_dim_embedding2[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL2)+'\n')

    for i in range(len(low_dim_embedding3[:,0])):
        fileprint1.write(str(vocabs3[i])+','+ str(low_dim_embedding3[:,0][i])+','+ str(low_dim_embedding3[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL3)+'\n')

    for i in range(len(low_dim_embedding4[:,0])):
        fileprint1.write(str(vocabs4[i])+','+ str(low_dim_embedding4[:,0][i])+','+ str(low_dim_embedding4[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL4)+'\n')
    
    for i in range(len(low_dim_embedding5[:,0])):
        fileprint1.write(str(vocabs5[i])+','+ str(low_dim_embedding5[:,0][i])+','+ str(low_dim_embedding5[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL5)+'\n')
    
    for i in range(len(low_dim_embedding6[:,0])):
        fileprint1.write(str(vocabs6[i])+','+ str(low_dim_embedding6[:,0][i])+','+ str(low_dim_embedding6[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL6)+'\n')


    plot_2D()    
    #plot_with_labels(low_dim_embedding1, vocabs1,low_dim_embedding2, vocabs2, low_dim_embedding3, vocabs3,low_dim_embedding4, vocabs4)
