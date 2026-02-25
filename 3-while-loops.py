def main():
    """ 
    A WHILE LOOP will run a chunk of code until a condition is met.

    This is used when you don’t know the exact number of times you want 
    the loop to repeat and it depends on another factor.
    """
    

    #how many continents
    answer = "7"
    is_correct_answer = False

    while not is_correct_answer: 
        #ask the user to make a guess of the answer
        guess=input("How many continents are there?")

        #check if answer is correct
        if int(guess) == int(answer):
            print ("Yay, you got it correct!")
            is_correct_answer = True
        else:
            print("You guessed:", guess)
            print ("Nope, that's not right, try again.")
        

    # guess the correct answer
    # WHILE answer is not correct loop
    # conditional inside while to check the answer


    pass


if __name__ == "__main__":
    main()
