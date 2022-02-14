import math

def find_ord(k, m):
	for r in range(1,m):
		if (k**r) % m == 1 % m:
			print("Order of ", k, "mod ", m, "is ", r)
			return r


ms = [5,7,15,19]
ks = []
for m in ms:
	for k in range(1,m):
		if math.gcd(m,k) == 1:
			ks.append(k)
			find_ord(k, m)
		ks = []
