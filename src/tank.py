import random
from src import timer
from src.object import Object
from src.fish import SmallFish

class Tank(Object):
	def __init__(self, width, height):
		super(Tank, self).__init__()

		self.width = width
		self.height = height

		self.timer = timer.createTimer()

		self.objects = []

	def update(self, cio, key):
		self.timer.update()

		if key == cio.key_a:
			smallFish = SmallFish()

			x = random.randint(1, self.width-2)
			y = random.randint(1, self.height-2)
			smallFish.setPos(x, y)

			self.objects.append(smallFish)

		for obj in self.objects:
			obj.update(self.timer.getDelta())

	def draw(self, cio):
		for y in range(0, self.height-1):
			cio.drawAscii(0, y, '|')
			cio.drawAscii(self.width-1, y, '|')

		for x in range(1, self.width-1):
			cio.drawAscii(x, 0, '~')
			cio.drawAscii(x, self.height-2, '-')

		for obj in self.objects:
			obj.draw(cio)

