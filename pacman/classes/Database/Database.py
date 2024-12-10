import os
import sys
import json
from Game_Controller import *

def get_base_path():
    if getattr(sys, 'frozen', False): # executable
        return sys._MEIPASS
    else:
        return os.path.dirname(__file__)
base_path = get_base_path()

class Database:
    def __init__(self):
        self.local_data={}
        self.DATABASE_PATH = os.path.join(base_path, '../../data/user/user_data.json')

class Save(Database):
    pass

class Load(Database):
    # def load_data(self):
    #     with open(self.DATABASE_PATH, 'r') as file:
    #         self.local_data = json.load(file)
    #     return self.local_data
    pass