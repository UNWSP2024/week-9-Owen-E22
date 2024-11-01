# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def main():

    loop = 'y'
    while loop == 'y':
        number_of_numbers = int(input('How many numbers would you like to add: '))
        if number_of_numbers > 1000:
            print('number cannot be greater than 1000: ')
            loop = 'y'
        else:
            loop = 'n'

    openfile = open('random_numbers.txt', 'w')
    for number in range(0, number_of_numbers):
        ran_num = str(random.randint(1,500))
        openfile.write(ran_num + '\n')


main()