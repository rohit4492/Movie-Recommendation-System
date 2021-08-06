#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[13]:


movie_titles_df = pd.read_csv('C:\\Users\\Praneeth\\Downloads\\Movie_Id_Titles.csv')


# In[15]:


movie_titles_df.head()


# In[16]:


movie_titles_df.tail()


# In[18]:


column_names = ['user_id', 'item_id', 'rating', 'timestamp']
movies_rating_df = pd.read_csv('C:\\Users\\Praneeth\\Downloads\\file.tsv',sep='\t',names=column_names)


# In[20]:


movies_rating_df


# In[24]:


movies_rating_df.drop(['timestamp'],axis=1,inplace=True)


# In[25]:


movies_rating_df


# In[26]:


movies_rating_df.describe()


# In[27]:


movies_rating_df.info()


# In[28]:


movie_rating_df = pd.merge(movies_rating_df,movie_titles_df,on='item_id')


# In[29]:


movie_rating_df


# In[31]:


movie_rating_df.shape


# In[32]:


movie_rating_df


# In[33]:


movie_rating_df.groupby('title').describe()


# In[34]:


movie_rating_df.groupby('title')['rating'].describe()


# In[35]:


ratings_df_mean = movie_rating_df.groupby('title')['rating'].describe()['mean']


# In[36]:


ratings_df_mean


# In[37]:


ratings_df_count = movie_rating_df.groupby('title')['rating'].describe()['count']


# In[38]:


ratings_df_count


# In[39]:


ratings_mean_count_df = pd.concat([ratings_df_count,ratings_df_mean],axis=1)


# In[40]:


ratings_mean_count_df


# In[41]:


ratings_mean_count_df.reset_index()


# In[42]:


ratings_mean_count_df['mean'].plot(bins=100,kind='hist',color='red')


# In[43]:


ratings_mean_count_df['count'].plot(bins=100,kind='hist',color='red')


# In[45]:


ratings_mean_count_df[ratings_mean_count_df['mean'] == 5]


# In[53]:


ratings_mean_count_df.sort_values('count',ascending = False).head(100)


# In[54]:


ratings_df_count.head()


# In[56]:


movie_rating_df.head()


# In[57]:


user_id_movietitle_matrix = movie_rating_df.pivot_table(index='user_id',columns='title',values='rating')


# In[58]:


user_id_movietitle_matrix


# In[59]:


titanic = user_id_movietitle_matrix['Titanic (1997)']


# In[61]:


titanic.head(20)


# In[63]:


starwars=user_id_movietitle_matrix['Star Wars (1977)']


# In[64]:


starwars


# In[66]:


titanic_cor = pd.DataFrame(user_id_movietitle_matrix.corrwith(titanic),columns=['correlation'])


# In[67]:


titanic_cor


# In[68]:


titanic_cor=titanic_cor.join(ratings_mean_count_df['count'])


# In[69]:


titanic_cor


# In[70]:


titanic_cor.dropna(inplace = True)


# In[71]:


titanic_cor


# In[72]:


titanic_cor.sort_values(['correlation'],ascending = False)


# In[75]:


titanic_cor[titanic_cor['count'] > 80].sort_values('correlation',ascending=False).head()


# In[76]:


user_id_movietitle_matrix


# In[82]:


movie_correlations = user_id_movietitle_matrix.corr(method ='pearson',min_periods = 80)


# In[80]:


movie_correlations


# In[101]:


my_ratings=pd.read_csv('C:\\Users\\Praneeth\\Downloads\\Book1.csv')


# In[102]:


my_ratings


# In[103]:


my_ratings.dropna(axis=1,inplace=True)


# In[104]:


my_ratings


# In[105]:


my_ratings['Movie Name'][0]


# In[106]:


similar_movies_list=pd.Series()
for i in range(0,2):
    similar_movie=movie_correlations[my_ratings['Movie Name'][i] ]
    similar_movie=similar_movie.map(lambda x:x*my_ratings['Ratings'][i])
    similar_movies_list=similar_movies_list.append(similar_movie)


# In[108]:


similar_movies_list.sort_values(inplace = True,ascending = False)
print(similar_movies_list.head(10))


# In[ ]:




