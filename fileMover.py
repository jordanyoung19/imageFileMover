import time
import shutil
import os

downloadsPath = "/Users/jordanyoung/Downloads"
airDropPath = "/Users/jordanyoung/Pictures/airDrop"

def running():
    running = True
    while running:
        for filename in os.listdir(downloadsPath):
            if filename.endswith(".heic"):
                shutil.move(filename, airDropPath)
        time.sleep(2)
    
if __name__ == "__main__":
    running()