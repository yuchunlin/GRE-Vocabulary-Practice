import os
import random

def editmode(c):
	if c.lower() == "y" or c.lower() == "yes":
		new_word = input("Please enter the new word: ")
		new_def  = input("Please enter a one word definition: ")
		cont     = input("Would you like to add a new word? \n Y/N: \t")
		editmode(cont)
	elif c.lower() == 'n' or c.lower() == 'no':
		print("Returning to main menu.")
		GREPractice()
	else:
		print("I'm sorry, that is not a valid option.")
		cont     = input("Would you like to add a new word? \n Y/N: \t")
		editmode(cont)


def GREPractice():

	print("Welcome to the GRE Practice Script.")
	print("Press 1 to enter flashcard practice.")
	print("Press 2 to edit the vocabulary databse.")
	print("Press anything else to leave the script.")
	mode = input("Please enter the desired mode: ")
	mode = str(mode)
	if mode == '1':
		print("Entering practice mode.")
	elif mode == '2':
		print("Entering edit mode.")
		editmode('Y')
	else:
		print("Exiting program.")
		exit()
	#with open("vocabularylist.txt") as f:

GREPractice()

