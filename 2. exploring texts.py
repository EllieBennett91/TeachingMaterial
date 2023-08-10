import re

#file = open("SAA1_Nimrud_lemma.txt", "r+", encoding="utf-8")
#text = file.read()
#print(file)

#-------------------------------
#How many tokens are in the file?
#-------------------------------
#tokens = text.split() 
#print('Total number of tokens in text file: ', len(tokens))

#-------------------------------
#Number of unique words
#-------------------------------
#unique = set(tokens) #set only includes unique values
#print("Number of unique words in text file: ", len(unique))

#-------------------------------
#Count a specific lemma in the file
#-------------------------------
#king = text.count("šarru[king]N") 
#print('Number of times \'šarru\' is mentioned in corpus:', king)

#-------------------------------
#First instance of a word (only yes or no)
#-------------------------------
#searchma = re.search("mā",text)
#print(searchma)

#-------------------------------
#Find all instances of word
#-------------------------------
#findallma = re.findall("mā",text)
#print(findallma)

#-------------------------------
#Regex of a lemma
#-------------------------------
findallregex = re.findall(r" [a-z]*mā.*?[ $]",text) #This is 'LUGAL' with anything afterwards that is part of the word
#print(findallregex)

#-------------------------------
# Regular expression that matches potentially interesting words
# [a-z] any alphabetic character
# *     zero or more times
# ?     tries to find the shortest possible string
# ^     string begins with
# $     string ends with
# .     any character
# +     repeat previous character 1+ times
# (x|y) disjunction, i.e. X or Y
#-------------------------------

#-------------------------------
#number of results
#-------------------------------
#number_of_elements = len(findallregex)
#print("Number of Regex results: ", number_of_elements)

#-------------------------------
#%age of the whole text
#-------------------------------
#quotient = len(findallregex) / len(tokens)
#percentage = quotient * 100
#print("Percentage of the text: ",percentage)
