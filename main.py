import turtle
import pandas
import write

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()
write = write.WriteTheState
correct_guesses = []

while len(correct_guesses) < 50:
    if len(correct_guesses) == 0:
        answer = screen.textinput(title="Guess the State", prompt="What's another State?").title()
    else:
        answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                  prompt="What's another State?").title()
    if answer in correct_guesses:
        print("You already guessed that one.")
    elif answer in states_list:
        correct_guesses.append(answer)
        row = (states[states.state == answer])
        # x = row["x"]
        # y = row["y"]
        # int_x = int(x)
        # int_y = int(y)
        state_data = states[states.state == answer]
        write(answer, int(state_data.x), int(state_data.y))
    elif answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guesses:
                missing_states.append(state)

        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break




