# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:53:56 2022

@author: Anupama
"""


import string 
from nltk.corpus import stopwords 
 
with open("C:/Users/Anupama/Documents/file2.txt.txt", "r") as inFile, open("C:/Users/Anupama/Documents/output2.txt","w") as outFile: 
	for line in inFile.readlines(): 
	    print(" ".join([word for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split()  
        	if len(word) >=4 and word not in stopwords.words('english')]), file=outFile) 