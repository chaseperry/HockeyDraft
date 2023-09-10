import random
import numpy as np
import pandas as pd


# the following three functions are basic printing functions for ease of code reading. 
def showframe(df):
    print(df)

def showorder(list):
    print(list)

def shuffle(list):
    random.shuffle(list)
    print(list)

#This function checks to see if a row was already selected
def space_check(df,position):

    try:
        if df['Person'][int(position)]=='':
            return False
        else:
            return True
    except:
        return True

#This function returns the number of picks by counting all of the name picks in each name frame
#Leaving this a bit more complicated than need be to return named dataframes with everyones picks in the future
def picks(list,df):
    
    name_dict={}
    picks=0
    for name in list:
        name_dict[name]=pd.DataFrame(df[df['Person']==name])
    
    for key in name_dict:
        name_frame=name_dict[key]
        picks=picks+name_frame['Person'].count()

    return picks

#Logic that moves the turns up and down and has the user pick their draft selection. 
def moveturn(turn,number_people,list,number_of_games,df):

        if turn == 0:
            turn = turn +1
            
        
        elif turn == number_people+1:
            turn = turn -1
            
            
        else:
            
            choice = input(f'{list[turn-1]} please pick a game, using the index number.')

            while not isinstance(choice,int):
                try:
                    choice=int(choice)
                except:
                    choice = input(f'{list[turn-1]} please pick a game, using the index number.')

            while int(choice)>number_of_games:
                print(f'pick valid position 0-{number_of_games-1}')
                choice = input(f'{list[turn-1]} please pick a game, using the index number.')
            
            while space_check(df,choice):
                print('someone has that game!')
                choice = input(f'{list[turn-1]} please pick a game, using the index number.')
                if picks(list,df)>=number_of_games:
                    break
            
            df['Person'][int(choice)]=list[turn-1]
            print(df[df['Person']==list[turn-1]])
        
        return(df)
                