# Copyright (C) 2011 by Ondrej Martinak <omartinak@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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

	def run(self, predators):
		if len(predators) is 0:
			return (None, None)

		# TODO: get closest je duplicitni
		cx = 0
		cy = 0
		closest = 1000 # TODO: make it a constant

		for predator in predators:
			fx, fy = predator.getPos()
			dist = math.hypot(self.x - fx, self.y - fy)
			if dist < closest:
				closest = dist
				cx = fx
				cy = fy

		if closest < 5:
			if self.x - cx > 0:
				mx = 1
			else:
				mx = -1
			if self.y - cy > 0:
				my = 1
			else:
				my = -1

			return (mx, my)
		else:
			return (None, None)

	def update(self, x, y, fishes, food, predators):
		self.x = x
		self.y = y
		#mx = random.randint(-1, 1)
		mx = 0
		my = 0

		mx, my = self.run(predators)
		if mx is None:
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
