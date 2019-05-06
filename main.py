import pandas as pd
import numpy as np
import matplotlib as plt

def binning(col, cut_points, labels=None):
    #Define min and max values:
    minval = col.min()
    maxval = col.max()

    #create list by adding min and max to cut_points
    break_points = [minval] + cut_points + [maxval]

    #if no labels provided, use default labels 0 ... (n-1)
    if not labels:
        labels = range(len(cut_points)+1)

    #Binning using cut function of pandas
    colBin = pd.cut(col, bins=break_points, labels=labels, include_lowest=True)
    return colBin

#1
df = pd.read_csv("train_Loan.csv")
#2
column_list=list(df)
for column in column_list:
    x=df[column].value_counts()
    print(x)
#3
print(df.dtypes)
#4
columns_to_fill_MV=['Married','Gender','Self_Employed']
for column in columns_to_fill_MV:
    df[column].fillna(df[column].mode()[0], inplace=True)
#5
max=df["LoanAmount"].max()
bins = [max/4, max*2/4, max*3/4] #Define bins as 0<=x<175, 175<=x<350, 350<=x<525, x>=525
group_names = ['Low', 'Medium', 'High', 'Extreme']
df["LoanAmount_Bin"] = binning(df["LoanAmount"], bins, group_names)#Discretize the values in LoanAmount attribute
print (pd.value_counts(df["LoanAmount_Bin"], sort=False)) #Count the number of observations which each value
print(df)
#6
# Keep only the ones that are within +3 to -3 standard deviations in the column 'LoanAmount'.
print(df[(np.abs(df.LoanAmount-df.LoanAmount.mean()) <= (3*df.LoanAmount.std()))])








