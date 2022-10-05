from operator import indexOf
import random

secret_num = str(random.randint(1, 999))
while len(secret_num) < 3:
    secret_num = '0' + secret_num

guesses = 0

def validate_input(user_guess):
    if len(user_guess) != 3:
        print("Please guess a number with 3 digits.")
        return False
    nums = [str(x) for x in range(0,10)]
    user_nums = list(user_guess)
    if not all(num in nums for num in user_nums):
        print("That is not a valid number. Please try again.")
        return False
    return True

def guess_validator(secret_digit, guess_digit):
    return secret_digit == guess_digit 

def start_screen():
    print("I will say 'Bagels' if your guess has no correct digits",
        "I will say 'Fermi' if your guess has a correct digit in the correct\
 place",
        "I will say 'Pico' if your guess has a correct digit in the wrong\
 place", sep='\n')

if __name__ == '__main__':

    start_screen()

    while guesses < 10:
        print(f'You have {10-guesses} guesses remaining.')
        guess = input("Guess the secret 3 digit number:\n>")
        valid_num = validate_input(guess)
        if not valid_num:
            continue

        if guess == secret_num:
            print("You got it!")
            #Add a play again option here
            play_again = input("Would you like to play again? Y/n")
            if play_again.lower() == 'y':
                start_screen()
                guesses = 0
                continue
            break

        guess_list = list(guess)
        secret_list = list(secret_num)

        guess_map = map(guess_validator, secret_list, guess_list)

        if all(num not in secret_list for num in guess_list):
            print("Bagels")
            guesses += 1
            continue

        for ind, val in enumerate(guess_list):
            if val in secret_list:
                if secret_list[ind] != val:
                    print("Pico")
                    continue
                print("Fermi")
        guesses += 1
print(f'The correct number was {secret_num}')


