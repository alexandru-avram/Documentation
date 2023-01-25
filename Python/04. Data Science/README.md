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
    
    import matplotlib.pyplot as plt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: plot, one plot, line, multiplots, multiple plots, plot in plot, classes, matplotlib classes

### [Subplots](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Matplotlib%20Library/02.%20Subplots.ipynb)
The `plt.subplots()` object will act as a more automatic axis manager.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: subplots, multiple plots, layout

### [Figure Size](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Matplotlib%20Library/03.%20Picture%20size.ipynb)
Matplotlib allows the aspect ratio, DPI and figure size to be specified when the Figure object is created. You can use the `figsize` and `dpi` keyword arguments.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: figure size, picture size, figsize, dpi, aspect ratio

### [Legends & Titles](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Matplotlib%20Library/04.%20Legend%20%26%20Titles.ipynb)
How to create a figure canvas and add axes instances to the canvas, let's look at how decorate a figure with titles, axis labels, and legends.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: titles, labels, legends, xlabel, ylabel

### [Color and Linetypes](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Matplotlib%20Library/05.%20Color%20and%20Linetypes.ipynb)
Matplotlib gives you a lot of options for customizing colors, linewidths, and linetypes.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: linetypes, colors, marker styles, types of lines

### [Plot Range](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Matplotlib%20Library/06.%20Plot%20Range.ipynb)
We can configure the ranges of the axes using the `set_ylim` and `set_xlim` methods in the axis object, or `axis('tight')` for automatically getting *tightly fitted* axes ranges.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: plot range, custom range, custom axes range, tight axes

### [Special Plot Types](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Matplotlib%20Library/07.%20Special%20Plot%20Types.ipynb)
There are many specialized plots we can create, such as barplots, histograms, scatter plots, and much more.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: scatter plot, histogram, boxplot

### [Advanced Matplotlib Concepts](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/04.%20Data%20Science/Matplotlib%20Library/08%20Advanced%20Matplotlib%20Concepts.ipynb)
Advance customization options using matplotlib.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: logarithmic, ticks, custom label ticks, axis number, label spacing, axis grid, axis spines, twin axes, axes where x & y is zero, fill, text annotation, colormap, 3D figures
