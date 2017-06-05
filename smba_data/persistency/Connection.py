from pymongo import MongoClient

def connect():
    uri=None
    try:
        import smba_data.configuration as DbServerParams
        #uri = "mongodb://{}:{}@{}".format(DbServerParams.user, DbServerParams.passw, DbServerParams.host)

    except ImportError:
        print("No DbServerParams.py file for db connection details provided!")
        raise ImportError
    db = MongoClient(DbServerParams.host, DbServerParams.port)[DbServerParams.db]
    db.authenticate(name=DbServerParams.user, password= DbServerParams.passw)
    return db

Db = connect()