def factorize(n):
	factors = [1,n]
	while n > 1:
		for p in range(2, n):
			if n % p == 0:
				factors.append(p)
				n = n // p
				break

		else: 
			#n is prime
			factors.append(n)
			break
	return factors

print(factorize(int(input(">> "))))