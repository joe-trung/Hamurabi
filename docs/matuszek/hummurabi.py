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
starved_death = 0
ruling_year = 1
rat_destruction = 200
land_utilization = 1000
dead_counter = 0
death_by_plague = 0


def play():
    global ruling_year
    for i in range(10):
        print(f"\n------------\nWelcome to your year #{ruling_year}\n")
        print_summary()
        new_cost_of_land()
        sell_land()
        buy_land()
        feed_people()
        uprising()
        starvation_death()
        acre_to_plant()
        plague_death()
        immigration()
        harvest()
        grain_eaten_by_rat()
        if population < 0 or bushel < 0 or land < 0:
            print(f"You drove your Kingdom under ground on year #{ruling_year}. GAME OVER")
            break
        ruling_year += 1
    print_final()


def play_again():
    pass


def sell_land():
    global land, bushel
    land_sold = int(input("\n----\nHow many acres of land do you want to sell? \n"
                          "Enter a number, or 0 if do not want to sell\n----"))
    land -= land_sold
    print(f"Your total land is {land} acres\n")
    bushel += land_sold * land_value
    print(f"Your total bushel is now {bushel} bushels\n")


def buy_land():
    global land, bushel
    land_purchased = int(input("\n----\nHow many acres of land do you want to buy? \n"
                               "Enter a positive number, or 0 if do not want to buy\n----"))
    land += land_purchased
    print(f"Your total land is {land} acres\n")
    bushel -= land_purchased * land_value
    print(f"Your total bushel is now {bushel} bushels\n")


def feed_people():
    global bushel, starved_death, population
    bushels_fed = int(input(f"\n----\n You currently have {population} people."
                            f"And it needs {population*20} bushels to feed all your.\n"
                            f"How many bushels do you want to feed your people?\n----"))
    if bushel < bushels_fed:
        print("You don't have that much bushels")
        feed_people()
    else:
        bushel -= bushels_fed
        print(f"Your total bushel is now {bushel} bushels\n")
        total_fed = bushels_fed // 20
        print(f"These bushed are enough for {total_fed} people\n")
        starved_death = population - total_fed


def uprising():
    global starved_death, population
    while (starved_death / population) > 0.45:
        print("There was an uprising. You got kicked out of office. GAME OVER\n")
        break


def starvation_death():
    global starved_death, population
    if starved_death > 0:
        print("You did not feed all your people \n"
              f"Total starvation death count was {starved_death}\n")
    else:
        print("You were a good ruler. All of your people \n"
              "were fed. You probably wasted some food\n")
        starved_death = 0
    population -= starved_death
    print(f"Population now is {population}")


def acre_to_plant():
    global land_utilization, bushel, land
    land_utilization = int(input("\n----\nHow many acres do you want to plant with grain? \n----"))
    if land_utilization > land:
        print("You don't have that much land.")
        acre_to_plant()
    else:
        bushel = land_utilization * productivity
        print(f"These land will make total of {bushel} bushels\n")


def is_plague():
    random_num = random.randint(1, 100)
    if random_num <= 15:
        return True
    else:
        return False


def plague_death():
    global starved_death, population, death_by_plague
    if is_plague():
        death_by_plague = population//2
        print(f"There is a plague during the year, and it killed {death_by_plague} people\n")
    else:
        print("There was no plague. Lucky you!!\n")
    population = death_by_plague
    print(f"Current population is {population}\n")


def immigration():
    global immigrant, population, starved_death
    if starved_death > 0:
        print("There was no immigration. No one wanted to die with you\n----")
        immigrant = 0
    else:
        immigrant = math.trunc((20 * land + bushel) / (100 * population) + 1)
        if immigrant <0:
            immigrant = 0
        else:
            print(f"There are {immigrant} people coming to your Kingdom\n")
            population += immigrant
    print(f"Current population is {population}\n")


def harvest():
    global total_harvest, land_utilization, bushel, productivity
    productivity = random.randint(1, 6)
    print(f"This year, one acre of land produced {productivity} bushel(s)\n----\n")
    total_harvest = land_utilization * productivity
    print(f"You made {total_harvest} this year \n")
    bushel += total_harvest
    print(f"Your total bushel is {bushel}\n")


def grain_eaten_by_rat():
    global rat_destruction, total_harvest, bushel
    i = random.randint(1, 10)
    if i <= 6:
        print("There was no Rat problem last year\n----")
        rat_destruction = 0
    else:
        random_destruction = random.uniform(0.10, 0.30)
        rat_destruction = round(total_harvest * random_destruction)
        print(f"The damm rats destroyed {rat_destruction} bushel of your harvest")
    bushel -= rat_destruction
    print(f"Your total bushel is {bushel}\n")


def new_cost_of_land():
    global land_value
    land_value = random.randint(17, 23)
    print(f"\n----\nCurrent land price is {land_value}\n")


def print_summary():
    print(f"\n\nKING {name}, I BEG TO REPORT TO YOU: \n\n"
          f"In year {ruling_year} under your ruling, \n"
          f"1. There were {starved_death} people was starved to death. \n"
          f"2. There were {immigrant} moved to your Kingdom.\n"
          f"3. The Kingdom population now is {population}.\n"
          f"4. You own {land} acres of land.\n"
          f"5. We harvested {total_harvest} bushels for you.\n"
          f"6. Productivity was {productivity} per acre.\n"
          f"7. {death_by_plague} people were killed by plague\n"
          f"8. The damm rats ate {rat_destruction} of your bushels.\n"
          f"9. You now have {bushel} bushels in stock.\n"
          f"10. Land is trading at {land_value} per acre")


def print_final():
    print("\n----\n----\nCONGRATULATION. YOUR SURVIVE YOUR 10 YEARS\n----\n----\n")
    print_summary()


play()
