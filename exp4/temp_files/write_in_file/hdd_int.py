import time

f = open("txt/hdd_int.txt", "a+")

for k in range(600):
	#print("Name of interrupt : ", end = '')
	interrupt_name = '0000:00:1f.2'

	f_int = open("/proc/interrupts", "r")
	j = '0'

	lines = f_int.readlines()
	for i in lines:
		if(len(i.split()) == 8 and (i.split())[7] == interrupt_name):
			f.write(i + "\n")
			j = (i.split())[0].split(':')[0]
	time.sleep(1)

