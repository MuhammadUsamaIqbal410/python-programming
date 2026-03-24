player_name = input ("Please enter you name:")


try:
    player_age = int(input("Please enter your age:"))
    if player_age > 90:
        print(f"sorry Mr.{player_name}, You're entering an invalid age, a player at {player_age}\nshould be immortal to play")
    elif player_age <12:
        print(f"Sorry Mr.{player_name}, You are not eligible for the football team.")
    elif player_age > 25:
        print(f"Sorry Mr.{player_name}, You are not eligible for the football team.")
    
    else:
        print(f"Congratulations Mr.{player_name}, You are eligible for the football team.")
except ValueError:
    print("please enter a vlid age")