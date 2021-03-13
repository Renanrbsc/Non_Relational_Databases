from uuid import uuid4
from mongoengine import Document, StringField, IntField, DictField


class People(Document):

    uuid = StringField(max_length=100, unique=True, default=str(uuid4()))
    name = StringField(min_length=3, max_length=100)
    lastname = StringField(min_length=5, max_length=100)
    age = IntField(min_value=0, max_value=120, default=0)

    cashbank = DictField()
    address = DictField()

    def serialize(self):
        return {"uuid": self.uuid,
                "name": self.name,
                "lastname": self.lastname,
                "age": self.age,
                "cashbank": self.cashbank,
                "address": self.address}
