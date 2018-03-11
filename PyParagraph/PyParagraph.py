#Imports 
import pandas as pd
import re
from nltk import tokenize

#open the paragraph text file
with open('Paragraph.txt', 'r') as myfile:
    paragraph = myfile.read()
#print(paragraph)

#find the word count for the paragraph
Word_Count = len(paragraph)

#Split the paragraph by sentence
Paragraph_Splt = tokenize.sent_tokenize(paragraph)
Word_Splt = re.split(" ", paragraph)
#Word_splt = Word_Splt.remove("-")
#print(Word_Splt)

#Find word count and sentance count
W_Count = len(Word_Splt)
S_Count = len(Paragraph_Splt)
Word_Len = 0
Sentance_Len = 0

#for each word in the word split paragraph find its length
for word in Word_Splt:
    Word_Len = Word_Len + len(word)

#Calculate the average length of each word
Word_Avg_Len = Word_Len/W_Count

#For each Sentence in the sentance split find its length
for Sentance in Paragraph_Splt:
    Sentance_Len = Sentance_Len + len(re.split(" ", Sentance))

#Calculated the average length of each sentence
Sentance_Avg_Len = Sentance_Len/S_Count

# print(W_Count)
# print(S_Count)
# print(Word_Avg_Len)
# print(Sentance_Avg_Len)


#Print the results to a txt file
file = open('ParagraphResults.txt','w')
file.write('Paragraph Results\n')
file.write('----------------------\n')
file.write('Approximate Word Count: ' + str(W_Count) +'\n')
file.write('Approximate Sentence Count: ' + str(S_Count) + '\n')
file.write('Average Letter Count: ' + str(Word_Avg_Len) + '\n')
file.write('Average Sentance Length: ' + str(Sentance_Avg_Len) +'\n')
