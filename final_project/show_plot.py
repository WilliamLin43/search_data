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




def plot_2D(Words_List1,Words_List2,Words_List3,Words_List4,keyword):
    
    fp = pd.read_csv("./analysisdata2D.csv",encoding="utf-8")#read csv lod data
    #fp = pd.read_csv("./analysisdata2D-cbow-w5-e1200-5000.csv",encoding="utf-8")#read csv lod data
    #fp = pd.read_csv("./analysisdata2D-cbow-w5-e1200-5000-mix.csv",encoding="utf-8")#read csv lod data
    df=pd.DataFrame(fp)
    #x=df["X"]
    #y=df["Y"]
    Words=df["Words"]
    #Value=df["Model"]
    #Group=df["Group"]
    #print(Group)
    for i in range(len(Words)):    
        if Words[i] in Words_List1 and df.loc[i,'Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model':               
            df=df.append({'Words' : df.loc[i,'Words'] , 'X' : df.loc[i,'X'], 'Y' : df.loc[i,'Y'],'Group' : df.loc[i,'Group'],'Value' : 3,'Model' : keyword[0]} , ignore_index=True)
        if Words[i] in Words_List2 and df.loc[i,'Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model':               
            df=df.append({'Words' : df.loc[i,'Words'] , 'X' : df.loc[i,'X'], 'Y' : df.loc[i,'Y'],'Group' : df.loc[i,'Group'],'Value' : 3,'Model' : keyword[1]} , ignore_index=True)
        if Words[i] in Words_List3 and df.loc[i,'Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model':               
            df=df.append({'Words' : df.loc[i,'Words'] , 'X' : df.loc[i,'X'], 'Y' : df.loc[i,'Y'],'Group' : df.loc[i,'Group'],'Value' : 3,'Model' : keyword[2]} , ignore_index=True)
        if Words[i] in Words_List4 and df.loc[i,'Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model':               
            df=df.append({'Words' : df.loc[i,'Words'] , 'X' : df.loc[i,'X'], 'Y' : df.loc[i,'Y'],'Group' : df.loc[i,'Group'],'Value' : 3,'Model' : keyword[3]} , ignore_index=True)
                
            
    #df2 = df.loc[df['Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model']
    #fig = px.scatter(df, x="X", y="Y", size="Value",color="Value",hover_name="Words")
    #print(df2)
    #fig = px.scatter(df2.sort_values(by=['Value']), x="X", y="Y", size="Value",color="Group",hover_name="Words")
    fig = px.scatter(df, x="X", y="Y", size="Value",color="Model",hover_name="Words")
    #fig.update_traces(textposition="top center")
    fig.show()
    
    #fig = px.scatter(df2, x="X", y="Y", text="Words", size="Value",color="Model",hover_name="Words")
    #fig.update_traces(textposition="top center")
    #fig.show()
    

def plot_3D(Words_List1,Words_List2,Words_List3,Words_List4,keyword):
    
    fp = pd.read_csv("./analysisdata3D.csv",encoding="utf-8")#read csv lod data
    #fp = pd.read_csv("./analysisdata3D-cbow-w5-e1200-5000.csv",encoding="utf-8")#read csv lod data
    #fp = pd.read_csv("./analysisdata3D-skipgram-w5-e1200-5000-mix.csv",encoding="utf-8")#read csv lod data
    df=pd.DataFrame(fp)
    #df2 = df.loc[df['Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model']
    Words=df["Words"]
    for i in range(len(Words)):    
        if Words[i] in Words_List1 and df.loc[i,'Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model':               
            df=df.append({'Words' : df.loc[i,'Words'] , 'X' : df.loc[i,'X'], 'Y' : df.loc[i,'Y'], 'Z' : df.loc[i,'Z'],'Group' : df.loc[i,'Group'],'Value' : 3,'Model' : keyword[0]} , ignore_index=True)
        if Words[i] in Words_List2 and df.loc[i,'Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model':               
            df=df.append({'Words' : df.loc[i,'Words'] , 'X' : df.loc[i,'X'], 'Y' : df.loc[i,'Y'], 'Z' : df.loc[i,'Z'],'Group' : df.loc[i,'Group'],'Value' : 3,'Model' : keyword[1]} , ignore_index=True)
        if Words[i] in Words_List3 and df.loc[i,'Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model':               
            df=df.append({'Words' : df.loc[i,'Words'] , 'X' : df.loc[i,'X'], 'Y' : df.loc[i,'Y'], 'Z' : df.loc[i,'Z'],'Group' : df.loc[i,'Group'],'Value' : 3,'Model' : keyword[2]} , ignore_index=True)
        if Words[i] in Words_List4 and df.loc[i,'Model'] == 'COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model':               
            df=df.append({'Words' : df.loc[i,'Words'] , 'X' : df.loc[i,'X'], 'Y' : df.loc[i,'Y'], 'Z' : df.loc[i,'Z'],'Group' : df.loc[i,'Group'],'Value' : 3,'Model' : keyword[3]} , ignore_index=True)
   

    #fig = px.scatter_3d(df2.sort_values(by=['Value']), x="X", y="Y", z="Z", size="Value",color="Group",hover_name="Words")
    fig = px.scatter_3d(df, x="X", y="Y", z="Z", size="Value",color="Model",hover_name="Words")
    #fig.update_traces(textposition="top center")
    fig.show()

    #fig = px.scatter_3d(df2, x="X", y="Y", z="Z", text="Words", size="Value",color="Model",hover_name="Words")
    #fig.update_traces(textposition="top center")
    #fig.show()
    


if __name__ == '__main__':
    
    f = open('./word2vec_covid-19.txt', 'r',encoding="utf-8")
    read_words = f.read()
    read_words1 = read_words.encode('utf-8').decode('utf-8')    
    read_words1 = re.sub(r'^\w\s',' ',str(read_words))
    Words_List1=word_tokenize(read_words1.lower())#變小寫

    f = open('./word2vec_mis-c.txt', 'r',encoding="utf-8")
    read_words = f.read()
    read_words1 = read_words.encode('utf-8').decode('utf-8')    
    read_words1 = re.sub(r'^\w\s',' ',str(read_words))
    Words_List2=word_tokenize(read_words1.lower())#變小寫

    f = open('./word2vec_endometriosis.txt', 'r',encoding="utf-8")
    read_words = f.read()
    read_words1 = read_words.encode('utf-8').decode('utf-8')    
    read_words1 = re.sub(r'^\w\s',' ',str(read_words))
    Words_List3=word_tokenize(read_words1.lower())#變小寫    

    f = open('./word2vec_sars-cov-2.txt', 'r',encoding="utf-8")
    read_words = f.read()
    read_words1 = read_words.encode('utf-8').decode('utf-8')    
    read_words1 = re.sub(r'^\w\s',' ',str(read_words))
    Words_List4=word_tokenize(read_words1.lower())#變小寫    
    
    keyword =['COVID-19','MIS-C','Endometriosis','SARS-COV-2']
    
    plot_2D(Words_List1,Words_List2,Words_List3,Words_List4,keyword)
    plot_3D(Words_List1,Words_List2,Words_List3,Words_List4,keyword)    
   