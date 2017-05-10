import os
from subprocess import call

irqs = os.listdir("/proc/irq")
print(irqs)

for irq_num in irqs[1 : len(irqs) - 1]:
	name = "/proc/irq/" + irq_num + "/smp_affinity"
	print(name)
	os.system('echo 01 > ' + name)		#First core




