import socket
import asyncio

class Connection(object):
    has_connection = False
    
    def __init__(self, port="8080", ip="", protocol_type=socket.SOCK_STREAM):
        
        self.port = port
        self.ip = ip
        
        #Create socket by protocol type
        if protocol_type == socket.SOCK_DGRAM:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        elif protocol_type == socket.SOCK_STREAM:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    def close_socket(self):
        self.socket.close()


class Listner_Connection(Connection):
    
    def __init__(self, port=8080, ip="", protocol_type=socket.SOCK_STREAM):
        super().__init__(port, ip, protocol_type)
        self.socket.bind((self.ip, self.port))        


    def socket_listen(self, connections=1):
        self.socket.listen(connections)
    
    
    async def await_connection(self):
        
        def wait(self):
            self.client, self.address = self.socket.accept()
            self.has_connection = True
            
        await asyncio.create_task(wait())


class Sender_Connection(Connection):
    
    
    def __init__(self, port="9090", ip="", protocol_type=socket.SOCK_STREAM):
        super().__init__(port, ip, protocol_type)
    
    
    def connect_to_client(self):
        connection_success, connection_fail = (True, False)
        
        try:
            self.socket.connect((self.ip, self.port))        
            
        except Exception as exception:
            print(f"{self} Failed to connect to {self.ip}, Exception {exception}")
            self.has_connection = connection_fail
            return self.has_connection
            
        else:
            self.has_connection = connection_success
            return self.has_connection 

    
    def send_data(self, data):
        self.socket.sendall(data)