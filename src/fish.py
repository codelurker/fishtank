from src.object import Object
from src.fish_agent import FishAgent
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

	def update(self, dt):
		mx, my = self.agent.update(self.x, self.y)
		self.move(mx * self.speed * dt, my * self.speed * dt)
