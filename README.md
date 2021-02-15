# DataFrames_rows_columns

## Code for selecting rows and columns in DataFrame, based on characters of Data.

### The whole code is executed in Spyder IDE with Python3.7

#### Following are the actions performed on Simple data set

1. Importing Library
2. Creating a dataset
3. Converting data into DataFrames
4. Selection of rows and columns based on Specific characters
#### 1. Importing Library
```
import pandas as pd
```
#### 2. Creating a dataset "boxes"
```
boxes = {'Color': ['Green', 'Green', 'Green', 'Blue', 'Blue', 'Red', 'Red', 'Red'],
         'Shape': ['Rectangle', 'Rectangle', 'Square', 'Rectangle','Square','Square','Square','Rectangle'],
         'Price': [10,15,5,5,10,15,15,5]
         }
```
##### Visualisation of variable "boxes"
![data](https://user-images.githubusercontent.com/49682375/107990116-fee2ef80-6fd3-11eb-96e2-3b28df172552.JPG)
#### 3. Converting "boxes" in to DataFrame "df"
```
df = pd.DataFrame(boxes, columns=['Color','Shape','Price'])
```
##### Visualisation of "df"
![dataframe](https://user-images.githubusercontent.com/49682375/107990407-b6780180-6fd4-11eb-8c30-6d7307eb4bd0.JPG)

#### 4. Selection of Rows, based on character of data
* Selecting rows of data with Specific Color "green" 
```
select_color = df.loc[df['Color'] == 'Green']
```
###### Visualisation of "select_color"
![color_green](https://user-images.githubusercontent.com/49682375/107990997-f4c1f080-6fd5-11eb-84c4-10b4d67bbb04.JPG)

* Selecting rows of data with Specific Shape "Rectangle"
```
select_shape = df.loc[df['Shape'] == 'Rectangle']
```
###### Visualisation of "select_shape"

* Selecting rows of data with Specific Price "5"
```
select_price = df.loc[df['Price']== 5]
```
###### Visualisation of "select_price"


Source: All the Data is taken from the link <https://datatofish.com/select-rows-pandas-dataframe/>
