import subprocess
import threading

def list_files_with_options(options):
    try:
        result = subprocess.run(["ls"] + options, capture_output=True, text=True, check=True)
        print(f"Options: {' '.join(options)}\nOutput:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except FileNotFoundError:
        print("Command 'ls' not found.")

if __name__ == "__main__":
    options_list = [
        ["-a"],
        ["-l"],
        ["-lh"]
    ]

    threads = []
    for options in options_list:
        thread = threading.Thread(target=list_files_with_options, args=(options,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

