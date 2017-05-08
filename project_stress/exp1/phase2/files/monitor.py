import subprocess
import time

f_m = open("txt/memory.txt", "a+")
f_c = open("txt/cores.txt", "a+")
f_d = open("txt/disk.txt", "a+")
f_h = open("txt/hdd_int.txt", "a+")

for k in range(720):
	#Memory info
	mem = open("/proc/meminfo", "r")
	lines = mem.readlines()

	for i in [0, 1, 6]:
		f_m.write(lines[i])

	cmd = ['free', '-h',]
	lines = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

	f_m.write(lines[1] + "\n")
	
	#Cores info
	cmd = ['mpstat', '-P', 'ALL']
	lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

	for i in lines[2:-1]:
		f_c.write(i + "\n")

	#Disk info
	cmd = ['iostat']
	lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

	for i in range(5, 7):
		f_d.write(lines[i] + '\n')

	#HDD Interrupts
	interrupt_name = '0000:00:1f.2'

	f_int = open("/proc/interrupts", "r")
	j = '0'

	lines = f_int.readlines()
	for i in lines:
		if(len(i.split()) == 8 and (i.split())[7] == interrupt_name):
			f_h.write(i + "\n")
			j = (i.split())[0].split(':')[0]
		
	f_m.write("\n")
	f_c.write("\n")
	f_d.write("\n")
	f_h.write("\n")

	time.sleep(1)





