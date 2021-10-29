'''
Game objective: You will be asked a series of animal questions.
At the end you will see your results.
Start by building out layout:
1. new game, 2. check answer, 3.display score, 4. play again.
Create dictionary to hold the questions with the correct answer key value.
'''

print("Welcome to the animal quiz!")

playing = input("Do you wish to test your animal knowledge? (yes or no)")

if playing != "yes":
    quit()


def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print(key)
        for answer_choices in options[question_number - 1]:
            print(answer_choices)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()    # Returns characters in uppercase, symbols and numbers are ignored.
        guesses.append(guess)    # We are adding their guess to the list of guesses

        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("Sorry, that is INCORRECT!")
        return 0


def display_score(correct_guesses, guesses):
    print("--------------------")
    print("Results: ")

    print("Correct answers: ", end="")    # we want all the answers to display next to each other and not in a new line
    for value in questions:
        print(questions.get(value), end="")
    print()

    print("Your answers: ", end="")
    for player_input in guesses:
        print(player_input, end="")
    print()

    score = ((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


# create a collection or dictionary to hold the questions and a list with answer choices.


questions = {
    "What shark makes an appearance in the movie Jaws? ": "C",
    "What is the smartest animal in the ocean? ": "A",
    "What animal is man's best friend? ": "A",
    "What animal goes 'oink, oink'? ": 'D',
    "What snake has the deadliest venom? ": "B",
}

options = [["A. Whale Shark", "B. Blue Shark", "C. Great White Shark", "D. HammerHead Shark"],
           ["A. Dolphin", "B. Starfish", "C. Goldfish", "D. SeaHorse"],
           ["A. Dog", "B. Cat", "C. Python", "D. Parrot"],
           ["A. Cow", "B. Hog", "C. Sheep", "D. Pig"],
           ["A. Black Mamba", "B. Inland Taipan", "C. Rattlesnake", "D. RatSnake"]]

# call your function here to start the game and call the loop:

new_game()

while play_again():
    new_game()

print("Fare Thee Well!")
