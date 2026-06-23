import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move (Rock, Paper, Scissor)\n=")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock, Computer Win")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice == "Paper":
    if comp_choice == "Scisssor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You Win")

elif user_choice == "scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You Win")
    else:
        print("Rock samshes scissor, Computer Win")


