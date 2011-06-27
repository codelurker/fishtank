import random
import logging
import math
import pdb
from src.agent import Agent

class PredatorAgent(Agent):
	def __init__(self):
		super(PredatorAgent, self).__init__()
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

	def hunt(self, fishes):
		if len(fishes) is 0:
			return (None, None)

		cx = 0
		cy = 0
		cfish = None
		closest = 1000 # TODO: make it a constant

		for fish in fishes:
			fx, fy = fish.getPos()
			dist = math.hypot(self.x - fx, self.y - fy)
			if dist < closest:
				closest = dist
				cx = fx
				cy = fy
				cfish = fish

		if int(self.x) is int(cx) and int(self.y) is int(cy):
			fishes.remove(cfish)
			return (0, 0)
		else:
			return self.goTo(cx, cy, 0, 0)

	def update(self, x, y, fishes):
		self.x = x
		self.y = y
		#mx = random.randint(-1, 1)
		mx = 0
		my = 0

		mx, my = self.hunt(fishes)
		if mx is None:
			mx = 0
			my = 0

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
