# A simple program that fetches the size of an image from an external url

import threading
import time
import requests

def downloads(url):
    print(f"Downloading image from {url}.")
    time.sleep(2)
    resp = requests.get(url)
    print(f"Finished {url} image download with size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg" ,
    "https//httpbin.org/image/png" ,
    "https://httpbin.org/image/svg" ,
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=downloads, args=(url, ))
    t.start()
    threads.append(t)

for url in urls:
    t.join()

end = time.time()
print(f"Downloads completed in {end-start:.2f} secs")
