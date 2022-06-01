# from ast import While
from sys import argv
import datetime

def check_user_name():
    global user_name
    try:
        # print(f"Welcome {argv[1].capitalize()}")
        user_name = argv[1]
    except:
        user_name = input("\nEnter your name: ")
    user_name = user_name.strip().capitalize()
    print(f"Welcome {user_name}!")




def log_take():
    global log_duration
    global log_note
    while True:
        log_duration = int(input("Enter the time you want to log(in minutes): "))
        if isinstance(log_duration, int):
            break
        else:
            continue
    # Asking the note the user wants to log
    log_note = input("Enter the note you want to log: \n ")
    log_note = log_note.strip()
    # Let the user preview the message he/she wrote previously
    print(f"\nHello {user_name} Your note(log) is \n{log_note}.")



def save_log():
    my_file = open("test_file.txt", "a+")
    my_file.write(f"\n{user_name}'s {log_duration} minutes log note is - {log_note}. ")
    my_file.close()

def see_log():
    my_file = open("test_file.txt")
    print(my_file.read())
    my_file.close()


if __name__ == "__main__":
    print(f"Today is {datetime.datetime.now()}")  # Returns Current time (exact)
    check_user_name()
    while True:
        # Ask what the user wants to do?
        print("\nIf you want to write down your logs with notes press 1\nIf you want to see your logs with notes press 2 \nPress 0 to exit.")
        choice = int(input("Enter What you want to do: "))
        if choice == 1:
            log_take() #To take the log note
            save_log()
        elif choice == 2:
            # Printing the whole .txt file here using  read func
            see_log()        
        elif choice == 0:
            # Printing the whole .txt file here using  read func
            print("Thank you for using this tool. Hope you've enjoyed this.")
            exit(1)
        else:
            print("Invalid input!!")
            print("Thank you for using this tool. Hope you've enjoyed this.")
            exit(1)




