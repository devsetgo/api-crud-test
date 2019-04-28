import requests
from datetime import datetime, timedelta
from random import randint
# from services.rw import r_w
import silly
from tqdm import tqdm
from unsync import unsync
import os
from dotenv import load_dotenv
load_dotenv()

ENVIRONMENT = os.getenv('ENVIRONMENT')

if ENVIRONMENT == 'dev':
    URL_BASE = os.getenv('URL_BASE_DEV')
else:
    URL_BASE = os.getenv('URL_BASE_PRD')


names = ['Mike','Dan','Ger','Chuck','Valerie','Cathy','Linda','Kristi','James','John','Robert','William','David','Richard','Charles','Joseph','Thomas','Mary','Patricia','Barbara','Elizabeth','Jennifer','Maria','Susan','Margaret','Dorothy']

surnames = ['SMITH','JOHNSON','WILLIAMS','JONES','BROWN','DAVIS','MILLER','WILSON','MOORE','TAYLOR','ANDERSON','THOMAS','JACKSON','WHITE','HARRIS','MARTIN','THOMPSON','GARCIA'
,'MARTINEZ','ROBINSON','CLARK','RODRIGUEZ','LEWIS','LEE','WALKER','HALL','ALLEN','YOUNG','HERNANDEZ','KING','WRIGHT','LOPEZ']

def randFirstName():
    l = len(names) - 1
    # print(l)
    name = names[randint(0,l)]
    # print(name)
    return name

def randLastName():
    l = len(surnames) - 1
    # print(l)
    surname = surnames[randint(0,l)]
    # print(name)
    return surname


def plus_something() -> str:
    x = randint(2,100)
    result = datetime.now() + timedelta(days=x)
    return str(result)

def ri(top: int) -> int:
    result = randint(1,top)
    return result

@unsync
def create_user(user):
    url =  f'{URL_BASE}/api/v1/users/create/'
    
    r = requests.post(url, json=user) 
    result = r.status_code
    
    if result != 200:
        print(result)


def uc_main(howmany: int):
    pw = f'{silly.noun()}{silly.verb()}'
    
    userList = []
    for i in range(howmany):
        j = {
                "firstName": randFirstName(),
                "lastName": randLastName(),
                "password": pw,
                "title": silly.title(capitalize=True),
                "company": silly.company(capitalize=True),
                "address": silly.address(),
                "city": silly.city(),
                "country": silly.country(),
                "postal": silly.postal_code(),
                "email": silly.email(),
                "website": silly.domain(),
                "description": silly.sentence()
            }
        userList.append(j)

    for u in tqdm(userList, desc='user create'):
        create_user(u)
        
        
howmany = 200
if __name__ == "__main__":
   uc_main(howmany)