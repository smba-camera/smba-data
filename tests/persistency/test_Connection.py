import smba_data.persistency.Connection as Con

def TestDbConnection():
    client = Con.connect()
    db = client.get_default_database()
    print(db.name)
    assert db.name != "" and db.name != None