# COGS 18 FINAL PROJECT: AMERICAN CAPITALS GAME QUIZ

# The following project is a user interactive game, in which the user guesses the capitals of the US states.
# The game consists of ten questions, and in order to win, the user needs to answer at least seven of the ten questions correctly.
# The user has the option to quit anytime during the game, and after each round, the score of the user is shown.
# The user can only miss up to two questions, or else the game ends early and presents the statistics.
# Below are the functions used to create this game

import string
import random

AFFIRMATIVE_RESPONSES = ['yes', 'yea', 'of course', 'yuh', 'yup', 'okay', 'sure', 'ok']
NEGATIVE_RESPONSES = ['no', 'nah', 'no thank you', 'nope', 'naw', 'not really']
prev_states = []

state_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne' }
states = list(state_capitals.keys())


def clean_word(input_string):
    """
    Cleans the word in that it gets rid of the punctuation
    and makes all the characters lowercase to be able to compare words
    Parameters
    ---------
    input_string : string
        The string that needs cleaning
    Returns
    ---------
    out_string : string
        A cleaned out version of the input string
    """
    out_string = ""
    for ind in input_string:
        if ind not in string.punctuation:
            out_string = out_string + ind
    return out_string.lower()


def generate_state():
    """
    Generates a randomized new U.S state to present to the user, not allowing
    repeats to occur
    Parameters
    ---------
    Input: None
    ---------
    Output : string
        An output string with a randomized state
    """
    state = states[random.randint(0, len(states)-1)]
    while (state in prev_states):
        state = states[random.randint(0, len(states)-1)]
    prev_states.append(state)
    return state


def generate_capital(state):
    """
    Based on the state that was provided, return the respective capital,
    all in lowercase
    Parameters
    ---------
    Input : state
        The state is the argument inputted
    Returns
    ---------
    out_string : capital
        An output string of the capital corresponding to the state
    """
    capital = state_capitals[state].lower()
    return capital


def play_game():
    """Main function to play Geography game.
    Parameters
    ---------
    Input: None
    ---------
    Output: None
    """

    num_wrong = 0;
    question_num = 1;
    num_right = 0;

    print("""Hey you! Let's see how well you know your American capitals! I
    will give you ten states and you need to get at least seven of their
    capitals correct in order to win!? You ready to play?""")
    print()

    no_legit_response = True

    while (no_legit_response):
        msg = input('YOU: ')
        msg = clean_word(msg)
        if (msg in AFFIRMATIVE_RESPONSES):
            print("That's what I like to hear! Alright, let's begin! If you want to quit at anytime, type 'quit'")
            print()
            no_legit_response = False
        elif (msg in NEGATIVE_RESPONSES):
            print("Okay, have a nice day!")
            return
        else:
            print("What did you say? I need either a yes or a no please")

    game = True;
    while game:
        # generating the state and respective capital
        state = generate_state()
        capital = generate_capital(state)

        print("Question " + str(question_num) + ": What is the capital of "
        + state + "?")

        answer = input('ANSWER: ')
        answer = clean_word(answer)

        # if user decides to quit
        if (answer == 'quit'):
            print("Done already? Well thanks for playing!")
            print("You finished with " + str(num_right) + " question(s) right and " + str(num_wrong) + " question(s) wrong!")
            game = False
            return

        #if user gets the right or wrong answer
        if (answer == capital):
            print("Good job! You got that right!")
            num_right += 1;
            question_num += 1;
        else:
            print("Nope, that is wrong. The correct capital is " + state_capitals[state])
            num_wrong += 1;
            question_num += 1;

        #checks to see if we continue the game or not
        if (num_wrong < 3 and question_num <= 10):
            print()
            print("You have gotten " + str(num_right) + " question(s) right and " + str(num_wrong) + " question(s) wrong!")
        elif (num_wrong == 3):
            game = False
            print()
            print("Oh no, you missed three questions! You finished with " + str(num_right) + " question(s) right and " + str(num_wrong) + " question(s) wrong!")
            print("Thanks for playing!")
        else:
            game = False
            print()
            print("And those are all the questions I have! You finished with " + str(num_right) + " question(s) right and " + str(num_wrong) + " question(s) wrong!")
            print("Thanks for playing!")

        print()
