import itertools
import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def check_termux():
    if "com.termux" not in os.getenv("PREFIX", ""):
        print(Fore.RED + "\n⚠️  This tool is only for Termux users!\n")
        sys.exit(1)

def show_banner():
    os.system("clear")
    banner = """
           ☠️  HCO-WORDLIST-GENERATOR  ☠️
        -----------------------------------
         By - Hackers Colony Official
         Author - AMIT
        -----------------------------------
    """
    print(Fore.GREEN + banner)

def welcome_message():
    os.system("clear")
    print(Fore.CYAN + """
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  ☠️  HCO-WORDLIST-GENERATOR ☠️  ┃
    ┃    The Best Wordlist Creator!    ┃
    ┃     By Hackers Colony Official   ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)
    time.sleep(3)

def main_menu():
    check_termux()
    welcome_message()
    
    while True:
        show_banner()
        print(Fore.YELLOW + "[1] Start Wordlist Generation")
        print(Fore.RED + "[2] Exit")
        choice = input(Fore.CYAN + "\nEnter choice: ")

        if choice == "1":
            generate_wordlist()
        elif choice == "2":
            exit_tool()
        else:
            print(Fore.RED + "\n⚠️  Invalid choice! Please enter 1 or 2.")

def exit_tool():
    print(Fore.YELLOW + "\n☠️  Thank you for using HCO WORD GEN.")
    print(Fore.GREEN + "Stay connected with Hackers Colony Tech.")
    print(Fore.RED + "See you again. ☠️\n")
    sys.exit(0)

def generate_wordlist():
    os.system("clear")
    show_banner()
    
    print(Fore.CYAN + "\nEnter victim details (press Enter to skip any):")
    name = input(Fore.YELLOW + "Victim's Name: ").strip()
    birth_year = input(Fore.YELLOW + "Birth Year: ").strip()
    pet = input(Fore.YELLOW + "Pet Name: ").strip()
    nickname = input(Fore.YELLOW + "Nickname: ").strip()
    fav_number = input(Fore.YELLOW + "Favorite Number: ").strip()

    details = [name, birth_year, pet, nickname, fav_number]
    details = [d for d in details if d]

    if not details:
        print(Fore.RED + "\n⚠️  Error: No details provided. Wordlist cannot be generated.\n")
        return

    print(Fore.GREEN + "\nVictim Details Used:", details)

    try:
        min_length = int(input(Fore.CYAN + "Enter minimum password length: "))
        max_length = int(input(Fore.CYAN + "Enter maximum password length: "))

        if min_length > max_length or min_length <= 0:
            print(Fore.RED + "\n⚠️  Invalid length range. Try again.\n")
            return
    except ValueError:
        print(Fore.RED + "\n⚠️  Invalid input. Please enter numbers only.\n")
        return

    filename = "hco_wordlist.txt"
    wordlist = set()

    print(Fore.YELLOW + "\nGenerating Wordlist... Please wait.")

    total_combinations = sum(len(details) ** length for length in range(min_length, max_length + 1))
    generated = 0

    with open(filename, "w") as f:
        for length in range(min_length, max_length + 1):
            for combination in itertools.product(details, repeat=length):
                word = "".join(combination)
                wordlist.add(word)
                f.write(word + "\n")

                generated += 1
                progress = (generated / total_combinations) * 100
                print(Fore.GREEN + f"\r☠️  Generating... {generated}/{total_combinations} words ({progress:.2f}%)", end="", flush=True)

    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        print(Fore.GREEN + f"\n\n☠️  Wordlist successfully saved as: {filename}")
        print(Fore.YELLOW + "☠️  You can check the file using: cat hco_wordlist.txt\n")
    else:
        print(Fore.RED + "\n⚠️  Error: Wordlist generation failed. Please try again.")

if __name__ == "__main__":
    main_menu()