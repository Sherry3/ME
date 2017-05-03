import subprocess
import time

f = open("txt/disk.txt", "a+")

for k in range(600):
	cmd = ['iostat']
	lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

	for i in range(5, 7):
		f.write(lines[i] + '\n')

	time.sleep(1)


