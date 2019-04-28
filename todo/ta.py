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

url_list = 'https://test-api.devsetgo.com/api/v1/todo/list'
# url_userId = 'http://localhost:5000/api/v1/users/c5b39c72'

def get_list():
    r = requests.get(url_list)
    result = r.json()
    return result

def makeUrlList(reqList):
    urls = []
    # print(reqList)
    for i in reqList:
        u = f"https://test-api.devsetgo.com/api/v1/todo/complete/{i['todoId']}"
        urls.append(u)
    
    # print(len(urls))
    return urls

@unsync
def complete_Id(url):
    r = requests.put(url)
    x =  r.status_code
    if x != 200:
        print(x)



def ta_main():
    l = get_list()
    if len(l) >=1:
        m = makeUrlList(l)

    count = 0
    maxCount = len(m)/2
    for a in tqdm(m, desc='todo complete'):
        if count >= maxCount:
            break
        complete_Id(a)
        count += 1
        

if __name__ == '__main__':
    ta_main()
