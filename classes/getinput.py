def getinput_between(min_value, max_value):
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if min_value <= choice <= max_value:
                break
            else:
                print("\nOption is not valid")
        except ValueError:
            print("\nIncorrect format")

    return choice
