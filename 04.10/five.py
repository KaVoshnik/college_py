import subprocess
import threading
import os

def copy_files(source_dir, dest_dir):
    try:
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            if os.path.isfile(source_path):
                subprocess.run(["cp", source_path, dest_path], check=True)
                print(f"Copied: {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error copying files: {e}")
    except FileNotFoundError:
        print("Command 'cp' not found or directory not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    source_directory = "folder1"
    destination_directory = "folder2"

    thread1 = threading.Thread(target=copy_files, args=(source_directory, destination_directory))
    thread1.start()
    thread1.join()