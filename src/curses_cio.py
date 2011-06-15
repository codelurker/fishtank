import curses

class CursesCIO:
	key_left   = curses.KEY_LEFT
	key_right  = curses.KEY_RIGHT
	key_up     = curses.KEY_UP
	key_down   = curses.KEY_DOWN
	key_q      = ord('q')

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
		self.screen.addstr(x, y, ascii)

	def refresh(self):
		self.screen.refresh()

	def getKey(self):
		return self.screen.getch()

	def getTermWidth(self):
		return self.screen.getmaxyx()[1]

	def getTermHeight(self):
		return self.screen.getmaxyx()[0]
