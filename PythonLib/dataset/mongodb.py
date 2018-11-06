import pymongo as pm
import pandas as pd

class MongoClient:
    
    def __init__(self, db={}, search={}):
        self.db = db
        self.search = search
        
        self.client   = pm.MongoClient(db["mongo_host"], db["mongo_port"])
        self.problems = self.client[db["mongo_db_nane"]]["datasets"]
        
    def get(self, q={}, f=None, index="ID"):
        record = self.problems.find_one(q,f)
        self.df = pd.DataFrame.from_dict(record["data"])
        self.df = self.df.set_index(index)
        
        return self.df
