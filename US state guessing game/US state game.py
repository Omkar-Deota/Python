import turtle
import pandas
obj=turtle.Screen()
obj.setup(750,510)
obj.title("U.S. State Game")
obj.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer = obj.textinput(f"{len(guessed_state)}/50 states", "HERE||").title()
    if answer=="Exit":
       missing_state=[]
       for state in all_states:
           if state not in guessed_state:
               missing_state.append(state)
       new_data = pandas.DataFrame(missing_state)
       new_data.to_csv("learn it.csv")
       break
       exit(0)
    if answer in all_states:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        ans_data = data[data.state == answer]
        t.goto(int(ans_data.x), int(ans_data.y))
        t.write(answer)

obj.exitonclick()
