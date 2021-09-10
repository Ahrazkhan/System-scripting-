# Define function that accept one parameter(int) and do some mathematical operations
def reducer(number: int):

    if number == 1:
        return 1
    elif number % 2 == 0:
        number = int(number / 2)
        print(number)
    else:
        number = int(number * 3 + 1)
        print(number)
    reducer(number)  # recursively call reducer() function.


# Request for only integer number input.
while True:
    try:
        num = int(input('Please enter an integer: '))
        break
    except ValueError:
        print('No valid integer! please try again...')
# Run the function
reducer(num)
