import requests

BASE_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

def test():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    return requests.get(url, headers=BASE_HEADERS).json()

if __name__=='__main__':
    print(test())