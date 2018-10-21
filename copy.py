import os
import sys

thisfile = sys.argv[0]
print(thisfile)
f = open("copy2.py", 'w+', encoding='UTF-8') 
f.write(open(thisfile).read())
f.close()
