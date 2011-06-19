import random
from src.agent import Agent

class FishAgent(Agent):
	def __init__(self):
		super(FishAgent, self).__init__()

	def update(self, x, y):
		mx = random.randint(-1, 1)
		my = 0

		if x <= self.minX and mx is -1:
			mx = 0
		if x >= self.maxX and mx is 1:
			mx = 0
		if y <= self.minY and my is -1:
			my = 0
		if y >= self.maxY and my is 1:
			my = 0

		return (mx, my)
