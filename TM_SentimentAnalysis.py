# -*- coding: utf-8 -*-
"""
@author: Hidam Nganthoiba Singh
"""
#Project-1
from textblob import TextBlob

Feedback1 = 'Cold Coffee is awesome.'
Feedback2 = 'Cold Coffee was bad.'
Feedback3 = 'Cold Coffee was Ok.'

b1 = TextBlob(Feedback1)
b2 = TextBlob(Feedback2)
b3 = TextBlob(Feedback3)

print(b1.sentiment)
print(b2.sentiment)
print(b3.sentiment)

#Project-2
#Import Library
import pandas as pd

#Load data
dataset = pd.read_csv('F:/CPMA/pywork/pydata/Obama.txt')
#Converting data into string format
dataset = dataset.to_string(index = False) 
type(dataset)

b1 =TextBlob(dataset)
print(b1.sentiment)

#-------------------Cleaning the data-----------------------------------
import re
dataset = re.sub("[^A-Za-z0-9]+"," ",dataset)

#----------------------Tokenization--------------------------------------------
import nltk
nltk.download()

for word in dataset[:500]:
    print(word, sep='',end='')
    
from nltk.tokenize import word_tokenize
Tokens = word_tokenize(dataset)
print (Tokens)

#No. of tokens in the dataset
len(Tokens)

#Freq of occurence of distinct elements
from nltk.probability import FreqDist
fdist = FreqDist()

for word in Tokens:
    fdist[word.lower()]+=1
fdist
fdist.plot(20)

#-------------------------Stemming----------------------------------------
from nltk.stem import PorterStemmer
pst=PorterStemmer()
pst.stem("having")


#-------------Remove the Stop Words---------------------
import nltk.corpus

#Enlisting the stopwords present in English lang
stopwords = nltk.corpus.stopwords.words('english')
stopwords[0:10]

#Getting rid of stopwords
for FinalWord in Tokens:
    if FinalWord not in stopwords:
        print(FinalWord)
        
#Classification of words as Positive, Negative & Neutral

#Calculating final Sentiment Score
b2 =TextBlob(FinalWord)
print(b2.sentiment)
