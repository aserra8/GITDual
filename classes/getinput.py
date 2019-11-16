def int_input_between(min_value, max_value):
    while True:
        try:
            user_input = int(input("\nEnter your choice: "))
            if min_value <= user_input <= max_value:
                break
            else:
                print("\nOption is not valid")
        except ValueError:
            print("\nIncorrect format")

    return user_input


def string_input_between(name, min_length, max_length,):
    while True:
        user_input = input("\nEnter {}: ".format(name.lower()))
        if len(user_input) < min_length:
            print("\n{} is too short".format(name))
        elif len(user_input) > max_length:
            print("\n{} is too long".format(name))
        else:
            break

    return user_input
