
# The Apocalypse: In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or else they face massive  nes. If all  milies abide by this policy-that is, they have continue to have children until they have one girl, at which point they immediately stop-what will the gender ratio of the new generation be? (Assume that the odds of someone having a boy or a girl on any given pregnancy is equal.) Solve this out logically and then write a computer simulation of it.

import random

def give_birth():
    boys = 0
    girls = 0

    while girls == 0:
        ran = random.randint(1, 2)
        print(ran)
        if ran == 1:
            boys += 1
        else:
            girls += 1

    return [boys, girls]

def answer(population):
    boys = 0
    girls = 0

    for i in range (0, population):
        x, y = give_birth()
        boys += x
        girls += y


    return boys/girls


print(answer(12312))

