#!/usr/bin/env python

import sys
import tty
import termios
import os

class _Getchar:
	def __init__(self):
		pass

	def __call__(self): 
		# Unix getchar()
		fd = sys.stdin.fileno()
		old = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old)
		return ch

def main():
	getchar = _Getchar()
	index = 0

	FILENAME = '../input/' + raw_input("Enter filename (Enter for default): ")
	
	if not os.path.isfile(FILENAME):
		# Load default
		FILENAME = '../input/kernel.txt'
	
	try:
		SPEED = int(raw_input("Enter speed (Enter for default): "))
		if SPEED <= 0:
			raise IndexError
	except ValueError, IndexError:
		# Load default
		SPEED = 3
	
	# Clear screen
	os.system('clear')

	with open(FILENAME) as f:
		lines = ''.join(f.readlines())

		while index < len(lines) - SPEED:
			c = getchar()

			# Escape key
			if ord(c) is 27:
				break

			sys.stdout.write(lines[index:index + SPEED])
			index += SPEED
	
	sys.stdout.write('\n')
	return 0

if __name__ == '__main__':
    main()  
