import sys
import os
# Project consts
HTML = 'index.html'
CSS = 'style.css'
JS = 'script.js'
temp = open('C:/workspace/python/cli/assets/template.html')

entry = sys.argv[1::]

def fronta() :
    print('----------------- Creating Project ------------------')
    dire = input('Type Project name: ')
    if os.path.exists(dire) :
        os.system('cls')
        print(f'The project({dire}) Already exists...')
        option = input('Want create with other name?(y/n)')
        if option == 'y' :
            fronta()
        else:
            print('Program finished...')
            sys.exit
    else:
        os.mkdir(dire)
    with open(f'{dire}/{HTML}','w') as f_i:
        temp1 = temp.read()
        f_i.write(temp1)
        f_i.close()
        open(f'{dire}/{CSS}', 'w')
        open(f'{dire}/{JS}', 'w')
# Verifyer of flags
if entry[1] == '--html' :
    fronta()
