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
