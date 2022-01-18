# -*- coding: utf-8 -*-
#KMeans
import os,sys
import nltk
import re
import math
import numpy as np
import matplotlib.pyplot as plt
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from gensim.models import word2vec
#from sklearn.decomposition import PCA
#from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib
from mpl_toolkits import mplot3d

def find_KMeans(top):

    models = word2vec.Word2Vec.load('COVID-19_MIS-C_Endometriosis_word2vec-skipgram-trained.model')
    #print(models.wv['endometriosis'].shape)
    #print(models.wv.most_similar(key,topn=top))
    print("【顯示詞語】")
    #print(models.wv.index_to_key)
    key=models.wv.index_to_key
    print(key[0:top])
    # 显示词向量矩阵
    #print("【词向量矩阵】")
    #vectors = models.wv.vectors
    # 提取词向量
    #vectors = [models.wv[word] for word in models.wv.index_to_key]
    vectors = [models.wv[word] for word in key[:]]
    #print(len(model.wv.index2word))
    #print(vectors)
    #print(vectors.shape)
    # 显示四个词语最相关的相似度
    '''print("【词向量相似度】")
    for i in range(top):
        print(models.wv.similar_by_vector(vectors[i]))'''
    # 基于KMeans聚类
    labels = KMeans(n_clusters=3).fit(vectors).labels_
    #print(labels)
    
    matplotlib.rcParams['axes.unicode_minus'] = False    # 显示负号
    fig = plt.figure()
    ax = mplot3d.Axes3D(fig)                             # 创建3d坐标轴
    colors = ['red', 'blue', 'green']
    # 绘制散点图 词语 词向量 类标(颜色)
    for word, vector, label in zip(key[0:top], vectors, labels):
        ax.scatter(vector[0], vector[1], vector[2], c=colors[label], s=500, alpha=0.4)
        ax.text(vector[0], vector[1], vector[2], word, ha='center', va='center')
        #adjustText.adjust_text(texts)  
    plt.show() 
    
if __name__ == '__main__':
    top =30
    find_KMeans(top)