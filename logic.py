if player_choose == computer_choose:
    print("You are draw.")
elif player_choose == 0 and computer_choose == 1:
    print("You are win.")
elif player_choose == 1 and computer_choose == 0:
    print("You are lose.")
elif player_choose == 0 and computer_choose == 2:
    print("You are lose.")
elif player_choose == 2 and computer_choose == 0:
    print("You are win")
elif player_choose == 1 and computer_choose == 2:
    print("You are win.")
elif player_choose == 2 and computer_choose == 1:
    print("You are lose.")