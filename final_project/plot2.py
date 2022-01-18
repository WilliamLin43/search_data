# -*- coding: utf-8 -*-
import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.manifold import TSNE
from sklearn import manifold
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
import re




def plot_2D():
    
    fp = pd.read_csv("./analysisdata2D.csv",encoding="utf-8")#read csv lod data
    df=pd.DataFrame(fp)
    fig = px.scatter(df, x="X", y="Y", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.show()


def plot_3D():
    
    fp = pd.read_csv("./analysisdata3D.csv",encoding="utf-8")#read csv lod data
    df=pd.DataFrame(fp)
    fig = px.scatter_3d(df, x="X", y="Y", z="Z", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.show()

    


if __name__ == '__main__':

    #MODEL1 = "COVID-19_Endometriosis_word2vec-skipgram-trained.model"
    #MODEL2 = "COVID-19_MIS-C_word2vec-skipgram-trained.model"
    MODEL1 = "COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model"

    
    model1 = Word2Vec.load(MODEL1)
    #model2 = Word2Vec.load(MODEL2)
    #model3 = Word2Vec.load(MODEL3)

    stop_words = set(stopwords.words('english'))
    


    
    vector_dim = 100
    vocabs1 = []
    #vocabs2 = []
    #vocabs3 = []

    tempvocabs1 =[]
    #tempvocabs2 =[]
    #tempvocabs3 =[]

    embedding1 = np.array([])
    #embedding2 = np.array([])
    #embedding3 = np.array([])

    words1 = list(model1.wv.key_to_index.keys())
    #words2 = list(model2.wv.key_to_index.keys())
    #words3 = list(model3.wv.key_to_index.keys())

    
    for word in words1:
        if word in words1 and not word in vocabs1 and not word in stop_words:
            vocabs1.append(word)
            print(word)
            #print((model1.wv[word]))
            embedding1 = np.append(embedding1, model1.wv[word])
    embedding1 = embedding1.reshape(len(vocabs1), vector_dim)
    #print(embedding1)
    '''
    for word in words2:
        if word in words2 and not word in vocabs2 and not word in stop_words:
            vocabs2.append(word)
            print(word)
            #print(len(model.wv[word]))
            embedding2 = np.append(embedding2, model2.wv[word])
    embedding2 = embedding2.reshape(len(vocabs2), vector_dim)
    
    for word in words3:
        if word in words3 and not word in vocabs3 and not word in stop_words:
            vocabs3.append(word)
            print(word)
            #print(len(model.wv[word]))
            embedding3 = np.append(embedding3, model3.wv[word])
    embedding3 = embedding3.reshape(len(vocabs3), vector_dim)    
    '''
    #降维
    tsne = TSNE(n_components=3,perplexity=5,n_iter=300,verbose=1,method='exact',init='random')
    low_dim_embedding1 = tsne.fit_transform(embedding1)
    #low_dim_embedding2 = tsne.fit_transform(embedding2)
    #low_dim_embedding3 = tsne.fit_transform(embedding3)
    
    #mds=manifold.MDS(n_components=3)
    #low_dim_embedding1 = mds.fit_transform(embedding1)
    #low_dim_embedding2 = mds.fit_transform(embedding2)

    fileprint1=open("./analysisdata3D.csv", "w",encoding="utf-8")    
    fileprint1.write("Words,X,Y,Z,Group,Value,Model\n")
    
    group=5     
    for i in range(len(low_dim_embedding1[:,0])):
        fileprint1.write(str(vocabs1[i])+','+ str(low_dim_embedding1[:,0][i])+','+ str(low_dim_embedding1[:,1][i])+','+ str(low_dim_embedding1[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL1)+'\n')
        
    #for i in range(len(low_dim_embedding2[:,0])):
    #    fileprint1.write(str(vocabs2[i])+','+ str(low_dim_embedding2[:,0][i])+','+ str(low_dim_embedding2[:,1][i])+','+ str(low_dim_embedding2[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL2)+'\n')
    
    #for i in range(len(low_dim_embedding3[:,0])):
    #    fileprint1.write(str(vocabs3[i])+','+ str(low_dim_embedding3[:,0][i])+','+ str(low_dim_embedding3[:,1][i])+','+ str(low_dim_embedding3[:,2][i])+','+ str(int(i/group))+',1,'+str(MODEL3)+'\n')

    #plot_3D()
    

       
    tsne = TSNE(n_components=2,perplexity=5,n_iter=300,verbose=1,method='exact',init='random')
    low_dim_embedding1 = tsne.fit_transform(embedding1)
    #low_dim_embedding2 = tsne.fit_transform(embedding2)
    #low_dim_embedding3 = tsne.fit_transform(embedding3)

        #mds=manifold.MDS(n_components=2)
    #print('low_dim_embedding1')
    #low_dim_embedding1 = mds.fit_transform(embedding1)
    #low_dim_embedding2 = mds.fit_transform(embedding2)

    print('write csv file')
    fileprint1=open("./analysisdata2D.csv", "w",encoding="utf-8")    
    fileprint1.write("Words,X,Y,Group,Value,Model\n")


    group=5     
    for i in range(len(low_dim_embedding1[:,0])):
        fileprint1.write(str(vocabs1[i])+','+ str(low_dim_embedding1[:,0][i])+','+ str(low_dim_embedding1[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL1)+'\n')
    
    #for i in range(len(low_dim_embedding2[:,0])):
    #    fileprint1.write(str(vocabs2[i])+','+ str(low_dim_embedding2[:,0][i])+','+ str(low_dim_embedding2[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL2)+'\n')
    
    #for i in range(len(low_dim_embedding3[:,0])):
    #    fileprint1.write(str(vocabs3[i])+','+ str(low_dim_embedding3[:,0][i])+','+ str(low_dim_embedding3[:,1][i])+','+  str(int(i/group))+',1,'+str(MODEL3)+'\n')


    plot_2D()
    