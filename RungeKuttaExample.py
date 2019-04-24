###From Section 9.2, Problem 14

import ast
import math
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint

print('Hi there!... I am about to solve problem 14 in Section 9.2')
time.sleep(2)
print('Gathering Problem Information...')
time.sleep(2)
print('Got it! Now computing the problem using RK4...')
time.sleep(3)

def Generic_Runge_Kutta(differential, parameter):
    x0 = float(parameter[0])
    y0 = float(parameter[1])
    x = float(parameter[2])
    step_height = float(parameter[3])
    iterations = int((x - x0) / step_height)
    y = y0
    for i in range(iterations):
        k1 = differential(x0, y)
        k2 = differential(x0 + (0.5 * step_height), y + (0.5 * step_height * k1))
        k3 = differential(x0 + (0.5 * step_height), y + (0.5 * step_height * k2))
        k4 = differential(x0 + step_height, y + (step_height * k3))
        y += ((step_height / 6) * (k1 + (2 * k2) + (2 * k3) + k4))
    return y

def problem_14(formula, parameters):
    differential = lambda x, y: eval(formula)
    ans = Generic_Runge_Kutta(differential, parameters)
    return ans

###FORMAT TO PUT IN [0,0.24,1,0.5]
###FORMULA FORMAT (y * (2.128 - (0.04432 * y)))

times = ['1', '2', '3', '4', '5']
observed = [2.78, 13.53, 36.30, 47.50, 49.40]
formula = "(y*(2.128-(0.04432*y)))"
allsteps = [[0,0.24,1,0.5], [0,0.24,2,0.5], [0,0.24,3,0.5], [0,0.24,4,0.5], [0,0.24,5,0.5]]
RK4_answer = []
for day in range(len(allsteps)):
    solved = problem_14(formula, allsteps[day])
    RK4_answer.append(solved)

RK4_y = RK4_answer

print('The RK4 answers have been computed! It is now time to solve this problem using separation of variables!')
time.sleep(3)
print('The work for the separartion of variables will be commented in this code')
time.sleep(2)
print('I will now compute the problem using the formula from separation of variables')
time.sleep(3)

###Separation of Variables Work!
'''

'''

SeparationFormula = lambda t: (((49.2593)*math.exp((2.128*t)-(5.31931))) / (1+math.exp((2.128*t)-(5.31931))))
SepAnswers = []
for day in range(len(times)):
    solved = SeparationFormula(int(times[day]))
    SepAnswers.append(solved)

Sep_Y = SepAnswers

print('Almost there.. hold your horses!')
time.sleep(2)
print('Done!')
time.sleep(1)
print('I will now display all of the data on a graph and table')
time.sleep(3)


def Graph_Answers(times, Observed, RK4y, SepY):
    times = [int(times[i]) for i in range(len(times))]
    times = np.array(times*3)
    area = np.array(Observed + RK4y + SepY)
    type = np.array(['Observed']*5 + ['Runge_Kutta']*5 + ['Separation']*5)
    data = {'Times': times, 'Area':area, 'type': type}
    df = pd.DataFrame(data=data, index=times)
    pprint(df)
    ax = sns.stripplot(x='Times', y='Area', hue='type', jitter=0, data=data)
    ax.set(xlabel ='t (days)', ylabel ='A (area)')
    plt.title('RK4 Estimation')
    plt.show()

print('This is the RK4 approximation for area: ', '\n')
time.sleep(2)
print(Graph_Answers(times, observed, RK4_y, Sep_Y))

time.sleep(2)
print('I hope you enjoy this program! Cheers!')
time.sleep(2)
