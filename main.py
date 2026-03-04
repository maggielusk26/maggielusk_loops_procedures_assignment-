"""
Assignment:
  Loops, Events, and Procedures

Instructions:
  Review the details below and complete the 5 steps. Be sure to commit and sync your
  code often so that you do not lose your work. Be sure to test your code using
  python main.py

Items to discuss in this lesson:

  - Previous Assignment:
    - Variables
      - Identifier
      - Value
      - Assignment Operator
    - Conditional Statements
      - if..then
    - Data Types (a few of them)
      - String
      - Number
      - Boolean
      - List (Array)

  - This Assignment:
    - Built-In Functions (e.g. print, len, input) - think of Tools - f string
    - Loops: allow you to easily repeat a chunk of code many times
    - Functions (Procedures): a piece of code you can easily use over and over
        - parameters
        - return value

Steps
  1. Create a list variable to store the books the member has checked out
  2. Use a for loop to print out each of the books from the variable in step 1
  3. Use for loops to iterate the list created in step 1
  4. Create a function to check the library rules
  5. Use a WHILE loop to keep checking until the user is ready to checkout


Expected Output:
    iterate books using for loop
    The Hobbit
    The Lord of the Rings
    The Hunger Games
    iterate books using for..range
    The Hobbit
    The Lord of the Rings
    The Hunger Games
    You can check out more books.
    Are you ready to checkout your books? Enter a y if so: y
    You are checked out, have a great day
"""

# add check library rules function here
# def your_function():


def main():
    print("=" * 75)

    # variables used in prior assignment
    member_name = "John Smith"
    #books_checked_out = 3
    account_is_active = True

    # ------------------------------------------------------------
    # STEP 1:
    #   Use a List data type to store the books the member has checked out
    # ------------------------------------------------------------

    # create a List variable to store the books
    # HINT: []

    books_checked_out= ["The Hunger Games", "Powerless", "Red Queen", "The Maze Runner"]


    # ------------------------------------------------------------
    # STEP 2:
    #   Use a for loop to print out each of the books from the variable in step 1
    # ------------------------------------------------------------

    # create a for loop and print out each book
    # for item in list

    for book in books_checked_out:
        print(book)  

    # ------------------------------------------------------------
    # STEP 3:
    #   Update the books_checked_out variable to use len() function
    #   to set the variable value to match the len of the variable in step 1
    #   and then write a for loop that uses a range to print out each book
    # ------------------------------------------------------------

    # store the books that are checked out (number)
    len_of_name= len(member_name) 
    print("Length of Name:", len_of_name)

    number_of_books = len(books_checked_out)
    print("Number of Books:", number_of_books)

    range_of_books = range(number_of_books)
    print("Range:", range_of_books)
    # iterate the books using range
    # for i in range
    for i in range(number_of_books):
      print(f"Index:{i}, Book: {books_checked_out[i]}, cool book")
    if i == 1:
         print("That book is the best")

    if book == "Powerless":
        print("That book is the best")

    for i in range_of_books:
        pass 


    # after adding the loops, comment out or remove these print statements
    print("Member Name:", member_name)
    print("Books Checked Out:", books_checked_out)
    print("Account Active:", account_is_active)

    # ------------------------------------------------------------
    # STEP 4:
    #   Create a Function that checks the library rules. It should have
    #   two parameters:
    #     1. account_is_active (bool)
    #     2. books_checked_out (int)
    #   It should return a variable called message that is a string
    # ------------------------------------------------------------

    # call your function here
    def check_library_rules(account_is_active: bool, books_checked_out: int):
        if not account_is_active :
          return ("You need an account to check out books")
        elif books_checked_out == 5:
          return ("You can only check out 5 books.")
        else: 
          return ("You can check out more books. ")
    
    message= check_library_rules(account_is_active, number_of_books)
    print("Rules:", message)






    # conditional statement to check the library rules - remove this code
    # after you have added a function to replace it
    #if not account_is_active:
    #print("You must have an active account in order to check out any books.")
    #elif books_checked_out >= 5:
    #print("You cannot check out anymore books, 5 is the limit.")
    #else:
     #   print("You can check out more books.")

    # ------------------------------------------------------------
    # STEP 5:
    #   Use a WHILE loop with the input function to ask the user
    #   if they are ready to check out and print the message
    #   HINT: us the input() function to ask the user and then
    #   check if they entered a value such as y
    # ------------------------------------------------------------

    # add WHILE LOOP here

    ready_to_checkout=False
    
    while not ready_to_checkout:
       user_input= input("Are you ready to checkout? Enter a y if so:")
       if user_input == "y":
          ready_to_checkout=True  #exit from while loop
       else: 
          print("Ok, let us know when you are ready")

    print("Have a great day!")
    

    print("=" * 75)


if __name__ == "__main__":
    main()
