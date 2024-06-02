# Author:       R4V3N
# Date:         2024-06-02
# Description:  A python app that will help organize cards for a Magic The Gathering deck.
#               Letting the usert know if there are doubles in the deck (if commander deck).

# Check if there are decks already made on system
# if yes then load the decks
# if no create JSON file to store the decks

print(f'\n1. Create new Deck\n2. List Decks\n3. Change cards in deck\n4. Print deck\nQ - Quit\n')
user_input = input('Input> ')

if user_input == '1':
    pass # List all the decks. (Deck name, commander (if applicable), [cards], notes)
elif user_input == '2':
    pass # Create a new deck. (Create a object to take and store the data for the deck)
elif user_input == '3':
    pass # Take the name of the deck that the user would like to edit. Then the card name to take out and the card name to replace it.
    # If the user just types the deck name then it will remove the deck.
elif user_input == '4':
    pass # Print the selected name of the deck. Or the user can enter ALL which will print all the decks in the JSON file.
elif user_input.lower() == 'q':
    # Quit the program
    # call the save deck function
    print('All decks have been saved!\n')
    exit()
else:
    print('Please choose an option above.')