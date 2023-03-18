import math
import random


population = 100
land = 1000
bushel = 2800
immigrant = 5
land_value = 19
total_harvest = 3000
productivity = 3
max_person_capability = 10
starved_death = 0
ruling_year = 0
rat_destruction = 200
land_utilization = 1000
dead_counter = 0
death_by_plague = 0


def test_sell_land(test_num):
    global land, bushel
    test_land_sold = test_num
    land -= test_land_sold
    bushel += test_land_sold * land_value
    print(f"Test1 Passed.... Bushels: {bushel} Land: {land}")


def sell_land():
    global land, bushel
    land_sold = input("\n----\nHow many acres of land do you want to sell? \n"
                      "Enter a number, or enter if do not want to sell\n----")
    if not land_sold:
        land_sold = 0
    land_sold = int(land_sold)
    land -= land_sold
    print(f"Your total land is {land} acres\n")
    bushel += land_sold * land_value
    print(f"Your total bushel is now {bushel} bushels\n")

def test_buy_land(test_num):
    global land, bushel
    test_land_purchased = test_num
    land += test_land_purchased
    bushel -= test_land_purchased * land_value
    print(f"Test2 Passed.... Bushels: {bushel} Land: {land}")

def buy_land():
    global land, bushel
    land_purchased = input("\n----\nHow many acres of land do you want to buy? \n"
                           "Enter a positive number, or enter if do not want to buy\n----")
    if not land_purchased:
        land_purchased = 0
    land_purchased = int(land_purchased)
    land += land_purchased
    print(f"Your total land is {land} acres\n")
    bushel -= land_purchased * land_value
    print(f"Your total bushel is now {bushel} bushels\n")

def test_feed_people(test_num):
    global bushel, starved_death, population
    test_bushels_fed = test_num
    bushel -= test_bushels_fed
    test_total_fed = test_bushels_fed //20
    starved_death = population - test_total_fed
    print(f"Test3 Passed.... Bushels: {bushel} Population: {population} Starved to death: {starved_death}")




def feed_people():
    global bushel, starved_death, population
    bushels_fed = input(f"\n----\n You currently have {population} people."
                        f"And it needs {population * 20} bushels to feed all your.\n"
                        f"How many bushels do you want to feed your people?\n"
                        f"Provide a number or press enter to feed all you people\n----")
    if not bushels_fed:
        bushels_fed = population*20
    bushels_fed = int(bushels_fed)
    if bushel < bushels_fed:
        print("You don't have that much bushels")
        feed_people()
    else:
        bushel -= bushels_fed
        print(f"Your total bushel is now {bushel} bushels\n")
        total_fed = bushels_fed // 20
        print(f"These bushed are enough for {total_fed} people\n")
        starved_death = population - total_fed

def test_uprising():
    global starved_death, population
    starved_death = starved_death//2
    population = population//2
    if starved_death / population > 0.45:
        print("Test4 Passed.... Uprising happened")
    else:
        print("Test4 Passed.... Uprising did not happen ")



def uprising():
    global starved_death, population
    while (starved_death / population) > 0.45:
        print("There was an uprising. You got kicked out of office. GAME OVER\n")
        break

def test_starvation_death():
    global starved_death, population
    if starved_death > 0:
        print(f"Test5 Passed.... Death count was {starved_death}")
    else:
        print("Test5 Passed.... Nobody died")
        starved_death = 0



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

def test_acre_to_plant(test_num):
    global land_utilization, bushel, land, population
    if test_num == 0:
        land_utilization = population *10
    if land_utilization < land:
        bushel = land_utilization * productivity
    print(f"Test6 Passed.... you will make {bushel} bushels")

def acre_to_plant():
    global land_utilization, bushel, land, population
    land_utilization = input("\n----\nHow many acres do you want to plant with grain?\n"
                             "Or enter to maximize you land use\n----")
    if not land_utilization:
        land_utilization = population * 10
    land_utilization = int(land_utilization)
    if land_utilization > land:
        print("You don't have that much land.")
        acre_to_plant()
    else:
        bushel = land_utilization * productivity
        print(f"These land will make total of {bushel} bushels\n")

