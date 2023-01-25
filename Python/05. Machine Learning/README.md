# Statistics & Machine-Learning

## [Statistics Glossary](https://github.com/alexandruavram-rusu/Documentation/edit/main/Python/05.%20Machine%20Learning/Theory%20-%20General%20Statistics/README.md)

### [Descriptive Statistics](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20General%20Statistics/01.%20Descriptive%20statistics.pdf) 

- Types of data: Categorical &  Numerical (Discrete or Continuous)
- Levels of measurements: Qualitative (Nominal or Ordinal) & Quantitative (Interval or Ratio)

Descriptive statistics graphs:
- Frequency distribution table
- Bar charts
- Pie chart
- Pareto diagram
- Histogram
- Scatter plots

**Cross tables** (or contingency tables) are used to represent categorical variables.

Mean, media, mode, skewness, variance, standard deviation, covariance, correlation

### [Inferential Statistics](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20General%20Statistics/02.%20Inferential%20Statistics.pdf)

Distribution:
- **Normal distribution**: A normal distribution is an arrangement of a data set in which most values cluster in the middle of the range and the rest taper off symmetrically toward either extreme.
- **Standard normal distribution**: The standard normal distribution, also called the z-distribution, is a special normal distribution where the mean is 0 and the standard deviation is 1.
- **Student t-distribution**: The T distribution, also known as the Student's t-distribution, is a type of probability distribution that is similar to the normal distribution with its bell shape but has heavier tails. T distributions have a greater chance for extreme values than normal distributions, hence the fatter tails.

The **Central Limit Theorem** (CLT)  states that no matter the underlying distribution of the dataset, the sampling distribution of the means would approximate a normal distribution.

Estimators, estimates, confidence interval, margin of error


### [Hypothesis Testing](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20General%20Statistics/03.%20Hypothesis%20testing.pdf)

- **Null hypothesis** is the hypothesis to be tested.
- The **alternative hypothesis** is the change or innovation that is contesting the status-quo.

Level of significance, type of tests

Statistical errors:
- Type I Error: false positive
- Type II Error: false negative

The **p-value** is the smallest level of significance at which we can still reject the null hypothesis, given the observed sample statistic.


### [Regression Analysis](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20General%20Statistics/04.%20Regression%20analysis.pdf)

A linear regression is a linear approximation of a causal relationship between two or more variables.

Correlation vs Regression, Regression metrics

OLS (ordinary least squares) is one of the most common methods for estimating the linear regression equation:
- Linearity: The specified model must represent a linear relationship.
- No endogeneity: The independent variables shouldn’t be correlated with the error term.
- Normality and homoscedasticity: The variance of the errors should be consistent across observations.
- No autocorrelation: No identifiable relationship should exist between the values of the error term.
- No multicollinearity: No predictor variable should be perfectly (or almost perfectly) explained by the other predictors.

[Supliment](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20General%20Statistics/04.1%20Intro%20to%20Linear%20Regression.pdf)


## Machine Learning

### [Machine Learning Concepts](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/01.%20Intro%20into%20ML.pdf)

Machine Learning Process:
1. Data acquisition
2. Data cleaning
3. Test data split (30% of total data)
4. Model testing and Model traning & building
5. Model deployment

Types of Machine Learning approaches:
- **Supervised learning** algorithms are trained using labeled exampeles such as an input where the desired output is known.
- **Unsupervised learning** is used against data that has no historical labels and the algorithm must figure out what is being shown.
- **Reinformced learning** algorithms disover through trial and error which actions yield the greatest rewards.

### [Bias Variance Trade-Off](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Bias%20Variance%20Trade-Off.pdf)

Train Test Splits:
- Regression
  * R^2
  * RMSE
- Classification
  * Precision
  * Recall
- Clustering
  * Within Sum of Squares Error

**Holdout Data**: you use the training data to fit your model, you use the test set to evaluate and adjust your model.

The bias-variance trade-off is the point where we are adding just noise by adding model complexity (flexibility).

* Low variance - High variance
* Low bias - High bias

A common temptation for beginners is to continually add complexity to a model until it fits the training set very well.


### [Metrics to Evaluate your Machine Learning Algorithm](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Metrics%20to%20Evaluate%20your%20Machine%20Learning%20Algorithm.pdf)

Your model may give you satisfying results when evaluated using a metric say accuracy score but may give poor results when evaluated against other metrics such as logarithmic loss or any other such metric.

**Classification Accuracy** is the ratio of number of correct predictions to the total number of input samples.

**Logarithmic Loss** or **Log Loss** works by penalizing the false classifications, the classifier must assign probability to each class for all the samples

**Confusion Matrix**  gives us a matrix as output and describes the complete performance of the model

|n=165|Predicted: NO|Predictes YES|
|----|----------|----------|
|Actual NO|50|10|
|Actual YES|5|100|

* True Positives: The cases in which we predicted YES and the actual output was also YES.
* True Negatives: The cases in which we predicted NO and the actual output was NO.
* False Positives: The cases in which we predicted YES and the actual output was NO.
* False Negatives: The cases in which we predicted NO and the actual output was YES

