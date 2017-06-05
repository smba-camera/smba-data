import os
from datetime import datetime
from bson import json_util
import json
from  smba_data.persistency.Connection import Db

collection_name = "weather"

class WeatherData:
    def __init__(self, data, location, time=None, id=""):
        self.location = location
        if time:
            self.time = time
        else:
            self.time = datetime.today()
        self.id = id
        self.data = data

    def save(self):
        col = Db.get_collection(collection_name)
        obj = self.to_dict()
        if not self.id:
            self.id = col.insert_one(obj).inserted_id
            return

        # already has id -> replace doc
        col.find_one_and_replace({'_id':self.id}, obj, upsert=True)

    def save_to_disk(self, path):
        name = self.time.strftime('%Y-%m-%d-%H%M%S') + "_" + str(self.location) + ".json"
        if not os.path.isdir(path):
            os.makedirs(path)
        p = os.path.join(path, name)
        f = open(p, "w")
        json.dump(json_util.dumps(self.to_dict()), f)
        f.close()

    def to_dict(self):
        obj = {
            'location': self.location,
            'time': self.time,
            'data': self.data,
        }
        if (self.id):
            obj['_id'] = self.id
        return obj

def create_weather_data_from_doc(doc):
    return WeatherData(doc['data'], doc['location'], time=doc['time'], id=doc["_id"])

def load_weather_data_one(query):
    col = Db.get_collection(collection_name)
    doc = col.find_one(query)
    return create_weather_data_from_doc(doc)

def load_weather_data(query):
    col = Db.get_collection(collection_name)
    result = []
    for doc in  col.find(query):
        result.append(create_weather_data_from_doc(doc))
    return result
