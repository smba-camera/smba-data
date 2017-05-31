from motor.motor_tornado import MotorClient as Client


def connect():
    uri=None
    try:
        from . import DbServerParams
        uri = "mongodb://{}:{}@{}".format(DbServerParams.user, DbServerParams.passw, DbServerParams.host)
    except ImportError:
        print("No DbServerParams.py file for db connection details provided!")
        raise ImportError
    return Client(uri)