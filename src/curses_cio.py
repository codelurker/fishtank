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

import curses

class CursesCIO:
	key_esc   = 27
	key_left  = curses.KEY_LEFT
	key_right = curses.KEY_RIGHT
	key_up    = curses.KEY_UP
	key_down  = curses.KEY_DOWN
	key_a     = ord('a')
	key_f     = ord('f')
	key_p     = ord('p')
	key_q     = ord('q')

	def init(self):
		self.screen = curses.initscr()
		curses.noecho()
		curses.cbreak()
		curses.curs_set(0)
		self.screen.keypad(1)

		curses.halfdelay(1) # block for 0.1s

	def cleanup(self):
		self.screen.keypad(0)
		curses.curs_set(1)
		curses.nocbreak()
		curses.echo()
		curses.endwin()

	def clear(self):
		# TODO: test self.screen for validity?
		self.screen.erase()

	def drawAscii(self, x, y, ascii):
		# x and y axis are switched for curses
		self.screen.addstr(y, x, ascii)

	def refresh(self):
		self.screen.refresh()

	def getKey(self):
		return self.screen.getch()

	def getTermWidth(self):
		return self.screen.getmaxyx()[1]

	def getTermHeight(self):
		return self.screen.getmaxyx()[0]

