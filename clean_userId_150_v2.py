"""
Date: 11/22/2019
Author: Shixuan Song
To clean our combined movie dataset and remove users who rated less or equal to 150 movies

Output: userId_150_v2.csv is a file with one row per user per movie rating.
This dataset only contains users who has rated more than 150 movies in our raw dataset.
It is ordered by number of rated movies of each user descendingly
"""
#import os
#dir = os.getcwd()
#print(dir)
#os.chdir(p)
#dir = os.getcwd()
#print(dir)

import pandas as pd
#from dfply import *
withsplitdata = pd.read_csv("withSplitDic.csv" ,index_col = 0)

#add a column to count the number of movies each user rated
withsplitdata['Count_movies']= withsplitdata.groupby(['userId'])['userId'].transform('count')
num_movies_rated = withsplitdata[withsplitdata['Count_movies'] < 150].index

#order by descending number of movies rated
sort_withsplitdata = withsplitdata.sort_values(by = ['Count_movies', 'userId'], ascending = False)
sort_withsplitdata.to_csv("userId_150_v3.csv")
 
