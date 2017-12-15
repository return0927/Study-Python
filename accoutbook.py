##############
import sys

print("hello, this is python account book")

def expense(money):
	i = int(input("input >> "))
	re = money - i
	return re

def plus(money):
	i = int(input("input >> "))
	re = money + i
	return re
money = int(input("input your money >> "))

print("1 : expense 2 : plus 3 : check 4 : exit\n")

while 1:
	cho = int(input("choose >> "))
	
	if cho == 1:
		money = expense(money)
	elif cho == 2:
		money = plus(money)
	elif cho == 3:
		print(str(money)+"\n")
	elif cho == 4:
		sys.exit(1)
	else:
		print("wrong input..\n")
