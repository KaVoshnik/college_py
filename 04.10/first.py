import os
import threading

def list_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            print(f"File: {filename}")

def list_folders(directory):
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            print(f"Folder: {filename}")

if __name__ == "__main__":
    directory = "."
    file_thread = threading.Thread(target=list_files, args=(directory,))
    folder_thread = threading.Thread(target=list_folders, args=(directory,))
    file_thread.start()
    folder_thread.start()
    file_thread.join()
    folder_thread.join()
