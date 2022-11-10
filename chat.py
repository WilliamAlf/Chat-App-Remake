from utils.prompts import *
import utils.repl as repl
from peer import Peer

class Chat:
    command_list = ["first command"]
    
    messages_sent = []
    messages_received = []
    message_buffer = []
    
    
    def __init__(self):
        self.peer = Peer()
        self.start_chat()
    
    
    def start_chat(self):
        print()
        prompt_success("welcome", "chat started")
        repl.start_repl(self)
    
    
    def send_message(self):
        pass
    
    
    def stop_chat(self):
        #Discard connections
        #Writes current state to machine to pickup state later
        def save_state():
            pass
        
        save_state()