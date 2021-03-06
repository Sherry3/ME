import matplotlib.pyplot as plt

f = open("txt/disk.txt", "r")
lines = f.readlines()

tps = []
r_s = []
w_s = []
r = []
w = []

for i in lines:
	j = i.split()
	if(len(j) > 0 and j[0] == "sda"):
		tps.append(float(j[1]))
		r_s.append(float(j[2]))
		w_s.append(float(j[3]))
		r.append(int(j[4]))
		w.append(int(j[5]))

plt.title('tps')
plt.plot(range(len(tps)), tps, 'ro')
plt.axis([0, len(tps), min(tps), max(tps)])
plt.show()

plt.title('read/s (KB)')
plt.plot(range(len(r_s)), r_s, 'ro')
plt.axis([0, len(r_s), min(r_s), max(r_s)])
plt.show()

plt.title('write/s (KB)')
plt.plot(range(len(w_s)), w_s, 'ro')
plt.axis([0, len(w_s), min(w_s), max(w_s)])
plt.show()

plt.title('read (KB)')
plt.plot(range(len(r)), r, 'ro')
plt.axis([0, len(r), min(r), max(r)])
plt.show()

plt.title('write (KB)')
plt.plot(range(len(w)), w, 'ro')
plt.axis([0, len(w), min(w), max(w)])
plt.show()
