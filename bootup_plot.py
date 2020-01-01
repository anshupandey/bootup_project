# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 22:01:40 2019

@author: anshu
"""

import matplotlib.pyplot as plt
import numpy as np


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


def radial_plot(df2):
    plt.figure(figsize=(10,10))
    ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
    
    N = df2.shape[1]
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
    radii = df2.mean()
    bars = plt.bar(theta, radii, width=0.9, bottom=0.0)
    
    for r,bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r/10.))
        bar.set_alpha(0.9)
    
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.show()
    return None