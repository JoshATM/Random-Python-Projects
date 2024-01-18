from datetime import datetime
import os
import random
import sys
import time

def simple_ai(user_input):                                                               # Defines the simple_ai function
    if "pick" in user_input and "random" in user_input and "number" in user_input:          # Picks a random number between 1-100
        return "A random number between 1-100 is " + str(random.randint(0, 100))         # Returns the random number
    #elif "another" in user_input or "again" in user_input or "different" in user_input:       # Only returns a random number if the user asks for another one
    #    return "Another random number between 1-100 is " + str(random.randint(0, 100))
    elif "time" in user_input:                                                             # Returns the current time
        return "Current time is " + str(datetime.now())
    else:                                                                                  # If the user doesn't ask for a random number or the time, it will return this
        return "I'm sorry, I didn't understand that."

while True:                                                                               # Loops the program
    user_input = input("Your Question: ")                                                # Asks the user for input
    response = simple_ai(user_input.lower())                                           # Converts the user input to lowercase and runs it through the simple_ai function
    print("AI: " + response)                                                          # Prints the response
