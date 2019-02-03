# Dataset/MongoClient
import pymongo as pm
import pandas as pd

class MongoClient:
    """Mongodb client to manipulate dataset store on a distant database"""
    
    def __init__(self, db={}, q={}, f=None):
        """
        Instantiate the pymogo client and target the right collection
        Example db conig:
        {
            "mongo_host": "ns396089.ip-37-59-38.eu",
            "mongo_port": 32771,
            "mongo_db_name": "NETWORK-AND-DISCRETE-LOCATION"
        }
        
        """
        self.db = db
        self.q  = q
        self.f  = f
        
        self.client   = pm.MongoClient(db["mongo_host"], db["mongo_port"])
        self.datasets = self.client[db["mongo_db_name"]]["datasets"]
        
    def get(self, index=None):
        """
        Return the dataset as a panda DataFrame
        """
        
        record = self.datasets.find_one(self.q,self.f)
        self.df = pd.DataFrame.from_dict(record["data"])
        
        if index:
            self.df = self.df.set_index(index).sort_index()
        else:
            self.df = self.df.reset_index(drop=True).sort_index()
        
        return self.df
    

    def get_metadata(self):
        """
        Return the metadata dict
        """
    
        return self.datasets.find_one(self.q,self.f)["metadata"]