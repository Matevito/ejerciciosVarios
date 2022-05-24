def printResponse(letters, numbers): 
    # transform the lists to strings and print them
    lettersString = " ".join(letters)

    numbersString = " ".join([str(n) for n in numbers])
    
    print(lettersString)
    print(numbersString)

# no se me ocurre un nombre para la función
def programForWilmer (list): 
    # 1. get response data
    previousLetter = ""
    shirtsList = []
    numbersList = []
    
    for shirt in list:
        if shirt == previousLetter:
            # increase last value on numbersList
            numbersList[-1] += 1
        else:
            # add new shirt and number value
            shirtsList.append(shirt)
            numbersList.append(1)
            
            # loop conditional
            previousLetter = shirt
            
    # 2. print response
    printResponse(shirtsList, numbersList)

# function test
test_array = [ "A", "A", "A", "R", "N", "N", "N", "N", "N", "A", "A", "M"]

programForWilmer(test_array)