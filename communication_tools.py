#Private Libraries
import encryption
from connection import Listner_Connection, Sender_Connection

class Listener :
    
    def __init__(self):
        self.connection = Listner_Connection()
    
    def open_socket(self):
        self.connection.listen()
        self.connection.await_connection()
    
    def close_socket(self):
        if self.connection.has_connection == True:
            self.connection.close_socket()
    
    def listen_for_message(self):
        pass
    
    def stop_listener(self):
        pass


class Sender:
    
    def __init__(self):
        self.connection = Sender_Connection()
    
    
    def send_message(self, message):
        self.connection.send_data(message)
