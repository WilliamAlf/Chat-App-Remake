from termcolor import colored

def print_error(prompt, data, end=""):
    print(colored(f" [{prompt.upper()}] {data} {end}", "red"))

def print_success(prompt, data, end=""):
    print(colored(f" [{prompt.upper()}] {data} {end}", "green"))

def print_status(prompt, data, end=""):
    print(colored(f" [{prompt.upper()}] {data} {end}", "cyan"))