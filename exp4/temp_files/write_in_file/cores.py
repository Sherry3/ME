import subprocess
import time

f = open("txt/cores.txt", "a+")

for k in range(600):
	cmd = ['mpstat', '-P', 'ALL']
	lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

	for i in lines[2:-1]:
		f.write(i + "\n")
	time.sleep(1)



