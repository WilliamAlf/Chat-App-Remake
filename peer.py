from communication_tools import Listener, Sender

class Peer:
    def __init__(self):
        self.listener = Listener()
        self.sender = Sender()

    