import sys
import os

dire = 'newProject'
html = 'index.html'
css = 'style.css'
js = 'script.js'
temp = open('C:/workspace/python/cli/assets/template.html')

entry = sys.argv[1::]

def fronta() :
    os.mkdir(dire)
    arch = open('{path}/{n1}'.format(path = dire, n1 = html) ,'w')
    temp1 = temp.read()
    arch.write(temp1)
    arch.close()
    open('{path}/{n1}'.format(path = dire, n1 = css), 'w')
    open('{path}/{n1}'.format(path = dire, n1 = js), 'w')

# Verifyer of flags
if entry[1] == '--html' :
    fronta()
