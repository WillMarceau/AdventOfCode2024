# this is the code that will solve the first puzzle of Advent of Code 2024

def parseInput():
    # this function will parse the input file into two lists

    # set up lists for return
    l1 = []
    l2 = []

    # open file
    with open("Input.txt", "r") as file:

        # read through file
        for line in file:

            # put numbers in respective lists
            numbers = line.split()
            l1.append(int(numbers[0]))
            l2.append(int(numbers[1]))

    return l1, l2

def calcDistance(l1, l2):
    # this function calculates the distance between all the pairs
    # where a pair is made between to two lowest available numbers in each list
    count = 0

    while(l1 and l2):
        # get min
        low1 = min(l1)
        low2 = min(l2)

        # remove from list
        l1.remove(low1)
        l2.remove(low2)

        # add distance to count
        count += (abs(low1-low2))

    return count
        



def main():
    l1, l2 = parseInput()
    result = calcDistance(l1, l2)
    print(result)



if __name__ == "__main__":
    main()