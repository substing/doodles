count = 0
for x in range (0,10):
	for y in range (0,10):
		if (3*x + y + 28)%10 == 0:
			count +=1
			print("Solution: x = ", x, "y = ", y)
print("Count: ", count)