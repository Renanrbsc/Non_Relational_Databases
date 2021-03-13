from uuid import uuid4
from mongoengine import Document, StringField


class Address(Document):

    uuid = StringField(max_length=100, unique=True, default=str(uuid4()))
    street = StringField(min_length=1, max_length=50)
    number = StringField(min_length=1, max_length=7)
    complement = StringField(min_length=1, max_length=100)
    zip_code = StringField(min_length=1, max_length=10)
    city = StringField(min_length=1, max_length=50)
    state = StringField(min_length=1, max_length=50)
    country = StringField(min_length=1, max_length=50)
    neighborhood = StringField(min_length=1, max_length=50)

    def serialize(self):
        return {"uuid": self.uuid,
                'street': self.street,
                'number': self.number,
                'complement': self.complement,
                'zip_code': self.zip_code,
                'city': self.city,
                'state': self.state,
                'country': self.country,
                'neighborhood': self.neighborhood}
