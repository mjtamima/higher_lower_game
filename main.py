from game_data import data
from art import logo, vs
import random


def format_data(account):
    name = account['name']
    des = account['description']
    country = account['country']
    return f"{name}, a {des}, from {country}."


def check_answer(usr, a_follower, b_follower):
    if a_follower > b_follower:
        return usr == 'A'
    elif b_follower > a_follower:
        return usr == 'B'


def higher_lower():
    print(logo)
    A = random.choice(data)
    B = random.choice(data)
    while A == B:
        B = random.choice(data)

    game_over = False
    score = 0

    while not game_over:
        print(f"Compare A: {format_data(A)}")
        print(vs)
        print(f"Against B: {format_data(B)}")
        usr = input("Who has more followers? Type 'A' or 'B': ").upper()

        is_correct = check_answer(usr, A['follower_count'], B['follower_count'])
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            A = B
            B = random.choice(data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


higher_lower()
