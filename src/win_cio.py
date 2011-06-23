import time
import WConio

class WinCIO:
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

	def clear(self):
		WConio.clrscr()

	def drawAscii(self, x, y, ascii):
		WConio.gotoxy(x, y)
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

