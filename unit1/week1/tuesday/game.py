# guessing game

# what does it do?
    # plays a guessing game with the user
    # would it be useful to have the program print out the rules at the beginning
    # How does the user communicate witht the program that it didn't guess wirh the right number?
        # too high, too low, or equal
        # after the program makes a guess, it will wait on user input from the command line
        # if the player says the number is too low, the program knows it needs to guess higher
        # if the player says the number is too high, the program knows it needs to guess lower
        # how does the program generate a guess?
    # How does the game actually run
        # loops until it exits
            # either when the user terminates it or when the program has successfully guessed the number
    # In the loop
        # Game generates a guess between 1 and 100
        # prints out the guess to the user
        # wit for users input for high, low, or equal
        # read users input
        # act according to the users input
# what are the rules?
    # the user will think of a number, the program has to guess it
    # is there a range of possible numbers? or can allow any number?
        # range is between 1 and 100

# RULES
print('\n RULES: \n Think of a number between 1 and 100, and I will try to guess it')
print('Once I guess, \n type \'high\' if im too high, \ntype \'low\' if im too low, \n type \'equal\' if i guessed it')

# if uinput == 'high':
#     # guess again
# elif uinput == 'low':
#     # guess again
# else:
#     print('I guessed your number correctly!') 

# vairables to store the floor and ceiling
floor = 1
ceiling = 100


got_it = False

while not got_it:
    guess = (floor + ceiling) // 2

    print(f"I'm guessing {guess}")
    result = input('Was I right? tell me if im high, low, or equal: ')
    result = result.lower()
    result = result[0]
    if result == 'h':
        ceiling = guess -1
    elif result == 'l':
        floor = guess + 1
    elif result == 'e':
        print('I guessed your number correctly!')
        got_it = True
    else:
        print('I dont know what that means, plese try again')