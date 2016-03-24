import os

numberLength = 5 # Length of number
maxGuessVal = 2 # allowed maximum guess attempts
stop = 1 # Number to stop game

# Check repeated number in given string
def isRepeated(checkArray,userArrayLength):
    repeated = 0 #constant to store value if number is repeated
    tempArray = []
    intTemp = 0; # Guesses done by user
    i = 0;
	
	# Check whole value to get repeated numbers
    for value in checkArray:
        i += 1
        if value not in tempArray:
            tempArray.append(value)
        
        if i == len(checkArray) and len(tempArray) != len(checkArray) and repeated == 0:
            repeated = 1 # Repeated number found
    
    if repeated == 0: # Number is perfect
        os.system("CLS")
        getGuess(checkArray,intTemp)
    else:
        print "Do not repeat numbers please !" # Value with repeated numbers, Ask again for input
        getInput()
        return

# Function to get guess
def getGuess(userArray,userGuessDone):    
    userArrayString = ''.join(userArray)
    if userGuessDone < maxGuessVal: # Check for guess limit 
        commonElements = 0
        unCommonElements = 0
        guessInput = input("Guess the number : ")
        
        if guessInput == stop: # To exit in between           
            print "You lost the game, You did "+str(userGuessDone)+" attempt(s)"
            print "Correct number was :"+userArrayString
            raw_input("Press ENTER to exit")
            print "Closing.."
        else: # Compare user input and admin number
            guessInputArray = list(guessInput)
            correctMatches = set(userArray).intersection(set(guessInputArray))
            correctMatchesLangth = len(correctMatches)
            correctMatchesNotMatched = len(guessInputArray)- correctMatchesLangth
            
        for key,matchArray in enumerate(userArray):
            if key < len(guessInputArray):
                if userArray[key] == guessInputArray[key]:
                    commonElements += 1
                else:
                    unCommonElements += 1
            else:
                unCommonElements += 1

        if commonElements == len(userArray): # Both value matched
            print "Congratulations, You won the game in "+str((userGuessDone+1))+" attemp(s) !!"
            closeInput = raw_input("Press ENTER to exit")
            print "Closing..."
        else: # Value does not matched
            userGuessDone += 1
            if userGuessDone < maxGuessVal: # Does not reached to maximum guess limit
                print str(commonElements)+" numbers are on correct position, "+str(unCommonElements)+" numbers are not on correct position"
                print str(correctMatchesLangth)+" numbers matched, "+str(correctMatchesNotMatched)+" numbers not matched"
                print "You are left with "+str(maxGuessVal - userGuessDone)+" attempt(s) only"
                print "Guess another number please, To stop press "+str(stop)
                getGuess(userArray,userGuessDone)
            else: # Reached to maximum guess limit
                lostMessage(userArrayString,maxGuessVal)
    else: # Reached to maximum guess limit
        lostMessage(userArrayString,maxGuessVal)
    return

#Function to display error message
def lostMessage(message,maxGuessVal):
    print "Sorry, You have reached maximum ("+str(maxGuessVal)+") guesses. You lost the game"
    print "Correct number was :"+str(message)
    closeInput = raw_input("Press ENTER to exit")
    print "Closing..."
    return

# Function to get Input from User
def getInput():
    getUserInput = input("Enter "+str(numberLength)+" digits number :")
    userInputArray = list(getUserInput)
    getCount = len(userInputArray)

    if getCount < numberLength or getCount > numberLength: # Check length of user input
        print str(numberLength)+" digits number please !"
        getInput()
        return
    else:
        getRepeated = isRepeated(userInputArray,getCount) # Check for repeated numbers in user input
        return
        
# Get User input first time
invalidInput = getInput();
