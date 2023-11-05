import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to check resource usage
def check_resources():
    try:
        # Rune the shell script and capture the output
        output = subprocess.check_output("./monitoring.sh", shell=True).decode()
        
        # Analyze the information collected
        resource_info = {}
        for line in output.splitlines():
            key, value = line.split('=')
            resource_info[key] = value

        message = f"CPU Usage: {resource_info['CPU_USAGE']}%\nMemory Usage: {resource_info['MEM_USAGE']}%\nDisk Usage: {resource_info['DISK_USAGE']}%"
        messagebox.showinfo("Resource Monitor", message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Resource Monitor")

# Create a button to check resources
check_button = tk.Button(root, text="Check Resources", command=check_resources)
check_button.pack(padx=20, pady=10)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(padx=20, pady=10)

# Start the graphical interface
root.mainloop()
