import random

a = 1
b = 0
c = 0

print("Welcome To Snake-Water-Gun Game \n Select : \n   1. For Snake\n   2. For Water\n   3. For Gun\n")


def snake():
    global a, b, c
    random_num = random.randint(1, 3)
    if random_num == 2:
        b = b + 1
        print("You Selected Snake & Computer Selected Water\n You =", b, "Computer =", c)
    elif random_num == 3:
        c = c + 1
        print("You Selected Snake & Computer Selected Gun\n You =", b, "Computer =", c)
    elif random_num == 1:
        print("GAME TIED")
    a = a + 1


def water():
    global a, b, c
    random_num = random.randint(1, 3)
    if random_num == 1:
        c = c + 1
        print("You Selected Water & Computer Selected Snake\n You =", b, "Computer =", c)
    if random_num == 3:
        b = b + 1
        print("You Selected Water & Computer Selected Gun\n You =", b, "Computer =", c)
    if random_num == 2:
        print("GAME TIED")
    a = a + 1


def gun():
    global a, b, c
    random_num = random.randint(1, 3)
    if random_num == 1:
        b = b + 1
        print("You Selected Gun & Computer Selected Snake\n You =", b, "Computer =", c)
    if random_num == 2:
        c = c + 1
        print("You Selected Gun & Computer Selected Water\n You =", b, "Computer =", c)
    if random_num == 3:
        print("GAME TIED")
    a = a + 1


while a in range(1, 11):
    inp = int(input("Select Now "))
    if inp == 1:
        snake()

    elif inp == 2:
        water()

    elif inp == 3:
        gun()

if b > c:
    print("\nYOU SCORED ", b, "AND COMPUTER SCORED ", c, "\n YOU WON THE GAME")
if c > b:
    print("\nYOU SCORED ", b, "AND COMPUTER SCORED ", c, "\n YOU LOSE THE GAME")
