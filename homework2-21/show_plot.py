# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 

def plot_zipf(filename,ststus,keyword,Rank1,Rank2):

    #filename = 'P1000_analysisdata_20211022155408.csv'
    
    fp = pd.read_csv(filename)#read csv lod data
    df=pd.DataFrame(fp)
    df.sort_values(by=['Frequency'], ascending=False, inplace=True)
    
    print(df)
    
    #df2 = df.head(5000)
    df2 = df[Rank1:Rank2]
    Words_rank = df2["Words"]
    Words_Frequency = df2["Frequency"] 
    
    '''
    df_long=pd.melt(df2, id_vars=['Words'], value_vars=['Frequency'])
    fig = px.line(df_long, x=Words_rank, y=Words_Frequency, color='variable', labels={"y":"Number of Word Frequency","x":"Words Rank"}, title=str(keyword) +" " + str(filename[35:-4]) + " Documents Zipf Distribution Rank:"+ str(Rank1) +"-" +str(Rank2))    
    
    fig.show()    
    '''
    
    y = np.tile(Words_Frequency,len(Words_rank))
    
    trace_bar = go.Bar(x=Words_rank, y=y, marker=dict(color="blue", opacity=0.8), name="Frequency Bar")
    trace_average = go.Scatter(x=Words_rank, y=y, mode="lines", name="Frequency")
    data = [trace_bar, trace_average]
    layout = go.Layout(title=str(filename[26:-4]) + " Documents "+ str(ststus) +" Zipf Distribution Rank:"+ str(Rank1) +"-" +str(Rank2), xaxis=dict(title="Words Rank"),yaxis=dict(title="Number of Word Frequency"))
    fig2 = go.Figure(data=data, layout=layout)
    fig2.show()
    
    
    


if __name__ == '__main__':
    filename = './SP_Data/analysisdata_SP_COVID-19_100.csv'
    keyword = 'COVID-19'
    Rank1=0
    Rank2=5000
    ststus='with Stopword & Porter’s algorithm'
    plot_zipf(filename,keyword,Rank1,Rank2)