def test_plague_death():
    global starved_death, population, death_by_plague
    if is_plague():
        death_by_plague = population // 2
        print(f"Test7 passed.... there is a plague during the year, and it killed {death_by_plague} people\n")
        population = death_by_plague
    else:
        print("Test7 passed.... there was no plague. Lucky you!!")


def is_plague():
    random_num = random.randint(1, 100)
    if random_num <= 15:
        return True
    else:
        return False


def plague_death():
    global starved_death, population, death_by_plague
    death_by_plague = 0
    if is_plague():
        death_by_plague = population // 2
        print(f"There is a plague during the year, and it killed {death_by_plague} people\n")
        population = death_by_plague
    else:
        print("There was no plague. Lucky you!!\n")
    print(f"Current population is {population}\n")

def test_immigration():
    global immigrant, population, starved_death
    if starved_death > 0:
        print("Test8 passed.... there was no immigration. No one wanted to die with you")
        immigrant = 0
    else:
        immigrant = math.trunc((20 * land + bushel) / (100 * population) + 1)
        if immigrant < 0:
            immigrant = 0
        else:
            print(f"Test8 passed.... there are {immigrant} people coming to your Kingdom")
            population += immigrant
def immigration():
    global immigrant, population, starved_death
    if starved_death > 0:
        print("There was no immigration. No one wanted to die with you\n----")
        immigrant = 0
    else:
        immigrant = math.trunc((20 * land + bushel) / (100 * population) + 1)
        if immigrant < 0:
            immigrant = 0
        else:
            print(f"There are {immigrant} people coming to your Kingdom\n")
            population += immigrant
    print(f"Current population is {population}\n")

def test_harvest():
    global total_harvest, land_utilization, bushel, productivity
    productivity = random.randint(1, 6)
    total_harvest = land_utilization * productivity
    bushel += total_harvest
    print("Test9 passed.... all variables were updated")


def harvest():
    global total_harvest, land_utilization, bushel, productivity
    productivity = random.randint(1, 6)
    print(f"This year, one acre of land produced {productivity} bushel(s)\n----\n")
    total_harvest = land_utilization * productivity
    print(f"You made {total_harvest} this year \n")
    bushel += total_harvest
    print(f"Your total bushel is {bushel}\n")

def test_grain_eaten_by_rat():
    global rat_destruction, total_harvest, bushel
    rat_destruction = 0
    i = random.randint(1, 10)
    if i <= 6:
        print("Test10 passed.... there was no Rat problem last year")
    else:
        random_destruction = random.uniform(0.10, 0.30)
        rat_destruction = round(total_harvest * random_destruction)
        print(f"Test10 passed.... the damm rats destroyed {rat_destruction} bushel of your harvest")
    bushel -= rat_destruction
def grain_eaten_by_rat():
    global rat_destruction, total_harvest, bushel
    rat_destruction = 0
    i = random.randint(1, 10)
    if i <= 6:
        print("There was no Rat problem last year\n----")
    else:
        random_destruction = random.uniform(0.10, 0.30)
        rat_destruction = round(total_harvest * random_destruction)
        print(f"The damm rats destroyed {rat_destruction} bushel of your harvest")
    bushel -= rat_destruction
    print(f"Your total bushel is {bushel}\n")

def test_new_cost_of_land():
    global land_value
    land_value = random.randint(17, 23)
    print(f"Test11 passed.... Current land price is {land_value}")
def new_cost_of_land():
    global land_value
    land_value = random.randint(17, 23)
    print(f"\n----\nCurrent land price is {land_value}\n")


test_sell_land(50)
test_buy_land(0)
test_buy_land(50)
test_feed_people(1500)
test_uprising()
test_starvation_death()
test_acre_to_plant(0)
test_plague_death()
test_immigration()
test_harvest()
test_grain_eaten_by_rat()
test_new_cost_of_land()




