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
from src import misc

class Agent(object):
	def __init__(self):
		self.owner = None
		self.dt = 0
		self.x = 0
		self.y = 0

		self.speed = 1
		self.step = 0
		self.moveX = 0
		self.moveY = 0

	def goTo(self, gx, gy):
		dx = gx - self.x
		dy = gy - self.y

		if math.fabs(dx) < self.step:
			mx = dx
		else:
			mx = self.step * misc.sign(dx)
		if math.fabs(dy) < self.step:
			my = dy
		else:
			my = self.step * misc.sign(dy)

		return (mx, my)

	def getClosest(self, objects):
		cx = 0
		cy = 0
		cobj = None
		closest = 1000 # TODO: make it a constant

		for obj in objects:
			ox, oy = obj.getPos()
			dist = math.hypot(self.x - ox, self.y - oy)
			if dist < closest:
				closest = dist
				cobj = obj
				cx = ox
				cy = oy

		return (cobj, closest, cx, cy)

	def update(self, owner, dt):
		self.owner = owner
		self.dt = dt
		self.x, self.y = owner.getPos()

		self.step = self.speed * dt

	def move(self):
		if self.owner is not None:
			self.owner.move(self.moveX, self.moveY)

