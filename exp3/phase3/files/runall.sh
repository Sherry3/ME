python3 set_core_affinity.py
echo 'IRQ Core affinity set'
python3 monitor.py&
dstat -d > /home/sourabh/Desktop/project/exp3/phase3/files/txt/disk_R_W.txt&
ls /media/sourabh/SHERRY/*.*
taskset 0x04 cp /home/sourabh/Videos/*.m* /media/sourabh/SHERRY 
cd /home/sourabh/perf-tools/fs
./cachestat > /home/sourabh/Desktop/project/exp3/phase3/files/txt/cache.txt
