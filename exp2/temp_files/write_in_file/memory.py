import time

f = open("txt/memory.txt", "a+")

for k in range(600):
	mem = open("/proc/meminfo", "r")
	lines = mem.readlines()

	for i in [0, 1, 6]:
		f.write(lines[i])
		
	f.write('\n')
	time.sleep(1)


