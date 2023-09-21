import random
import game_data
import art
import os


# def clear():
#     os.system('clear')


def randomise_a():
    a = (random.choice(game_data.data))
    return a


def randomise_b(a):
    b = (random.choice(game_data.data))
    while b == a:
        b = (random.choice(game_data.data))
    return b


def start(a, b, score):
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(
        f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(
        f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")


def player_bet():
    x = input("Who has more followers? Type 'A' or 'B': ").lower()
    return x


score = 0
game_over = False

while not game_over:
    if score == 0:
        a = randomise_a()
        b = randomise_b(a)
    elif score > 0:
        a = b
        b = randomise_b(a)
    start(a, b, score)
    player_choice = player_bet()
    if player_choice == "a" and a["follower_count"] > b["follower_count"]:
        score += 1
        os.system('cls')
    elif player_choice == "b" and a["follower_count"] < b["follower_count"]:
        score += 1
        os.system('cls')
    else:
        os.system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True
