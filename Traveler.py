def Greetings(): #defining the function
    print(f"Welcome traveler, please enter your name to continue on your journey.") #welcome message
    name = input("Enter your name: ")  # get user input
    print(f"Hello {name}. Welcome to the candy shop!")  # prints user input
    grocery =input("Enter the item you are looking to purchase for replenishment:") #get user input
    print(f"You're lucky. Here's the last {grocery}.") #prints user input
    print(f"Safe travels on your journey traveler. Come back soon!") #closing message

Greetings()  # Call the function
