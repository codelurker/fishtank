class Object:
	def __init__(self):
		self.x = 0.0
		self.y = 0.0

	def update(self, dt):
		pass

	def draw(self, cio):
		pass

	def getPos(self):
		return (self.x, self.y)

	def setPos(self, x, y):
		self.x = x
		self.y = y

	def move(self, x, y):
		self.x += x
		self.y += y
