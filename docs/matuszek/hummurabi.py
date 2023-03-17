import math
import random


def play():
    pass


def play_again():
    pass


current_kingdon_status = dict()


def sell_land():
    return int(input("How acre of land you want to sell? \n"
                     "Enter a number, or 0 if do not want to sell"))


def buy_land():
    return int(input("How many acre of land you want to buy? \n"
                     "Enter a positive number, or 0 if do not want to buy"))


def feed_people():
    return int(input("How many bushel you want to feed your people? \n"
                     "(20 to feed 1 person per year)"))


def acre_to_plant():
    return int(input("How many acre you want to plant with grain? "))


def is_plague():
    return bool(random.getrandbits(1))


def plague_death():
    if is_plague():
        death = random.randint(1, 10)
        print("There is a plague during the year, and it killed " + str(death))
        return death


def starvation_death():
    death = population - feed_people() // 20
    if death > 0:
        print("You did not feed all your people \n"
              "Total starvation death was" + str(death))
        return death
    else:
        print("Your was a good ruler. All of your people \n"
              "was fed. You probably wasted some food")
        return 0


def uprising():
    while (starvation_death()/population) > 0.45:
        print("There was an uprising. You got kicked out of office. GAME OVER")
        break


def immigration():
    if starvation_death() > 0:
        print("There was no immigration. No one want to die with you")
        return 0
    else:
        return math.trunc((20 * land + bushel) / (100 * population) + 1)



def harvest():
    productivity = random.randint(1, 6)
    print(f"This year, one acre of land produce {productivity} bushels")
    return planting_land * productivity


def grain_eaten_by_rat():
    i = random.randint(1, 10)
    if i <= 6:
        print("There was no Rat problem last year")
        return 0
    else:
        random_destruction = random.uniform(0.10, 0.30)
        return harvest * random_destruction


def new_cost_of_land():
    return random.randint(17, 23)


def print_summary():
    pass


def print_final():
    pass
