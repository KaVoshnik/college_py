import threading
import time

def print_time():
    while True:
        print(f"Time: {time.strftime('%H:%M:%S')}")
        time.sleep(2)

def print_date():
    while True:
        print(f"Date: {time.strftime('%Y-%m-%d')}")
        time.sleep(3)

if __name__ == "__main__":
    time_thread = threading.Thread(target=print_time)
    date_thread = threading.Thread(target=print_date)
    time_thread.daemon = True
    date_thread.daemon = True
    time_thread.start()
    date_thread.start()
    time.sleep(10)
