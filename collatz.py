import random

num = random.randrange(1000000)

def first_step(x):

    if x % 2 == 0:
        x = x/2
    else:
        x = x * 3 + 1

    counter = 1
    if x == 1:
        print(x)
        return
    else:
        print(x)
        counter += 1
        first_step(x)

first_step(num)
