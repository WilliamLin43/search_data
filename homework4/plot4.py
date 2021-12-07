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




def plot_2D(Words_List):
    
    #fp = pd.read_csv("./analysisdata2D-skipgram-w5-e1200-5000.csv",encoding="utf-8")#read csv lod data
    fp = pd.read_csv("./analysisdata2D-cbow-w5-e1200-5000.csv",encoding="utf-8")#read csv lod data
    #fp = pd.read_csv("./analysisdata2D-cbow-w5-e1200-5000-mix.csv",encoding="utf-8")#read csv lod data
    df=pd.DataFrame(fp)
    #x=df["X"]
    #y=df["Y"]
    Words=df["Words"]
    #Value=df["Model"]
    #Group=df["Group"]
    #print(Group)
    
    for i in range(len(Words)):
        #print(Words[i])        
        if Words[i] in Words_List:                
            df.loc[i,'Group'] = 'Keyword'
            df.loc[i,'Value'] = 3
        else:
            df.loc[i,'Group'] = 'Words'
            

    #df2 = df.loc[df['Group'] < 5]
    #fig = px.scatter(df, x="X", y="Y", size="Value",color="Value",hover_name="Words")
    #print(df2)
    fig = px.scatter(df, x="X", y="Y", text="Words", size="Value",color="Group",hover_name="Words")
    #fig = px.scatter(df, x="X", y="Y", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.show()
    
    #fig = px.scatter(df2, x="X", y="Y", text="Words", size="Value",color="Model",hover_name="Words")
    #fig.update_traces(textposition="top center")
    #fig.show()
    

def plot_3D(Words_List):
    
    #fp = pd.read_csv("./analysisdata3D-skipgram-w5-e1200-5000.csv",encoding="utf-8")#read csv lod data
    fp = pd.read_csv("./analysisdata3D-cbow-w5-e1200-5000.csv",encoding="utf-8")#read csv lod data
    #fp = pd.read_csv("./analysisdata3D-skipgram-w5-e1200-5000-mix.csv",encoding="utf-8")#read csv lod data
    df=pd.DataFrame(fp)
    #df2 = df.loc[df['Group'] < 5]
    Words=df["Words"]
    for i in range(len(Words)):
        #print(Words[i])        
        if Words[i] in Words_List:                
            df.loc[i,'Group'] = 'Keyword'
            df.loc[i,'Value'] = 3
        else:
            df.loc[i,'Group'] = 'Words'

    fig = px.scatter_3d(df, x="X", y="Y", z="Z", text="Words", size="Value",color="Group",hover_name="Words")
    #fig = px.scatter_3d(df, x="X", y="Y", z="Z", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.show()

    #fig = px.scatter_3d(df2, x="X", y="Y", z="Z", text="Words", size="Value",color="Model",hover_name="Words")
    #fig.update_traces(textposition="top center")
    #fig.show()
    


if __name__ == '__main__':
    
    f = open('./sentences_data/keyword_tf_top20.txt', 'r',encoding="utf-8")
    read_words = f.read()
    read_words1= re.sub(r'[^\w\s]','',read_words.replace('/', ' '))
    Words_List=word_tokenize(read_words1.lower())#變小寫

    
    plot_3D(Words_List)
    plot_2D(Words_List)    
    #plot_with_labels(low_dim_embedding1, vocabs1,low_dim_embedding2, vocabs2, low_dim_embedding3, vocabs3,low_dim_embedding4, vocabs4)
