stress -c 4 -t 7200&
python3 set_core_affinity.py
echo 'IRQ Core affinity set'
python3 monitor.py&
dstat -d > /home/sourabh/Desktop/project/exp4/phase0/files/txt/disk_R_W.txt&
cd /home/sourabh/perf-tools/fs
./cachestat > /home/sourabh/Desktop/project/exp4/phase0/files/txt/cache.txt
