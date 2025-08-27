import random

money = 100
win_count = 0
lose_count = 0

print("Welcome to the Guessing Number Game!")
print("You start with $100. Each game costs $5. Win = +$10 reward.")
print("Game ends if you lose all your money.\n")

while money >= 5:
    comp_number = random.randint(1, 100)
    level = int(input("Choose level [1=Easy, 2=Medium, 3=Hard]: "))

    times = 10 if level == 1 else 5 if level == 2 else 3
    is_win = False

    money -= 5

    for attempt in range(times):
        guess = int(input(f"Enter your guess #{attempt + 1}: "))

        if guess == comp_number:
            print("Correct! You win!")
            is_win = True
            money += 10
            win_count += 1
            break
        elif guess < comp_number:
            print("Too low!")
        else:
            print("Too high!")

    if not is_win:
        print(f"Game over! The number was {comp_number}")
        lose_count += 1

    print("-" * 30)
    print(f"Money left: ${money}")
    print(f"Wins: {win_count} | Losses: {lose_count}")
    print("-" * 30)

    if money < 5:
        print("You don't have enough money to continue. Game ends.")
        break

    cont = input("Do you want to play again? [yes/no]: ")
    if cont.lower() == 'n':
        break

print("\n===== Final Report =====")
print(f"Total Wins: {win_count}")
print(f"Total Losses: {lose_count}")
print(f"Final Money: ${money}")
print("========================")
