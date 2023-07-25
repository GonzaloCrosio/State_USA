import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# To use picture in game:
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()      # data.state is the key that takes you to the name of the state and converts it into a list

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()    # title me reconoce mayúsculas

    # To create a CSV with the names of the states that we failed to guess:
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    # To detect if the written text is equal to the states of the country
    # If it is correct, the Turtle has to write the name of the state at the coordinates X, Y.
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()                                # Turtle creator
        t.hideturtle()                                     # Hide the turtle
        t.penup()                                          # Make the turtle not write
        state_data = data[data.state == answer_state]      # Compare the answer with the name of the state
        t.goto(int(state_data.x), int(state_data.y))       # Location of the turtle. With .x, it retrieves the X or Y coordinate
        t.write(answer_state)                              # To write the name of state

