class Agent:
	def __init__(self):
		self.centerX = 0
		self.centerY = 0

	def setBoundaries(self, minX, minY, maxX, maxY):
		self.minX = minX
		self.minY = minY
		self.maxX = maxX
		self.maxY = maxY

	def update(self, x, y):
		pass

	def getCenter(self):
		return (self.centerX, self.centerY)
