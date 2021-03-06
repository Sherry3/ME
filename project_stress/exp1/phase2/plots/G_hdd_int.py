import matplotlib.pyplot as plt

f = open("txt/hdd_int.txt", "r")
lines = f.readlines()

intr = []

for i in lines:
	if(i != "\n"):
		intr.append(int(i.split()[4]))


plt.title('HDD interrupts')
plt.plot(range(len(intr)), intr, 'k')
plt.axis([0, len(intr), min(intr), max(intr)])
plt.show()


