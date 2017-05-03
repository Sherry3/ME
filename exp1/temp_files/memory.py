mem = open("/proc/meminfo", "r")

lines = mem.readlines()

print()
for i in [0, 1, 6]:
	print(lines[i], end = '')
		
print()
