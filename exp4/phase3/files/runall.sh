stress -c 4 -t 7200&
python3 set_core_affinity.py
echo 'IRQ Core affinity set'
python3 monitor.py&
dstat -d > /home/sourabh/Desktop/project/exp4/phase3/files/txt/disk_R_W.txt&
ls /media/sourabh/SHERRY/*.*
taskset 0x04 cp /home/sourabh/Videos/*.m* /media/sourabh/SHERRY 
cd /home/sourabh/perf-tools/fs
./cachestat > /home/sourabh/Desktop/project/exp4/phase3/files/txt/cache.txt
