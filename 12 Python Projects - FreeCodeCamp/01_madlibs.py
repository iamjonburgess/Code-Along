# madlibs.py

"""
In this project we use string concatenation to create a 
madlib (take user input to fill in blanks in a story).
"""
# 1:40 - Concatenation Tutorial

# # string concatenation (aka how to put strings together)
# # Suppose we want to create a string that says "subscribe to ______"
# youtuber = 'IMJB' # some string variable

# # few ways to do this

# # concatenate a variable:
# print('subscribe to'  + youtuber)

# # Format strings:
# print('subscribe to {}'.format(youtuber))
# # or
# print(f'subscribe to {youtuber}')

# 3:40

adj = input('Adjective: ')
verb1 = input('Verb: ')
verb2 = input('Verb: ')
famous_person = input('Famous person: ')

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)