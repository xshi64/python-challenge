f=open('poll_analysis.txt',"a")

import pandas as pd

data_file2 = "election_data.csv"
data_file2_df = pd.read_csv(data_file2)
data_file2_df

count2 = data_file2_df.shape[0]
count2

CandidateName = data_file2_df["Candidate"].unique()
CandidateName

AA = CandidateName[0]
AA
BB = CandidateName[1]
BB
CC = CandidateName[2]
CC
DD = CandidateName[3]
DD

countA = data_file2_df[data_file2_df['Candidate'] == AA]
countAA = countA.shape[0]
countAA
countB = data_file2_df[data_file2_df['Candidate'] == BB]
countBB = countB.shape[0]
countBB
countC = data_file2_df[data_file2_df['Candidate'] == CC]
countCC = countC.shape[0]
countCC
countD = data_file2_df[data_file2_df['Candidate'] == DD]
countDD = countD.shape[0]
countDD

PercentageAA = round((countAA/count2)*100,3)
PercentageAA
PercentageBB = round((countBB/count2)*100,3)
PercentageBB
PercentageCC = round((countCC/count2)*100,3)
PercentageCC
PercentageDD = round((countDD/count2)*100,3)
PercentageDD

print("Election Results", file=f)
print("_ _ _ _ _ _ _ _ _ _ _ _ _", file=f)
print("Total Votes: ", count2, file=f)
print("_ _ _ _ _ _ _ _ _ _ _ _ _", file=f)
print(AA, ": ", PercentageAA, countAA, file=f)
print(BB, ": ", PercentageBB, countBB, file=f)
print(CC, ": ", PercentageCC, countCC, file=f)
print(DD, ": ", PercentageDD, countDD, file=f)
print("_ _ _ _ _ _ _ _ _ _ _ _ _", file=f)
print("Winner: ", AA, file=f)

f.close()
