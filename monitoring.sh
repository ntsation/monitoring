#!/bin/bash

# Coleta as informações
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d. -f1)
mem_usage=$(free | grep Mem | awk '{print $3/$2 * 100}')
disk_usage=$(df -h | grep '/dev/sda1' | awk '{print $5}' | cut -d% -f1)

echo "CPU_USAGE=$cpu_usage"
echo "MEM_USAGE=$mem_usage"
echo "DISK_USAGE=$disk_usage"
