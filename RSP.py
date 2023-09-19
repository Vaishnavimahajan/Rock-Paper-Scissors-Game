import random
l=["rock","paper","scissor"]

while True:
    c_count = 0
    u_count = 0
    user_choice = int(input('''
Game Start.....
1.Yes
2.No

    '''))
    if user_choice == 1:
        for a in range(1,6):
            user_input = int(input('''
1. Rock
2. Scissor
3. Paper
        '''))
            if user_input == 1:
                u_choice ="rock"
            elif user_input ==2:
                u_choice ="scissor"
            elif user_input == 3:
                u_choice ="paper"
            C_choice = random.choice(l)
            if C_choice == u_choice:
                print("Computer Value",C_choice)
                print("User Value",u_choice)
                print("Game draw")
                u_count=u_count+1
                c_count=c_count+1
            elif (u_choice == "rock" and C_choice == "scissor") or (u_choice == "paper"
                  and C_choice == "rock")or (u_choice == "scissor" and C_choice == "paper"):
                print("Computer Value",C_choice)
                print("User Value",u_choice)
                print("You Win")
                u_count = u_count+1
            else:
                print("Computer Value",C_choice)
                print("User Value",u_choice)
                print("Computer Win")
                c_count = c_count+1
        if u_count == c_count:
            print("Finel game Draw....")
            print("User Score",u_count)
            print("Computer Score",c_count)
        elif u_count > c_count:
            print("Finel you win the game....")
            print("User Score",u_count)
            print("Computer Score",c_count)
        else:
            print("Finel computer win the game....")
            print("User Score",u_count)
            print("Computer Score",c_count)
 
    else:
        break