import subprocess
cmd = ['mpstat', '-P', 'ALL']
lines = subprocess.Popen( cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split('\n')

print()
for i in lines[2:-1]:
	print(i)


