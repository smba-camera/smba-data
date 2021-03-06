from datetime import datetime
import os
import time
from  smba_data.persistency.Connection import Db
import base64

collection_name = "image"

class Image:
    def __init__(self, img, location, time=None, id=""):

        self.img = img
        if time:
            self.time = time
        else:
            self.time = datetime.today()
        self.location = location
        self.id = id

    def save(self):

        col = Db.get_collection(collection_name)
        obj = {
            "img": base64.b64encode(self.img),
            "time": time.mktime(self.time.timetuple()),
            "location": self.location,
        }
        if not self.id:
            self.id = col.insert_one(obj).inserted_id
            return

        # already
        obj["_id"]=self.id
        col.find_one_and_replace({'_id':self.id}, obj, upsert=True)

    def save_to_disk(self, path):
        name = self.time.strftime('%Y-%m-%d-%H%M%S') + "_" + str(self.location)+".jpg"
        if not os.path.isdir(path):
            os.makedirs(path)
        p = os.path.join(path, name)
        f = open(p, "wb")
        f.write(self.img)
        f.close()



def create_image_from_doc(doc):
    t = datetime.utcfromtimestamp(doc["time"])
    i = base64.b64decode(doc["img"])
    return Image(i, doc["location"], time=t, id=doc["_id"])

def loadImages(query):
    col = Db.get_collection(collection_name)
    result = []

    for img in col.find(query):
        result.append(create_image_from_doc(img))
    return result

def loadImage(query):
    col = Db.get_collection(collection_name)
    doc = col.find_one(query)
    #print(doc.keys())
    return create_image_from_doc(doc)
