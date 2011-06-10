import data.fish

class Fish:
	def __init__(self, ascii):
		self.ascii = ascii
		self.x = 0
		self.y = 0

	def render(self, scr):
		scr.addstr(self.x, self.y, self.ascii)

	def setPos(self, x, y):
		self.x = x
		self.y = y

class SmallFish(Fish):
	def __init__(self):
		super(SmallFish, self).__init__(data.fish.fish)
