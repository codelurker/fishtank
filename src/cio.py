import os

def createCio():
	if os.name == "posix":
		from src.curses_cio import CursesCIO
		return CursesCIO()
	elif os.name == "nt":
		from src.win_cio import WinCIO
		return WinCIO()
	else:
		print("Unsupported platform '%s' - no console I/O to use" % (os.name))
		return None

