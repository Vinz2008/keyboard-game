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
