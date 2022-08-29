import random

def main():
    score = input("Enter your score: ")
    get_score(score)
    get_random_score()


def get_score(score):
    print("Your score is {}".format(score))


def get_random_score():
    random_score = random.randint(1, 100)
    print("The random score is {}".format(random_score))

main()