from uuid import uuid4
from mongoengine import Document, StringField, IntField, DictField


class CashBank(Document):

    uuid = StringField(max_length=100, unique=True, default=str(uuid4()))
    balance = IntField(min_value=0, max_value=1000000)

    banknotes = DictField()

    def serialize(self):
        return {"uuid": self.uuid,
                "balance": self.balance,
                "banknotes": self.banknotes}
