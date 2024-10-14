import os
import shutil
import itertools
import time
import sys
from datetime import datetime

spotlight_folder = "C:\\Users\\<user>\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
destination_folder = r"C:\Your\Path\Here"

spinner = itertools.cycle(['/', '-', '\\', '|', '|'])

print(f"Starting to copy files from '{spotlight_folder}' to '{destination_folder}'...")

name_counter = 1

current_time = datetime.now()

for file in os.listdir(spotlight_folder):
    path = os.path.join(spotlight_folder, file)

    if os.path.isfile(path): #Make sure it is getting only files and not a folder(although there shouldn't be folders anyway)
        new_filename = f"{name_counter}.jpg"
        destination_path = os.path.join(destination_folder, new_filename)
        
        shutil.copy(path, destination_path)
        
        os.utime(destination_path, (current_time.timestamp(), current_time.timestamp())) #Updates the files to the current date and time so it easy to find in destination folder

        sys.stdout.write(f"\rCopying... {next(spinner)} {file} -> {new_filename}")
        sys.stdout.flush()
        time.sleep(0.1)

        name_counter+=1

print("\nFinished running.")
