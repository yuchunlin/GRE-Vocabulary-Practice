#!/usr/bin/env python
import os, random

def editmode():
    with open("data.txt", "a") as f:
        new_word = raw_input("Please enter the new word: \t")
        new_word = new_word.upper()
        new_def  = raw_input("Please enter a definition: \t")
        new_def = new_def.lower()
        ### here, we need to open the vocabulary list and make a new entry ###
        f.write("{0}, {1}, \n".format(new_word, new_def))  


def generatequestion():
     with open("data.txt", "r") as f:
     	word_definition_pairs = [line.split(",") for line in f]
     	rand_option = random.randint(0, len(word_definition_pairs) - 1)
     	word = word_definition_pairs[rand_option][0]
     	definition = word_definition_pairs[rand_option][1]
     	possible_answers = []
     	possible_answers.append(definition)
     	correct_choice = 0
     	for i in range(0, 4):
     		elem = word_definition_pairs[random.randint(0, len(word_definition_pairs) - 1)][1]
     		while elem in possible_answers:
     			elem = word_definition_pairs[random.randint(0, len(word_definition_pairs) - 1)][1]
     		possible_answers.append(elem)
     	print("The word is:\t" + word)
     	for j in range(1, len(possible_answers) + 1): 
     		choice = random.choice(possible_answers)
     		if choice == definition:
     			correct_choice = j
     		possible_answers.remove(choice)
     		print("" + str(j) + ":\t" + choice)
     	return (correct_choice, definition)



def GREPractice():
    not_exit = True
    while not_exit:
        print("\n\nWelcome to the GRE Practice Script.\n\n")
        print("Press 1 to enter flashcard practice.")
        print("Press 2 to edit the vocabulary database.")
        print("Press anything else to leave the script.\n")
        mode = raw_input("Please enter the desired mode: \t")
        mode = str(mode)
        if mode   == '1':
            print("\nEntering practice mode.\n")
            print("Please select the correct definition, or type exit to return to the main menu.\n")
            continue_test = True
            while continue_test:
            	(w, d) = generatequestion()
            	w = str(w)
            	d = str(d)
            	d = d.split(" ", 1)[1]
            	answer = raw_input("Your answer: \t Definition ")
            	if answer.lower() == "exit":
            		continue_test = False
            	elif answer.lower() == w:
            		print("Correct!\n")
            	else:
            		quotes = '"'
            		print("Incorrect. The correct answer is " + quotes + d + quotes + ".\n")

        elif mode == '2':
            print("\nEntering edit mode. \n")
            edit_requested = True
            while edit_requested:
                editmode()
                request_invalid = True
                while request_invalid:
                    cont = raw_input("\nWould you like to add a new word? \n Y/N: \t")
                    if cont.lower() == "y":
                        request_invalid = False                    
                    elif cont.lower() =="n":
                        request_invalid = False
                        edit_requested = False
                    else:
                        print("I'm sorry, that is not a valid option.")                
            print("Returning to main menu.")
        else:
            not_exit = False
            print("Exiting program.")
            
if __name__ == "__main__":
    GREPractice()



"""
dictionary = {}
open('data.txt','r') as f:
    for line in f.readlines():
        word, definition = parse_line(line)
        if word in dictionary:
            continue
        else:
            dictionary[word] = definition 
        
        
def parse_line(line):
    word, definition = line.split(',').strip()
    return word, definition
    """