** Area Under Curve** of a classifier is equal to the probability that the classifier will rank a randomly chosen positive example higher than a randomly chosen negative example.
* True Positive Rate (Sensitivity) corresponds to the proportion of positive data points that are correctly considered as positive, with respect to all positive data points.
* True Negative Rate (Specificity) orresponds to the proportion of negative data points that are correctly considered as negative, with respect to all negative data points.
* False Positive Rate corresponds to the proportion of negative data points that are mistakenly considered as positive, with respect to all negative data points.

**F1 Score** is used to measure a test’s accuracy, is the Harmonic Mean between precision and recall. The range for F1 Score is [0, 1]. It tells you how precise your classifier is (how many instances it classifies correctly), as well as how robust it is (it does not miss a significant number of instances).

**Precision** is the number of correct positive results divided by the number of positive results predicted by the classifier.

**Recall** is the number of correct positive results divided by the number of all relevant samples (all samples that should have been identified as positive).

**Mean Absolute Error (MAE)** is the average of the difference between the Original Values and the Predicted Values.

**Mean Squared Error (MSE)** is quite similar to Mean Absolute Error, the only difference being that MSE takes the average of the square of the difference between the original values and the predicted values. 

**Root Mean Square Error (RMSE)** is the standard deviation of the residuals (prediction errors). Residuals are a measure of how far from the regression line data points are; RMSE is a measure of how spread out these residuals are. In other words, it tells you how concentrated the data is around the line of best fit.

### [Logistic Regression](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Logistic%20Regression.pdf)

The convention for **binary classification** is to have two classes 0 and 1 and can be predicted with a **linear regression**. **Logistic regressions** allow us to solve classification problems, where we are trying to predict discrete categories.

The **Sigmoid (aka Logistic)** Function takes in any value and outputs it to be between 0 and 1.


### [K Nearest Neighbors (KNN)](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/K%20Nearest%20Neighbors.pdf)

K Nearest Neighbors is a classification algorithm that calculates the distance from sorts points in your data in order to group them into different classes.

Choosing a different K-number will affect what class a new point is assigned to.


### [Decision Trees](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Tree%20Methods.pdf)

A decision tree is a support tool with a tree-like structure that models probable outcomes, cost of resources, utilities, and possible consequences. Decision trees provide a way to present algorithms with conditional control statements. They include branches that represent decision-making steps that can lead to a favorable result.

To improve performance, we can use many trees with a random sample of features chosen as the split. A new random sample of features is chosen for every single tree at every single split.


### [Support Vector Machines (SVMs)](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Support%20Vector%20Machines.pdf)

A **support vector machine (SVM)** is a supervised machine learning model that uses classification algorithms for two-group classification problems. After giving an SVM model sets of labeled training data for each category, they’re able to categorize new text. 

A support vector machine takes these data points and outputs the hyperplane (which in two dimensions it’s simply a line) that best separates the tags. This line is the decision boundary. The hyperplane is a line, or a circle or something else, whose distance to the nearest element of each tag is the largest.

### [K Means Clustering](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Support%20Vector%20Machines.pdf)

K Means Clustering is an unsupervised learning algorithm that will attempt to group similar clusters together in your data. The overall goal is to divide data into distinct groups such that observations within each group are similar. 

There is no easy answer for choosing a *best K value*. One way is the elbow method in which you compute the sum of **squared error** (SSE) for some values of Ks and choose the K where the SSE decreases abruptly.

### [Principal Component Analysis](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Principal%20Component%20Analysis.pdf)

Known as **factor analysis**, it is an unsupervised statistical technique used to examine the interrelations among a set of variables in order to identify the underlying structure of those variables. Where regression determines a line of best fit to a data set,factor analysis determines several orthogonal lines of best
fit to the data set.

Components are a linear transformation that chooses a variable system for the data set such that the greatest variance of the data set comes to lie on the first axis.

### [Recommender Systems](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Recommender%20Systems.pdf)

Recommender systems are the systems that are designed to recommend things to the user based on many different factors. These systems predict the most likely product that the users are most likely to purchase and are of interest to. The recommender system deals with a large volume of information present by filtering the most important information based on the data provided by a user and other factors that take care of the user’s preference and interest. It finds out the match between user and item and imputes the similarities between users and items for recommendation. 

### [Natural Language Processing (NLP)](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Natural%20Language%20Processing.pdf)

A document represented as a vector of word counts is called a **Bag of Words**. We can improve on Bag of Words by adjusting word counts based on their frequency in corpus (the group of all the documents).

* Term Frequency - Importance of the term within that document
* Inverse Document Frequency - Importance of the term in the corpus

### [Neural Nets](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/Neural%20Nets.pdf)

Neural networks are modeled after biological neural networks and attempt to allow computers to learn in a similar manner to humans - reinforcement learning.

A perceptron consists of one or more inputs, a processor,  and a single output. A perceptron follows the “feed-forward” model, meaning  inputs are sent into the neuron, are processed, and result in an output. Each input that is sent into the neuron must first be  weighted, i.e. multiplied by some value (often a number between -1 and 1). The output of a perceptron is generated by passing that sum through an activation function.

### [Artificial Neural Networks](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/05.%20Machine%20Learning/Theory%20-%20Machine%20Learning%20Statistics/ANN%20Artificial%20Neural%20Networks.pdf)

The whole idea behind deep learning is to have computers artificially mimic biological natural intelligence.
