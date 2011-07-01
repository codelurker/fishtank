#!/usr/bin/python

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

import sys
import logging
import src.cio
from src.tank import Tank

if __name__ == "__main__":
	logging.basicConfig(filename="fish.log", level=logging.INFO)

	cio = src.cio.createCio()
	if cio is None:
		sys.exit(1)

	cio.init()
	logging.info("initialized")

	if not cio.has_colors():
		logging.info("colors are not supported")

	tank = Tank(cio.getTermWidth(), cio.getTermHeight())

	exit = False
	while not exit:
		key = cio.getKey()

		cio.clear()
		tank.update(cio, key)
		tank.draw(cio)
		cio.refresh()

		if key == cio.key_q or key == cio.key_esc:
			exit = True

	cio.cleanup()
	logging.info("cleaned up")

