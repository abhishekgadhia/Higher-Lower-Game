from art import logo, vs
from game_data import data
import random


# get random account
def get_random_account():
    """
    get a random account from the data and return it
    :return:
    """
    return random.choice(data)


# get all the data about it
def account_info(account: dict):
    """
    get the account as input and then access the name, description, and the
    country to which the account belongs and return it in a formatted string
    :param account:
    :return:
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]

    # return this info
    return f"{name}, a {description}, from {country}"


# check user answer
def check_answer(guess, a_followers: int, b_followers: int):
    """
    checks which account has higher number of followers and returns True or False based
    on whether user's guess was correct
    :param guess:
    :param a_followers:
    :param b_followers:
    :return:
    """
    if a_followers > b_followers:
        return guess == "a"

    else:
        return guess == "b"


# main game loop
def main():
    """
    main game loop
    :return:
    """
    print(logo)
    score = 0
    should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while should_continue:
        # assign account a as the account b from last round
        account_a = account_b
        account_b = get_random_account()

        # if both accounts are same then get a new account for b
        while account_a == account_b:
            account_b = get_random_account()

        print(f"a: {account_info(account_a)}")
        print(vs)
        print(f"b: {account_info(account_b)}")

        user_guess = input("Who has more followers? Type 'a' or 'b': ")

        followers_a = account_a["follower_count"]
        followers_b = account_b["follower_count"]

        # use the check_answer() function to check if the user's guess is correct
        correct = check_answer(user_guess, followers_a, followers_b)

        print(logo)
        # if user guesses correctly
        if correct:
            # increment and print score
            score += 1
            print(f"You're correct, current score: {score}")
        # if guess is incorrect
        else:
            # end game loop and print final score
            should_continue = False
            print(f"You're incorrect, final score: {score}")


if __name__ == '__main__':
    main()
