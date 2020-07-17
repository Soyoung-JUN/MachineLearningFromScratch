####################################################################################
# File Name : week1_hw1_jsy                                                                     #  
# Date  : 2020/07/17                                                               #  
# OS : Windows 10                                                                  #  
# Author : Soyoung JUN                                                                        #
# -------------------------------------------------------------------------------  #  
# requirements : python 3.7                                                        #
#                                                                                  #
####################################################################################   

import random                      
import numpy as np                 
import pandas as pd                 
import matplotlib.pyplot as plt    
import warnings                     


try:
    from sklearn.cluster import KMeans  # check installation of sklearn
except:
    print("Not installed scikit-learn.") 
    pass


if __name__ == '__main__': # Start from main
    #Implement Load and Plot Code here
    df = pd.read_csv("data.csv")
    # Basic Scatter Plot
    plt.plot('Sepal length','Sepal width', data=df, linestyle='none', marker='o', markersize=10, color='blue', alpha=0.5)
    plt.title('from scikit-learn library', fontsize=20)
    plt.xlabel('sepal length(cm)', fontsize=14)
    plt.ylabel('sepal width(cm)', fontsize=14)    
    plt.show() # show plot
