import subprocess
cmd = ['iostat']
lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

print()
for i in range(5, 7):
	print(lines[i])

