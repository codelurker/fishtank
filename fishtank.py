#!/usr/bin/python

import curses
from fish import SmallFish

if __name__ == "__main__":
	myscreen = curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
	myscreen.keypad(1)

	curses.halfdelay(1) # block for 0.1s

	smallFish = SmallFish()
	smallFish.setPos(20, 20)

	exit = False
	x = 20
	y = 20
	while not exit:
		myscreen.erase()
		smallFish.setPos(x, y)
		smallFish.render(myscreen)
		myscreen.refresh()

		ch = myscreen.getch()
		if ch == curses.KEY_LEFT and x > 0:
			y -= 1
		if ch == curses.KEY_RIGHT:
			y += 1
		if ch == curses.KEY_UP and y > 0:
			x -= 1
		if ch == curses.KEY_DOWN:
			x += 1
		if ch == ord('q'):
			exit = True

	myscreen.keypad(0)
	curses.curs_set(1)
	curses.nocbreak()
	curses.echo()
	curses.endwin()

