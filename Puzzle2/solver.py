# this file solves the puzzle 2 from advent of code 2024

def testSafety(numbers):
    safe = True
    if int(numbers[0]) > int(numbers[0 + 1]):
        decending = True
    else:
        decending = False

    if decending:
        for i in range(0, len(numbers) - 1):
            # calc difference
            diff = abs(int(numbers[i]) - int(numbers[i + 1]))

            # check decending
            if (int(numbers[i])) < int(numbers[i + 1]):
                safe = False
                return safe, i

            elif diff < 1 or diff > 3:
                safe = False
                return safe, i
    else:
        for i in range(0, len(numbers) - 1):
            # calc difference
            diff = abs(int(numbers[i]) - int(numbers[i + 1]))

            # check ascending
            if (int(numbers[i])) > int(numbers[i + 1]):
                safe = False
                return safe, i

            elif diff < 1 or diff > 3:
                safe = False
                return safe, i

    return safe, 0

    

def calcSafeLevels():
    with open("input.txt", "r") as file:

        count = 0

        # read through file
        for line in file:

            # put numbers in list
            numbers = line.split()

            state, index = testSafety(numbers)

            # if true increment
            if state:
                count += 1
            
            else:
                res2 = None
                res3 = None
                # remove element that caused problem and neighboring element
                num1 = numbers.copy()
                del num1[index]

                if (index < len(numbers) - 1):
                    num2 = numbers.copy()
                    del num2[index + 1]
                    res2, tmp3 = testSafety(num2)

                if (index > 0):
                    num3 = numbers.copy()
                    del num3[index - 1]
                    res3, tmp4 = testSafety(num3)

                # check both lists
                res1, tmp2 = testSafety(num1)

                if res1 or res2 or res3:
                    count += 1
    
    return count

def main():
    result = calcSafeLevels()
    print(result)




if __name__ == "__main__":
    main()