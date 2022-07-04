# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 23:38:08 2022

@author: Anupama
"""


f1 = open("C:/Users/Anupama/Documents/output.txt")
  # Path of second file
f2 = open("C:/Users/Anupama/Documents/output2.txt")
   

file1_words = set()

file2_words = set()


for word in f1.read().split():

    file1_words.add(word.lower())

for word in f2.read().split():

    file2_words.add(word.lower())


common_words = file1_words.intersection(file2_words)

merge_file = open("C:/Users/Anupama/Documents/merge.txt", mode="w")

for word in common_words:
    word = word + ", "
    merge_file.write(word)

merge_file.close()
