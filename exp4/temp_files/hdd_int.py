#print("Name of interrupt : ", end = '')
interrupt_name = '0000:00:1f.2'

f_int = open("/proc/interrupts", "r")
j = '0'

print()

lines = f_int.readlines()
for i in lines:
	if(len(i.split()) == 8 and (i.split())[7] == interrupt_name):
		print("HDD interrupts : ")
		print(i)
		j = (i.split())[0].split(':')[0]

if(j == '0'):
	print(interrupt_name + " interrupt not found")
else:
	f_hdd = open("/proc/irq/"+str(j)+"/smp_affinity", "r")
	print(interrupt_name + " core affinity : " , f_hdd.readlines()[0])
