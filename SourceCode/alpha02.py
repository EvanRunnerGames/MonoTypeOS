import os
import datetime
import linecache
import colorama
from colorama import Fore, Back
import glob

colorama.init()

global start

global user

orange = '\x1b[38;2;255;165;0m'

def termilink():
    print("Welcome to EvanRunnerStudios (TM) TermiLink")




def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#This makes all text orange
print(orange)

#ui stands for user input
global ui
#this is the commands list that stores all the commands
global page1
page1 = "\nhelp\ntime\nfileread\nfilecreate\nrun\nfilelist\nfiledelete\nfilefix\ncustom commands\nclear\n"



def system():
    termilink()
    print("Type help for a list of commands!\n")

    #this is for if the system is running
    global run
    run = True
    
    while run:

        user = 'guest'

        time = datetime.datetime.now()


        ui = input(f'termilink#{Fore.BLUE}{user}{orange}~ ').lower().strip(' ')


        if ui == "help":
            print(page1)
            print("for more information on a specific command type the commands name and help like filefix+help\n")
        if ui == "time":
            print(f"The the current date and time is: {time}")
        if ui == "fileread":
            lr = input("what file would you like to read: ")
            fileco = linecache.getline(f"{lr}.txt", 1)
            print('\n' + fileco.replace("||", "\n"))
        if ui == "filecreate":
            ln = input("File Name: ")

            li =  input("type in the file || to create a new line: ")

            with open(f"{ln}.txt", "w") as file:
                file.write(li)
        if ui == "run":
            try:
                ftr = input("Enter the file to run: ")

                with open(f"{ftr}.txt", "r") as file:
                    python_code = file.read().replace("||", "\n")
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

        if ui == "filedelete":
            #this stands for what file to delete
            wftd = input("What file would you like to delete: ")
            try:
                os.remove(f"{wftd}.txt")
                if wftd == "cc":
                    print(Back.RED + Fore.WHITE + "\n\nERROR CC NOT FOUND:\nPOWER OFF YOUR SYSTEM THEN POWER BACK ON TO GET CC BACK ITS A REQUIRED FILE\n\n" + orange + Back.RESET)
                    print(orange)
                    print()
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
            print("\ntermilink is a terminal based os made in python and can execute python code")
            print("termilink also is linux based if your running this as your os it has it an boots it automatically")
            print("termilink is made by Evan Runner Pason as an online alias")
            print("termilink has Some Important features you can utilize such as custom commands if this file is not already there")
            print("you can create it yourself do filecreate the file name is cc for custom commands then you can write in that file")
            print("for the first line write the ammount of custom commands you will be using then like 1 or 2 then do || for the next line")
            print("then write the file that you want to cc to run simple as that you do NOT NEED TO PUT THE FILE EXTINSION you will most likely")
            print("NEVER NEED TO DO THAT IN termilink OS because all files are .txt but then compile to other file types the custom command")
            print("is going to be the files name so now you can type the files name and it will run automatically as a command\n")

        if ui == "clear":
            clear()

        if ui.startswith("echo "):  # Check if the input starts with 'echo'
            ui = ui.strip('echo ')
            print(ui)  # Output the remaining part of the string

            



        #THIS IS FOR THE HELP COMMANDS OF THE COMMANDS

        #THIS IS FOR THE CUSTOM COMMANDS

        #ccl stands for custom command lines lines

        # Read the number of custom commands from the file

        try:
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
                except:
                    # If there's an error, print it with colors for visibility
                    print(Back.RED + Fore.WHITE + "ERROR IN COMPILING" + orange + Back.RESET)
                    print("\n")
        except:
            print(Back.RED + Fore.WHITE + "ERROR WITH CUSTOM COMMANDS: FIX DELETE cc" + orange + Back.RESET)
            print("\n")
            

def boot():
    clear()
    print("BOOTING...")
    file_path = 'cc.txt'
    files = glob.glob(file_path)
    if files:
        pass
    else:
        with open(file_path, 'w') as file:
            file.write("0")
    clear()
    system()
            
#This is the main function
boot()
