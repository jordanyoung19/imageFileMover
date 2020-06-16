import time
import shutil
import os

downloadsPath = "downloads folder path here"
destinationPath = "path to folder you want to move pictures too"

def running():
    running = True
    while running:
        print("running")
        for filename in os.listdir(downloadsPath):
            print("filename:", filename)
            if filename.endswith(".HEIC"):
                fileToMove = downloadsPath + '/' + filename
                shutil.move(fileToMove, airDropPath)
        time.sleep(2)

if __name__ == "__main__":
    running()
