from user.uc import uc_main
from user.ua import ua_main
from user.ud import ud_main
from todo.tc import tc_main
from todo.ta import ta_main
from todo.td import td_main
import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'dev':
    URL_BASE = os.getenv('URL_BASE_DEV')
else:
    URL_BASE = os.getenv('URL_BASE_PRD')

    
todo_count_url = f'{URL_BASE}/api/v1/todo/list/count'
user_count_url = f'{URL_BASE}/api/v1/users/list/count'

def get_todo_count():
    url = todo_count_url
    r = requests.get(url)
    x = r.json()
    result = x['count']
    # print(result)
    return result

def get_todo_count_true():
    url = todo_count_url + '?complete=true'
    r = requests.get(url)
    x = r.json()
    result = x['count']
    # print(result)
    return result

def get_todo_count_false():
    url = todo_count_url + '?complete=false'
    r = requests.get(url)
    x = r.json()
    result = x['count']
    # print(result)
    return result

def todo_check(howmany: int):
    tc_main(howmany)
    time.sleep(20)
    tcount_f = get_todo_count_false()
    tcount_t = get_todo_count_true()
    print(f'todo complete = false: {tcount_f} true: {tcount_t}')
    ta_main()
    time.sleep(20)
    tcount_f = get_todo_count_false()
    tcount_t = get_todo_count_true()
    print(f'todo complete = false: {tcount_f} true: {tcount_t}')
    td_main()
    time.sleep(20)
    tcount_f = get_todo_count_false()
    tcount_t = get_todo_count_true()
    print(f'todo complete = false: {tcount_f} true: {tcount_t}')

def get_user_count():
    url = user_count_url
    r = requests.get(url)
    x = r.json()
    result = x['count']
    # print(result)
    return result

def get_user_count_true():
    url = user_count_url + '?active=true'
    r = requests.get(url)
    x = r.json()
    result = x['count']
    # print(result)
    return result

def get_user_count_false():
    url = user_count_url + '?active=false'
    r = requests.get(url)
    x = r.json()
    result = x['count']
    # print(result)
    return result

def user_check(howmany: int):
    uc_main(howmany)
    time.sleep(5)
    tcount_f = get_user_count_false()
    tcount_t = get_user_count_true()
    print(f'users active = false: {tcount_f} true: {tcount_t}')
    ua_main()
    time.sleep(5)
    tcount_f = get_user_count_false()
    tcount_t = get_user_count_true()
    print(f'users active = false: {tcount_f} true: {tcount_t}')
    ud_main()
    time.sleep(5)
    tcount_f = get_user_count_false()
    tcount_t = get_user_count_true()
    print(f'users active = false: {tcount_f} true: {tcount_t}')



def main():
    howmany = 100
    todo_check(howmany)
    time.sleep(5)
    user_check(howmany)

if __name__ == '__main__':
    main()