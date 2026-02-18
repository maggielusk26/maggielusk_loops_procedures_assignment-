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

def main():
    pass 

    # print()
    print("Hello!") 

    name="Bob"
    print("Hello!;", name)

    # type()
    member_name="Kai"
    total_points=220
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
    
    # range()

    # int() 

    # str()

    # float()

    # bool()

    # list() 


if __name__ == "__main__":
    main()
