def jokeMachine():
    jokeNum = int(input("Enter a number between 1-10 to hear a joke, press ENTER to reveal the punchline: "))
    jokes = 1
    # jokes = 1 sets the variable at 1 which then counts how many times the user enters a number in, allowing the loop to break after the set number
    # incorporated while loops below to allow program to still run if a number outside of 1-10 is entered
    while jokeNum > 10:
        print("...I said between 1-10!")
        jokeNum = int(input("Try again: "))
    while jokeNum <= 0:
        print("...I said between 1-10!")
        jokeNum = int(input("Try again: "))
    while jokeNum > 0 and jokeNum <= 10:
        # both conditions must be met in order for the joke machine to allow you to enter a number
        if jokeNum == 1:
            print("Why do we tell actors to 'break a leg'?")
            # input() ensures the user has to press ENTER in order to get the next line of code rather than the whole joke printing at once
            input()
            print("...because every play has a cast!")
        elif jokeNum == 2:
            print("Where are average things manufactured?")
            input()
            print("...in the satis-factory!")
        elif jokeNum == 3:
            print("What does a nosy pepper do?")
            input()
            print("...gets jalapeño business!")
        elif jokeNum == 4:
            print("Why don't mathmaticians throw parties?")
            input()
            print("...because you shouldn't drink and derive.")
        elif jokeNum == 5:
            print("What do you call a parade of rabbits hopping backwards?")
            input()
            print("...a receding hare-line.")
        elif jokeNum == 6:
            print("What do you call a fake noodle?")
            input()
            print("...an impasta!")
        elif jokeNum == 7:
            print("How do you make a tissue dance?")
            input()
            print("...put a little boogie in it.")
        elif jokeNum == 8:
            print("What do you call a magic dog?")
            input()
            print("...a labra-cadabra-dor!")
        elif jokeNum == 9:
            print("What did the shark say when he ate the clownfish?")
            input()
            print("...this tastes a little funny.")
        elif jokeNum == 10:
            print("Why can't you hear a pterodactyl go to the bathroom?")
            input()
            print("...because the 'P' is silent!")
        input()
        jokeNum = int(input("Please enter a different number between 1-10 for another joke: "))
        # this message shows after the user receives a joke, if the user then enters a number outside of 1-10, the while loops below will allow user to re-enter 
        # if a number between 1-10 is entered, another joke will be displayed until 10 jokes have been displayed - the loop will then break (as shown below)
        while jokeNum > 10:
            print("...I said between 1-10!")
            jokeNum = int(input("Try again: "))
        while jokeNum <= 0:
            print("...I said between 1-10!")
            jokeNum = int(input("Try again: "))
        jokes = jokes + 1
        if jokes == 11:
            print("That's enough jokes for now!")
            break
jokeMachine()