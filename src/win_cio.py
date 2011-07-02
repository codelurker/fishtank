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

import time
import logging
import WConio

class WinCIO(object):
	key_esc   = chr(27)
	key_left  = "left"
	key_right = "right"
	key_up    = "up"
	key_down  = "down"
	key_a     = 'a'
	key_f     = 'f'
	key_p     = 'p'
	key_q     = 'q'

	def init(self):
		pass

	def cleanup(self):
		WConio.textmode()

	def has_colors(self):
		logging.info("WinCIO.has_colors returns always True")
		return True

	def clear(self):
		WConio.clrscr()

	def drawAscii(self, x, y, ascii, color=""):
		if color is "green":
			col = WConio.GREEN
		if color is "cyan":
			col = WConio.CYAN
		if color is "red":
			col = WConio.RED
		if color is "yellow":
			col = WConio.YELLOW
		else:
			col = WConio.WHITE

		WConio.gotoxy(x, y)
		WConio.textcolor(col)
		WConio.cputs(ascii)

	def refresh(self):
		time.sleep(0.01)

	def getKey(self):
		if WConio.kbhit():
			return WConio.getkey()

	def getTermWidth(self):
		#return WConio.gettextinfo()[8]
		return WConio.gettextinfo()[2]

	def getTermHeight(self):
		#return WConio.gettextinfo()[7]
		return WConio.gettextinfo()[3]

