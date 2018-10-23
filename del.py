import os
i=1
while i<=10:
    dir_1 = os.path.join(os.getcwd(), 'NewDir_{}'.format(i))
    try:
        os.rmdir(dir_1)
    except FileNotFoundError:
        print('Такая папка уже удалена')
    i+=1
