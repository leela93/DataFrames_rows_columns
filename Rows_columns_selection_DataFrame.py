# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:26:26 2021

@author: leela
"""
# importing library
import pandas as pd

# Creating a dataset in boxes
boxes = {'Color': ['Green', 'Green', 'Green', 'Blue', 'Blue', 'Red', 'Red', 'Red'],
         'Shape': ['Rectangle', 'Rectangle', 'Square', 'Rectangle','Square','Square','Square','Rectangle'],
         'Price': [10,15,5,5,10,15,15,5]
         }

# 1.Conveting data in to DataFrame
df = pd.DataFrame(boxes, columns=['Color','Shape','Price'])

# 2.Selecting rows of data with Specific Color Characters
select_color = df.loc[df['Color'] == 'Green']

# 3.Selecting rows of data with specific Shape characters
select_shape = df.loc[df['Shape'] == 'Rectangle']

# 4.Selecting rows of data with specific Price characters
select_price = df.loc[df['Price']== 5]

# 5.Selecting rows of data with specific color and shape
select_col_and_sha = df.loc[(df['Color'] == 'Green' )& (df['Shape'] == 'Rectangle')]

# 6.Select rows where the price is equal or greater than 10
select_price_gre_10 = df.loc[df['Price'] >= 10]

# 7.Select rows where the color is green OR the shape is rectangle 
select_col_or_sha = df.loc[(df['Color'] == 'Green' )|(df['Shape'] == 'Rectangle')]

# 8.Select rows where the price is not equal to 15
select_price_notequal_15 = df.loc[df['Price'] != 15]

## Selecting 1 column
select_column_1 = df['Color']

## Selecting 2 column
select_column_2 = df[['Color', 'Shape']]