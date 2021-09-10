# generate random integer numbers.
from random import randint

word_list = []
# Request for input word or numbers 12 times and save into list.
for number in range(1, 13):
    word_list.append(input(f'{number}) Enter word or number: '))

# word_list = ['4', '5', 'me', 'her', '3', '8', 'see', '9', 'he', '7', '6', '2']

question = True

num = 0
# request a user to enter the number(only integer) of items to be deleted.
while question:
    try:
        num = int(input('Please enter the number of delete items: '))
        if 2 < num < 6:
            print(f'{num} items were randomly deleted.')
            question = False
        else:
            print('The number should fall between 2 and 6')
    except ValueError:
        print('You must enter int value to delete items.')


# To actually copy the list and display it after the function runs.
original_list = list(word_list)


# Define a function that accepts two-parameter(list and integer number) and delete items from a list.
def function(lst: list, x: int):
    for i in range(x):
        lst.pop(randint(1, 4))
    return f'Result tuple: {tuple(lst)}'


# run the function and display original list.
print(function(word_list, num))
print(f'Original list: {original_list}')
