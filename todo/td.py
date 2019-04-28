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


url_list =  f'{URL_BASE}/api/v1/todo/list'
# url_userId = 'http://localhost:5000/api/v1/users/c5b39c72'

def get_list():
    print(url_list)
    r = requests.get(url_list)
    result = r.json()
    return result

def makeUrlList(reqList):
    urls = []
    # print(reqList)
    for i in reqList:
        u = f"{URL_BASE}/api/v1/todo/{i['todoId']}"
        urls.append(u)
    return urls

@unsync
def delete_todoId(url):
    r = requests.delete(url)
    x =  r.status_code
    if x != 200:
        print(x)

def td_main():
    l = get_list()
    m = makeUrlList(l)

    for i in tqdm(m, desc='todo delete'):
        delete_todoId(i)

if __name__ == '__main__':
    td_main()


