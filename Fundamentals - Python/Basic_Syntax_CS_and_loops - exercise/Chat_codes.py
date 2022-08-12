number_of_messages = int(input())
for message in range(1, number_of_messages + 1):
    current_message = int(input())
    if current_message == 88:
        print("Hello")
    elif current_message == 86:
        print("How are you?")
    elif current_message > 88:
        print("Bye.")
    elif current_message != 88 and current_message != 86 and current_message < 88:
        print("GREAT!")
