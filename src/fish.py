from src.object import Object
import data.fish

class Fish(Object):
	def __init__(self, ascii):
		super(Fish, self).__init__()

		self.ascii = ascii

	def draw(self, cio):
		cio.drawAscii(self.x, self.y, self.ascii)

class SmallFish(Fish):
	def __init__(self):
		super(SmallFish, self).__init__(data.fish.fish)
