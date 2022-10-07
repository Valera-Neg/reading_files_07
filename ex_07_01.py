# Exercise 1: Write a program to read through a file and print the 
# contents of the file (line by line) all in upper case. 
# Executing the program will look as follows:

# <python shout.py 
# Enter a file name : mbbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AS.ZA
# ........ so on

# You can download the file from
# www.pythonlearn.com/code3/mbox-short.txt


fileName = input("Enter a filename: ")
try:
    fileHand = open(fileName)
except:
    print("File cannot be opened: ", fileName)
    quit()
for line in fileHand:   
  res = line.rstrip().upper()
  print(res)     

