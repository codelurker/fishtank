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

		self.agent = None

		self.ascii = ascii
		self.dir = "left"
		self.head = "normal"

	def setBoundaries(self, minX, minY, maxX, maxY):
		self.minX = minX
		self.minY = minY
		self.maxX = maxX
		self.maxY = maxY

	def draw(self, cio):
		anim = self.dir + "_" + self.head
		cio.drawAscii(int(self.x), int(self.y), self.ascii[anim], self.color)
		xx, yy = self.agent.getCenter()
		cio.drawAscii(int(xx), int(yy), "X")

	def move(self, x, y):
		super(Fish, self).move(x, y)

		# Set the correct direction
		if x < 0:
			self.dir = "left"
		if x > 0:
			self.dir = "right"

		# Keep the fish in the tank
		if self.x < self.minX:
			self.x = self.minX
		if self.x > self.maxX:
			self.x = self.maxX
		if self.y < self.minY:
			self.y = self.minY
		if self.y > self.maxY:
			self.y = self.maxY

	def changeHead(self, head):
		self.head = head

	def postUpdate(self):
		if self.agent is not None:
			self.agent.move()

class SmallFish(Fish):
	def __init__(self, color=""):
		super(SmallFish, self).__init__(data.fish.fish, color)

		self.agent = FishAgent()

	def update(self, dt, fishes, food, predators):
		self.agent.update(self, dt, fishes, food, predators)

class PredatorFish(Fish):
	def __init__(self, color=""):
		super(PredatorFish, self).__init__(data.fish.predator, color)

		self.agent = PredatorAgent()

	def update(self, dt, fishes):
		self.agent.update(self, dt, fishes)

