from MongoDB.POO.app.services.actions import Action


class Viewer:
    def __init__(self):
        self.action = Action()

    def post(self):
        self.action.create()
