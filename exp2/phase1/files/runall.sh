stress -c 4 -t 7200&
python3 set_core_affinity.py
echo 'IRQ Core affinity set'
python3 monitor.py&
dstat -d > /home/sourabh/Desktop/project/exp2/phase1/files/txt/disk_R_W.txt&
ls /media/sourabh/SHERRY/*.m*
taskset 0x08 cp /media/sourabh/SHERRY/*.m* /home/sourabh/Videos
cd /home/sourabh/perf-tools/fs
./cachestat > /home/sourabh/Desktop/project/exp2/phase1/files/txt/cache.txt