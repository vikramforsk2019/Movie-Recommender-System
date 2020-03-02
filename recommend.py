#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:39:38 2020

@author: jagveer
"""
import pandas as pd
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
path='file.tsv'
df = pd.read_csv(path, sep='\t', names=column_names) 
df.head()

movie_titles = pd.read_csv('Movie_Id_Titles.csv') 
movie_titles.head() 

data = pd.merge(df, movie_titles, on='item_id') 
data.head() 
