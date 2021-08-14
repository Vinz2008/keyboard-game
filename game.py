import time
import termios, os, sys
tiret = "-"
barre = "|"
slash = "/"
pose = 0
espace = False
nbDePoint = 0
def flush_to_stdout(c):
    if c == b'\x7f':
        sys.stdout.write("\b \b")
    else:
        sys.stdout.write(c.decode("utf-8"))
        sys.stdout.flush()
def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)       
        flush_to_stdout(c)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    if c == b'\x7f': # Backspace/delete is hit
        return "delete"
    return c.decode("utf-8")

def get_word():
    s = ""
    while True:
        a = getkey()
        # if ENTER or SPACE is hit
        if a == " " or a == "\n": 
            return s
        elif a == "delete":
            s = s[:-1]
        else:
            s += a
def pose1():
	print(barre+tiret+tiret+tiret+tiret+tiret+tiret+tiret)
	pose = 1

def pose2():
	print(tiret+barre+tiret+tiret+tiret+tiret+tiret+tiret)
	pose = 2

def pose3():
	print(tiret+tiret+barre+tiret+tiret+tiret+tiret+tiret)
	pose = 3

def pose4():
	print(tiret+tiret+tiret+slash+tiret+tiret+tiret+tiret)
	pose = 4

def pose5():
	print(tiret+tiret+tiret+tiret+slash+tiret+tiret+tiret)
	pose = 5

def pose6():
	print(tiret+tiret+tiret+tiret+tiret+barre+tiret+tiret)
	pose = 6

def pose7():
	print(tiret+tiret+tiret+tiret+tiret+tiret+barre+tiret)
	pose = 7

def pose8():
	print(tiret+tiret+tiret+tiret+tiret+tiret+tiret+barre)
	pose = 8

def espaceClicked():
	if espace == True:
		if pose == 4 or pose == 5:
			nbDePoint = nbDePoint + 1
while True:
	pose1()
	time.sleep(0.115)
	pose2()
	time.sleep(0.115)
	pose3()
	time.sleep(0.115)
	pose4()
	time.sleep(0.115)
	pose5()
	time.sleep(0.115)
	pose6()
	time.sleep(0.115)
	pose7()
	time.sleep(0.115)
	pose8()
	time.sleep(0.115)
	
	pose8()
	time.sleep(0.115)
	pose7()
	time.sleep(0.115)
	pose6()
	time.sleep(0.115)
	pose5()
	time.sleep(0.115)
	pose4()
	time.sleep(0.115)
	pose3()
	time.sleep(0.115)
	pose2()
	time.sleep(0.115)
	pose1()
	time.sleep(0.115)
