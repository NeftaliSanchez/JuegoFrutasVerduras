import os 

abspath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(abspath)

rpython = f'{fileDirectory}\\env\\Scripts\\python.exe'
fgame = f'{fileDirectory}\\main.py'
os.system(rpython + ' '+ fgame)