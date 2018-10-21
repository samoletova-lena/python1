import os
i=1
while i<=10:
        dirr = os.path.join(os.getcwd(), 'NewDir_{}'.format(i))
        try:
                os.mkdir(dirr)
        except FileExistsError:
                print('Такая папка уже существует')
        i=i+1



