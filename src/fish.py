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

from src.object import Object
from src.fish_agent import FishAgent
from src.predator_agent import PredatorAgent
import data.fish

class Fish(Object):
	def __init__(self, ascii, color=""):
		super(Fish, self).__init__(color)

		self.speed = 1
		self.ascii = ascii

	def setBoundaries(self, minX, minY, maxX, maxY):
		self.agent.setBoundaries(minX, minY, maxX, maxY)

	def draw(self, cio):
		cio.drawAscii(int(self.x), int(self.y), self.ascii, self.color)
		xx, yy = self.agent.getCenter()
		cio.drawAscii(int(xx), int(yy), "X")

class SmallFish(Fish):
	def __init__(self, color=""):
		super(SmallFish, self).__init__(data.fish.fish["left"], color)

		self.agent = FishAgent()
		self.speed = 8

	def move(self, x, y):
		super(SmallFish, self).move(x, y)
		if x < 0:
			self.ascii = data.fish.fish["left"]
		if x > 0:
			self.ascii = data.fish.fish["right"]

	def update(self, dt, fishes, food, predators):
		mx, my = self.agent.update(self.x, self.y, fishes, food, predators)
		self.move(mx * self.speed * dt, my * self.speed * dt)

class PredatorFish(Fish):
	def __init__(self, color=""):
		super(PredatorFish, self).__init__(data.fish.predator["left"], color)

		self.agent = PredatorAgent()
		self.speed = 8

	def move(self, x, y):
		super(PredatorFish, self).move(x, y)
		if x < 0:
			self.ascii = data.fish.predator["left"]
		if x > 0:
			self.ascii = data.fish.predator["right"]

	def update(self, dt, fishes):
		mx, my = self.agent.update(self.x, self.y, fishes)
		self.move(mx * self.speed * dt, my * self.speed * dt)
