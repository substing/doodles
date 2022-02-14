for a in range(0,100):
	for b in range(0,100):
		p = a**2 + b**2
		if p%2 != 0:
			if (p%4 != 1):
				print("counterexample: ", a, b)
