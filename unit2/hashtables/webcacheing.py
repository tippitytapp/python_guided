'''
1. Have an input loop that gets a URL from the user
2. Fetch the data at the URL and display it
'''
import urllib.request
import datetime

class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = get_timestamp()

cache = {}

def get_timestamp():
    return datetime.datetime.now().timestamp()

def get_data(url):
    cur_time = get_timestamp()
    if (url not in cache) or (cur_time - cache[url].timestamp > 10):
        print('cache miss')
        resp = urllib.request.urlopen(url)
        data = resp.read()
        resp.close()
        data.decode()
        cache[url] = CacheEntry(url, data)
    # print(cache[url].timestamp)
    return cache[url].data


if __name__ == "__main__":
    while True:
        url = input("Enter a URL:")
        # print(get_data(url))
        print(get_data(url)[:100])