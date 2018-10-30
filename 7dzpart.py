import random

#список от 1 до 90
list_number=list(range(1,91))
users={"user":1, "computer":2}

class Card():
	def __init__(self):
		pass
	
	def make_card(self):
		self.card_number=random.sample(list_number,15)

	def printcard(self):
		self.srt1=[]
		self.str2=[]
		self.srt3=[]
		self.cardnumberm=[]
		self.str1=self.card_number[0:5]
		self.str2=self.card_number[5:10]
		self.str3=self.card_number[10:15]
		self.str1.sort()
		self.str2.sort()
		self.str3.sort()
		self.i=0
		while self.i != 4:
			self.ind1=0
			self.ind2=0
			self.ind3=0
			self.ind1=random.randint(0,4)
			self.str1.insert(self.ind1,"--")
			self.ind2=random.randint(0,4)
			self.str2.insert(self.ind2,"--")
			self.ind3=random.randint(0,4)
			self.str3.insert(self.ind3,"--")
			self.i+=1
		self.cardnumberm=self.str1+self.str2+self.str3
		print("\n",self.cardnumberm[0:9],"\n",self.cardnumberm[9:18],"\n",self.cardnumberm[18:27])
		
	
def boch_num():
	listboch=list_number
	oldlistboch=[]
	Bochonok=0
	Bochonok=random.choice(listboch)
	print("Выпал бочонок:",Bochonok)
	listboch.remove(Bochonok)
	oldlistboch.append(Bochonok)
	print("Бочонков в мешке",len(listboch))

def isnumberincard(card_number):
	for el in card_number:
		if boch_num in card_number:
			cardindex=card_number.index(boch_num)
			card_number.pop(cardindex)
			card_number.insert(cardindex,"X")
			print(card_number)
	else:
		pass

def do_game():
	usercard=Card()
	usercard.make_card()
	compcard=Card()
	compcard.make_card()
	useranswer=input("Играем?, да - Y, нет- N")
	if useranswer == "Y":
		boch_num()
		usercard.printcard()
		compcard.printcard()
		isnumberincard(usercard)
		isnumberincard(compcard)
	else:
		exit


do_game()




