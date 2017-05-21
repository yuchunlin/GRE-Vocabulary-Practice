#!/usr/bin/env python
import os, random

def editmode():
    with open("data.txt", "a") as f:
        new_word = input("Please enter the new word: \t")
        new_def  = input("Please enter a one word definition: \t")
        ### here, we need to open the vocabulary list and make a new entry ###
        f.write("{0}, {1}, \n".format(new_word, new_def))  
           
def GREPractice():
    not_exit = True
    while not_exit:
        print("Welcome to the GRE Practice Script.")
        print("Press 1 to enter flashcard practice.")
        print("Press 2 to edit the vocabulary databse.")
        print("Press anything else to leave the script.")
        mode = input("Please enter the desired mode: ")
        mode = str(mode)
        if mode   == '1':
            print("Entering practice mode.")
        elif mode == '2':
            print("Entering edit mode.")
            edit_requested = True
            while edit_requested:
                editmode()
                request_invalid = True
                while request_invalid:
                    cont = input("Would you like to add a new word? \n Y/N: \t")
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