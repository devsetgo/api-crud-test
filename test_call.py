import requests
from unsync import unsync
from tqdm import tqdm

url_list = 'http://localhost:5000/api/v1/users/list'
url_userId = 'http://localhost:5000/api/v1/users/c5b39c72'

def get_list():
    r = requests.get(url_list)
    result = r.json()
    return result

def makeUrlList(reqList):
    urls = []
    # print(reqList)
    for i in tqdm(reqList):
        u = f"http://localhost:5000/api/v1/users/{i['userId']}"
        urls.append(u)
    return urls

@unsync
def call_userId(url):
    r = requests.get(url)
    x =  r.status_code
    if x != 200:
        print(x)

def main():
    l = get_list()
    m = makeUrlList(l)

    for i in tqdm(m):
        call_userId(i)

if __name__ == '__main__':
    main()


