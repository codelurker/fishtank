#!/usr/bin/python

import os
import sys
import src.cio
from src.tank import Tank

if __name__ == "__main__":
	cio = src.cio.createCio()
	if cio is None:
		sys.exit(1)

	cio.init()

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

