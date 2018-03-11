import pandas as pd
import csv

#Import the election results CSV file
Results = pd.read_csv('election_data_1.csv')

#Save the data to a datafram
Poll_Results = Results['Candidate'].value_counts().to_frame()

Poll_Results = Poll_Results.rename(columns = {'Candidate':'Votes'})

Total_Votes = sum(Poll_Results['Votes'])
Poll_Results['Percentage'] = Poll_Results['Votes']/Total_Votes*100
Poll_Results = Poll_Results.round()

Candidates = list(Poll_Results.index)
Leader = Candidates[0]

file = open('ElectionResultsTest.txt','w')
file.write('Election Results\n')
file.write('-----------------\n')
file.write(str(Candidates[0]) + ": " + str(Poll_Results['Percentage'][0]) + "% (" + str(Poll_Results['Votes'][0]) + ")\n")
file.write(str(Candidates[1]) + ": " + str(Poll_Results['Percentage'][1]) + "% (" + str(Poll_Results['Votes'][1]) + ")\n")
file.write(str(Candidates[2]) + ": " + str(Poll_Results['Percentage'][2]) + "% (" + str(Poll_Results['Votes'][2]) + ")\n")
file.write(str(Candidates[3]) + ": " + str(Poll_Results['Percentage'][3]) + "% (" + str(Poll_Results['Votes'][3]) + ")\n")
file.write('-----------------\n')
file.write('Winner: ' + Leader)
