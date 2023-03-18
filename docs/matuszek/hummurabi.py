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
death = 0
ruling_year = 1
rat_destruction = 200
land_utilization = 1000
dead_counter = 0


def play():
    global ruling_year

    for i in range(10):
        print_summary()
        sell_land()
        buy_land()
        acre_to_plant()
        plague_death()
        starvation_death()
        uprising()
        immigration()
        harvest()
        grain_eaten_by_rat()









        ruling_year += 1



def play_again():
    pass


def sell_land():
    global land
    global bushel
    land_sold = int(input("\nHow many acres of land do you want to sell? \n"
                     "Enter a number, or 0 if do not want to sell\n----"))
    land -= land_sold
    bushel += land_sold * land_value
    return land

def buy_land():
    global land
    land_purchased = int(input("How many acres of land do you want to buy? \n"
                     "Enter a positive number, or 0 if do not want to buy\n----"))
    land += land_purchased
    return land


def feed_people():
    global bushel
    bushels_fed = int(input("How many bushels do you want to feed your people? \n"
                     "(20 bushels to feed 1 person per year)\n----"))
    bushel -= bushels_fed
    return bushel

def acre_to_plant():
    acres_used = int(input("How many acres do you want to plant with grain? \n----"))
    return acres_used


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
    global death
    death = population - feed_people() // 20
    if death > 0:
        print("You did not feed all your people \n"
              "Total starvation death count was" + str(death))
        return death
    else:
        print("You were a good ruler. All of your people \n"
              "were fed. You probably wasted some food")
        death = 0
        return death


def uprising():
    while (starvation_death()/population) > 0.45:
        print("There was an uprising. You got kicked out of office. GAME OVER")
        break


def immigration():
    global immigrant
    if starvation_death() > 0:
        print("There was no immigration. No one wantsd to die with you\n----")
        immigrant = 0
        return immigrant
    else:
        immigrant = math.trunc((20 * land + bushel) / (100 * population) + 1)
        return immigrant


def harvest():
    global total_harvest
    global land_utilization
    x = random.randint(1, 6)
    print(f"This year, one acre of land produced {x} bushel(s)\n----")
    total_harvest = land_utilization * x
    return total_harvest


def grain_eaten_by_rat():
    global rat_destruction
    i = random.randint(1, 10)
    if i <= 6:
        print("There was no Rat problem last year\n----")
        rat_destruction = 0
        return rat_destruction
    else:
        random_destruction = random.uniform(0.10, 0.30)
        rat_destruction = harvest * random_destruction
        return rat_destruction


def new_cost_of_land():
    global land_value
    land_value = random.randint(17, 23)
    return land_value


def print_summary():
    print(f"\n\nKING {name}, I BEG TO REPORT TO YOU: \n\n"
          f"In year {ruling_year} under your ruling, \n"
          f"1. There were {death} people was starved to death. \n"
          f"2. THere were {immigrant} moved to your Kingdom.\n"
          f"3. The Kingdom population now is {population}.\n"
          f"4. You own {land} acres of land.\n"
          f"5. We harvested {total_harvest} bushels for you.\n"
          f"6. Productivity was {productivity} per acre.\n"
          f"7. The damm rats ate {rat_destruction} of your bushels.\n"
          f"8. You now have {bushel} bushels in stock.\n"
          f"9. Land is trading at {land_value} per acre")



def print_final():
    pass


play()
