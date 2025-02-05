def TavernInn(): #define the function
    print(f"Welcome traveler. You seem to be tired after your long journey.") #prints welcome message
    rooms = input("How many rooms would you like?") #gets user input
    if rooms <= 1: #if statement if room input less than or equal to 1
        print(f"You're in luck. We have {rooms} room available.") #outputs message
    elif rooms > 1: #if statement if room input greater than 1
        print(f"You're in luck. We have {rooms} rooms available.") #outputs message
    print(f"Enjoy your stay traveler!") #prints closing message

TavernInn() #call the function