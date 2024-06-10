import json
import pandas as pd

def read_user_info():
    with open('./data/user_info.json','r') as f:
        return json.load(f)
    
def dump_user_info(name,sex,age,height):
    info = {"name": name, "sex": sex, "age": age, "height": height}
    with open('./data/user_info.json','w',encoding='utf-8') as f:
        return json.dump(info,f)