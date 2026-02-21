# What is a Function?
#   A PROCEDURE is a piece of code that you can easily use over and over. 
#   We will refer to this as a FUNCTION in this class
#   A function is a piece of code that has a name and completes a specific task.
#
# Creating Functions
#   We declare a function using the keyword def at the start
#   A function is invoked using parens () 
#   A function can accept parameters
#   A function can have a return value
#
# built in functions (these are like tools available to you)
#   print()
#   type()
#   len()
#   input()
#   range()
#   int(), str(), float(), bool(), list()
#   many more
#
# you can create your own functions
# you can comment functions to help organize and document what they do
# 
# Parts of a Function
#   Declare - def - give it a name and add the code to execute when it is called
#   Parameter (param1, param2) - values passed into a function
#   Return - return "foo" - also known as Output 
#   Call - my_method() - when you want to use the function
#

# TASK 1: Create a new function to give a greeting (aka procedure) 
# Use the def keyword to declare your function and give it a name of say_hi 
# Add a parameter named name for the function
# Declare a variable named greeting and set the value to be your greeting, for example print("Hello there:", name)
# Return the variable greeting 
# Somewhere in the main() function call the new say_hi function you have created and print the result
# Example to use in your main(): print(say_hi("Bob"))
# Commit and Push your work! 

# TASK 2: Create a new function to indicate if you can check out books
# Use the def keyword to declare your function and give it a name of checkout_books
# Add a parameter named has_account
# Add a parameter named number_of_books
# Add a conditional statement inside the function
# The conditional statement should have an if, elif, else
# if not has_account then you should print "You need an account to check out books"
# else if (elif) number_of_books > 5 print "You can only check out 5 books"
# else print "You can check out more books"
# Somewhere in the main() function call the new checkout_books() function
# You don't have to print the result of this function because it already handles print for you
# Commit and Push your work! 

def checkout_books(has_account, number_of_books):
    if not has_account :
     print ("You need an account to check out books")
    elif number_of_books > 5:
        print ("You can only check out 5 books.")
    else: 
        print ("You can check out more books. ")


def say_hi(name): 
     greeting = "What's up? " + name 
     return greeting 


def average_score(total_points, games_played):  
     average_score=total_points / games_played 
     return average_score 
 


def main():
    pass 

    # print()
    print("Hello!") 

    name="Bob"
    print("Hello!;", name)

    # type()
    member_name="Kai"
    total_points=123
    games_played=5
    is_playing_game=True

    print("member_name type:", type(member_name))
    print("total_points type:", type(total_points))
    print("games_played type:" , type(games_played))
    print("is_playing_game type:" , type(is_playing_game))

    # len()
    store_name="Ulta"
    print(len(store_name))

    if len(store_name) < 10:
        print("Hey, you need a longer store name.")
    else: 
        print("Store name looks good.")

    favorite_players=("Larry Bird", "Kobe Bryant", "Michael Jordan") 
    print("favorite_players:", len(favorite_players)) 


    # input()
    age=input("How old are you?")
    print("You entered:", age)
    if int(age) <= 19 and int(age) >= 13:
            print("You ARE a teenager")
    else: 
         print("You are not a teenager")

    your_name=input("Enter your name:")
    #print("Hello!:", your_name)

    # range()

    # int() 

    # str()

    # float()

    # bool()

    # list() 
    print (say_hi(your_name))

    has_account= True  
    number_of_books = 3
    checkout_books(has_account, number_of_books)

if __name__ == "__main__":
    main()
