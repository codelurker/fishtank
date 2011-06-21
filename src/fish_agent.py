import random
import logging
import math
from src.agent import Agent

class FishAgent(Agent):
	def __init__(self):
		super(FishAgent, self).__init__()
		self.x = 0
		self.y = 0

	def goTo(self, gx, gy, tx, ty):
		mx = 0
		my = 0

		if int(self.x) < gx-tx:
			mx = 1
		if int(self.x) > gx+tx:
			mx = -1
		if int(self.y) < gy-ty:
			my = 1
		if int(self.y) > gy+ty:
			my = -1

		return (mx, my)

	def school(self, fishes):
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

		return self.goTo(cx, cy, 5, 3)

	def feed(self, food):
		if len(food) is 0:
			return (None, None)

		cx = 0
		cy = 0
		cf = None
		closest = 1000 # TODO: make it a constant

		for ff in food:
			fx, fy = ff.getPos()
			dist = math.hypot(self.x - fx, self.y - fy)
			if dist < closest:
				closest = dist
				cx = fx
				cy = fy
				cf = ff

		if int(self.x) is int(cx) and int(self.y) is int(cy):
			food.remove(cf)
			return (0, 0)
		else:
			return self.goTo(cx, cy, 0, 0)

	def update(self, x, y, fishes, food):
		self.x = x
		self.y = y
		#mx = random.randint(-1, 1)
		mx = 0
		my = 0

		mx, my = self.feed(food)
		if mx is None:
			mx, my = self.school(fishes)

		# Keep the fish in the tank
		if self.x <= self.minX and mx is -1:
			mx = 0
		if self.x >= self.maxX and mx is 1:
			mx = 0
		if self.y <= self.minY and my is -1:
			my = 0
		if self.y >= self.maxY and my is 1:
			my = 0

		return (mx, my)
