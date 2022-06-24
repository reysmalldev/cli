import sys
import os
# Project consts
HTML = 'index.html'
CSS = 'style.css'
JS = 'script.js'
temp = open('C:/workspace/python/cli/assets/template.html')
# arguments for receive on script is executed
entry = sys.argv[1::]

#a function to create the project
def fronta() :
    print('Creating You Project... ')
    dire = input('Type Project name: ')
    # test if this folder already exists
    if os.path.exists(dire) :
        # write cls in terminal
        os.system('cls')
        print(f'The project({dire}) Already exists...')
        option = input('Want create with other name?(y/n)')
        if option == 'y' :
            fronta()
        else:
            print('Program finished...')
            # finish execution
            sys.exit
    else:
        # create a folder with dire variable value(name)
        os.mkdir(dire)
    #open dire folder and create a html file
    with open(f'{dire}/{HTML}','w') as f_i:
        # read template file and save in temp1 var
        temp1 = temp.read()
        # write in f_i(html file) a same text that exists in template
        f_i.write(temp1)
        # close file
        f_i.close()
        # create css file
        open(f'{dire}/{CSS}', 'w')
        # create javascript file
        open(f'{dire}/{JS}', 'w')

def default():
    print('Use "creator --html to create a Html Project!..."')

# Verifyer of flags
# test if entrance lenght is more larger of 2 
# relember... the first argument is directory path where you executed command
if len(entry) == 2:
    # test if second argument is a parammeter --html
    if entry[1] == '--html' :
        # if is run function fronta()
        fronta()
else:
    # if lenght is smaller than 2 run default function
    default()
