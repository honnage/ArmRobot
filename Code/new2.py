import math

def unk():
	a = 10
	b = 12
	c = 10*12
	return c
	
sum = [0,0,0,0]
print(sum[:])

for i in range (0,4,1):
	sum[i] = 4

for i in range (0,4,1):
	if (sum[i] >= 4):
		print("ok")
	
print(sum[:])
