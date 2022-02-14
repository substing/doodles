import random

def test():
	a = random.randint(-1000,1000)
	n = random.randint(1,1000)
	if ((-a)%n != a % n):
		print("a = ", a, "\nn = ", n)
		return 
	else:
		print("No error")

test()