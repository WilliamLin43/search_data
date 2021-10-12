# -*- coding: utf-8 -*-
import plotly.express as px 
import pandas as pd 

def plot_data(filename):
    #print(filename)
    df = pd.read_csv(filename)    
    df_long=pd.melt(df, id_vars=['File Name'], value_vars=['Characters1(without \)', 'Characters2(without \ n)','Words1(re)','Words2(nltk)','Lines','Sentences','Keyword sentences mateches'])
    fig = px.line(df_long, x='File Name', y='value', color='variable')    
    fig.show()
    
if __name__ == '__main__':
    filename = 'Search_log_20211009114825.csv'
    plot_data(filename)