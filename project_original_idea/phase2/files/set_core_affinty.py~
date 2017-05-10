import os
from subprocess import call

irqs = os.listdir("/proc/irq")
print(irqs)

for irq_num in irqs[1 : len(irqs) - 1]:
	name = "/proc/irq/" + irq_num + "/smp_affinity"
	print(name)
	os.system('echo 07 > ' + name)		#First three cores

interrupt_name = '0000:00:1f.2'			#HDD interrupt name

f_int = open("/proc/interrupts", "r")
j = '0'

lines = f_int.readlines()
for i in lines:
	if(len(i.split()) == 8 and (i.split())[7] == interrupt_name):
		j = (i.split())[0].split(':')[0]

if(j == '0'):
	print(interrupt_name + " interrupt not found")
else:
	os.system('echo 08 > ' + "/proc/irq/" + str(j) + "/smp_affinity")
	print("Affinity updated to 08 of " + "/proc/irq/" + str(j) + "/smp_affinity")


