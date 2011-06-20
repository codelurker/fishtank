from src.object import Object
import data.food

class Food(Object):
	def __init__(self):
		super(Food, self).__init__()

		self.ascii = data.food.food

	def draw(self, cio):
		cio.drawAscii(int(self.x), int(self.y), self.ascii)

