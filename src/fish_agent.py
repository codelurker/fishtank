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

from src.agent import Agent

class FishAgent(Agent):
	def __init__(self):
		super(FishAgent, self).__init__()
		self.speed = 8

	def school(self, fishes):
		self.owner.changeHead("normal")
		self.speed = 8

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

	def feed(self, foods):
		if len(foods) is 0 or self.owner is None:
			return (None, None)
		self.owner.changeHead("normal")
		self.speed = 8

		food, dist, cx, cy = super(FishAgent, self).getClosest(foods)

		if int(self.x) is int(cx) and int(self.y) is int(cy):
			foods.remove(food)
			self.owner.changeHead("eat")
			return (0, 0)
		else:
			return self.goTo(cx, cy, 0, 0)

	def run(self, predators):
		if len(predators) is 0:
			return (None, None)
		self.owner.changeHead("run")
		self.speed = 12

		predator, dist, cx, cy = super(FishAgent, self).getClosest(predators)

		if dist < 5:
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

	def update(self, owner, dt, fishes, food, predators):
		super(FishAgent, self).update(owner)

		# A hierarchy of the behavioral rules
		# Rules are sorted according to their priority
		mx, my = self.run(predators)
		if mx is None:
			mx, my = self.feed(food)
		if mx is None:
			mx, my = self.school(fishes)

		# Move the fish
		super(FishAgent, self).move(dt, mx, my)

