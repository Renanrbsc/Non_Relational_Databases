from mongoengine import connect


class Connection:
    def __init__(self):
        connect(db='mongodb_test_poo',
                host='localhost',
                port=27017)
