import matplotlib.pyplot as plt

f = open("txt/memory.txt", "r")
lines = f.readlines()

free = []
active = []
used = []
shared = []
buff = []
cache = []

j = 0
for i in lines:
	if(j % 5 == 1):
		k = i.split()
		free.append(int(k[1]))
	
	if(j % 5 == 2):
		k = i.split()
		active.append(int(k[1]))

	if(j % 5 == 3):
		k = i.split()
		used.append(float(k[2][:-1]))
		shared.append(float(k[4][:-1]))
		buff.append(float(k[5][:-1]))
		cache.append(float(k[6][:-1]))
	j += 1
	

plt.title('free and active')
plt.plot(range(len(free)), free, 'ro')
plt.plot(range(len(active)), active, 'go')
plt.axis([0, len(free), min([min(free), min(active)]), max(max(free), max(active))])
plt.show()

plt.title('used')
plt.plot(range(len(used)), used, 'ro')
plt.axis([0, len(used), min(used), max(used)])
plt.show()

plt.title('shared')
plt.plot(range(len(shared)), shared, 'ro')
plt.axis([0, len(shared), min(shared), max(shared)])
plt.show()

plt.title('buffer')
plt.plot(range(len(buff)), buff, 'ro')
plt.axis([0, len(buff), min(buff), max(buff)])
plt.show()

plt.title('cached')
plt.plot(range(len(cache)), cache, 'ro')
plt.axis([0, len(cache), min(cache), max(cache)])
plt.show()
