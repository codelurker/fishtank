import random
from src.agent import Agent

class FishAgent(Agent):
	def __init__(self):
		super(FishAgent, self).__init__()

	def school(self, x, y, fishes):
		cx = 0
		cy = 0
		for fish in fishes:
			fx, fy = fish.getPos()
			cx += fx
			cy += fy

		cx /= len(fishes)
		cy /= len(fishes)

		self.centerX = cx
		self.centerY = cy

		mx = 0
		my = 0
		if x < cx-5:
			mx = 1
		if x > cx+5:
			mx = -1
		if y < cy-5:
			my = 1
		if y > cy+5:
			my = -1

		return (mx, my)

	def update(self, x, y, fishes):
		#mx = random.randint(-1, 1)
		mx = 0
		my = 0

		mx, my = self.school(x, y, fishes)

		if x <= self.minX and mx is -1:
			mx = 0
		if x >= self.maxX and mx is 1:
			mx = 0
		if y <= self.minY and my is -1:
			my = 0
		if y >= self.maxY and my is 1:
			my = 0

		return (mx, my)
