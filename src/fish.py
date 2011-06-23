from src.object import Object
from src.fish_agent import FishAgent
from src.predator_agent import PredatorAgent
import data.fish

class Fish(Object):
	def __init__(self, ascii):
		super(Fish, self).__init__()

		self.speed = 1
		self.ascii = ascii

	def setBoundaries(self, minX, minY, maxX, maxY):
		self.agent.setBoundaries(minX, minY, maxX, maxY)

	def draw(self, cio):
		cio.drawAscii(int(self.x), int(self.y), self.ascii)
		xx, yy = self.agent.getCenter()
		cio.drawAscii(int(xx), int(yy), "X")

class SmallFish(Fish):
	def __init__(self):
		super(SmallFish, self).__init__(data.fish.fish["left"])

		self.agent = FishAgent()
		self.speed = 8

	def move(self, x, y):
		super(SmallFish, self).move(x, y)
		if x < 0:
			self.ascii = data.fish.fish["left"]
		if x > 0:
			self.ascii = data.fish.fish["right"]

	def update(self, dt, fishes, food):
		mx, my = self.agent.update(self.x, self.y, fishes, food)
		self.move(mx * self.speed * dt, my * self.speed * dt)

class PredatorFish(Fish):
	def __init__(self):
		super(PredatorFish, self).__init__(data.fish.predator["left"])

		self.agent = PredatorAgent()
		self.speed = 8

	def move(self, x, y):
		super(PredatorFish, self).move(x, y)
		if x < 0:
			self.ascii = data.fish.predator["left"]
		if x > 0:
			self.ascii = data.fish.predator["right"]

	def update(self, dt, fishes):
		mx, my = self.agent.update(self.x, self.y, fishes)
		self.move(mx * self.speed * dt, my * self.speed * dt)
