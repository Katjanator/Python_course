# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def rock_paper_scissors(user_input, computer_input):
    
 #   user_input = input("Please decide: paper, rock or scissors?") 
  #  computer_input = input("Please decide: paper, rock or scissors?") 
    
    if user_input is 'rock' and computer_input is 'paper':
        return 'computer wins'
    if user_input is 'paper' and computer_input is 'rock':
        return 'user wins' 
    if user_input is 'scissors' and computer_input is 'paper':
        return 'user wins'
    if user_input is 'paper' and computer_input is 'scissors':
        return 'computer wins'
    if user_input is 'scissors' and computer_input is 'rock':
        return 'computer wins'
    if user_input is 'rock' and computer_input is 'scissors':
        return 'user wins'
    if user_input is 'rock' and computer_input is 'rock':
        return 'tied game'
    if user_input is 'paper' and computer_input is 'paper':
        return 'tied game'
    if user_input is 'scissors' and computer_input is 'scissors':
        return 'tied game'
    
if __name__ == "__main__":
    possibilities = ['rock', 'paper', 'scissors']
    for user_input in possibilities:
        for computer_input in possibilities:
            if user_input == computer_input:
                assert rock_paper_scissors(user_input, computer_input) == 'tied game'
    print('alles gut')
    
     # als dictionary versuchen !!!
    # set--> nur ein element von jedem in einer Liste 
    #immer schreiben for element in my_list[1:5]:
    #element