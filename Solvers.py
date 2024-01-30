import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint


s = 1500.0
e = 1.0
i = 1.0
r = 0.0
beta = 0.0005
gamma = 0.1
exposure = 0.2
birth_rate = 0
death_rate = 0
time = 60.0
deltat = 0.0001
sValues = [s]
iValues = [i]
rValues = [r]
tValues = [0.0]

def eulerMethod(x):
    methodHasRan = False
    while tValues[-1] < time:
        if x == 'sir':

            sValues.append(sValues[-1] - deltat * beta * sValues[-1] * iValues[-1])
            iValues.append(iValues[-1] + deltat * beta * sValues[-2] * iValues[-1] - deltat * gamma * iValues[-1])
            rValues.append(rValues[-1] + deltat * gamma * iValues[-2])
            tValues.append(tValues[-1] + deltat)
            methodHasRan = True

        else:
            tValues.append(60)
            print("No Such equation Exists")

    createGraph(methodHasRan)

def rungeKuttaMethod(x):
    methodHasRan = False
    while tValues[-1] < 60:

        if x == 'sir':

            s0 = deltat * -beta * sValues[-1] * iValues[-1]
            i0 = deltat * (beta * sValues[-1] * iValues[-1] - (gamma * iValues[-1]))

            s1 = deltat * (-beta * (sValues[-1] + 0.5 * s0) * (iValues[-1] + 0.5 * i0))
            i1 = deltat * (
                        (beta * (sValues[-1] + 0.5 * s0) * (iValues[-1] + 0.5 * i0)) - (gamma * iValues[-1] + 0.5 * i0))

            s2 = deltat * (-beta * (sValues[-1] + 0.5 * s1) * (iValues[-1] + 0.5 * i1))
            i2 = deltat * (
                        (beta * (sValues[-1] + 0.5 * s1) * (iValues[-1] + 0.5 * i1)) - (gamma * iValues[-1] + 0.5 * i1))

            s3 = deltat * (-beta * (sValues[-1] * s2) * (iValues[-1] * i2))
            i3 = deltat * ((beta * (sValues[-1] * s2) * (iValues[-1] * i2)) - (gamma * iValues[-1] * i2))

            sValues.append(sValues[-1] + ((s0 + 2 * s1 + 2 * s2 + s3) / 6))
            iValues.append(iValues[-1] + ((i0 + 2 * i1 + 2 * i2 + i3) / 6))

            rValues.append(1501 - sValues[-1] - iValues[-1])
            tValues.append(tValues[-1] + deltat)

            methodHasRan = True
        else:
            tValues.append(60)
            print("No Such equation Exists")

    createGraph(methodHasRan)

def createGraph(methodHasRan):
    if (methodHasRan):
        fig = plt.subplot()
        plt.plot(tValues, sValues, label="Susceptible")
        plt.plot(tValues, iValues, label="Infected")
        plt.plot(tValues, rValues, label="Recovered")
        plt.legend()
        plt.show()


def SIR(Values, t):
    #if birth set to value
    #else birth set to 0

    return [-beta * Values[0] * Values[1] + birth_rate * (Values[0] + Values[1] + Values[0]),
            beta * Values[0] * Values[1] - gamma * Values[1] - birth_rate * Values[1],
            (1 - death_rate) * (gamma * Values[1]) - birth_rate * Values[2],
            death_rate * (gamma * Values[1])]

def SIS(Values, t):

    return [-beta * Values[0] * Values[1] + (1 - death_rate) * (gamma * Values[1]) + birth_rate * (Values[0] + Values[1] + Values[0]),
            beta * Values[0] * Values[1] - gamma * Values[1] - birth_rate * Values[1],
            death_rate * (gamma * Values[1])]

def SEIR(Values, t):

    return [-beta * Values[0] * Values[2] + birth_rate * (Values[0] + Values[1] + Values[0]),
            beta * Values[0] * Values[2] - exposure * Values[1] - birth_rate * Values[1],
            exposure * Values[1] - gamma * Values[2] - birth_rate * Values[2],
            (1 - death_rate) * (gamma * Values[2]) - birth_rate * Values[3],
            death_rate * (gamma * Values[2])]

def solver(chart_type, parameters):
    ts = np.arange(0, 60, 0.01)
    global beta
    global gamma
    global exposure
    global birth_rate
    global death_rate

    # either 0 if not selected or slider value if selected
    birth_rate = parameters["births"]
    death_rate = parameters["deaths_from_disease"]
    d = 0
    s = parameters["susceptible"]
    i = parameters["infected"]
    beta = parameters["beta"]
    gamma = parameters["gamma"]

    if chart_type == "SIR":

        r = parameters["recovered"]

        Us = odeint(SIR, [s, i, r, d], ts)

        S, I, R, D = Us[:, 0], Us[:, 1], Us[:, 2], Us[:, 3]

        return [S,I,R,D,ts]

    if chart_type == "SIS":

        Us = odeint(SIS, [s, i, d], ts)

        S, I, D = Us[:, 0], Us[:, 1], Us[:, 2]

        return [S,I,D,ts]

    if chart_type == "SEIR":

        e = parameters["exposed"]
        r = parameters["recovered"]
        exposure = parameters["exposure"]

        Us = odeint(SEIR, [s, e, i, r, d], ts)

        S, E, I, R, D = Us[:, 0], Us[:, 1], Us[:, 2], Us[:, 3], Us[:, 4]

        return [S,E,I,R,D,ts]






