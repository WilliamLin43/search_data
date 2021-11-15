# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.manifold import TSNE
import nltk
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from gensim.models import Word2Vec

from mpl_toolkits.mplot3d.axes3d import Axes3D
import plotly.express as px
from nltk.corpus import stopwords


def plot_with_labels(low_dim_embs, labels, filename='tsne.pdf'):

    rcParams['font.family'] = ['serif']
    rcParams['font.serif'] = ['Times New Roman']
    rcParams['axes.unicode_minus'] = False
    assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
    plt.figure(figsize=(18, 18))  # in inches
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(label,
                 xy=(x, y),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')
    plt.show()
    plt.savefig(filename)


def plot_2D(low_dim_embs, labels):
    x= low_dim_embs[:,0]
    y= low_dim_embs[:,1]
    
    fileprint=open("./analysisdata2D.csv", "w",encoding="utf-8")    
    fileprint.write("Words,X,Y,Value\n")
        
    for i in range(len(x)):
        fileprint.write(str(labels[i])+','+ str(x[i])+','+ str(y[i])+',1\n')
    
    fp = pd.read_csv("./analysisdata2D.csv")#read csv lod data
    df=pd.DataFrame(fp)    
    
    fig = px.scatter(df, x="X", y="Y", size="Value",color="Words",hover_name="Words")
    fig.show()
    


def plot_3D(low_dim_embs, labels):
    x= low_dim_embs[:,0]
    y= low_dim_embs[:,1]
    z= low_dim_embs[:,2]   
    

    fileprint=open("./analysisdata3D.csv", "w",encoding="utf-8")    
    fileprint.write("Words,X,Y,Z,Value\n")
        
    for i in range(len(x)):
        fileprint.write(str(labels[i])+','+ str(x[i])+','+ str(y[i])+','+ str(z[i])+',1\n')
    
    fp = pd.read_csv("./analysisdata3D.csv")#read csv lod data
    df=pd.DataFrame(fp)    
    
    fig = px.scatter_3d(df, x="X", y="Y", z="Z", size="Value",color="Words",hover_name="Words")
    fig.show()

    
    #value = np.ones((1,len(x)), dtype=int)
    
    # 製作figure
    #fig = plt.figure()
    #ax = Axes3D(fig)
    
    # 製作 color map
    #color_map = plt.cm.get_cmap()
    
    # 設定ax為散佈圖，製作color bar

    #map = ax.scatter(x, y, z, c =value, cmap=color_map)
    #fig.colorbar(map, ax = ax)
    
    

    
    #plt.show()
    

if __name__ == '__main__':
    #MODEL = "covid_word2vec-cbow-trained.model"
    #MODEL = "covid_word2vec-skipgram-trained.model"
    MODEL = "dysautonomia_word2vec-cbow-trained.model"
    #MODEL = "dysautonomia_word2vec-skipgram-trained.model"
    
    model = Word2Vec.load(MODEL)    
    tempfile = '../dataset/keyword2.txt'
    f = open(tempfile, 'r',encoding="utf-8")
    read_words = f.read()
    #read_words = read_words.replace('\n', '')
    list_words = word_tokenize(read_words)
    
    stop_words = set(stopwords.words('english'))
    
    vector_dim = 100
    vocabs = []
    embedding = np.array([])
    words = list(model.wv.key_to_index.keys())
    
    for word in list_words:
        if word in words and not word in vocabs and not word in stop_words:
            vocabs.append(word)
            #print(word)
            #print(len(model.wv[word]))
            embedding = np.append(embedding, model.wv[word])
    embedding = embedding.reshape(len(vocabs), vector_dim)

    #降维
    #tsne = TSNE(n_components=2,perplexity=1,n_iter=250,init='pca',verbose=1,method='exact')
    #low_dim_embedding = tsne.fit_transform(embedding)
    
    #plot_with_labels(low_dim_embedding, vocabs)
    
    tsne = TSNE(n_components=2,perplexity=1,n_iter=250,init='pca',verbose=1,method='exact')
    low_dim_embedding = tsne.fit_transform(embedding)
    print(low_dim_embedding)
    plot_2D(low_dim_embedding, vocabs)    
    

    tsne = TSNE(n_components=3,perplexity=1,n_iter=250,init='pca',verbose=1,method='exact')
    low_dim_embedding = tsne.fit_transform(embedding)
    print(low_dim_embedding)
    plot_3D(low_dim_embedding, vocabs)
        
