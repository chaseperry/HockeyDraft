# HockeyDraft
Automated Draft script and logic. Currently using this for season ticket draft between friends. 

Avs draft Read Me:

***The user will have to set their current directory in the python script in line 2 of the Avs_Draft.py file
 and use a standard python implementation/python kernel and NOT anaconda for running this script.*** 

Versions:
Make sure you are running python 3.9.12 or earlier. 
Install Pandas, numpy, openpyxl, and jinja2 using pip. 
All current versions of these packages as of 9/9/2023 should work. 

How it Works:
The purpose of this script is to automate a custom draft with any number of people for any number of picks that 
are organized into a csv file. The draft order will be randomly shuffled and then continue through a snake draft
until all the picks are completed. At this point, all the picks that were selected by each person will be displayed,
then the total results will be saved to an excel file with a name that is chosen. 

If you use the "AvSchedule_23_24.csv" file to run the draft, you can test the script. Also, make sure to copy over the
file/folder structure so that you get the draft_module incorporated correctly. 

Organization:
Draft setup and user input is handled through the Avs_Draft.py script. 
A small package was created with functions in the "draft_package" folder and then the "draft_module.py" script. 


