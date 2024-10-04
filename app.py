from colorama import Fore, init
import time


init()

r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
re = Fore.RESET


class Tagebuch():
    def __init__(self):
        self.commands = [
            {
                "name": "add",
                "command": self.add,
                "description": "Add a new entry."
             },
             {
                "name": "list",
                "command": self.list,
                "description": "Lists all entries."
             },
             {
                "name": "exit",
                "command": self.close,
                "description": "Closes this program."
             }
        ]

        for command in self.commands:
            print(c + "[*] " + re + "{:<10}".format(command["name"]) + command["description"])

        choose = input(y + "[+] " + re)
        notFound = True

        for command in self.commands:
            if choose == command["name"]:
                notFound = False
                command["command"]()

        if notFound:
            print("")
            print(r + "[!] " + re + "Command " + r + choose + re + " not found!")
            print("")
            self.__init__()

    
    def add(self):
        print("")

        today = input(y + "[+] Today? [Y|n]: " + re)

        if today == "" or today == "Y" or today == "y":
            date = time.strftime("%d.%m.%Y")
            day = time.strftime("%A")[:3].upper()

            print(c + "[*] " + re + "Date: " + date)
            print(c + "[*] " + re + "Day: " + day)
        else:
            date = input(y + "[+] Date (DD.MM.YYYY): " + re)
            day = input(y+ "[+] Day (DDD): " + re)

        text = input(y + "[+] Text: " + re)

        with open("data.txt", "a") as data:
            data.write(date + " | " + day + " | " + text + "\n")

        again = input(y + "[+] Again? [Y|n]: " + re)

        if again == "" or again == "Y" or again == "y":
            
            self.add()
        else:
            print("")
            self.__init__()


    def list(self):
        try:
            print("")
            with open("data.txt", "r") as data:
                for index, line in enumerate(data.readlines(), 1):
                    print(g + "[*] " + re + "{:03d}".format(index) + " | " + line.strip("\n"))
            print("")
            self.__init__()

        except Exception:
            print("")
            print(r + "[!] " + re + "No data found!")
            print("")
            self.__init__()

    
    def close(self):
        print("")
        print(r + "[!] " + re + "Program closed.")
        print("")
        exit()


print("")
Tagebuch()