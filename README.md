# Scatter Plot
This is a python program where we are reading CSV file with the dataset of Breast Cancer with label of Benign or Malignant and features attached with it. We are shuffling the data set and we will use first 75% of the data set in training set and other 25% of the data set in testing data. We use this data to plot scatter plots for three pairs of the features. Next, we are plotting the bar chart for the frequency of the labels.  Source for the data set : http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

# Read & Split the Data
Python script that reads the CSV file and splits the data set randomly into testing and training data. It uses 5 Numpy arrays for this: feature names, training data, training labels, testing data, and testing labels. It seperates the training set contains about 75% of the data and the testing set has the other 25%. Each time the script is run, it produces a different split.

# Summarize It
Printed summary information for the training and testing data: The name of each feature, followed by it’s minimum, maximum, mean, and median in the training set and in the testing set. Made proper use of the NumPy array type for this (i.e. no loops has been used!)

# Graph It
Explored training data by creating 2D scatter plots of pairs of features. Made sure the different class labels are represented with different colors. Found 3 pairs that seem promising for separating the classes and add code to your Python script to produce those 3 scatter plots.
