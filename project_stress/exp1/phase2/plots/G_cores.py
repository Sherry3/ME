import matplotlib.pyplot as plt

f = open("txt/cores.txt", "r")
lines = f.readlines()

usr = []
nice = []
sys = []
iowait = []
irq = []
soft = []
idle = []

choice = int(input("Plotting scheme (1 - cpu vise, 2 - attribute vise) : "))

for i in range(5):
	usr.append([])
	nice.append([])
	sys.append([])
	iowait.append([])
	irq.append([])
	soft.append([])
	idle.append([])

for i in lines:
	k = i.split()	
	if(len(k) > 1 and k[2] != 'CPU'):
		if(k[2] == 'all'):
			usr[4].append(float(k[3]))
			nice[4].append(float(k[4]))
			sys[4].append(float(k[5]))
			iowait[4].append(float(k[6]))
			irq[4].append(float(k[7]))
			soft[4].append(float(k[8]))
			idle[4].append(float(k[12]))
		else:
			usr[int(k[2])].append(float(k[3]))
			nice[int(k[2])].append(float(k[4]))
			sys[int(k[2])].append(float(k[5]))
			iowait[int(k[2])].append(float(k[6]))
			irq[int(k[2])].append(float(k[7]))
			soft[int(k[2])].append(float(k[8]))
			idle[int(k[2])].append(float(k[12]))

if(choice == 1):
	for i in range(5):
		plt.title('CPU ' + str(i))
		plt.plot(range(len(usr[i])), usr[i], 'ro')
		plt.plot(range(len(nice[i])), nice[i], 'r+')
		plt.plot(range(len(sys[i])), sys[i], 'bo')
		plt.plot(range(len(iowait[i])), iowait[i], 'g+')
		plt.plot(range(len(irq[i])), irq[i], 'r+')
		plt.plot(range(len(soft[i])), soft[i], 'b+')
		plt.plot(range(len(idle[i])), idle[i], 'gs')

		plt.axis([0, len(usr[i]), 0, 100])
		plt.show()

else:
	plt.title('usr')
	plt.plot(range(len(usr[0])), usr[0], 'r+')
	plt.plot(range(len(usr[1])), usr[1], 'g+')
	plt.plot(range(len(usr[2])), usr[2], 'b+')
	plt.plot(range(len(usr[3])), usr[3], 'y+')
	plt.plot(range(len(usr[4])), usr[4], 'c+')
	plt.axis([0, len(usr[0]), 0, 100])
	plt.show()

	plt.title('nice')
	plt.plot(range(len(nice[0])), nice[0], 'r+')
	plt.plot(range(len(nice[1])), nice[1], 'g+')
	plt.plot(range(len(nice[2])), nice[2], 'b+')
	plt.plot(range(len(nice[3])), nice[3], 'y+')
	plt.plot(range(len(nice[4])), nice[4], 'c+')
	plt.axis([0, len(usr[0]), 0, 100])
	plt.show()

	plt.title('sys')
	plt.plot(range(len(sys[0])), sys[0], 'r+')
	plt.plot(range(len(sys[1])), sys[1], 'g+')
	plt.plot(range(len(sys[2])), sys[2], 'b+')
	plt.plot(range(len(sys[3])), sys[3], 'y+')
	plt.plot(range(len(sys[4])), sys[4], 'c+')
	plt.axis([0, len(usr[0]), 0, 100])
	plt.show()

	plt.title('iowait')
	plt.plot(range(len(iowait[0])), iowait[0], 'r+')
	plt.plot(range(len(iowait[1])), iowait[1], 'g+')
	plt.plot(range(len(iowait[2])), iowait[2], 'b+')
	plt.plot(range(len(iowait[3])), iowait[3], 'y+')
	plt.plot(range(len(iowait[4])), iowait[4], 'c+')
	plt.axis([0, len(usr[0]), 0, 100])
	plt.show()

	plt.title('irq')
	plt.plot(range(len(irq[0])), irq[0], 'r+')
	plt.plot(range(len(irq[1])), irq[1], 'g+')
	plt.plot(range(len(irq[2])), irq[2], 'b+')
	plt.plot(range(len(irq[3])), irq[3], 'y+')
	plt.plot(range(len(irq[4])), irq[4], 'c+')
	plt.axis([0, len(usr[0]), 0, 100])
	plt.show()

	plt.title('soft')
	plt.plot(range(len(soft[0])), soft[0], 'r+')
	plt.plot(range(len(soft[1])), soft[1], 'g+')
	plt.plot(range(len(soft[2])), soft[2], 'b+')
	plt.plot(range(len(soft[3])), soft[3], 'y+')
	plt.plot(range(len(soft[4])), soft[4], 'c+')
	plt.axis([0, len(usr[0]), 0, 100])
	plt.show()

	plt.title('idle')
	plt.plot(range(len(idle[0])), idle[0], 'r+')
	plt.plot(range(len(idle[1])), idle[1], 'g+')
	plt.plot(range(len(idle[2])), idle[2], 'b+')
	plt.plot(range(len(idle[3])), idle[3], 'y+')
	plt.plot(range(len(idle[4])), idle[4], 'c+')
	plt.axis([0, len(usr[0]), 0, 100])
	plt.show()






