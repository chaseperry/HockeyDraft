#set current directory in order to pickup the files in the folder. 
import os
import sys
os.chdir(r'C:\Users\chase\Documents\python\ForGithub\AvsDraft')
sys.path.append(r'C:\Users\chase\Documents\python\ForGithub\AvsDraft')

#Modules needed are numpy, pandas, the python random library, and the system 
#All of the sublogic functions are organized in the draft functions module
import numpy as np
import pandas as pd
import random
import sys
from draft_package.draft_module import showframe, moveturn, picks


#input the csv document that has all the games
csv = input(f'Please type in the file name with games that is in this folder.\n'
             'Note: The format of the games needs to match previous years\n')

#This block will setup the dataframe with an additional column that tracks the person who drafts each game
while True:
    
    try:
        #Read in the csv document. 
        avs_games = pd.read_csv(csv)
        avs_games.style.set_properties(**{'text-align': 'left'})  
        avs_games['Person'] =""
        number_of_games=avs_games['Person'].count()
        break

    # if the dataframe isn't read in have the user specify the file again.
    except:
        
        print('Either the file is not in this folder or the name was mispelled, please try again\n')

        csv = input(f'Please type in the file name with games that is in this folder.\n'
                'Note: The format of the games needs to match previous years\n')

# show the avs_games dataframe and make sure it looks good. 
print(avs_games)

user_input = input('Alright, do the games look good? (yes/no),\n' 
                   'no will exit the program so you can fix the file\n')

#if the game doesnt look good they can input no to kill the program and fix it. 
if user_input.lower() == "no":
    sys.exit()

#if things look good, get the names of everyone drafting. 
else:
    names=input("Please type the names of everyone drafting, separated by commas.\n")
    names = names.split(',')

    #This block makes sure you are happy with the names
    while True:
        
        userinput=input(f'Does {names} look right? y/n\n')
        
        if userinput.lower() == "y":
            break
        
        else:
            names=input("Please the names of everyone drafting, separated by commas.\n")
            names = names.split(', ')

    #If it all looks good, shuffle the order, print it, and then figure out the number of people 
    order=names
    random.shuffle(order)
    print(f'Here is your order {order}!')
    number_people=len(order)

    #Right now turn has to be defined as 0 in the main code for the moveturn function to work. 
    turn = 0


#This logic will run through the move turns function until everything is picked, following a snake draft
while picks(order,avs_games) < number_of_games:
     
    #make the turns go up until you hit the end of the order
    while turn <=len(order):

        if picks(order,avs_games)>=number_of_games:
            break 

        moveturn(turn,number_people,order,number_of_games,avs_games)
        showframe(avs_games)
        turn = turn+1
        
            
    #make the turns go down until you hit the end of the order     
    while turn >0:
        
        if picks(order,avs_games)>=number_of_games:
            break

        moveturn(turn,number_people,order,number_of_games,avs_games)
        showframe(avs_games)
        turn = turn-1
        
 

#After the draft is complete, show everyone what games they got, then create a file with all the pick data. 
print('All the games are taken, here is who got what.\n')

name_dict={}

for name in order:
    name_dict[name]=pd.DataFrame(avs_games[avs_games['Person']==name])

for name in name_dict:
        print(name_dict[name])

filename=input('Please type in the file you want to save the picks to.\n'
               'Note, dont include file extension\n')


avs_games.to_excel(os.getcwd()+'//'+str(filename)+'.xlsx',sheet_name='Sheet1')