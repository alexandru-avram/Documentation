# Data Science

## Numpy

### [Creating NumPp Arrays](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Numpy%20Library/01.%20Creating%20NumPy%20Arrays.ipynb)
NumPy's arrays are more compact than Python lists -- a list of lists as you describe, in Python, would take at least 20 MB or so, while a NumPy 3D array with single-precision floats in the cells would fit in 4 MB. Access in reading and writing items is also faster with NumPy.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: numpy, numpy arrays, creating numpy arrays, arrange, zeros, ones, linespace, eye, random, rand, randn, randint


### [Numpy Shapes](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Numpy%20Library/02.%20Shape%20and%20Reshape.ipynb)
Numpy arrays can have two shapes: 1d and 2d.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: numpy shape, reshape, flatten

### [Indexing and Selection](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Numpy%20Library/03.%20Indexing%20%26%20Slicing.ipynb)
Numpy arrays can be indexed with other arrays or any other sequence with the exception of tuples.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: numpy indexing, bracket indexing, broadcasting, fancy indexing, conditional selection

### [Numpy Methods](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Numpy%20Library/04.%20NumPy%20Methods.ipynb)
As with lists, we are able to use various methods on arrays. We can sort, delete or append items to an array. We can even merge two arrays.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: numpy methods, append, sort, delete, concatenate

### [Numpy Operations](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Numpy%20Library/05.%20NumPy%20Operations.ipynb)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: numpy operations, max, min, argmax, argmin, arithmetic, array functions

## Pandas

### [Pandas Series](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Pandas%20Library/01.%20Pandas%20Series.ipynb)
A Series is very similar to a NumPy array (in fact it is built on top of the NumPy array object). What differentiates the NumPy array from a Series, is that a Series can have axis labels, meaning it can be indexed by a label, instead of just a number location. It also doesn't need to hold numeric data.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: pandas series, creating a pandas series, indexing

### [DataFrames](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Pandas%20Library/02.%20DataFrames.ipynb)
We can think of a DataFrame as a bunch of Series objects put together to share the same index.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: creating a DataFrame from list, pandas indexing, pandas selection, selecting rows, loc, iloc, dropping a row, drop, conditional selection, indexing, reset_index, set_index, multiindex, hierarchy

### [Missing Data](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Pandas%20Library/03.%20%20Missing%20Data.ipynb)
Clearing data, filling missing data, finding null values, filling null values.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: missing data, data cleaning, null values, isnull, dropna, fillna

### [GroupBy](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Pandas%20Library/04.%20GroupBy.ipynb)
The `groupby` method allows you to group rows of data together and call aggregate functions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: groupby, pandas group, groupping, transpose

### [Data Modeling](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Pandas%20Library/05.%20Merging%2C%20joining%20%26%20Concatenating.ipynb)
Pandas allows users to concatenate, merge and join multiple DataFrames in order to perform data modeling processes.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: concatenate, merge, join

### [Pandas Operations](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Pandas%20Library/06.%20Operations.ipynb)
There are lots of operations with pandas that will be really useful to you in pandas.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: unique values, value counts, unique, applying functions to pandas, sort, order, pivot

### [Data Input and Output](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Pandas%20Library/07.%20Data%20Input%20and%20Output.ipynb)
Importing and exporting data from/into multiple file types.\
Use `pd.read_file type` to import and `pd.to_file type`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: pd.read_, pd.to_ CSV,  Excel, HTML, SQL

## Matplotlib

### [Matplotlib Overview](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Matplotlib%20Library/01.%20Matplotlib%20Concepts.ipynb)
Matplotlib allows you to create reproducible figures programmatically. Let's learn how to use it! Before continuing this lecture, I encourage you just to explore the official [Matplotlib web page](http://matplotlib.org/)\
`import matplotlib.pyplot as plt`
