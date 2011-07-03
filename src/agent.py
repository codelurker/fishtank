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

class Agent(object):
	def __init__(self):
		self.centerX = 0
		self.centerY = 0

		self.owner = None
		self.x = 0
		self.y = 0

		self.speed = 1

	def setBoundaries(self, minX, minY, maxX, maxY):
		self.minX = minX
		self.minY = minY
		self.maxX = maxX
		self.maxY = maxY

	def getCenter(self):
		return (self.centerX, self.centerY)

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

	def update(self, owner):
		self.owner = owner
		(self.x, self.y) = owner.getPos()

	def move(self, dt, mx, my):
		if self.owner is not None:

			# Keep the fish in the tank
			if self.x <= self.minX and mx is -1:
				mx = 0
			if self.x >= self.maxX and mx is 1:
				mx = 0
			if self.y <= self.minY and my is -1:
				my = 0
			if self.y >= self.maxY and my is 1:
				my = 0

			# Move the fish
			self.owner.move(mx * self.speed * dt, my * self.speed * dt)

