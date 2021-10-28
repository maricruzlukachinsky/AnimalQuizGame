'''
Game objective: You will be asked a series of animal questions.
At the end you will see your results.
'''


def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print(key)
        for question in options[question_number - 1]:
            print(question)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

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

    print("Correct answers: ", end="")
    for value in questions:
        print(questions.get(value), end="")
    print()

    print("Your answers: ", end="")
    for player_input in guesses:
        print(player_input, end="")
    print()

    score = ((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


# create a collection or dictionary to hold the questions and answers.


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