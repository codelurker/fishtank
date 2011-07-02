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
from src.timer import Timer
from src.object import Object
from src.fish import SmallFish, PredatorFish
from src.food import Food
from src.grass import Grass

class Tank(Object):
	def __init__(self, width, height):
		super(Tank, self).__init__()

		self.width = width
		self.height = height

		self.timer = Timer()

		self.fishes = []
		self.predators = []
		self.food = []
		self.grass = []

		grass_num = int(self.width / 20)
		for i in range(0, grass_num):
			x = random.randint(1, self.width-2)
			y = self.height-3

			grass = Grass("green")
			grass.setPos(x, y)
			grass.setHeight(random.randint(1, self.height-3))

			self.grass.append(grass)

	def update(self, cio, key):
		self.timer.update()

		if key == cio.key_a:
			smallFish = SmallFish("cyan")

			smallFish.setBoundaries(2, 2, self.width-2, self.height-3)
			x = random.randint(1, self.width-2)
			y = random.randint(1, self.height-3)
			smallFish.setPos(x, y)

			self.fishes.append(smallFish)

		if key == cio.key_p:
			predatorFish = PredatorFish("red")

			predatorFish.setBoundaries(2, 2, self.width-2, self.height-3)
			x = random.randint(1, self.width-2)
			y = random.randint(1, self.height-3)
			predatorFish.setPos(x, y)

			self.predators.append(predatorFish)

		if key == cio.key_f:
			food = Food("yellow")
			x = random.randint(1, self.width-2)
			y = random.randint(1, self.height-3)
			food.setPos(x, y)

			self.food.append(food)

		for predator in self.predators:
			predator.update(self.timer.getDelta(), self.fishes)

		for fish in self.fishes:
			fish.update(self.timer.getDelta(), self.fishes, self.food, self.predators)

	def draw(self, cio):
		for y in range(0, self.height-1):
			cio.drawAscii(0, y, '|')
			cio.drawAscii(self.width-1, y, '|')

		for x in range(1, self.width-1):
			cio.drawAscii(x, 0, '~')
			cio.drawAscii(x, self.height-2, '-')

		for grass in self.grass:
			grass.draw(cio)
		for food in self.food:
			food.draw(cio)
		for fish in self.fishes:
			fish.draw(cio)
		for predator in self.predators:
			predator.draw(cio)

