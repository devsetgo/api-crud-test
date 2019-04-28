import requests
from datetime import datetime, timedelta
from random import randint
# from .services.rw import r_w
import silly
from tqdm import tqdm
from unsync import unsync
import asyncio
from dotenv import load_dotenv
import os
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
def create_todo(todo):
    url =  f'{URL_BASE}/api/v1/todo/create/'
    
    r = requests.post(url, json=todo) 
    result = r.status_code
    
    if result != 200:
        print(result)


def randDate():
    n = randint(1,100)
    result = datetime.now() + timedelta(days=n) 
    return result

def tc_main(howmany: int):
    pw = f'{silly.noun()}{silly.verb()}'
    
    todoList = []
    for i in range(howmany):
        j = {
            "title": silly.thing(),
            "userId": "string",
            "description": silly.paragraph(length=1),
            "dateDue": str(randDate())
            }
        todoList.append(j)

    for t in tqdm(todoList, desc='todo create'):
        stat = create_todo(t)


howmany = 200
if __name__ == "__main__":
   tc_main(howmany)