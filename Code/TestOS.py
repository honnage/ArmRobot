import os
import runfile_test
import time

a = runfile_test.ia

b = 0

for i in range(3000):
	a = a+i
	if(a<150):
		print(a)
		time.sleep(0.5)
	else:
		exit()
		b = 1

command = "python runfile_test.py"
os.system(command)
		
print("babo")

		
if(b==1):
	print("b = 1")
else:
	print("b = 0")
