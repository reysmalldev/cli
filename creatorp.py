import sys
import os
# Project consts
HTML = 'index.html'
CSS = 'style.css'
JS = 'script.js'
temp = open('C:/workspace/python/cli/assets/template.html')

entry = sys.argv[1::]

def fronta() :
    print('----------------- Criando seu projeto ------------------')
    dire = input('Insira o nome do projeto: ')
    if os.path.exists(dire) :
        print('O projeto(newProject) já existe...')
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
