from peer import Peer

class Chat:
    messages_sent = []
    messages_received = []
    message_buffer = []
    
    
    def __init__(self):
        self.peer = Peer()
    
    
    def start_chat(self):
        pass
    
    
    def send_message(self):
        pass
    
    
    def stop_chat(self):
        
        #Writes current state to machine to pickup state later
        def save_state():
            pass
        
        save_state()