from mongoengine import Document, StringField, IntField
from uuid import uuid4


class BankNotes(Document):

    uuid = StringField(max_length=100, unique=True, default=str(uuid4()))
    twenty = IntField(min_value=0, max_value=10000, default=0)
    fifty = IntField(min_value=0, max_value=10000, default=0)
    hundred = IntField(min_value=0, max_value=10000, default=0)

    def serialize(self):
        return {"uuid": self.uuid,
                "twenty": self.twenty,
                "fifty": self.fifty,
                "hundred": self.hundred}
