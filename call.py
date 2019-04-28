import requests
from datetime import datetime, timedelta
from random import randint
from rw import r_w

names = ['Mike','Dan','Ger','Chuck','Valerie','Cathy','Linda','Kristi']

def randName():
    l = len(names) - 1
    # print(l)
    name = names[randint(0,l)]
    # print(name)
    return name

def plus_something() -> str:
    x = randint(2,100)
    result = datetime.now() + timedelta(days=x)
    return str(result)

def ri(top: int) -> int:
    result = randint(1,top)
    return result

url = 'http://localhost:5000/api/v1/todo/create/'
for i in range(5000):
    j = {'todo':{
            "title": r_w(ri(5))
            ,"description": r_w(ri(20))
            ,"dateDue": str(plus_something())
            ,"userId": str(randName())
            ,"checklist": [
                        {
                                "item": "thing",
                                "description": "a thing",
                                "completed": False
                        }
                        ],
                }
    }
    
    print(j)
    r = requests.post(url, json=j)