import os
import subprocess
import signal
import sys
import time

def signal_handler(sig, frame):
    print('Shutting down the server...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def start_server():
    # Kill any existing Python processes
    try:
        subprocess.run(["pkill", "-f", "python app.py"], stderr=subprocess.DEVNULL)
        print("Killed existing server processes")
    except:
        pass
    
    # Start the Flask server
    print("Starting the server...")
    
    # Use Python's subprocess to start the server
    process = subprocess.Popen(
        ["python", "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Wait a moment for the server to start
    time.sleep(2)
    
    if process.poll() is not None:
        # Process already terminated
        stdout, stderr = process.communicate()
        print("Server failed to start:")
        print(f"STDOUT: {stdout}")
        print(f"STDERR: {stderr}")
        return False
    
    print("Server successfully started!")
    print(f"The website is available at: http://0.0.0.0:8000")
    print("Press Ctrl+C to stop the server")
    
    return True

if __name__ == "__main__":
    if start_server():
        # Keep the script running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Server stopped by user")
    else:
        print("Failed to start the server")