from utils.prompts import *

# TODO : same data at two places, combine with repl match
commands = ["start chat", "start server", "stop program"]


def print_commands():
        print("\n", "Commands:")
        for i in range(len(commands)):
            print(f"{i+1}. {commands[i]}")
            
        print("")


def start_repl(obj):
    
    while True:
        print_commands()
        
        input_command = input("Command> ")
        print("")
        
        match input_command.lower():
            case "start chat" | "sc":
                print_success("command found", "starting chat")
                obj.start_chat()
            
            case "start server" | "ss":
                print_success("command found", "starting server")
                obj.start_server()
                
            case "stop program" | "sp":
                print_success("command found", "stopping program")
                return obj.stop_program()
            
            case default:
                    print_error("invalid command", f"Command \"{input_command}\" not found, try again")  