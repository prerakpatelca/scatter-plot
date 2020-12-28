"""This is a python program where we are reading CSV file with the dataset of Breast Cancer with label of Benign or Malignant and features attached with it. We are shuffling the data set and we will use first 75% of the data set in training set and other 25% of the data set in testing data. We use this data to plot scatter plots for three pairs of the features. Next, we are plotting the bar chart for the frequency of the labels.

Source for the data set : http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

Prerak Patel, Student, Mohawk College, 2020
"""

from matplotlib import pyplot as plt
import numpy as np
import csv

## READ IT

# opening the CSV file here
train_data_file = open("breast-cancer-wisconsin.csv","r")

# creating CSV readers
csv_reader = csv.reader(train_data_file, delimiter=",")

# declaring the arrays for the sotring data
train_data = []
train_labels = []
test_data = []
test_labels = []
header_count = 0
for row in csv_reader:
    if header_count == 0:
        # reading features
        feature_names = row
        header_count += 1
        continue
    # train_data
    train_data += [[int(num) for num in row]]

# convert to NumPy arrays
data_set = np.array(train_data)
# shuffle the data set
np.random.shuffle(data_set)
# storing data set labels
labels = data_set[:,10]
# using the first 75% of the data set into training data
train_data = data_set[:,1:10][:int(len(data_set)*0.75)]
train_labels = data_set[:,10][:int(len(data_set)*0.75)]
# using the other 25% of the data set into testing data
test_data = data_set[:,1:10][int(len(data_set)*0.75):]
test_labels = data_set[:,10:][int(len(data_set)*0.75):]
# filtering the data for Benign if the label has the value of 2
train_data_ben = train_data[train_labels == 2]
# filtering the data for Malignant if the label has the value of 4
train_data_mal = train_data[train_labels == 4]

## SUMMARIZE IT

# count to loop through the feature_names
count = 0
# position to get the index from the train_data
position = 0
# looping through feature names to print out the summary of each attribute for training and testing data
for attribute in feature_names:
    # leaving out the first and last classes as those are not the attributes
    if( count != 0 and count != (len(feature_names) - 1) ):
        print(str(count) + ". " + attribute + "\n\tTraining Set: Minimum: " + str(train_data[:,position].min()) + " Maximum: " + str(train_data[:,position].max()) + " Mean: " + str(train_data[:,position].mean()) + " Median: " + str(np.median(train_data[:,position])) + "\n\tTesting Set: Minimum: " + str(test_data[:,position].min()) + " Maximum: " + str(test_data[:,position].max()) + " Mean: " + str(test_data[:,position].mean()) + " Median: " + str(np.median(test_data[:,position])) )
        position +=1
    count += 1

## GRAPH IT

# set up the parameters of the plot figure 1 with features Clump Thickness and Uniformity of Cell Size
plt.figure(1)
plt.title("Breast Cancer Diagnostic")
plt.xlabel(feature_names[1])
plt.ylabel(feature_names[2])
plt.ylim(ymin=-1, ymax=11)
plt.xlim(xmin=-1, xmax=11)
# creating 2D scatter plots with red label for Malignant
plt.scatter(train_data_mal[:,0], train_data_mal[:,1], c="red", marker=".")
# creating 2D scatter plots with red label for Benign
plt.scatter(train_data_ben[:,0], train_data_ben[:,1], c="green", marker=".")

# set up the parameters of the plot figure 2 with features Uniformity of Cell Shape and Marginal Adhesion
plt.figure(2)
plt.title("Breast Cancer Diagnostic")
plt.xlabel(feature_names[3])
plt.ylabel(feature_names[4])
plt.ylim(ymin=-1, ymax=11)
plt.xlim(xmin=-1, xmax=11)
# creating 2D scatter plots with red label for Malignant
plt.scatter(train_data_mal[:,2], train_data_mal[:,3], c="red", marker=".")
# creating 2D scatter plots with red label for Benign
plt.scatter(train_data_ben[:,2], train_data_ben[:,3], c="green", marker=".")

# set up the parameters of the plot figure 3 with features Bland Chromatin and Normal Nucleoli
plt.figure(3)
plt.title("Breast Cancer Diagnostic")
plt.xlabel(feature_names[7])
plt.ylabel(feature_names[8])
plt.ylim(ymin=-1, ymax=11)
plt.xlim(xmin=-1, xmax=11)
# creating 2D scatter plots with red label for Malignant
plt.scatter(train_data_mal[:,6], train_data_mal[:,7], c="red", marker=".")
# creating 2D scatter plots with red label for Benign
plt.scatter(train_data_ben[:,6], train_data_ben[:,7], c="green", marker=".")

# Figure 4 - set up the bar chart parameters labels (Benign or Malignant)
plt.figure(4)
langs = ['Benign','Malignant']
students = [len(data_set[labels == 2]),len(data_set[labels == 4])]
plt.bar(langs,students)
# show the plot window
plt.show()
