from MongoDB.POO.app.services.connection import Connection
from MongoDB.POO.app.orm.Cash_bank.models import CashBank
from MongoDB.POO.app.orm.Bank_notes.models import BankNotes
from MongoDB.POO.app.orm.People.models import People
from MongoDB.POO.app.orm.Addresses.models import Address


class Action:

    def __init__(self):
        self.connection = Connection()
        self.banknotes = BankNotes()
        self.cashbank = CashBank()
        self.address = Address()
        self.people = People()

    def create(self):
        self.banknotes.twenty = 20
        self.banknotes.fifty = 50
        self.banknotes.hundred = 10

        self.cashbank.balance = 20000
        self.cashbank.banknotes = self.banknotes.serialize()

        self.address.street = "Street"
        self.address.number = "45"
        self.address.complement = "Complement"
        self.address.zip_code = "Code"
        self.address.city = "City"
        self.address.state = "State"
        self.address.country = "Country"
        self.address.neighborhood = "Neighborhood"

        self.people.name = "Renan"
        self.people.lastname = "Berti Ribas"
        self.people.age = 21
        self.people.cashbank = self.cashbank.serialize()
        self.people.address = self.address.serialize()

        self.save_all()

    def save_all(self):
        self.banknotes.save()
        self.cashbank.save()
        self.address.save()
        self.people.save()

