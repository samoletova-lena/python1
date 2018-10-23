import os

from easy import opendir
from easy import makedir
from easy import DirView
from easy import deldir


def makechoice():
    answer=int(input("\nВыберите действие, которое нужно сделать:\n" 
                 "1. Перейти в папку;\n" 
                 "2. Просмотреть содержимое текущей папки;\n" 
                 "3. Удалить папку;\n" 
                 "4. Создать папку\n"
                 "5. Выход\n", ))
    if answer == 1:
        DirName_open = input("Какую папку нужно открыть,")
        print(opendir(DirName_open))
        makechoice()
    elif answer == 2:
        DirName_to_view = input("Какую папку посмотрим?,")
        DirView(DirName_to_view)
        makechoice()
    elif answer == 3:
        DirName_del=input("Введите название папки, которую нужно удалить")
        deldir(DirName_del)    
        makechoice()
    elif answer == 4:
        DirName_make=input("Введите название папки, которую нужно создать")
        quantity = int(input("Сколько папок нужно создать",))
        print("Создано:", makedir(DirName_make,quantity))
        makechoice()
    elif answer == 5:
        #exit(0)
        pass
    else:
        print("Вы ввели что-то не то")

makechoice()

   

