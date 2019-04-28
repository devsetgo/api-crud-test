import requests
from unsync import unsync
from tqdm import tqdm
from dotenv import load_dotenv
import os
load_dotenv()

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'dev':
    URL_BASE = os.getenv('URL_BASE_DEV')
else:
    URL_BASE = os.getenv('URL_BASE_PRD')

url_list = f'{URL_BASE}/api/v1/users/list'
# url_userId = 'http://localhost:5000/api/v1/users/c5b39c72'

def get_list():
    r = requests.get(url_list)
    result = r.json()
    return result

def makeUrlList(reqList):
    urls = []
    # print(reqList)
    for i in tqdm(reqList):
        u = f"{URL_BASE}/api/v1/users/deactivate/{i['userId']}"
        urls.append(u)
    # print(urls)
    return urls

@unsync
def deactivate_userId(url):
    r = requests.put(url)
    x =  r.status_code
    if x != 200:
        print(x)

def ua_main():
    l = get_list()
    m = makeUrlList(l)
    count = 0
    maxCount = len(m)/2
    print(len(m), maxCount)
    
    for i in tqdm(m, desc='user deactivate'):
        if count >= maxCount:
            break
        # print(i)
        deactivate_userId(i)
        count += 1

if __name__ == '__main__':
    ua_main()

