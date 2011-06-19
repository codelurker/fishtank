import os
import time

def createTimer():
	if os.name == "posix":
		return TimerPosix()
	elif os.name == "nt":
		return TimerNT()
	else:
		print("Unable to create timer for platform '%s'" % (os.name))
		return None

class Timer:
	def __init__(self):
		self.last = 0
		self.current = 0
		self.update()

	def update(self):
		self.last = self.current
		self.current = self.getTime()

	def getTime(self):
		return 0

	def getDelta(self):
		return self.current - self.last

class TimerPosix(Timer):
	def __init__(self):
		super(TimerPosix, self).__init__()

	def getTime(self):
		return time.time()

class TimerNT:
	def __init__(self):
		super(TimerNT, self).__init__()

	def getTime(self):
		return time.clock()

