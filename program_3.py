# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    infile = open('numbers.txt', 'r')
    total = 0

    try:

        for line in infile:
            line = infile.readline()

            amount = float(line)

            total += amount
        print(f'The total of the numbers is {total}')
        infile.close()


    except IOError:
        print('There was an error reading the file')
    except ValueError:
        print('Non-numeric data found in the file')
    except:
        print('An error occurred')





# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()