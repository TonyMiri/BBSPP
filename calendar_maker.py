import calendar
import math

user_input_date = input("Enter a month and year in the following format: mm/yyyy\n>")

#going to have to clean input
date_values = user_input_date.split("/")
my_month = int(date_values[0])
my_year = int(date_values[1])

#Get the calendar for the given month and month before
last_nums = calendar.month(my_year, my_month-1)
my_nums = calendar.month(my_year,my_month)
next_nums = calendar.month(my_year, my_month + 1)

#Split the calendar by "rows"
last_last_nums = last_nums.split("\n")[-2].split(" ")
my_nums_split = my_nums.split("\n")

#Make each row into a separate list
arr1 = [i.split(" ") for i in my_nums_split]

for x, y in enumerate(arr1):
    #Remove blanks
    arr1[x] = [i for i in y if i != ""]

    #If it's at least the 3rd list and not the last list 
    if x >= 2 and x != len(arr1) - 1:
        #Shift the last element of the list to the next list
        arr1[x+1].insert(0, arr1[x].pop())

arr1[-1] += []

#Move 'Su' to the front
arr1[1].insert(0, arr1[1].pop())

#Add values to last list for the upcoming month
x = 1
if len(arr1[-1]) < 7:
    nums_to_fill = 7 - len(arr1[-1])
    for x in range(1, nums_to_fill+1):
        arr1[-1].append(str(x))

#Populate the first week dates with missing dates from previous month
if len(arr1[2]) < 7:
    boop = -1* (7 - len(arr1[2]))
    arr1[2].insert(0, last_last_nums[boop:])
    arr1[2][0] = arr1[2][0][0]

#Create the top line of the calendar border
cal_top = ""
x = 0
while x <= 84:
    char = "-"
    if x % 12 == 0:
        char = "+"
    cal_top += char
    x += 1

#Center the title of the calendar
title = " ".join(arr1[0])
title_mid = int(len(title)/2)
calendar_center = 42
title_center = 42-title_mid
centered_title = f'{" " * title_center}{title}'
    
#Print the day names centered over their respective columns
day_names = {"Su":"Sunday", "Mo":"Monday", "Tu":"Tuesday", "We":"Wednesday", "Th":"Thursday", "Fr":"Friday",
             "Sa":"Saturday"}
weekday_names_string = ""
for x in arr1[1]:
    name_length = len(day_names[x])
    name_spaces = 12 - name_length
    front_spaces = math.ceil(name_spaces/2)
    tail_spaces = math.floor(name_spaces/2)
    weekday_names_string += f'{"." * front_spaces}{day_names[x]}{"." * tail_spaces}.'

#Create the lines for vertical whitespace in the calendar
calendar_blankspace = ""
x = 0
while x <= 84:
    char = " "
    if x % 12 == 0:
        char = "|"
    calendar_blankspace += char
    x += 1

#Start the formatted printing of the various lines
print(centered_title)
print(weekday_names_string)

date_string = ""
for x in arr1[2:]:
    print(cal_top)
    for y in x:
        date_string += f'|{y}{" "* (11 - len(y))}'
    date_string += "|"
    print(date_string)
    print(calendar_blankspace, calendar_blankspace, calendar_blankspace, sep="\n")

    date_string = ""

print(cal_top)


#NOTES:

# Should be using datetime module to do all date handling
# datetime.date(year, month, 1)
# datetime.timedelta(days=1)

