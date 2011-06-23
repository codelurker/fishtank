import random
from src import timer
from src.object import Object
from src.fish import SmallFish, PredatorFish
from src.food import Food

class Tank(Object):
	def __init__(self, width, height):
		super(Tank, self).__init__()

		self.width = width
		self.height = height

		self.timer = timer.createTimer()

		self.fishes = []
		self.predators = []
		self.food = []

	def update(self, cio, key):
		self.timer.update()

		if key == cio.key_a:
			smallFish = SmallFish()

			smallFish.setBoundaries(2, 2, self.width-2, self.height-3)
			x = random.randint(1, self.width-2)
			y = random.randint(1, self.height-3)
			smallFish.setPos(x, y)

			self.fishes.append(smallFish)

		if key == cio.key_p:
			predatorFish = PredatorFish()

			predatorFish.setBoundaries(2, 2, self.width-2, self.height-3)
			x = random.randint(1, self.width-2)
			y = random.randint(1, self.height-3)
			predatorFish.setPos(x, y)

			self.predators.append(predatorFish)

		if key == cio.key_f:
			food = Food()
			x = random.randint(1, self.width-2)
			y = random.randint(1, self.height-3)
			food.setPos(x, y)

			self.food.append(food)

		for predator in self.predators:
			predator.update(self.timer.getDelta(), self.fishes)

		for fish in self.fishes:
			fish.update(self.timer.getDelta(), self.fishes, self.food)

	def draw(self, cio):
		for y in range(0, self.height-1):
			cio.drawAscii(0, y, '|')
			cio.drawAscii(self.width-1, y, '|')

		for x in range(1, self.width-1):
			cio.drawAscii(x, 0, '~')
			cio.drawAscii(x, self.height-2, '-')

		for food in self.food:
			food.draw(cio)
		for fish in self.fishes:
			fish.draw(cio)
		for predator in self.predators:
			predator.draw(cio)

