f=open('bank_analysis.txt',"a")

import pandas as pd

data_file = "budget_data.csv"
data_file_df = pd.read_csv(data_file)
data_file_df.head()

count = data_file_df.shape[0]
count

total = data_file_df["Profit/Losses"].sum()
total

AccountChange = data_file_df["Profit/Losses"].diff()
AccountChange

data_file_df["diff"] = AccountChange
data_file_df.head()

average = AccountChange.mean()
averagemean = round(average,2)
averagemean

maxvalue = AccountChange.max()
maxvalue

minvalue = AccountChange.min()
minvalue

GreatestIn = data_file_df[data_file_df['diff']==maxvalue]
GreatestIn
data_file_df.iloc[25,0]

SmallestIn = data_file_df[data_file_df['diff']==minvalue]
SmallestIn
data_file_df.iloc[44,0]

print("Financial Analysis", file=f)
print("_ _ _ _ _ _ _ _ _ _ _ _ _", file=f)
print("Total Months: ", count, file=f)
print("Total: ", total, file=f)
print("Average  Change: ", averagemean, file=f)
print("Greatest Increase in Profits: ", data_file_df.iloc[25,0], maxvalue,file=f)
print("Greatest Decrease in Profits: ", data_file_df.iloc[44,0], minvalue, file=f)

f.close()
