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

import math
import random
import time
from src.agent import Agent
from src import misc
import logging

# Ooooh, dirtyyyy
walkX = 0
walkY = 0
walkLast = 0

class FishAgent(Agent):
	def __init__(self):
		super(FishAgent, self).__init__()
		self.speed = 8
		walkX = 0
		walkY = 0

	def randomWalk(self):
		self.owner.changeHead("normal")
		self.speed = 8

		# Ooooh, dirtyyyy
		global walkX, walkY, walkLast
		if time.time()-walkLast > random.randint(1, 3):
			walkX = random.choice((-1, 1))
			walkY = random.choice((-1, 1))
			walkLast = time.time()

		mx = walkX * self.step
		my = walkY * self.step

		return (mx, my)

	def school(self, fishes):
		if len(fishes) is 0:
			return (None, None)
		self.owner.changeHead("normal")
		self.speed = 8

		cx = 0
		cy = 0
		for fish in fishes:
			#if fish is not self.owner:
			fx, fy = fish.getPos()
			cx += fx
			cy += fy

		cx /= len(fishes)
		cy /= len(fishes)

		dist = math.hypot(self.x - cx, self.y - cy)
		if dist < 8:
			return (None, None)
		else:
			return self.goTo(cx, cy)

	def scatter(self, fishes):
		if len(fishes) is 0:
			return (None, None)
		self.owner.changeHead("normal")
		self.speed = 8

		for fish in fishes:
			if fish is not self.owner:
				fx, fy = fish.getPos()
				dist = math.hypot(self.x - fx, self.y - fy)
				if dist <= 0.9:
					mx = random.choice((-1, 1))
					my = random.choice((-1, 1))
					return (self.step * mx, self.step * my)

		return (None, None)

	def feed(self, foods):
		if len(foods) is 0:
			return (None, None)
		self.owner.changeHead("normal")
		self.speed = 8

		food, dist, cx, cy = super(FishAgent, self).getClosest(foods)

		if dist <= 1:
			foods.remove(food)
			self.owner.changeHead("eat")
			return (0, 0)
		else:
			return self.goTo(cx, cy)

	def run(self, predators):
		if len(predators) is 0:
			return (None, None)
		self.owner.changeHead("run")
		self.speed = 10

		predator, dist, cx, cy = super(FishAgent, self).getClosest(predators)

		if dist < 5:
			mx = self.step * misc.sign(self.x - cx)
			my = self.step * misc.sign(self.y - cy)

			return (mx, my)
		else:
			return (None, None)

	def update(self, owner, dt, fishes, food, predators):
		super(FishAgent, self).update(owner, dt)

		# A hierarchy of behavior rules
		# Rules are sorted according to their priority
		newFish = False
		mx, my = self.scatter(fishes)
		if mx is None:
			mx, my = self.run(predators)
		if mx is None:
			mx, my = self.feed(food)
			if mx is 0 and my is 0:
				newFish = True
		if mx is None:
			mx, my = self.school(fishes)
		if mx is None:
			mx, my = self.randomWalk()

		# Store the movement, will be used in postUpdate
		self.moveX = mx
		self.moveY = my

		return newFish

