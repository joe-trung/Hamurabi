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
ruling_year = 0
rat_destruction = 200
land_utilization = 1000
dead_counter = 0
death_by_plague = 0
game_over = False


def play():
    global ruling_year, game_over
    for i in range(10):
        print(f"\n------------\nYEAR #{ruling_year} REPORT\n")
        print_summary()
        new_cost_of_land()
        sell_land()
        buy_land()
        feed_people()
        uprising()
        if game_over:
            break
        else:
            starvation_death()
            acre_to_plant()
            plague_death()
            immigration()
            harvest()
            grain_eaten_by_rat()
            if population < 0 or bushel < 0 or land < 0:
                print(f"\033[91mYou drove your Kingdom under ground on year #{ruling_year}. GAME OVER\033[m")
                game_over = True
                break
            ruling_year += 1
    if not game_over:
        print_final()
        play_again()


def play_again():
    if input("\n-----\n-----\nYou are elected for another term.\n"
             "Do you want to take the office again? (y or n)") == "y":
        play()


def sell_land():
    global land, bushel
    land_sold = input("\n----\nHow many acres of land do you want to sell? \n"
                      "Enter a number, or enter if do not want to sell\n----")
    if not land_sold:
        land_sold = 0
    land_sold = int(land_sold)
    if land < land_sold:
        print(f"You don't have that much land to sell, max {land}\n")
        sell_land()
    else:
        land -= land_sold
        print(f"Your total land is {land} acres\n")
        bushel += land_sold * land_value
        print(f"Your total bushel is now {bushel} bushels\n")


def buy_land():
    global land, bushel
    land_purchased = input("\n----\nHow many acres of land do you want to buy? \n"
                           "Enter a positive number, or enter if do not want to buy\n----")
    if not land_purchased:
        land_purchased = 0
    land_purchased = int(land_purchased)
    if bushel < land_purchased * land_value:
        print(f"You don't have enough bushels to buy that much land. \n"
              f"Current bushel is {bushel}, max purchase is {bushel*land_value}\n")
        buy_land()
    else:
        land += land_purchased
        print(f"Your total land is {land} acres\n")
        bushel -= land_purchased * land_value
        print(f"Your total bushel is now {bushel} bushels\n")


def feed_people():
    global bushel, starved_death, population
    bushels_fed = input(f"\n----\nYou currently have {population} people."
                        f"And it needs {population * 20} bushels to feed all your.\n"
                        f"How many bushels do you want to feed your people?\n"
                        f"Provide a number or press enter to feed all you people\n----")
    if not bushels_fed:
        bushels_fed = population * 20
    bushels_fed = int(bushels_fed)
    if bushel < bushels_fed:
        print(f"You don't have that much bushels. Only {bushel} available\n")
        feed_people()
    else:
        bushel -= bushels_fed
        if bushels_fed - population * 20 > 0:
            print(f"You wasted {bushels_fed - population * 20} bushels.\n")
        total_fed = bushels_fed // 20
        print(f"You fed enough for {total_fed} / {population} of your people\n")
        print(f"Your total bushel is now {bushel} bushels\n")
        starved_death = population - total_fed


def uprising():
    global starved_death, population, game_over
    if (starved_death / population) > 0.45:
        print(f"\033[91mThere was an uprising. You got kicked out of office. GAME OVER\033[m\n")
        game_over = True


def starvation_death():
    global starved_death, population
    if starved_death > 0:
        print("You did not feed all your people \n"
              f"Total starvation death count was {starved_death}\n")
    else:
        print(f"\033[94mYou were a good ruler. All of your people \n"
              "were fed.\033[m\n")
        starved_death = 0
    population -= starved_death
    print(f"Population now is {population}")


def acre_to_plant():
    global land_utilization, bushel, land, population
    land_utilization = input("\n----\nHow many acres do you want to plant with grain?\n"
                             "Or enter to maximize human labor\n----")
    if not land_utilization:
        land_utilization = population * 10
    land_utilization = int(land_utilization)
    if land_utilization > land:
        print(f"You don't have that much land. Only {land} available\n")
        acre_to_plant()
    elif bushel < land_utilization * 2:
        print(f"You don't have enough bushel to start cultivation. Only {bushel} available.\n")
        acre_to_plant()
    elif population * 10 < land_utilization:
        print(f"You don't have enough people to cultivate that much land. Max {population*10}\n")
        acre_to_plant()
    else:
        bushel -= land_utilization * 2
        print(f"This crop will cost you {land_utilization * 2} bushels\n"
              f"Will make total of {land_utilization * productivity} bushels\n"
              f"by year end\n"
              f"Your current bushel is {bushel}")


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
        print("\033[94mThere was no plague. Lucky you!!\033[m\n")
    print(f"Current population is {population}\n")


def immigration():
    global immigrant, population, starved_death
    if starved_death > 0:
        print(f"\033[91mThere was no immigration. No one wanted to die with you\033[m\n----")
        immigrant = 0
    else:
        immigrant = math.trunc((20 * land + bushel) / (100 * population) + 1)
        if immigrant < 0:
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


def new_cost_of_land():
    global land_value
    land_value = random.randint(17, 23)
    print(f"\n----\nCurrent land price is {land_value}\n")


def print_summary():
    print(f"\n\n\033[93mKing {name}, KING of the Kings, I beg to report to you honor: \033[m\n\n"
          f"In year {ruling_year} under your ruling, \n"
          f"1. \033[94mThere were {starved_death} people was starved to death. \033[m\n"
          f"2. There were {immigrant} moved to your Kingdom.\n"
          f"3. \033[94mThe Kingdom population now is {population}.\033[m\n"
          f"4. You own {land} acres of land.\n"
          f"5. \033[94mProductivity this year was {productivity} per acre.\033[m\n"
          f"6. We harvested {total_harvest} bushels for you.\n"
          f"7. \033[94m{death_by_plague} people were killed by plague\033[m\n"
          f"8. The damm rats ate {rat_destruction} of your bushels.\n"
          f"9. \033[94mYou now have {bushel} bushels in stock.\033[m\n"
          f"10. Land is trading at {land_value} per acre")


def print_final():
    print("\033[44;93m\n----\n----\n!!! CONGRATULATION !!!\nYOU SURVIVED YOUR 10 YEARS\n----\n----\n\033[m")
    print_summary()


play()
