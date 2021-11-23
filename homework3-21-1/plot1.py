# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.manifold import TSNE
import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.text import Text
from gensim.models import Word2Vec
from nltk.stem import PorterStemmer
from mpl_toolkits.mplot3d.axes3d import Axes3D
import plotly.express as px
from nltk.corpus import stopwords


def plot_with_labels(low_dim_embs1, labels1,low_dim_embs2, labels2,low_dim_embs3, labels3,low_dim_embs4, labels4):

    rcParams['font.family'] = ['serif']
    rcParams['font.serif'] = ['Times New Roman']
    rcParams['axes.unicode_minus'] = False
    assert low_dim_embs1.shape[0] >= len(labels1), "More labels than embeddings"
    plt.figure(figsize=(18, 18))  # in inches
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


def plot_2D(list_words):
    NUMBER=2
    fp = pd.read_csv("./analysisdata2D.csv")#read csv lod data
    df=pd.DataFrame(fp)
    df2 = df.loc[df['ListWords'] == list_words[NUMBER]]    
    #fig = px.scatter(df, x="X", y="Y", size="Value",color="Value",hover_name="Words")
    print(df)
    fig = px.scatter(df, x="X", y="Y", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.update_layout(title={'text': "Key Word : "+str(list_words), 'y':0.95, 'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.show()

    fig = px.scatter(df, x="X", y="Y", text="Words", size="Value",color="ListWords",hover_name="Words")
    fig.update_traces(textposition="top center")
    fig.update_layout(title={'text': "Key Word : "+str(list_words), 'y':0.95, 'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.show()    
    
    fig = px.bar(df2, y="Model", x="Value", color="Words", orientation='h', text="Value")    
    fig.update_traces(textposition="inside")  # ['inside', 'outside', 'auto', 'none']
    fig.update_layout(title={'text': "Key Word : "+str(list_words[NUMBER]), 'y':0.95, 'x':0.5,'xanchor': 'center','yanchor': 'top'})    
    fig.show()
    


def plot_3D(list_words):
    
    NUMBER=0

    fp = pd.read_csv("./analysisdata3D.csv")#read csv lod data
    df=pd.DataFrame(fp)
    df2 = df.loc[df['Group'] == NUMBER]
    #print(df)

    fig = px.scatter_3d(df, x="X", y="Y", z="Z", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")    
    fig.update_layout(title={'text': "Key Word : "+str(list_words), 'y':0.95, 'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.show()
    
    fig = px.scatter_3d(df2, x="X", y="Y", z="Z", text="Words", size="Value",color="Model",hover_name="Words")
    fig.update_traces(textposition="top center")    
    fig.update_layout(title={'text': "Key Word : "+str(list_words[NUMBER]), 'y':0.95, 'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.show()
    

if __name__ == '__main__':
    MODEL1 = "covid_word2vec-cbow-trained.model"
    MODEL2 = "covid_word2vec-skipgram-trained.model"
    MODEL3 = "dysautonomia_word2vec-cbow-trained.model"
    MODEL4 = "dysautonomia_word2vec-skipgram-trained.model"
    MODEL5 = "dailymail_word2vec-cbow-trained.model"
    MODEL6 = "dailymail_word2vec-skipgram-trained.model"
    PRECISION = 4
    model1 = Word2Vec.load(MODEL1)
    model2 = Word2Vec.load(MODEL2)
    model3 = Word2Vec.load(MODEL3)
    model4 = Word2Vec.load(MODEL4)    
    model5 = Word2Vec.load(MODEL5)
    model6 = Word2Vec.load(MODEL6) 
    tempfile = '../dataset/keyword.txt'
    f = open(tempfile, 'r',encoding="utf-8")
    read_words = f.read()
    #read_words = read_words.replace('\n', '')
    stop_words = set(stopwords.words('english'))
    
    tokens = word_tokenize(read_words)
    list_words = [w for w in tokens if not w in stopwords.words('english')]
    
    ps = PorterStemmer()
    for i in range(len(list_words)):
        list_words[i] = ps.stem(list_words[i])

    
    print(list_words)

    
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
    tempvalue1 =[]
    tempvalue2 =[]
    tempvalue3 =[]
    tempvalue4 =[]
    tempvalue5 =[]
    tempvalue6 =[]
    value1 =[]
    value2 =[]
    value3 =[]
    value4 =[]
    value5 =[]
    value6 =[]
    embedding0 = np.array([])
    embedding1 = np.array([])
    embedding2 = np.array([])
    embedding3 = np.array([])
    embedding4 = np.array([])
    embedding5 = np.array([])
    embedding6 = np.array([])
    templist_words =[]
    templist_words_value = []
    words1 = list(model1.wv.key_to_index.keys())
    words2 = list(model2.wv.key_to_index.keys())
    words3 = list(model3.wv.key_to_index.keys())
    words4 = list(model4.wv.key_to_index.keys())
    words5 = list(model5.wv.key_to_index.keys())
    words6 = list(model6.wv.key_to_index.keys())
    
    for word in list_words:
            #for i in range(0, n):
                #print(model1.wv.most_similar(word, topn = n)[i][0])                  
            #templist_words.append(model3.wv.most_similar(word, topn = 1)[0][0])
            #templist_words_value.append(round((model3.wv.most_similar(word, topn = 1)[0][1]),PRECISION))
            templist_words_value.append(1)
            embedding0 = np.append(embedding0, model3.wv[word])
            
    #print(list_words)
    #print(templist_words_value)
    embedding0 = embedding0.reshape(len(list_words), vector_dim)
            
        #print(tempvocabs1)
        #print(tempvocabs2)
    n=5
    
    for word in list_words:
        if not word in stop_words:
            for i in range(0, n):
                #print(model1.wv.most_similar(word, topn = n)[i][0])                  
                tempvocabs1.append(model1.wv.most_similar(word, topn = n)[i][0])                  
                tempvocabs2.append(model2.wv.most_similar(word, topn = n)[i][0])                  
                tempvocabs3.append(model3.wv.most_similar(word, topn = n)[i][0])                
                tempvocabs4.append(model4.wv.most_similar(word, topn = n)[i][0])
                tempvocabs5.append(model5.wv.most_similar(word, topn = n)[i][0])
                tempvocabs6.append(model6.wv.most_similar(word, topn = n)[i][0])
                       
                tempvalue1.append(round(model1.wv.most_similar(word, topn = n)[i][1],PRECISION))
                tempvalue2.append(round(model2.wv.most_similar(word, topn = n)[i][1],PRECISION))
                tempvalue3.append(round(model3.wv.most_similar(word, topn = n)[i][1],PRECISION))
                tempvalue4.append(round(model4.wv.most_similar(word, topn = n)[i][1],PRECISION))
                tempvalue5.append(round(model5.wv.most_similar(word, topn = n)[i][1],PRECISION))
                tempvalue6.append(round(model6.wv.most_similar(word, topn = n)[i][1],PRECISION))
            
    k=0
    for word in tempvocabs1:
        if word in words1 and not word in vocabs1 and not word in stop_words:
            vocabs1.append(word)
            value1.append(tempvalue1[k])
            #print(word)
            #print(len(model1.wv[word]))
            embedding1 = np.append(embedding1, model1.wv[word])
            #print(embedding1)
        k+=1
    embedding1 = embedding1.reshape(len(vocabs1), vector_dim)
    #print(embedding1)
    k=0
    for word in tempvocabs2:
        if word in words2 and not word in vocabs2 and not word in stop_words:
            vocabs2.append(word)
            value2.append(tempvalue2[k])
            #print(word)
            #print(len(model.wv[word]))
            embedding2 = np.append(embedding2, model2.wv[word])
        k+=1
    embedding2 = embedding2.reshape(len(vocabs2), vector_dim)
    
    k=0
    for word in tempvocabs3:
        if word in words3 and not word in vocabs3 and not word in stop_words:
            vocabs3.append(word)
            value3.append(tempvalue3[k])
            #print(word)
            #print(len(model.wv[word]))
            embedding3 = np.append(embedding3, model3.wv[word])
        k+=1
    embedding3 = embedding3.reshape(len(vocabs3), vector_dim)
    
    k=0
    for word in tempvocabs4:
        if word in words4 and not word in vocabs4 and not word in stop_words:
            vocabs4.append(word)
            value4.append(tempvalue4[k])
            #print(word)
            #print(len(model.wv[word]))
            embedding4 = np.append(embedding4, model4.wv[word])
        k+=1
    embedding4 = embedding4.reshape(len(vocabs4), vector_dim)

    k=0
    for word in tempvocabs5:
        if word in words5 and not word in vocabs5 and not word in stop_words:
            vocabs5.append(word)
            value5.append(tempvalue5[k])
            #print(word)
            #print(len(model.wv[word]))
            embedding5 = np.append(embedding5, model5.wv[word])
        k+=1
    embedding5 = embedding5.reshape(len(vocabs5), vector_dim)

    k=0
    for word in tempvocabs6:
        if word in words6 and not word in vocabs6 and not word in stop_words:
            vocabs6.append(word)
            value6.append(tempvalue6[k])
            #print(word)
            #print(len(model.wv[word]))
            embedding6 = np.append(embedding6, model6.wv[word])
        k+=1
    embedding6 = embedding6.reshape(len(vocabs6), vector_dim)


    #降成3维
    tsne = TSNE(n_components=3,perplexity=5,n_iter=300,verbose=1,method='exact')
    low_dim_embedding0 = tsne.fit_transform(embedding0)
    low_dim_embedding1 = tsne.fit_transform(embedding1)
    low_dim_embedding2 = tsne.fit_transform(embedding2)
    low_dim_embedding3 = tsne.fit_transform(embedding3)
    low_dim_embedding4 = tsne.fit_transform(embedding4)
    low_dim_embedding5 = tsne.fit_transform(embedding5)
    low_dim_embedding6 = tsne.fit_transform(embedding6)
    print(low_dim_embedding0)
    
    fileprint1=open("./analysisdata3D.csv", "w",encoding="utf-8")    
    fileprint1.write("ListWord,Words,X,Y,Z,Group,Value,Model\n")
    
    for i in range(len(list_words)):
        fileprint1.write(str(list_words[i])+','+str(list_words[i])+','+str(low_dim_embedding0[i,0])+','+str(low_dim_embedding0[i,1])+','+str(low_dim_embedding0[i,2])+',-1,'+str(templist_words_value[i])+',Key_Words\n')
    
    group=5     
    for i in range(len(low_dim_embedding1[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs1[i])+','+ str(low_dim_embedding1[:,0][i])+','+ str(low_dim_embedding1[:,1][i])+','+ str(low_dim_embedding1[:,2][i])+','+ str(int(i/group))+','+str(value1[i])+','+str(MODEL1)+'\n')
        
    for i in range(len(low_dim_embedding2[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs2[i])+','+ str(low_dim_embedding2[:,0][i])+','+ str(low_dim_embedding2[:,1][i])+','+ str(low_dim_embedding2[:,2][i])+','+ str(int(i/group))+','+str(value2[i])+','+str(MODEL2)+'\n')

    for i in range(len(low_dim_embedding3[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs3[i])+','+ str(low_dim_embedding3[:,0][i])+','+ str(low_dim_embedding3[:,1][i])+','+ str(low_dim_embedding3[:,2][i])+','+ str(int(i/group))+','+str(value3[i])+','+str(MODEL3)+'\n')

    for i in range(len(low_dim_embedding4[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs4[i])+','+ str(low_dim_embedding4[:,0][i])+','+ str(low_dim_embedding4[:,1][i])+','+ str(low_dim_embedding4[:,2][i])+','+ str(int(i/group))+','+str(value4[i])+','+str(MODEL4)+'\n')
    
    for i in range(len(low_dim_embedding5[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs5[i])+','+ str(low_dim_embedding5[:,0][i])+','+ str(low_dim_embedding5[:,1][i])+','+ str(low_dim_embedding5[:,2][i])+','+ str(int(i/group))+','+str(value5[i])+','+str(MODEL5)+'\n')
    
    for i in range(len(low_dim_embedding6[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs6[i])+','+ str(low_dim_embedding6[:,0][i])+','+ str(low_dim_embedding6[:,1][i])+','+ str(low_dim_embedding6[:,2][i])+','+ str(int(i/group))+','+str(value6[i])+','+str(MODEL6)+'\n')
  
    plot_3D(list_words)

    #降成2维    
    tsne = TSNE(n_components=2,perplexity=5,n_iter=300,verbose=1,method='exact')
    low_dim_embedding0 = tsne.fit_transform(embedding0)
    low_dim_embedding1 = tsne.fit_transform(embedding1)
    low_dim_embedding2 = tsne.fit_transform(embedding2)
    low_dim_embedding3 = tsne.fit_transform(embedding3)
    low_dim_embedding4 = tsne.fit_transform(embedding4)
    low_dim_embedding5 = tsne.fit_transform(embedding5)
    low_dim_embedding6 = tsne.fit_transform(embedding6)
    #print(low_dim_embedding2)

    fileprint1=open("./analysisdata2D.csv", "w",encoding="utf-8")    
    fileprint1.write("ListWords,Words,X,Y,Group,Value,Model\n")

    for i in range(len(list_words)):
        fileprint1.write(str(list_words[i])+','+str(list_words[i])+','+str(low_dim_embedding0[i,0])+','+str(low_dim_embedding0[i,1])+',-1,'+str(templist_words_value[i])+',Key_Words\n')
   

    group=5    
    for i in range(len(low_dim_embedding1[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs1[i])+','+ str(low_dim_embedding1[:,0][i])+','+ str(low_dim_embedding1[:,1][i])+','+ str(int(i/group)) +','+ str(value1[i]) +',covid-19-cbow\n')

    for i in range(len(low_dim_embedding2[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs2[i])+','+ str(low_dim_embedding2[:,0][i])+','+ str(low_dim_embedding2[:,1][i])+','+ str(int(i/group)) +','+ str(value2[i]) +',covid-19-skipgram\n')

    for i in range(len(low_dim_embedding3[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs3[i])+','+ str(low_dim_embedding3[:,0][i])+','+ str(low_dim_embedding3[:,1][i])+','+ str(int(i/group)) +','+ str(value3[i]) +',dysautonomia-cbow\n')

    for i in range(len(low_dim_embedding4[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs4[i])+','+ str(low_dim_embedding4[:,0][i])+','+ str(low_dim_embedding4[:,1][i])+','+ str(int(i/group)) +','+ str(value4[i]) +',dysautonomia-skipgram\n')

    for i in range(len(low_dim_embedding5[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs5[i])+','+ str(low_dim_embedding5[:,0][i])+','+ str(low_dim_embedding5[:,1][i])+','+ str(int(i/group)) +','+ str(value5[i]) +',dailymail-cbow\n')

    for i in range(len(low_dim_embedding6[:,0])):
        fileprint1.write(str(list_words[int(i/group)])+','+str(vocabs6[i])+','+ str(low_dim_embedding6[:,0][i])+','+ str(low_dim_embedding6[:,1][i])+','+ str(int(i/group)) +','+ str(value6[i]) +',dailymail-skipgram\n')
        
        
    #time.sleep(1)
    plot_2D(list_words)    
    #plot_with_labels(low_dim_embedding1, vocabs1,low_dim_embedding2, vocabs2, low_dim_embedding3, vocabs3,low_dim_embedding4, vocabs4)
