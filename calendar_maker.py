import calendar
import math
import datetime

user_input_date = input("Enter a month and year in the following format: mm/yyyy\n>")

#going to have to clean input
date_values = user_input_date.split("/")
my_month = int(date_values[0])
my_year = int(date_values[1])

#Get the calendar for the given month and month before
input_date = datetime.datetime.strptime(f'{my_year}/{my_month}', "%Y/%m")
prev_month = input_date.month % 12 - 1
prev_year = my_year
if prev_month == 0:
    prev_month = 12
    prev_year -= 1

last_nums = calendar.month(prev_year, prev_month)
my_nums = calendar.month(my_year,my_month)

#Split the calendar by "rows"
last_nums = last_nums.split("\n")
my_nums_split = my_nums.split("\n")
last_last_nums = " ".join(last_nums[-3:-1]).split(" ")

#Make each row into a separate list
arr1 = [i.split(" ") for i in my_nums_split]

for x, y in enumerate(arr1):
    #Remove blanks
    arr1[x] = [i for i in y if i != ""]

    #If it's at least the 3rd list and not the last list 
    if x >= 2 and x != len(arr1) - 1:
        #Shift the last element of the list to the next list
        arr1[x+1].insert(0, arr1[x].pop())

#Move 'Su' to the front
arr1[1].insert(0, arr1[1].pop())

def fill_week(week):
    counter = 1
    while len(week) < 7:
        week.append(counter)
        counter += 1

#Fill last and second-to-last calendar week in the month
if len(arr1[-2]) < 7:
    arr1[-2] += arr1[-1]
    fill_week(arr1[-2])

if len(arr1[-1]) < 7:
    fill_week(arr1[-1])

#Populate the first week dates with missing dates from previous month
if len(arr1[2]) < 7:
    missing_days = 1 * (7 - len(arr1[2]))
    for x in range(missing_days):
        arr1[2].insert(0, last_last_nums[(x+1)*-1])

#Create the top line of the calendar border
cal_top = ""
x = 0
while x <= 77:
    char = "-"
    if x % 11 == 0:
        char = "+"
    cal_top += char
    x += 1

#Center the title of the calendar
title = " ".join(arr1[0])
title_mid = int(len(title)/2)
title_center = 34-title_mid
centered_title = f'{" " * title_center}{title}'
    
#Print the day names centered over their respective columns
day_names = {"Su":"Sunday", "Mo":"Monday", "Tu":"Tuesday", "We":"Wednesday", "Th":"Thursday", "Fr":"Friday",
             "Sa":"Saturday"}
weekday_names_string = ""
for x in arr1[1]:
    name_spaces = 10 - len(day_names[x])
    if name_spaces % 2 == 0:
        front_spaces = int(name_spaces/2)
        tail_spaces = front_spaces
    else:
        front_spaces = math.floor(name_spaces/2)
        tail_spaces = math.ceil(name_spaces/2)
    #print(f'{x} - front: {front_spaces}, tail: {tail_spaces}')
    #print(weekday_names_string)
    weekday_names_string += f'.{"." * front_spaces}{day_names[x]}{"." * tail_spaces}'
weekday_names_string += "."

#Create the lines for vertical whitespace in the calendar
calendar_blankspace = ""
x = 0
while x <= 84:
    char = " "
    if x % 11 == 0:
        char = "|"
    calendar_blankspace += char
    x += 1

#Start the formatted printing of the various lines
with open(f'{my_month}_{my_year}_calendar.txt', "w+") as f:
    f.write(centered_title + "\n")
    f.write(weekday_names_string + "\n")

    date_string = ""
    for x in arr1[2:]:
        f.write(cal_top + "\n")
        for y in x:
            date_string += f'|{y}{" "* (10 - len(str(y)))}'
        date_string += "|"
        f.write(date_string + "\n")
        f.write(calendar_blankspace + "\n" + calendar_blankspace + "\n" + calendar_blankspace + "\n")

        date_string = ""

    f.write(cal_top)



#NOTES:

# Should be using datetime module to do all date handling
# datetime.date(year, month, 1)
# datetime.timedelta(days=1)

