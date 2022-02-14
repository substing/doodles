#quadratic residue
def quadratic_residue(k, m):
	


import math
ms = [5,7,15,19]
ks = []
for m in ms:
	for k in range(1,m):
		if math.gcd(m,k) == 1:
			ks.append(k)
			quadratic residue(k, m)
		ks = []
