import pymongo as pm
import pandas as pd

class MongoClient:
    
    def __init__(self, db={}, search={}):
        self.db = db
        self.search = search
        
        self.client   = pm.MongoClient(db["mongo_host"], db["mongo_port"])
        self.problems = self.client[db["mongo_db_nane"]]["datasets"]
        
    def get(self, q={}, f=None, index=None):
        record = self.problems.find_one(q,f)
        self.df = pd.DataFrame.from_dict(record["data"])
        if index:
            self.df = self.df.set_index(index)
        else:
            self.df = self.df.reset_index()
        
        return self.df
