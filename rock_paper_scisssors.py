import random

choice = input("Enter choice: 1: Rock, 2: Paper, 3: Scissors. \nYour choice: ")
choice = int(choice)
computer_choice = random.randint(1, 3)

if choice == computer_choice:
    print(f"Draw! {choice} - {computer_choice}")

elif choice > computer_choice:
    if (computer_choice == 1) & (choice == 3):
        print(f"You lose!!! You: {choice} - Computer: {computer_choice}")
    else:
        print(f"You win!! You:{choice} - Computer:{computer_choice}")

else:
    if (computer_choice == 3) & (choice == 1):
        print(f"You win!! You:{choice} - Computer:{computer_choice}")
    else:
        print(f"You lose!! You:{choice} - Computer:{computer_choice}")
