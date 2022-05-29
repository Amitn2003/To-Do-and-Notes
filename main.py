from ast import While
from sys import argv
import datetime

def check_name():
    global name
    try:
        # print(f"Welcome {argv[1].capitalize()}")
        name = argv[1]
    except:
        name = input("\nEnter your name: ")
    print(f"Welcome {name.capitalize()}!")




def log_take():
    global log_duration
    global log_note
    log_duration = int(input("Enter the time you want to log(in minutes): "))
    # Asking the note the user wants to log
    log_note = input("Enter the note you want to log: \n ")
    # Let the user preview the message he/she wrote previously
    print(f"\nHello {name} Your note(log) is \n{log_note}")



def save_log():
    my_file = open("test_file.txt", "a+")
    my_file.write(f"\n{name}'s {log_duration} minutes' log note is - {log_note}. ")
    my_file.close()

def see_log():
    my_file = open("test_file.txt")
    print(my_file.read())
    my_file.close()


if __name__ == "__main__":
    print(f"Today is {datetime.datetime.now()}")  # Returns Current time (exact)
    check_name()
    # Ask what the user wants to do?
    while True:
        print("\nIf you want to write down your logs with notes press 1\nIf you want to see your logs with notes press 2")
        choice = int(input("Enter What you want to do: "))
        if choice == 1:
            log_take() #To take the log note
            save_log()
        elif choice == 2:
            # print("Printing the whole .txt file here using r+ readlines")
            see_log()
        else:
            print("Invalid input!!")
            exit(1)
            break

    print("Thank you for using this tool. Hope you've enjoyed this.")



