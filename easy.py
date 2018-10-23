import os

curdir=os.getcwd()

def makedir(DirName_make,quantity):
    i=1
    listdir=[]
    while i<=quantity:
        dirr = os.path.join(os.getcwd(),DirName_make + str(i))
        try:
            os.mkdir(dirr)
            listdir.append(dirr)
        except FileExistsError:
            print('Такая папка уже существует')
        i=i+1
    return listdir


def deldir(DirName_del):
    dirr = os.path.join(os.getcwd(),DirName_del)
    try:
        os.rmdir(dirr)
        print("Папка удалена")
    except FileNotFoundError:
        print('Такая папка уже удалена')
        

def opendir(DirName_open):
    os.chdir(DirName_open)
    strtoret = "Открыта папка {}".format(os.path.basename(os.getcwd()))
    return strtoret


def DirView(DirName_to_view):
    os.chdir(curdir)
    allfiles=os.listdir(DirName_to_view)
    print("Содержимое папки {}".format(DirName_to_view), allfiles)


if __name__ == "__main__":
    DirName_make=input("Введите название папки, которую нужно создать")
    quantity = int(input("Сколько папок нужно создать",))
    print("Создано:", makedir(DirName_make,quantity))

    DirName_del=input("Введите название папки, которую нужно удалить")
    deldir(DirName_del)    

    DirName_open = input("Какую папку нужно открыть,")
    print(opendir(DirName_open))

    DirName_to_view = input("Какую папку посмотрим?,")
    DirView(DirName_to_view)