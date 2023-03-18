import math
import random

name = input("Welcome to Hammurabi! Please enter your name: \n").upper()
population = 100
land = 1000
bushel = 2800
immigrant = 5
land_value = 19
total_harvest = 3000
productivity = 3
max_person_capability = 10
starved_to_death = 0
ruling_year = 0
rat_destruction = 200
land_utilization = 1000


def play():
    print_summary()


def play_again():
    pass


def sell_land():
    return int(input("How acre of land you want to sell? \n"
                     "Enter a number, or 0 if do not want to sell"))


def buy_land():
    return int(input("How many acre of land you want to buy? \n"
                     "Enter a positive number, or 0 if do not want to buy"))


def feed_people():
    return int(input("How many bushel you want to feed your people? \n"
                     "(20 bushels to feed 1 person per year)"))


def acre_to_plant():
    return int(input("How many acre you want to plant with grain? "))


def is_plague():
    random_num = random.randint(1, 100)
    if random_num <= 15:
        return True
    else:
        return False


def plague_death():
    if is_plague():
        death = random.randint(0, 100)
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
    x = random.randint(1, 6)
    print(f"This year, one acre of land produce {x} bushels")
    return land_utilization * x


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
    print(f"\n\nKING {name}, I BEG TO REPORT TO YOU: \n\n"
          f"In year {ruling_year} under your ruling, \n"
          f"1. There were{starved_to_death} people was starved to death. \n"
          f"2. THere were {immigrant} moved to your Kingdom.\n"
          f"3. The Kingdom population now is {population}.\n"
          f"4. You own {land} acres of land.\n"
          f"5. We harvested {total_harvest} bushels for you.\n"
          f"6. Productivity was {productivity} per acre.\n"
          f"7. The damm rats ate {rat_destruction} of your bushels.\n"
          f"8. You now have {bushel} bushels in stock.\n"
          f"9. Land is trading at {land_value} per acre")


def print_final():


play()