import datetime

print("===================================")
print("      SIMPLE PYTHON CHATBOT")
print("===================================")
print("Type 'bye' to stop the chatbot.\n")

while True:

    # Take user input
    user_input = input("You: ")

    # Convert to lowercase
    user_input = user_input.lower().strip()

    # Remove question marks
    user_input = user_input.replace("?", "")

    # Greeting messages
    if user_input in ["hi", "hello", "hii", "hey"]:

        print("Bot: Hello! Nice to meet you.")

    # Asking chatbot health
    elif user_input in ["how are you", "how are u"]:

        print("Bot: I am fine. How are you?")

    # User replies
    elif user_input in ["good", "fine", "i am good", "i am fine"]:

        print("Bot: Nice to hear that!")

    # Asking chatbot name
    elif user_input in ["what is your name", "your name"]:

        print("Bot: My name is Python Chatbot.")

    # Asking about creator
    elif user_input in ["who created you", "who made you"]:

        print("Bot: I was created using Python programming.")

    # Asking time
    elif user_input == "time":

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print("Bot: Current time is", current_time)

    # Asking date
    elif user_input == "date":

        current_date = datetime.datetime.now().strftime("%d-%m-%Y")

        print("Bot: Today's date is", current_date)

    # Help command
    elif user_input == "help":

        print("Bot: You can ask me:")
        print("- hi")
        print("- how are you")
        print("- your name")
        print("- time")
        print("- date")
        print("- bye")

    # Thank you message
    elif user_input in ["thanks", "thank you"]:

        print("Bot: You are welcome!")

    # Bye message
    elif user_input == "bye":

        print("Bot: Bye! Have a nice day.")
        break

    # Unknown messages
    else:

        print("Bot: Sorry, I don't understand that.")