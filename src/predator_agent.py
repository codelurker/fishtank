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

class PredatorAgent(Agent):
	def __init__(self):
		super(PredatorAgent, self).__init__()
		self.speed = 8

	def hunt(self, fishes):
		if len(fishes) is 0 or self.owner is None:
			return (None, None)
		self.owner.changeHead("hunt")
		self.speed = 16

		fish, dist, cx, cy = super(PredatorAgent, self).getClosest(fishes)

		if dist <= 1.4:
			fishes.remove(fish)
			self.owner.changeHead("eat")
			return (0, 0)
		elif dist < 6:
			return self.goTo(cx, cy, 0, 0)
		else:
			return (None, None)

	def findPrey(self, fishes):
		if len(fishes) is 0 or self.owner is None:
			return (None, None)
		self.owner.changeHead("normal")
		self.speed = 8

		fish, dist, cx, cy = super(PredatorAgent, self).getClosest(fishes)

		return self.goTo(cx, cy, 0, 0)

	def sleep(self):
		self.owner.changeHead("sleep")
		self.speed = 4
		return (0, self.step)

	def update(self, owner, dt, fishes):
		super(PredatorAgent, self).update(owner, dt)

		# A hierarchy of behavior rules
		# Rules are sorted according to their priority
		mx, my = self.hunt(fishes)
		if mx is None:
			mx, my = self.findPrey(fishes)
		if mx is None:
			mx, my = self.sleep()

		# Store the movement, will be used in postUpdate
		self.moveX = mx
		self.moveY = my

