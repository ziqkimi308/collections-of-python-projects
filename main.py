# Import
import turtle
import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

# CONSTANT
US_STATES_CSV = "./50_states.csv"
BLANK_US_STATES_IMG = "./blank_states_img.gif"

# Setup screen
# call Screen class
screen = turtle.Screen()
screen.title("U.S State Game")
image = BLANK_US_STATES_IMG
screen.addshape(image)
turtle.shape(image)

# Open csv
data = pandas.read_csv(US_STATES_CSV)

# Convert state column to list
data_state = data["state"].to_list()

guessed_state = []
while len(guessed_state) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_state)}/50 Guess the state", prompt="What's another state's name?").title()

    # Break loop with secret code
    if user_answer == "Exit":
        # missing_states = []
        # for state in data_state:
        #     if state not in guessed_state:
        #         missing_states.append(state)

        # Updated shorter using list comprehension
        missing_states = [state for state in data_state if state not in guessed_state]

        # Convert list to dataframe to csv
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("remaining_states.csv")
        break

    # Check answer
    if user_answer in data_state:
        guessed_state.append(user_answer)
        # Call Turtle class
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Specify row that contain answer
        answer_row = data[data.state == user_answer]
        # Goto that row's x and y coordinate and write the state name using .item()
        t.goto(int(answer_row.x), int(answer_row.y))
        t.write(answer_row.state.item())
