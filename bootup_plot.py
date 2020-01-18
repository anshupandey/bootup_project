# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 22:01:40 2019

@author: anshu
"""

import matplotlib.pyplot as plt
import numpy as np


dictionary = {'basic_python': 'Basic Python \n Programming',
 'advance_python': 'Advance Python \n Programming',
 'basic_ds': 'Basic \n Data Science',
 'advance_ds': 'Advance \n Data Science',
 'basic_ml': 'Basic \n Machine Learning',
 'advance_ml': 'Advance \n Machine Learning',
 'deep_learning': 'Deep \n Learning',
 'natural_language_processing': 'Natural Language \n Processing',
 'big_data_analytics':"Big Data \n Analytics",
 'r_prog':"R Programming"}



def generate_barplot(basic_score,advance_score,overall=False,name=None,domains=[]):
    plt.figure(figsize=(18,10))
    pos = np.arange(len(domains))
    # change the bar color to be less bright blue
    bars = plt.bar(pos, basic_score, align='center', linewidth=0, color='lightslategrey')
    bars2 = plt.bar(pos, advance_score, align='center', linewidth=0, bottom=basic_score, color='orangered')
    # soften all labels by turning grey
    plt.xticks(pos, domains, alpha=0.8)
    # remove the Y label since bars are directly labeled
    if overall:
        plt.ylabel('Average Score', alpha=0.8)
        plt.title('Overall Analysis', alpha=0.8)
    else:
        plt.ylabel('Assessment Score', alpha=0.8)
        plt.title(name, alpha=0.8)
    # remove all the ticks (both axes), and tick labels on the Y axis
    plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
    # remove the frame of the chart
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    # direct label each bar with Y axis values
    for bar in bars[:-1]:
        plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height()-1, str(int(bar.get_height())),ha='center', color='w', fontsize=22)
    for bar,eb in zip(bars2,bars):
        plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height()-1+eb.get_height(), str(int(bar.get_height())),ha='center', color='w', fontsize=22)
    plt.legend(["Basic","Advance"])
    if overall:
        plt.savefig("Final_Graphs/barplot1.jpg")
    else:
        plt.savefig("Employee_graphs//"+name+"//"+"_".join(name.split())+"_barplot1.jpg")
    plt.show()
    return None



def disss(N):
  out = np.ones(N).tolist()
  out[0]=0
  if N%2!=0:
    for i in range(1,int((N+1)/2)):
      out[i]=-1
    return out
  else:
    for i in range(1,int(N/2)):
      out[i]=-1
    if N%2==0:
      out[int(N/2)]=0
    if N%4==0:
      out[int(N/4)]=0
      out[int(3*N/4)]=0
  return out

def generate_polarplot(df,dictionary=dictionary):
    plt.style.use('ggplot')
    plt.figure(figsize=(10,10))
    ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
    N = df.shape[1]
    theta = np.linspace(0.0, 2 * np.pi, N+1)[:-1]
    radii = df.mean()
    bars = plt.bar(theta, radii, width=6.28/N, bottom=0.0)
    colors=['salmon','orangered','dodgerblue','royalblue','lawngreen','limegreen','gold','darkcyan']
    for r,bar in zip(colors, bars):
        bar.set_facecolor(r)
        bar.set_alpha(0.99)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_axisbelow(False)
    ax.xaxis.grid(lw=2)
    ax.yaxis.grid(lw=2)
    md = max(radii)
    angle = 360/N
    rot=[-90+(k*angle) for k in range(N)]
    md = max(radii)+2
    dist=disss(N)
    texts = [dictionary[val] for val in list(df.columns)]
    fact = [0.45,0.45,0.55,0.55,0.5,0.5,0.45,0.45,0.55,0.55,0.5,0.5]
    for bar,ang,text,loc,fac in zip(bars,rot,texts,dist,fact):
      plt.gca().text(bar.get_x() + bar.get_width()/2, md+loc*(6.28/N), str(int(bar.get_height()))+"/30",ha='center', color='b', fontsize=22,rotation=ang)
      plt.gca().text(bar.get_x() + bar.get_width()*fac, md+2+loc*(2*6.28/N), text,ha='center', color='black', fontsize=15,rotation=ang)
    plt.savefig("Final_Graphs/polarplot1.jpg")
    plt.show()
