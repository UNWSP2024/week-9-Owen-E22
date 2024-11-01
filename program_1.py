# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.


def count_file_lines():
    names = open('names.txt', 'w')
    names.write('Owen\n')
    names.write('John\n')
    names.write('Sally\n')
    names.write('Tom\n')
    names.write('Dave\n')
    names.write('Beth\n')
    names.close()

    infile = open('names.txt', 'r')
    total = 0
    name = infile.readline()
    name = name.rstrip('\n')


    while name != '':
        name = infile.readline()
        name = name.rstrip('\n')
        total += 1

    ######################
    print(f'There are {total} names in the file')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()