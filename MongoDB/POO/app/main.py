from MongoDB.POO.app.services.viewer import Viewer


class Main:
    def __init__(self):
        viewer = Viewer()
        viewer.post()
