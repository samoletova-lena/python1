import os

allfiles=os.listdir(os.getcwd())
print(allfiles)

for i in allfiles:
        if os.path.isdir(i):
                print(i)


