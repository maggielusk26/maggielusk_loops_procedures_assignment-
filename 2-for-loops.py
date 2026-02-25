def bounce_ball(number_of_bounces):
    for i in range(number_of_bounces): 
        print ("move up")
        print ("fall down")

def main():
    """
    Loop Statements allow you to easily repeat a chunk of code many times.

    Example: in a game with a bouncing ball, it would be too much work to type
    out the code to make the ball bounce up and down a thousand times
    (move up, then fall down, move up then fall down, repeat 1000 times).
    Instead you can put the repeated code in a loop

    Loops not only save programmers time, they also make programs shorter.
    """

    # bounce a ball
    print("move up")
    print("fall down")

    # now repeat this 1000 times 

    # FOR LOOP (range)
    bounce_ball(1000)

    # FOR iterate
    # bounce_actions = []

    bucket = [
        "Catfish"
        "Trout", 
        "Bass",
        "Carp", 
        "Goldfish", 
        "Shark",
        "Swordfish"

    ]

    for fish in bucket:
        print ("Fish:",fish)




if __name__ == "__main__":
    main()
