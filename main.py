import time
import utils.repl as repl
from utils.prompts import *
from chat import Chat

"""
TODO : 
    1. Flytta command_list till mer lämpligt ställe
    2. Improve error prints to automatically format based on error class
"""


class Main:
    command_list = menu_commands = ["start chat", "start server", "exit"]
    
    chat = None
    server = None
    
    def __init__(self):
        self.start_program()
    
    
    def start_program(self):
        print()
        prompt_success("Welcome")
        repl.start_repl(self)
                    
    
    def start_chat(self):
        prompt_status("chat started", "entering chatmode")
        self.chat = Chat()
    

    def start_server(self):
        time.sleep(3)
        print("\ntime out")


    def stop_program(self):
        prompt_status("Goodbye", "program stopped", "\n")


if __name__ == "__main__":
    Main()
    
