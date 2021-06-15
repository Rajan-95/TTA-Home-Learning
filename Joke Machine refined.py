import random

jokeList = [
    "Why do we tell actors to 'break a leg'?",
    "Where are average things manufactured?",
    "What does a nosy pepper do?",
    "Why don't mathematicians throw parties?",
    "What do you call a parade of rabbits hopping backwards?",
    "What do you call a fake noodle?",
    "How do you make a tissue dance?",
    "What do you call a magic dog?",
    "What did the shark say when he ate the clownfish?",
    "Why can't you hear a pterodactyl go to the bathroom?"
]

ansList = [
    "...because every play has a cast!",
    "...in the satis-factory!",
    "...gets jalapeño business!",
    "...because you shouldn't drink and derive.",
    "...a receding hare-line.",
    "...an impasta!",
    "...put a little boogie in it.",
    "...a labra-cadabra-dor!",
    "...this tastes a little funny.",
    "...because the 'P' is silent!"
]


def joke_machine(jokeIndex):
    print(jokeList[jokeIndex])
    input()
    print(ansList[jokeIndex])
    jokeList.pop(jokeIndex)
    ansList.pop(jokeIndex)
# joke_game_1 works well for random generation (randint) of numbers 1-10 leading to a new joke each time.
def joke_game_1():
    print("This machine will randomly generate 10 jokes from a list of 10!")
    input("Press ENTER to continue")
    randomJokeIndex = random.randint(0,len(jokeList)-1)
    while len(jokeList) > 0:
        joke_machine(randomJokeIndex)
        input()
        if len(jokeList) > 0:
            randomJokeIndex = random.randint(0,len(jokeList)-1)
    print("That's enough jokes for now!")
        

# joke_game_2 works well with user manually entering number 1-10
# which displays joke corresponding to user's number 
# the displayed joke cannot be duplicated even if user enters the same number twice
def joke_game_2():
    joke_index = int(input("Please enter a number between 1-10 to hear a joke: "))-1
    jokes_told_index_list = []
    while joke_index > -1 and joke_index < len(jokeList)-1:
        joke = jokeList[joke_index]
        answer = ansList[joke_index]
        print(joke)
        input()
        print(answer)
        jokes_told_index_list.append(joke_index)
        joke_index = int(input("Please enter a number between 1-10 to hear a joke: "))-1
        while joke_index in jokes_told_index_list:
            joke_index = int(input("Duplicate joke, pick another number: "))-1


#joke_game_1()

joke_game_2()











