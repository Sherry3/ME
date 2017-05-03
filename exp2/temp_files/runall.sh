python3 set_core_affinity.py
echo 'IRQ Core affinity set'
python3 write_in_file/cores.py&
echo 'Monitoring cores'
python3 write_in_file/hdd_int.py&
echo 'Monitoring interrupts'
python3 write_in_file/memory.py&
echo 'Monitoring RAM'
python3 write_in_file/disk.py&
echo 'Monitoring disk'
cd /home/sourabh/perf-tools/fs
./cachestat
