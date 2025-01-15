import psutil
import subprocess

# Path to your Yara executable and rules file
yara_executable = "yara64.exe"  # Update this path
yara_rules = "help.yar"          # Update this path

# Function to scan a process with Yara
def scan_process(pid):
    try:
        # Run the Yara command
        command = [yara_executable, "-s", "-f", yara_rules, str(pid)]
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Print the output
        if result.stdout:
            print(f"Results for PID {pid}:\n{result.stdout}")
        if result.stderr:
            print(f"Error for PID {pid}:\n{result.stderr}")
    except Exception as e:
        print(f"Failed to scan PID {pid}: {e}")

# List all running processes
for proc in psutil.process_iter(['pid', 'name']):
    try:
        pid = proc.info['pid']
        name = proc.info['name']
        print(f"Scanning process: {name} (PID: {pid})")
        scan_process(pid)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
