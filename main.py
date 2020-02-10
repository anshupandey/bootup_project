# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 04:13:42 2020

@author: anshu
"""

import pandas as pd
import os
from bootup_plot import generate_barplot

def main(all_subjects):
    domains=['Python Programming', 'Data Science', 'Machine Learning',"Deep Learning", "NLP"]

    all_headers = ['basic_python', 'advance_python', 'basic_ds', 'advance_ds', 'basic_ml', 'advance_ml', 'deep_learning', 'natural_language_processing', 'big_data_analytics', 'r_prog']
    current_subjects = [i for i in all_subjects if i!='0']
    current_headers = [all_headers[i] for i in range(len(all_headers)) if all_subjects[i]!='0']
    print(current_headers)
    print("Processing Visualization for Current Subjects - ")
    for i in current_subjects: print(i)
    
    
    df = pd.read_excel(current_subjects[0]) # taking name and email of participants from first file
    df = df[['Email address','Full Name']]
    for file_name,head in zip(current_subjects,current_headers) :
      new_file = pd.read_excel(file_name)
      new_file = new_file[['Email address','Score']]
      new_file.rename(columns={'Score':head},inplace=True)
      df = pd.merge(left=df,right=new_file,on='Email address')
      
    print("loaded data , loaded data for %d candidates and showing top 5 rows here "%(df.shape[0]))
    print(df.head())
    
    
    ###########################################################################
    ## downloading the combined file
    df2 = df.copy()
    new_cols = [i for i in list(df.columns) if '_' in i]
    new_cols2 = [" ".join([k.upper() for k in i.split('_')]) for i in new_cols]
    change = dict(list(zip(new_cols,new_cols2)))
    df2.rename(columns=change,inplace=True)
    
    print("Downloading the combined file ")
    df2.to_excel("Final_Report.xlsx")
    #downloading the final report
    from google.colab import files
    #files.download("Final_Report.xlsx")
    
    
    print("\n\n********************\n")
    print("barplot of each candidate with their scores")
    
    os.mkdir("Employee_graphs")
    os.mkdir("Final_Graphs")
    
    basic_names = []
    advance_names = []
    
    for bn in ['basic_python','basic_ds','basic_ml']:
        if bn in current_headers:
            basic_names.append(bn)
    
    for bn in ['advance_python','advance_ds','advance_ml','deep_learning', 'natural_language_processing', 'big_data_analytics', 'r_prog']:
        if bn in current_headers:
            advance_names.append(bn)
    
    print(basic_names)
    print(advance_names)
    
    for i in range(df.shape[0]):
      cdata = df.iloc[i,:]
      name = cdata['Full Name']
      basic_data=[cdata[k] for k in basic_names]
      advance_data=[cdata[k] for k in advance_names]
      for i in range(len(advance_data)-len(basic_data)):
        basic_data.append(0)
      os.mkdir("Employee_graphs//"+name)
      
      generate_barplot(basic_score=basic_data,advance_score=advance_data,name=name,domains=domains)
    
    
    print("overall barplot")
    
    basic_score = [df[col].mean() for col in basic_names]
    advance_score = [df[col].mean() for col in advance_names]
    for i in range(len(advance_score)-len(basic_score)):
        basic_score.append(0)
    
    generate_barplot(basic_score=basic_score,advance_score=advance_score,overall=True,domains=domains)
    
    
    
    
    
    
    ###########################
    print("Polar Plot ")
    import bootup_plot
    df3 = df[current_headers]
    bootup_plot.generate_polarplot(df3)