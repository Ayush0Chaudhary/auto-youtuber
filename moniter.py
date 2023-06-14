import sys
import os
import re
import logging
import subprocess
from threading import Timer
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from direct_authenticate_upload import initialize_upload

def on_Created(event):
    new_file_path = event.src_path
    new_file_name = re.split("/", new_file_path)[-1]

    print(new_file_name)

    direc_path = "./recordings"

    if not os.path.exists(direc_path):
        os.makedirs(direc_path)
    
    already_present = os.listdir(direc_path)

    if len(already_present) > 1:
        for file in already_present:
            if file != new_file_name:
                os.remove(direc_path+"/"+file)

    try:
        initialize_upload(new_file_name, "This is sample yt video description", ["happy", "dsa", "cp", "hft", "iitr"], "22", "public", new_file_path)
    except NameError as e:
        print("We are fucked!")
        print(e)
    




if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s - %(message)s',
    #                     datefmt='%Y-%m-%d %H:%M:%S')

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    event_handler.on_created = on_Created
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt as e:
        observer.stop()
        observer.join()
    finally:
        observer.stop()
        observer.join()




