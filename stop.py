import subprocess
import os
import globals

from led_ws281x import *


def stop_start_py():
    # Tìm tất cả tiến trình liên quan đến start.py
    colorWipe(strip, Color(0,0,0))
    try:
        # Chạy lệnh 'ps aux' để liệt kê tất cả tiến trình
        result = subprocess.check_output(['ps', 'aux'])
        result = result.decode('utf-8')

        # Tìm dòng chứa 'start.py'
        for line in result.splitlines():
            if 'start.py' in line:
                # Tìm PID (Process ID) trong dòng đó
                pid = int(line.split()[1])
                print(f"Stopping process {pid}")
                os.kill(pid, 9)  # Gửi tín hiệu SIGKILL để dừng tiến trình
                
        
        if globals.process and globals.process.poll() is None:
            globals.process.terminate()
            print("Đã dừng phát nhạc.")
            globals.check_play = 0
            time.sleep(1)    
            
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    stop_start_py()
