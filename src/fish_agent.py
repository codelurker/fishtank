import random
import math
from src.agent import Agent

class FishAgent(Agent):
	def __init__(self):
		super(FishAgent, self).__init__()

	def goTo(self, x, y, gx, gy):
		mx = 0
		my = 0

		if x < gx:
			mx = 1
		if x > gx:
			mx = -1
		if y < gy:
			my = 1
		if y > gy:
			my = -1

		return (mx, my)

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

		return self.goTo(x, y, cx, cy)

	def feed(self, x, y, food):
		cx = 0
		cy = 0
		closest = 1000
		for ff in food:
			fx, fy = ff.getPos()
			dist = math.hypot(x-fx, y-fx)
			if dist < closest:
				closest = dist
				cx = fx
				cy = fy

		return self.goTo(x, y, cx, cy)

	def update(self, x, y, fishes, food):
		#mx = random.randint(-1, 1)
		mx = 0
		my = 0

		#mx, my = self.school(x, y, fishes)
		mx, my = self.feed(x, y, food)

		# Keep the fish in the tank
		if x <= self.minX and mx is -1:
			mx = 0
		if x >= self.maxX and mx is 1:
			mx = 0
		if y <= self.minY and my is -1:
			my = 0
		if y >= self.maxY and my is 1:
			my = 0

		return (mx, my)
