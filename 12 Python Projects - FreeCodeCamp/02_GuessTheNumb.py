# GuessTheNumb.py

"""
Create a game where a secret number is generated,
and the user or computer must guess the number.
"""

# 7:12 (User Guess)

import random

def guess(x):
	random_number = random.randint(1, x)
	guess = 0 # So that guess never equals random numb accidentally
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		if guess < random_number:
			print('Sorry, guess again. Too low.')
		elif guess > random_number:
			print('Sorry, guess again, Too high')

	print(f'Congrats! You have guessed the number {random_number} correctly!')

# 13:30 (Computer Guess)

def computer_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		if low != high:
			guess = random.randint(low, high)
		else:
			guess = low #could also be high b/c low = high
		feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
		if feedback == 'h':
			high = guess - 1
		elif the feedback == 'l':
			low = guess + 1
	print(f'The computer guessed your number, {guess}, correctly!')

guess(10)