import os
import sys
print('sys.argv = ', sys.argv)
def print_help():
	print("help - получение справки")
	print("mkdir <dir_name> - создание директории")
	print("ping - тестовый ключ")
	print("copy - копия файла")
	print("remfile - удаление файла")
	print("ls - где я")

def ping():
	print("pong")

def ls(): #текущая директория
	print("Вы здесь", os.getcwd())

def make_dir():
	if not dir_name:
		print("Необходимо указать имя директории вторым параметром")
		return
	dir_path = os.path.join(os.getcwd(), dir_name)
	try:
		os.mkdir(dir_path)
		print('директория {} создана'.format(dir_name))
	except FileExistsError:
		print('директория {} уже существует'.format(dir_name))

def copy():
	f = open(newfilename, 'w+', encoding='UTF-8') 
	f.write(open(filename).read())
	f.close()


def remfile():
	f = os.path.join(os.getcwd(),filename_del)
	try:
		os.remove(f)
		print("Файл удален")
	except FileNotFoundError:
		print('Такого файла и не было(')

def cd(): #смена директории
	os.chdir(cddir)
	print("Вы в папке", os.path.basename(cddir))
	
do = {
	"help": print_help,
	"mkdir": make_dir,
	"ping": ping,
	"copy": copy,
	"del": remfile,
	"change": cd,
	"ls": ls,
	}
try:
	dir_name = sys.argv[2] #создание папки
except IndexError:
	dir_name = None

try:
	filename = sys.argv[2] #создание файла
	if len(sys.argv) > 3:
		newfilename = sys.argv[3]
except FileExistsError:
	newfilename = None

try:
	filename_del = sys.argv[2] #удаление файла
except FileNotFoundError:
	filename = None

try:
	cddir = sys.argv[2] #смена директории
except IndexError:
	cddir = None

try:
	key = sys.argv[1]
except IndexError:
	key = None
if key:
	if do.get(key): #возвращает по ключу значение из словаря do (если значение есть)
		do[key]()
	else:
		print("Задан неверный ключ")
		print("Укажите ключ help для получения справки")

