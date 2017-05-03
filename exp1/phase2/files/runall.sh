python3 set_core_affinity.py
echo 'IRQ Core affinity set'
python3 monitor.py&
dstat -d > /home/sourabh/Desktop/project/exp1/phase2/files/txt/disk_R_W.txt&
ls /media/sourabh/SHERRY/*.*
taskset 0x08 cp /media/sourabh/SHERRY/*.* /home/sourabh/Documents
cd /home/sourabh/perf-tools/fs
./cachestat > /home/sourabh/Desktop/project/exp1/phase2/files/txt/cache.txt
