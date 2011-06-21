#!/usr/bin/python

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

