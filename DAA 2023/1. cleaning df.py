import pandas as pd

#df = pd.read_csv('SAA1_python_example.csv', sep=',')#when columns are separated with a comma, use '\t'

#print(df) #this is an enormous table, so it takes forever to load. We won't do this today. 

#-----------------------
#remove duplicates
#-----------------------
#nodupes = df.drop_duplicates(subset=['id_text'], keep='last')
#print(nodupes)

#-----------------------
#Choose which metadata and the order it should come in
#-----------------------
#ordered = nodupes[['id_text','designation','ancient_author','ancient_recipient','sender_loc','genre','provenience','lemma']]
#print(ordered)

#-----------------------
#How many unique entries in a column?
#-----------------------
#unique = len(pd.unique(ordered['sender_loc']))
#print("Number of unique values :", unique)

#-----------------------
#What are the unique values?
#-----------------------
#df:
#location = ordered[['sender_loc']]
#loca = location.drop_duplicates(subset=['sender_loc'], keep='last')
#print(loca)
#List:
#location = pd.unique(ordered['sender_loc'])
#print(location)

#-----------------------
#filtering according to a column
#-----------------------
#nimrud = ordered[ordered['sender_loc']=='Nimrud']
#print(nimrud)

#-----------------------
#display only one column
#-----------------------
#lemma = nimrud[['lemma']]
#print(lemma)

#-----------------------
#re-order the index to start from 0
#-----------------------
#indexed = lemma.reset_index(drop=True)#Change drop to False if you want to retain the original Id number to the original dataset.
#print(index)

#-----------------------
#add ID column (the row index plus one)
#-----------------------
#indexed['Id'] = indexed.index + 1 #needs to be the same as the one before
#print(indexed)

#-----------------------
#Re-order - this is the same code as before!
#-----------------------
#Id = indexed[['Id','lemma']]
#print(Id)

#-----------------------
#saving the file
#-----------------------
#indexed.to_csv("D:\DAA 2023\Python\SAA1_Nimrud_lemma.txt",index=False,header=False,sep=",")
#remember you can have this as tab-separated with sep="\t".
#index and header determines if you save the index or the headers
