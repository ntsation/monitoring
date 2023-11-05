# System Resource Monitoring

This is a system resource monitoring system that displays information about CPU, memory, and disk usage in a graphical interface.

## Requirements

- Python 3.x
- Tkinter (Python library for graphical interface)
- Zenity (for displaying dialog boxes in the shell)

## How to Use

1. Clone or download the repository to your system.

2. Make sure you have the listed requirements installed as mentioned above.

3. Run the Python script:

 ```
python main.py
 ```

4. This will open the monitoring system's graphical interface.

5. Click on the "Check Resources" button to check resource usage. A dialog box will display information about CPU, memory, and disk usage.

6. Click on the "Exit" button to close the application.

## Files
1. **resource_monitor.py**: Python script that creates the graphical interface and calls shell commands to monitor resources.

2. **monitoring.sh**: Shell file containing resource monitoring commands.

## Customization
You can customize alert limits for CPU, memory, and disk usage by editing the monitoring.sh file. Adjust the CPU_LIMIT, MEM_LIMIT, and DISK_LIMIT variables as needed.
