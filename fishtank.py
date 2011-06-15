#!/usr/bin/python

import os
import sys
from src.fish import SmallFish

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
		if ch == cio.key_left and y > 0:
			y -= 1
		if ch == cio.key_right and y < (cio.getTermWidth()-2):
			y += 1
		if ch == cio.key_up and x > 0:
			x -= 1
		if ch == cio.key_down and x < (cio.getTermHeight()-1):
			x += 1
		if ch == cio.key_q:
			exit = True

	cio.cleanup()

