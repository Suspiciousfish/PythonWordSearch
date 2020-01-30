import string
import random
import time

NewLine1 = []
NewLine2 = []
NewLine3 = []
MasterGrid = []

''' This makes the list of all known words available to the word search program, and splits each word so we can make comparisons for later'''
openFile = open('words.txt', 'r')
with openFile as x:
	MasterDictionary = [words for line in x for words in line.split()]

''' Defining what ASCII letters we are going to use for the word search grid'''
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyz'


''' This Function defines the word search board and the displays it to the user'''

def CREATING_THE_GRID():
	
	for j in range (0,15):
		group1 = (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters))
		group2 = (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters))
		group3 = (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters)) + (random.choice(string.ascii_letters))
		(grid) = group1 + group2 + group3
		
		MasterGrid.append(grid)

	print((str(len(MasterGrid))) + ' |  is the length of master grid' )


''' THis Function searches for words '''
def SEARCHING_ALG():
	for y in MasterGrid:
	


CREATING_THE_GRID()
print(MasterGrid)

SEARCHING_ALG()
