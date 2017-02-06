class Animal(object):
	has4legs = {'qstn':"* Does it has four legs? ",'value':False}
	has2legs = {'qstn':"* Does it has two legs? ",'value':False}
	carnivorous = {'qstn':'* Is it a carnivorous? ','value':False}
	herbivorous = {'qstn':'* Is it a herbivorous? ','value':False}
	omnivorous = {'qstn':'* Is it omnivorous? ','value':False}
	color1 = {'qstn':'* Is black and white in color? ','value':False}
	fly = {'qstn':'* Can fly? ','value':False}
	lay_eggs = {'qstn':'* Can lay eggs? ','value':False}
	def __init__(self,name,has4legs=False,has2legs=False,carnivorous=False,herbivorous=False,omnivorous=False,color1=False,fly=False,lay_eggs=False):
		self.name = name
		self.has4legs = {'qstn':"* Does it has four legs?",'value':has4legs}
		self.has2legs = {'qstn':"* Does it has two legs?",'value':has2legs}
		self.carnivorous = {'qstn':'* Is it a carnivorous?','value':carnivorous}
		self.herbivorous = {'qstn':'* Is it a herbivorous?','value':herbivorous}
		self.omnivorous = {'qstn':'* Is it omnivorous?','value':omnivorous}
		self.color1 = {'qstn':'* Is black and white in color?','value':color1}
		self.fly = {'qstn':'* Can fly?','value':fly}
		self.lay_eggs = {'qstn':'* Can lay eggs? ','value':lay_eggs}

	def to_dict(self):
		return {'has4legs':self.has4legs['value'],'has2legs':self.has2legs['value'],'carnivorous':self.carnivorous['value'],
		'herbivorous':self.herbivorous['value'],'omnivorous':self.omnivorous['value'],
		'color1':self.color1['value'],'fly':self.fly['value'],'lay_eggs':self.lay_eggs['value']}
			 
oLion = Animal('lion',has4legs=True,carnivorous=True)
oParrot = Animal('parrot',has2legs=True,omnivorous=True,fly=True)
# print oParrot.__dict__
oCrow = Animal('crow',has2legs=True,carnivorous=True,fly=True)
oCat = Animal('cat',has4legs=True,omnivorous=True)
oMan = Animal('man',has2legs=True,omnivorous=True)
oZebra = Animal('zebra',has4legs=True,herbivorous=True,color1=True)
oPenguin = Animal('penguin',has2legs=True,carnivorous=True,color1=True,lay_eggs=True)
lAll_animals = [oLion,oParrot,oCrow,oCat,oMan,oZebra,oPenguin]
def question():
 		print "Answer Yes or No (y/n) to the following questions about the animal you have in mind"
		lFilteredAnimals = []
		sAnswer = raw_input(Animal.has4legs['qstn'])
		for oAnimal in lAll_animals:
			if sAnswer=='y': # or answer start with Y or y
				if oAnimal.has4legs['value']:
					lFilteredAnimals.append(oAnimal)
			else:
				if not oAnimal.has4legs['value']:
					lFilteredAnimals.append(oAnimal)
		lFilteredAnimals1 =[]
		sAnswer = raw_input(Animal.carnivorous['qstn'])
		for oAnimal in lFilteredAnimals:
			if sAnswer =='y':
				if oAnimal.carnivorous['value']:
					lFilteredAnimals1.append(oAnimal)
			else:
				if not oAnimal.carnivorous['value']:
					lFilteredAnimals1.append(oAnimal)
		if len(lFilteredAnimals1)<=1:
			for ofinal in lFilteredAnimals1:
				print "You were thinking about: ",ofinal.name
				return
		lFilteredAnimals2 = []
		sAnswer = raw_input(Animal.omnivorous['qstn'])
		for oAnimal in lFilteredAnimals1:
			if sAnswer =='y':
				if oAnimal.omnivorous['value']:
					lFilteredAnimals2.append(oAnimal)
			else:
				if not oAnimal.omnivorous['value']:
					lFilteredAnimals2.append(oAnimal)
		if len(lFilteredAnimals2)  <= 1:
			for ofinal in lFilteredAnimals2:
				print "You were thinking about: ",ofinal.name
				return
		if len(lFilteredAnimals2) < 1:
			print "Incorrect Guess.Try again"
			sAnswer = raw_input(Animal.omnivorous['qstn'])
			for oAnimal in lFilteredAnimals1:
				if sAnswer =='y':
					if oAnimal.omnivorous['value']:
						lFilteredAnimals2.append(oAnimal)
				else:
					if not oAnimal.omnivorous['value']:
						lFilteredAnimals2.append(oAnimal)
		lFilteredAnimals3 = []
		sAnswer = raw_input(Animal.fly['qstn'])
		for oAnimal in lFilteredAnimals2:
			if sAnswer == 'y':
				if oAnimal.fly['value']:
					lFilteredAnimals3.append(oAnimal)
			else:
				if not oAnimal.fly['value']:
					lFilteredAnimals3.append(oAnimal)
		if len(lFilteredAnimals3)<=1:
			for ofinal in lFilteredAnimals3:
				print "you were thinking about: ",ofinal.name
				return
		if len(lFilteredAnimals3) < 1:
			print "Incorrect Guess.Try again"
			sAnswer = raw_input(Animal.fly['qstn'])
			for oAnimal in lFilteredAnimals2:
				if sAnswer == 'y':
					if oAnimal.fly['value']:
						lFilteredAnimals3.append(oAnimal)
				else:
					if not oAnimal.fly['value']:
						lFilteredAnimals3.append(oAnimal)
		lFilteredAnimals4 = []
		sAnswer = raw_input(Animal.lay_eggs['qstn'])
		for oAnimal in lFilteredAnimals3:
			if sAnswer == 'y':
				if oAnimal.lay_eggs['value']:
					lFilteredAnimals4.append(oAnimal)
			else:
				if not oAnimal.lay_eggs['value']:
					lFilteredAnimals4.append(oAnimal)
		for oAnimal in lFilteredAnimals4:
			print 'You were thinking about:', oAnimal.name
		if len(lFilteredAnimals4) < 1:
			print "Incorrect Guess.Try again"
			sAnswer = raw_input(Animal.lay_eggs['qstn'])
			for oAnimal in lFilteredAnimals3:
				if sAnswer == 'y':
					if oAnimal.lay_eggs['value']:
						lFilteredAnimals4.append(oAnimal)
				else:
					if not oAnimal.lay_eggs['value']:
						lFilteredAnimals4.append(oAnimal)
			for oAnimal in lFilteredAnimals4:
				print 'You were thinking about:', oAnimal.name
while True:
		question()
		sContinue = raw_input("Do you want to continue the game?(y/n) ")
		if sContinue == 'y':
			question()
		elif sContinue == 'n':
			print 'Thank you'
			break
		else:
			print "Wrong choice"
			sContinue = raw_input("Do you want to continue the game?(y/n) ")
	