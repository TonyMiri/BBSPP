import datetime
from datetime import timedelta
import random

#364 or 365?

today = datetime.date.today()

def rand_date(today_date):
    #Is this inclusive on both/either end?
    rand_num = random.randrange(0, 365)
    rand_date = today_date + timedelta(days=rand_num)
    return rand_date.strftime('%b %d')

num_of_people = input("How many people are in the room?\n>")

print(f'Generating {num_of_people} birthdays 100,000 times.')

counter = 0
match_cases = 0
while counter < 100000:
    if counter % 10000 == 0:
        print(f'{counter} iterations generated')

    bday_list = []
    for x in range(int(num_of_people)):
        bday = rand_date(today)
        if bday in bday_list:
            match_cases += 1
            break
        bday_list.append(bday)
    counter += 1

match_prob = match_cases / 1000
print(f'100,000 iterations generated. The probability of two people having the \
same birthday in a room of {num_of_people} people is {match_prob}%')

    