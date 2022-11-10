import time
import utils.repl as repl
from utils.prompts import *
from chat import Chat


class Main:
    chat = None
    server = None
    
    def __init__(self):
        self.start_program()
    
    
    def start_program(self):
        print()
        print_success("start", "Entering REPL")
        repl.start_repl(self)
                    
    
    def start_chat(self):
        print_success("chat started", "entering chatmode")
        self.chat = Chat()
    

    def start_server(self):
        time.sleep(10)
        print("time out")


    def stop_program(self):
        print_success("end", "program stopped", "\n")


if __name__ == "__main__":
    Main()
    
