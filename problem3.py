for k in range(-100, 100):
	x = (1/3)*(19*k + 1)
	print(3*x % 19)
	if 3*x % 19 != 1:
		print("BAD!!")
print("Done.")