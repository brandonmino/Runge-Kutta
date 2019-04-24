###Runge-Kutta Method
import ast
import time
import numpy as np

question_one = input('Are you trying to solve a differential equation using Runge Kutta? y/n ')

check = False

if question_one == 'y':
    check = True
    parameters = ast.literal_eval(input('Excellent! Please enter your values in the following order in a comma seperated list: [x0, y0, x, step_height] ' '\n'))
    formula = input('Thanks! Now input your differential equation (must be in terms of "y") ' '\n')
    print('All set! Now let me calculate that!')
    time.sleep(3)
    print('...doing the math...')
    time.sleep(3)
    print('...almost there...')
    time.sleep(3)
    differential = lambda x, y: eval(formula)
    def Generic_Runge_Kutta():
        x0 = float(parameters[0])
        y0 = float(parameters[1])
        x = float(parameters[2])
        step_height = float(parameters[3])
        iterations = int((x - x0) / step_height)
        y = y0
        for i in range(iterations):
            k1 = differential(x0, y)
            k2 = differential(x0 + (0.5 * step_height), y + (0.5 * step_height * k1))
            k3 = differential(x0 + (0.5 * step_height), y + (0.5 * step_height * k2))
            k4 = differential(x0 + step_height, y + (step_height * k3))
            y += ((step_height / 6) * (k1 + (2 * k2) + (2 * k3) + k4))
        print('Got it! Let me display it...')
        time.sleep(3)
        print('\n', y, '\n')
        print('*****   Hope you found this tool helpful! Cheers!   *****')
        print('\n')
    Generic_Runge_Kutta()

if question_one == 'n':
    check = True
    print('Then why are you here... bye!')

if check == False:
    print('You clicked something wrong... try either "y" or "n" again... or go back to sleep ...zzzzzz...')
