from colorama import Fore

def wrap(cls):
    def wrapper(*args, **kwargs):
        obj = cls(*args, **kwargs)
        obj.print()

    return wrapper

@wrap
class Message:
    def __init__(self, text, color=None):
        self.text = text
        self.color = color

    def print(self):
        if self.color == None:
            print(self.text)
        else:
            if self.color == "red":
                print(Fore.RED+self.text)
                print(Fore.RESET)
            elif self.color == "yellow":
                print(Fore.YELLOW+self.text)
                print(Fore.RESET)
            elif self.color == "green":
                print(Fore.GREEN+self.text)
                print(Fore.RESET)
            elif self.color == "blue":
                print(Fore.BLUE+self.text)
                print(Fore.RESET)
            elif self.color == "black":
                print(Fore.BLACK+self.text)
                print(Fore.RESET)
            elif self.color == "white":
                print(Fore.WHITE+self.text)
                print(Fore.RESET)