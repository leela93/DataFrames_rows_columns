# DataFrames_rows_columns

## Code for selecting rows and columns in DataFrame, based on characters of Data.

### The whole code is executed in Spyder IDE with Python3.7

#### Following are the actions performed on Simple data set

1. Importing Library
2. Creating a dataset
3. Converting data into DataFrames
4. Selection of based on Specific characters

#### 1. Importing Library
```
import pandas as pd
```

#### 2. Creating a dataset
```
boxes = {'Color': ['Green', 'Green', 'Green', 'Blue', 'Blue', 'Red', 'Red', 'Red'],
         'Shape': ['Rectangle', 'Rectangle', 'Square', 'Rectangle','Square','Square','Square','Rectangle'],
         'Price': [10,15,5,5,10,15,15,5]
         }
```
##### Visualisation of Data
![data](https://user-images.githubusercontent.com/49682375/107990116-fee2ef80-6fd3-11eb-96e2-3b28df172552.JPG)
#### 3. Converting data in to DataFrame
```
df = pd.DataFrame(boxes, columns=['Color','Shape','Price'])
```

Source: All the Data is taken from the link <https://datatofish.com/select-rows-pandas-dataframe/>
