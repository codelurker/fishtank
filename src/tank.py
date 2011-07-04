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
from src.timer import Timer
from src.fish import SmallFish, PredatorFish
from src.food import Food
from src.grass import Grass

class Tank:
	def __init__(self, width, height):
		logging.info("Preparing fishtank (size %d, %d)..." % (width, height))
		# Prepare window and tank dimensions
		self.win_w = width - 1
		self.win_h = height - 1
		self.tank_w = self.win_w - 1
		self.tank_h = self.win_h - 2

		# Create a timer for the simulation
		self.timer = Timer()

		# Prepare empty lists for tank objects
		self.fishes = []
		self.predators = []
		self.food = []
		self.grass = []

		# Generate some grass in the tank
		logging.info("Generating grass...")
		self.generateGrass(20)

		# Generate an initial population of fish
		logging.info("Generating fish population...")
		self.generateFish(10)

		# Prepare a help text
		self.help = "[q]uit, [c]yan fish, [f]ood, [p]redator"

	def generateGrass(self, density):
		# Compute how much grass to create
		grassNum = int(self.tank_w / density)

		# Create each grass
		for i in range(0, grassNum):
			x = random.randint(1, self.tank_w)
			y = self.tank_h

			grass = Grass("green")
			grass.setPos((x, y))
			grass.setHeight(random.randint(1, self.tank_h))

			self.grass.append(grass)

	def generateFish(self, density):
		# Create each fish
		for i in range (0, density):
			smallFish = SmallFish("cyan")
			self.initFish(smallFish)
			self.fishes.append(smallFish)

	def randPos(self):
		x = random.randint(1, self.tank_w)
		y = random.randint(1, self.tank_h)
		return (x, y)

	def initFish(self, fish):
		fish.setBoundaries(1, 1, self.tank_w, self.tank_h)
		fish.setPos(self.randPos())

	def update(self, cio, key):
		self.timer.update()

		# 'c' key - creates new cyan small fish
		if key == cio.key_c:
			smallFish = SmallFish("cyan")
			self.initFish(smallFish)
			self.fishes.append(smallFish)

		# 'p' key - creates new predator fish
		if key == cio.key_p:
			predatorFish = PredatorFish("red")
			self.initFish(predatorFish)
			self.predators.append(predatorFish)

		# 'f' key - adds some food for the fishes
		if key == cio.key_f:
			food = Food("yellow")
			food.setPos(self.randPos())
			self.food.append(food)

		# Update all the objects in the tank
		for predator in self.predators:
			predator.update(self.timer.getDelta(), self.fishes)
		for fish in self.fishes:
			newFish = fish.update(self.timer.getDelta(), self.fishes, self.food, self.predators)
			if newFish:
				smallFish = SmallFish("cyan")
				smallFish.setBoundaries(1, 1, self.tank_w, self.tank_h)
				smallFish.setPos(fish.getPos())
				self.fishes.append(smallFish)

		# Move the objects (movements were stored in update)
		for predator in self.predators:
			predator.postUpdate()
		for fish in self.fishes:
			fish.postUpdate()

	def drawHelp(self, cio):
		cio.drawAscii(0, self.win_h, self.help)

	def draw(self, cio):
		# Draw the tank outline and water
		for y in range(0, self.win_h):
			cio.drawAscii(0, y, '|')
			cio.drawAscii(self.win_w, y, '|')

		for x in range(1, self.win_w):
			cio.drawAscii(x, 0, '~', "blue")
			cio.drawAscii(x, self.win_h-1, '-')

		# Draw objects in the tank
		for grass in self.grass:
			grass.draw(cio)
		for food in self.food:
			food.draw(cio)
		for fish in self.fishes:
			fish.draw(cio)
		for predator in self.predators:
			predator.draw(cio)

		# Draw a help text
		self.drawHelp(cio)

