'''
from math import log10, floor
import math
def round_to_1(x):
	print( round(x, -int(floor(log10(abs(x))))))
	
while True:
	#x = input("\nEnter average_Arm: ")
	#print(str(round(int((x)), 3 )))
	print(int(math.ceil(4.2)))
 
'''
'''
from math import log10, floor
x = 0.0232

def round_to_1(x):
	return round(x, -int(floor(log10(abs(x)))))
	print(x)

round_to_1(x)
'''
print('%s' % float('%.1g' % 32.25))
