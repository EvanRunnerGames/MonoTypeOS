import time
import os
import datetime
import pygame
import linecache
import colorama
from colorama import Fore, Back
import glob

pygame.init()
colorama.init()

global start

start = pygame.mixer.Sound("boot.mp3")
tape = pygame.mixer.Sound("background.mp3")

orange = '\x1b[38;2;255;165;0m'

BLINK = '\033[5m'  # ANSI escape sequence for blinking
RESET = '\033[0m'  # ANSI escape sequence to reset formatting



def reset():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#This makes all text orange
print(orange)

def termilink():
    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")

    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print(R"| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |   _____      | || |     _____    | || | ____  _____  | || |  ___  ____   | |")

    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print(R"| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |   _____      | || |     _____    | || | ____  _____  | || |  ___  ____   | |")
    print(R"| | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |  |_   _|     | || |    |_   _|   | || ||_   \|_   _| | || | |_  ||_  _|  | |")

    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print(R"| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |   _____      | || |     _____    | || | ____  _____  | || |  ___  ____   | |")
    print(R"| | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |  |_   _|     | || |    |_   _|   | || ||_   \|_   _| | || | |_  ||_  _|  | |")
    print(R"| | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__| |   | || |  |   \/   |  | || |    | |       | || |      | |     | || |  |   \ | |   | || |   | |_/ /    | |")

    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print(R"| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |   _____      | || |     _____    | || | ____  _____  | || |  ___  ____   | |")
    print(R"| | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |  |_   _|     | || |    |_   _|   | || ||_   \|_   _| | || | |_  ||_  _|  | |")
    print(R"| | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__| |   | || |  |   \/   |  | || |    | |       | || |      | |     | || |  |   \ | |   | || |   | |_/ /    | |")
    print(R"| |     | |      | || |   |  _|  _   | || |   |  __ /    | || |  | |\  /| |  | || |    | |   _   | || |      | |     | || |  | |\ \| |   | || |   |  __'.    | |")

    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print(R"| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |   _____      | || |     _____    | || | ____  _____  | || |  ___  ____   | |")
    print(R"| | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |  |_   _|     | || |    |_   _|   | || ||_   \|_   _| | || | |_  ||_  _|  | |")
    print(R"| | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__| |   | || |  |   \/   |  | || |    | |       | || |      | |     | || |  |   \ | |   | || |   | |_/ /    | |")
    print(R"| |     | |      | || |   |  _|  _   | || |   |  __ /    | || |  | |\  /| |  | || |    | |   _   | || |      | |     | || |  | |\ \| |   | || |   |  __'.    | |")

    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print(R"| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |   _____      | || |     _____    | || | ____  _____  | || |  ___  ____   | |")
    print(R"| | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |  |_   _|     | || |    |_   _|   | || ||_   \|_   _| | || | |_  ||_  _|  | |")
    print(R"| | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__| |   | || |  |   \/   |  | || |    | |       | || |      | |     | || |  |   \ | |   | || |   | |_/ /    | |")
    print(R"| |     | |      | || |   |  _|  _   | || |   |  __ /    | || |  | |\  /| |  | || |    | |   _   | || |      | |     | || |  | |\ \| |   | || |   |  __'.    | |")
    print(R"| |    _| |_     | || |  _| |___/ |  | || |  _| |  \ \_  | || | _| |_\/_| |_ | || |   _| |__/ |  | || |     _| |_    | || | _| |_\   |_  | || |  _| |  \ \_  | |")

    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print(R"| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |   _____      | || |     _____    | || | ____  _____  | || |  ___  ____   | |")
    print(R"| | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |  |_   _|     | || |    |_   _|   | || ||_   \|_   _| | || | |_  ||_  _|  | |")
    print(R"| | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__| |   | || |  |   \/   |  | || |    | |       | || |      | |     | || |  |   \ | |   | || |   | |_/ /    | |")
    print(R"| |     | |      | || |   |  _|  _   | || |   |  __ /    | || |  | |\  /| |  | || |    | |   _   | || |      | |     | || |  | |\ \| |   | || |   |  __'.    | |")
    print(R"| |    _| |_     | || |  _| |___/ |  | || |  _| |  \ \_  | || | _| |_\/_| |_ | || |   _| |__/ |  | || |     _| |_    | || | _| |_\   |_  | || |  _| |  \ \_  | |")
    print(R"| |   |_____|    | || | |_________|  | || | |____| |___| | || ||_____||_____|| || |  |________|  | || |    |_____|   | || ||_____|\____| | || | |____||____| | |")

    time.sleep(0.1)
    reset()

    print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.")
    print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    print(R"| |  _________   | || |  _________   | || |  _______     | || | ____    ____ | || |   _____      | || |     _____    | || | ____  _____  | || |  ___  ____   | |")
    print(R"| | |  _   _  |  | || | |_   ___  |  | || | |_   __ \    | || ||_   \  /   _|| || |  |_   _|     | || |    |_   _|   | || ||_   \|_   _| | || | |_  ||_  _|  | |")
    print(R"| | |_/ | | \_|  | || |   | |_  \_|  | || |   | |__| |   | || |  |   \/   |  | || |    | |       | || |      | |     | || |  |   \ | |   | || |   | |_/ /    | |")
    print(R"| |     | |      | || |   |  _|  _   | || |   |  __ /    | || |  | |\  /| |  | || |    | |   _   | || |      | |     | || |  | |\ \| |   | || |   |  __'.    | |")
    print(R"| |    _| |_     | || |  _| |___/ |  | || |  _| |  \ \_  | || | _| |_\/_| |_ | || |   _| |__/ |  | || |     _| |_    | || | _| |_\   |_  | || |  _| |  \ \_  | |")
    print(R"| |   |_____|    | || | |_________|  | || | |____| |___| | || ||_____||_____|| || |  |________|  | || |    |_____|   | || ||_____|\____| | || | |____||____| | |")
    print(R"| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |")
    print(R"| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
    print(R" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")    



#ui stands for user input
global ui
#this is the commands list that stores all the commands
commands = "\rrestart\nhelp\ntime\nfileread\nfilecreate\ndestroy\nrun\nfilelist\ndeletefile\nfilefix\nmoreinfo"



def system():
    termilink()
    print("Type help for a list of commands!\n")

    #this is for if the system is running
    global run
    run = True
    
    while run:

        time = datetime.datetime.now()

        try:
            tape.play()
        except:
            pass


        ui = input("").lower()

        if ui == "help":
            print(commands)
            print("for more information on a specific command type the commands name and help like filefix+help\n")
        if ui == "time":
            print(f"The the current date and time is: {time}")
        if ui == "restart":
            reset()
            boot()
        if ui == "destroy":
            run = False
        if ui == "fileread":
            lr = input("what log would you like to read: ")
            fileco = linecache.getline(f"{lr}.txt", 1)
            print('\n' + fileco.replace("||", "\n"))
        if ui == "filecreate":
            ln = input("Log Name: ")

            li =  input("type in the log || to create a new line: ")

            with open(f"{ln}.txt", "w") as log:
                log.write(li)
        if ui == "run":
            try:
                ftr = input("Enter the file/log to run: ")

                with open(f"{ftr}.txt", "r") as log:
                    python_code = log.read().replace("||", "\n")
                    exec(python_code)
            except:
                print(Back.RED + Fore.WHITE + "ERROR IN COMPILING" + orange + Back.RESET)
                print(orange)
        if ui == "filelist":


            # List all files in the current directory
            files = glob.glob('*.*')

            print("\nListing All Files...\n")

            # Print the list of files
            for file in files:
                print(file)
            print('\n')

        if ui == "deletefile":
            #this stands for what file to delete
            wftd = input("What file would you like to delete: ")
            try:
                os.remove(f"{wftd}.txt")
            except FileNotFoundError:
                print(Back.RED + Fore.WHITE + "ERROR THIS FILE DOES NOT EXIST" + orange + Back.RESET)
                print(orange)
            except PermissionError:
                print(Back.RED + Fore.WHITE + f"ERROR NO PERMISSION: CANT DELETE {wftd}" + orange + Back.RESET)
                print(orange)
            except:
                print(Back.RED + Fore.WHITE + "AN UNKNOWN ERROR OCCURED" + orange + Back.RESET)
                print(orange)
        if ui == "filefix":
            print(Back.RED + Fore.WHITE + "WARNING:\nARE YOU SURE YOU WANT TO USE THIS IT ONLY FIXES IF YOU DID NOT USE\n|| FOR NEW LINES IF IS ANOTHER ISSUE IT MIGHT BREAK THE PROGRAM\n " + orange + Back.RESET)
            print(orange)
            #wc stands for warning confirm 
            wc = input("Y OR N: ").lower()
            if wc == "y":
                pass#THIS IS GOING TO BE MADE IN THE FUTURE
            else:
                print(Back.RED + Fore.WHITE + "ABORTING" + orange + Back.RESET)
                print(orange)
            
        if ui == "moreinfo":
            print("\nTERMLINK is a terminal based os made in python and can execute python code")
            print("TERMLINK also is linux based if your running this as your os it has it an boots it automatically")
            print("TERMLINK is made by Jacob Allen B****** but usually goes by Evan Runner Pason as an online alias")
            print("TERMLINK has Some Important features you can utilize such as custom commands if this file is not already there")
            print("you can create it yourself do filecreate the file name is cc for custom commands then you can write in that file")
            print("for the first line write the ammount of custom commands you will be using then like 1 or 2 then do || for the next line")
            print("then write the file that you want to cc to run simple as that you do NOT NEED TO PUT THE FILE EXTINSION you will most likely")
            print("NEVER NEED TO DO THAT IN TERMLINK OS because all files are .txt but then compile to other file types the custom command")
            print("is going to be the files name so now you can type the files name and it will run automatically as a command\n")

        #THIS IS FOR THE HELP COMMANDS OF THE COMMANDS

        #THIS IS FOR THE CUSTOM COMMANDS

        #ccl stands for custom command lines lines

        # Read the number of custom commands from the file
        ccl = int(linecache.getline('cc.txt', 1).strip())
        customcommands = []

        # Load custom commands from the file
        for i in range(ccl):
            command = linecache.getline('cc.txt', i + 2).strip()  # Read and strip newlines and whitespace
            customcommands.append(command)

        if ui in customcommands:
            try:
                # Open the corresponding command file and execute its Python code
                with open(f"{ui}.txt", "r") as file:
                    python_code = file.read().replace("||", "\n")
                    print('\n')
                    exec(python_code)
            except Exception as e:
                # If there's an error, print it with colors for visibility
                print(Back.RED + Fore.WHITE + "ERROR IN COMPILING" + orange + Back.RESET)
                print(f"Compilation Error: {e}")


            
                





def boot():
    def srobco():


        time.sleep(0.7)
        reset()

        print(R".----------------. ")
        print(R"| .--------------. |")
        print(R"| |  _______     | |")
        print(R"| | |_   __ \    | |")
        print(R"| |   | |__| |   | |")
        print(R"| |   |  __ /    | |")
        print(R"| |  _| |  \ \_  | |")
        print(R"| | |____| |___| | |")
        print(R"| |              | |")
        print(R"| '--------------' |")
        print(R" '----------------'")

        time.sleep(0.1)
        reset()


        print(R".----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. ")
        print(R"| |  _______     | || |     ____     | ")
        print(R"| | |_   __ \    | || |   .'    `.   | ")
        print(R"| |   | |__| |   | || |  /  .--.  \  | ")
        print(R"| |   |  __ /    | || |  | |    | |  | ")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | ")
        print(R"| | |____| |___| | || |   `.____.'   | ")
        print(R"| |              | || |              | ")
        print(R"| '--------------' || '--------------' ")
        print(R" '----------------'  '----------------'")

        time.sleep(0.3)
        reset()

        print(R".----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------.")
        print(R"| |  _______     | || |     ____     | || |   ______     |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   |")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__| |  |")
        print(R"| | |____| |___| | || |   `.____.'   | || |  |_______/   |")
        print(R"| |              | || |              | || |              |")
        print(R"| '--------------' || '--------------' || '--------------'")
        print(R" '----------------'  '----------------'  '----------------'")

        time.sleep(0.1)
        reset()

        print(R".----------------.  .----------------.  .----------------.  .----------------.")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------.")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   | || |  | |         |")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__| |  | || |  \ `.___.'\  |")
        print(R"| | |____| |___| | || |   `.____.'   | || |  |_______/   | || |   `._____.'  |")
        print(R"| |              | || |              | || |              | || |              |")
        print(R"| '--------------' || '--------------' || '--------------' || '--------------'")
        print(R" '----------------'  '----------------'  '----------------'  '----------------")

        time.sleep(0.025)
        reset()

        print(R".----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  | || |  /  .--.  \  | |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   | || |  | |         | || |  | |    | |  | |")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__| |  | || |  \ `.___.'\  | || |  \  `--'  /  | |")
        print(R"| | |____| |___| | || |   `.____.'   | || |  |_______/   | || |   `._____.'  | || |   `.____.'   | |")
        print(R"| |              | || |              | || |              | || |              | || |              | |")
        print(R"| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
        print(R" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'")


    def trobco():


        print("WAIT...")

        file_path = 'cc.txt'

        files = glob.glob(file_path)

        if files:
            pass
        else:
            with open(file_path, 'w') as file:
                file.write("0")

        try:
            tape.play()
        except:
            pass

        time.sleep(7)
        reset()
        
        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")

        time.sleep(0.5)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")

        time.sleep(0.1)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")

        time.sleep(0.1)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")

        time.sleep(0.4)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  | || |  /  .--.  \  | |")

        time.sleep(0.1)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  | || |  /  .--.  \  | |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   | || |  | |         | || |  | |    | |  | |")

        time.sleep(0.3)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  | || |  /  .--.  \  | |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   | || |  | |         | || |  | |    | |  | |")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__| |  | || |  \ `.___.'\  | || |  \  `--'  /  | |")

        time.sleep(0.1)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  | || |  /  .--.  \  | |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   | || |  | |         | || |  | |    | |  | |")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__| |  | || |  \ `.___.'\  | || |  \  `--'  /  | |")
        print(R"| | |____| |___| | || |   `.____.'   | || |  |_______/   | || |   `._____.'  | || |   `.____.'   | |")

        time.sleep(0.1)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  | || |  /  .--.  \  | |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   | || |  | |         | || |  | |    | |  | |")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__| |  | || |  \ `.___.'\  | || |  \  `--'  /  | |")
        print(R"| | |____| |___| | || |   `.____.'   | || |  |_______/   | || |   `._____.'  | || |   `.____.'   | |")
        print(R"| |              | || |              | || |              | || |              | || |              | |")

        time.sleep(0.1)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  | || |  /  .--.  \  | |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   | || |  | |         | || |  | |    | |  | |")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__| |  | || |  \ `.___.'\  | || |  \  `--'  /  | |")
        print(R"| | |____| |___| | || |   `.____.'   | || |  |_______/   | || |   `._____.'  | || |   `.____.'   | |")
        print(R"| |              | || |              | || |              | || |              | || |              | |")
        print(R"| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")

        time.sleep(0.2)
        reset()

        print(R" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
        print(R"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print(R"| |  _______     | || |     ____     | || |   ______     | || |     ______   | || |     ____     | |")
        print(R"| | |_   __ \    | || |   .'    `.   | || |  |_   _ \    | || |   .' ___  |  | || |   .'    `.   | |")
        print(R"| |   | |__| |   | || |  /  .--.  \  | || |    | |_| |   | || |  / .'   \_|  | || |  /  .--.  \  | |")
        print(R"| |   |  __ /    | || |  | |    | |  | || |    |  __'.   | || |  | |         | || |  | |    | |  | |")
        print(R"| |  _| |  \ \_  | || |  \  `--'  /  | || |   _| |__| |  | || |  \ `.___.'\  | || |  \  `--'  /  | |")
        print(R"| | |____| |___| | || |   `.____.'   | || |  |_______/   | || |   `._____.'  | || |   `.____.'   | |")
        print(R"| |              | || |              | || |              | || |              | || |              | |")
        print(R"| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
        print(R" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'")

    trobco()

    srobco()

    time.sleep(1)

    system()


boot()
