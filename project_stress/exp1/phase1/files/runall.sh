python3 set_core_affinity.py
echo 'IRQ Core affinity set'
python3 monitor.py&
taskset 0x08 stress -d 1 --hdd-bytes 10G -t 600
