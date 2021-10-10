from colorama import Fore

def ctext(text, color=None):
    if color == None:
        c = str(text)
    else:
        if color == "red":
            c = Fore.RED+str(text)+Fore.RESET
        elif color == "yellow":
            c = Fore.YELLOW+str(text)+Fore.RESET
        elif color == "green":
            c = Fore.GREEN+str(text)+Fore.RESET
        elif color == "blue":
            c = Fore.BLUE+str(text)+Fore.RESET
        elif color == "cyan":
            c = Fore.CYAN+str(text)+Fore.RESET
        elif color == "purple":
            c = Fore.MAGENTA+str(text)+Fore.RESET
        elif color == "black":
            c = Fore.BLACK+str(text)+Fore.RESET
        elif color == "white":
            c = Fore.WHITE+str(text)+Fore.RESET
    return c

def cprint(text, color=None):
    if color == None:
        print(str(text))
    else:
        if color == "red":
            print(Fore.RED+str(text)+Fore.RESET)
        elif color == "yellow":
            print(Fore.YELLOW+str(text)+Fore.RESET)
        elif color == "green":
            print(Fore.GREEN+str(text)+Fore.RESET)
        elif color == "blue":
            print(Fore.BLUE+str(text)+Fore.RESET)
        elif color == "cyan":
            print(Fore.CYAN+str(text)+Fore.RESET)
        elif color == "purple":
            print(Fore.MAGENTA+str(text)+Fore.RESET)
        elif color == "black":
            print(Fore.BLACK+str(text)+Fore.RESET)
        elif color == "white":
            print(Fore.WHITE+str(text)+Fore.RESET)
