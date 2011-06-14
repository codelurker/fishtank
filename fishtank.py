#!/usr/bin/python

import os
import sys
from fish import SmallFish

if __name__ == "__main__":
	if os.name == 'posix':
		from src.curses_cio import CursesCIO
		cio = CursesCIO()
	elif os.name == 'nt':
		from src.win_cio import WinCIO
		cio = WinCIO()
	else:
		print("Unsupported platform '%s' - no console I/O to use" % (os.name))
		sys.exit(1)

	cio.init()

	smallFish = SmallFish()
	smallFish.setPos(20, 20)

	exit = False
	x = 20
	y = 20
	while not exit:
		cio.clear()
		smallFish.setPos(x, y)
		smallFish.draw(cio)
		cio.refresh()

		ch = cio.getKey()
		#if ch == curses.KEY_LEFT and x > 0:
		#	y -= 1
		#if ch == curses.KEY_RIGHT:
		#	y += 1
		#if ch == curses.KEY_UP and y > 0:
		#	x -= 1
		#if ch == curses.KEY_DOWN:
		#	x += 1
		if ch == ord('q'):
			exit = True

	cio.cleanup()

