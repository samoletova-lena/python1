 #Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
class Triangle:
	def __init__(self,x1,y1,x2,y2,x3,y3):
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
		self.x3=x3
		self.y3=y3

	def square(self):
		z1=0
		h1=0
		z2=0
		h2=0
		sg=0
		z1=self.x1-self.x3
		h1=self.y1-self.y3
		z2=self.x2-self.x3
		h2=self.y2-self.y3
		sg=(z1*h2-z2*h1)/2
		if sg<0:
			sg*(-1)
		return sg

	def perim(self):
		AB=0
		BC=0
		CA=0
		ABC=0
		AB=sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		BC=sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
		CA=sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
		ABC=AB+BC+CA
		return ABC


	def high(self):
		AB=0
		BC=0
		CA=0
		HAB=0
		AB=sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		BC=sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
		CA=sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
		z1=0
		h1=0
		z2=0
		h2=0
		sg=0
		z1=self.x1-self.x3
		h1=self.y1-self.y3
		z2=self.x2-self.x3
		h2=self.y2-self.y3
		sg=(z1*h2-z2*h1)/2
		HAB=2*sg/AB
		return HAB
	

Tr1=Triangle(1,1,4,2,0,4)
print(Tr1.square())
print(Tr1.perim())
print(Tr1.high())

Tr2=Triangle(0,1,3,3,0,3)
print(Tr2.perim())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapetze:
	def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
		
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
		self.x3=x3
		self.y3=y3
		self.x4=x4
		self.y4=y4
		AB=None
		BC=None
		CD=None
		DA=None
		# AB=sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		# BC=sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
		# CD=sqrt((self.x4-self.x3)**2+(self.y4-self.y3)**2)
		# DA=sqrt((self.x1-self.x1)**2+(self.y1-self.y4)**2)

	def rb(self):
		# AB=0
		# BC=0
		# CD=0
		# DA=0
		AB=sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		BC=sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
		CD=sqrt((self.x4-self.x3)**2+(self.y4-self.y3)**2)
		DA=sqrt((self.x1-self.x1)**2+(self.y1-self.y4)**2)
		if AB==CD or BC==DA:
			print("Трапеция равнобочная")
		else:
			print("Кособочная")


	def AB(self):
		#AB=0
		AB=sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		print("Длина стороны AB", AB)

	def perim(self):
		AB=sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		BC=sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
		CD=sqrt((self.x4-self.x3)**2+(self.y4-self.y3)**2)
		DA=sqrt((self.x1-self.x1)**2+(self.y1-self.y4)**2)
		per=AB+BC+CD+DA
		print("Периметр", per)

	def sg(self):
		h1=0
		h2=0
		if self.x1==self.x4 and self.x2==self.x3:
			print("BC и AD основания трапеции")
			BC=sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
			DA=sqrt((self.x1-self.x1)**2+(self.y1-self.y4)**2)
			h1=self.x1
			h2=self.y2
			high=sqrt((self.x2-h1)**2+(self.y2-h2)**2)
			sgtrap =((BC+DA)**2)/2*high
			print("Площадь трапеции", sgtrap)
		else:
			pass 



Trap1=Trapetze(0,0,3,1,3,3,0,4)
Trap1.rb()
Trap1.AB()
Trap1.perim()
Trap1.sg()


