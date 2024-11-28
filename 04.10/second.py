import requests
import threading

def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded: {filename}")

if __name__ == "__main__":
    urls = [
        "https://example-files.online-convert.com/document/txt/example.txt"
    ]
    filenames = ["exemple.txt"]

    threads = []
    for i in range(len(urls)):
        thread = threading.Thread(target=download_file, args=(urls[i], filenames[i]))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
