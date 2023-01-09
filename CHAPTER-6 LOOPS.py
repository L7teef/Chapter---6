##1.                   Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#                                                      print a message saying you’ll add that topping to their pizza.

#ANSWER :

# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print("  I'll add " + topping + " to your pizza.")
#     else:
#         break

##2.A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
# they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
# age, and then tell them the cost of their movie ticket

#ANSWER :

# age = int(input("Enter youer age: "))
# if age < 4:
#     print("Your TICKET cost $0")
# elif age < 18:
#     print("Your TICKET costs $25")
# else:
#     print("Your TICKET cost $40")

##3.Write a loop that never ends, and run 

#ANSWER :

# while True:
#     age = input("How old are you? ")
    
#     age = int(age)
#     if age < 3:
#         print("Your ticket is free")
#     elif age < 12:
#         print("Your ticket is $10") 
#     else:
#         print("Your ticket is $15")


##4.Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
# move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

#ANSWER :

# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I'm working on your " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print("I made a " + sandwich + " sandwich.")


##5.Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
# occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

#ANSWER :

# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []

# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print("\n")
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I'm working on your " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print("I made a " + sandwich + " sandwich.")

