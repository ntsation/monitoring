# System Resource Monitoring

👀 This is a shell project that monitors CPU, memory, and disk space usage on a Linux system and displays notifications when these resources reach critical levels.

## Requirements

- A Linux system
- The `notify-send` tool for displaying notifications (usually already installed on desktop-based systems like GNOME and KDE)

## Configuration

Before running the script, you need to configure the alert thresholds and the check interval:

- Open the `monitor.sh` file in a text editor.
- Modify the `CPU_LIMIT`, `MEM_LIMIT`, `DISK_LIMIT` variables with your desired percentage values to trigger alerts.
- Save the file.

## Usage

To start monitoring, run the `monitor.sh` script in the terminal:

```
./monitor.sh
```
The script will periodically check CPU, memory, and disk space usage and display desktop notifications when any of these resources reach critical levels.

To stop monitoring, press Ctrl + C in the terminal where the script is running.

## Customization
You can customize this project to fit your needs, such as the check frequency or the way notifications are displayed. Feel free to make changes to the script as needed.

## License
This project is provided under the MIT License. See the LICENSE file for details.

### Note 📝: 
This project is provided for demonstration purposes only. The accuracy and effectiveness of resource monitoring may vary depending on the environment and system requirements. Be sure to adapt and test the script in your own environment.