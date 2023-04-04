import os 

abspath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(abspath)

rpython = f'{fileDirectory}\\env\\Scripts\\python.exe'
fgame = f'{fileDirectory}\\gameplataform.py'
if os.system(rpython+' '+fgame) != 0: os.system("py"+' '+fgame)
