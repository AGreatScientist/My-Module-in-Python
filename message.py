# Версия модуля 1.1.1


from colors import *

def ctext(text, color=None):
    if color == None:
        c = str(text)
    else:
        if color == "red":
            c = RED+str(text)+END
        elif color == "yellow":
            c = YELLOW+str(text)+END
        elif color == "green":
            c = GREEN+str(text)+END
        elif color == "blue":
            c = BLUE+str(text)+END
        elif color == "cyan":
            c = CYAN+str(text)+END
        elif color == "darkcyan":
            c = DARKCYAN+str(text)+END
        elif color == "purple":
            c = PURPLE+str(text)+END
        elif color == "bold":
            c = BOLD+str(text)+END
        elif color == "underline":
            c = UNDERLINE+str(text)+END
        else:
            raise SyntaxError(RED+str('Такого цвета не существует!\nВсе цвета:\nred\nyellow\ngreen\nblue\ncyan\ndarkcyan\nbold\nunderline')+END)
    return c

def cprint(text=None, color=None):
    if not text:
        raise TypeError(RED+str('Не найден аргумент text (text="Hello world!")')+END)
    elif not color:
        print(str(text))
    else:
        if color == "red":
            print(RED+str(text)+END)
        elif color == "yellow":
            print(YELLOW+str(text)+END)
        elif color == "green":
            print(GREEN+str(text)+END)
        elif color == "blue":
            print(BLUE+str(text)+END)
        elif color == "cyan":
            print(CYAN+str(text)+END)
        elif color == "darkcyan":
            print(DARKCYAN+str(text)+END)
        elif color == "purple":
            print(PURPLE+str(text)+END)
        elif color == "bold":
            print(BOLD+str(text)+END)
        elif color == "underline":
            print(UNDERLINE+str(text)+END)
        else:
            raise SyntaxError(RED+str('Такого цвета не существует!\nВсе цвета:\nred\nyellow\ngreen\nblue\ncyan\ndarkcyan\nbold\nunderline')+END)
