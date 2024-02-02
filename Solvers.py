import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint


s = 1500.0
e = 1.0
i = 1.0
r = 0.0
beta0 = 0.0005
gamma = 0.1
exposure = 0.2
birth_rate = 0
death_rate = 0
vaccination_rate = 0
reduction_infect = 0
num_in_treat = 0
removal_rate_treat = 0
seasonal_forcing = 0
removal_rate_q = 0
reduction_interaction_q = 0
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

            sValues.append(sValues[-1] - deltat * beta0 * sValues[-1] * iValues[-1])
            iValues.append(iValues[-1] + deltat * beta0 * sValues[-2] * iValues[-1] - deltat * gamma * iValues[-1])
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

            s0 = deltat * -beta0 * sValues[-1] * iValues[-1]
            i0 = deltat * (beta0 * sValues[-1] * iValues[-1] - (gamma * iValues[-1]))

            s1 = deltat * (-beta0 * (sValues[-1] + 0.5 * s0) * (iValues[-1] + 0.5 * i0))
            i1 = deltat * (
                    (beta0 * (sValues[-1] + 0.5 * s0) * (iValues[-1] + 0.5 * i0)) - (gamma * iValues[-1] + 0.5 * i0))

            s2 = deltat * (-beta0 * (sValues[-1] + 0.5 * s1) * (iValues[-1] + 0.5 * i1))
            i2 = deltat * (
                    (beta0 * (sValues[-1] + 0.5 * s1) * (iValues[-1] + 0.5 * i1)) - (gamma * iValues[-1] + 0.5 * i1))

            s3 = deltat * (-beta0 * (sValues[-1] * s2) * (iValues[-1] * i2))
            i3 = deltat * ((beta0 * (sValues[-1] * s2) * (iValues[-1] * i2)) - (gamma * iValues[-1] * i2))

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


def calc_seasonal_forcing(t):

    if seasonal_forcing == 0:
        return beta0
    else:
        return beta0 * (1 + (seasonal_forcing * np.cos(2 * np.pi * (t / 60))))


def sir(values, t):

    beta = calc_seasonal_forcing(t)
    return [-beta * values[0] * (values[1] + reduction_infect * values[5] + reduction_interaction_q * values[6]) + birth_rate * (values[0] + values[1] + values[0]) - vaccination_rate * values[0],
            beta * values[0] * (values[1] + reduction_infect * values[5]) - (gamma + num_in_treat) * values[1] - birth_rate * values[1] - removal_rate_q * values[1],
            (1 - death_rate) * (gamma * values[1]) - birth_rate * values[2] + gamma * values[6],
            death_rate * (gamma * values[1]),
            vaccination_rate * values[0],
            num_in_treat * values[1] - removal_rate_treat * values[5],
            removal_rate_q * values[1] - gamma * values[6]]


def sis(values, t):

    beta = calc_seasonal_forcing(t)
    return [-beta * values[0] * (values[1] + reduction_infect * values[4] + reduction_interaction_q * values[5]) + (1 - death_rate) * (gamma * values[1]) + birth_rate * (values[0] + values[1] + values[0]) - vaccination_rate * values[0],
            beta * values[0] * (values[1] + reduction_infect * values[4]) - (gamma + num_in_treat) * values[1] - birth_rate * values[1] - removal_rate_q * values[1],
            death_rate * (gamma * values[1]),
            vaccination_rate * values[0],
            num_in_treat * values[1] - removal_rate_treat * values[4],
            removal_rate_q * values[1]]


def seir(values, t):

    beta = calc_seasonal_forcing(t)
    return [-beta * values[0] * (values[2] + reduction_infect * values[6] + reduction_interaction_q * values[7]) + birth_rate * (values[0] + values[1] + values[0]) - vaccination_rate * values[0],
            beta * values[0] * values[2] - exposure * values[1] - birth_rate * values[1],
            exposure * values[1] - (gamma + num_in_treat) * values[2] - birth_rate * values[2] - removal_rate_q * values[2],
            (1 - death_rate) * (gamma * values[2]) - birth_rate * values[3],
            death_rate * (gamma * values[2]),
            vaccination_rate * values[0],
            num_in_treat * values[1] - removal_rate_treat * values[6],
            removal_rate_q * values[2]]


def solver(chart_type, parameters):

    ts = np.arange(0, 60, 0.01)

    global beta0
    global gamma
    global exposure
    global birth_rate
    global death_rate
    global vaccination_rate
    global reduction_infect
    global num_in_treat
    global removal_rate_treat
    global seasonal_forcing
    global removal_rate_q
    global reduction_interaction_q

    # either 0 if not selected or slider value if selected
    birth_rate = parameters["births"]
    death_rate = parameters["deaths_from_disease"]
    vaccination_rate = parameters["vaccinated"]
    d = 0
    v = 0
    t = 0
    s = parameters["susceptible"]
    i = parameters["infected"]
    beta0 = parameters["beta"]

    gamma = parameters["gamma"]

    reduction_infect = parameters["reduction infect"]
    num_in_treat = parameters["num in treatment"]
    removal_rate_treat = parameters["removal from treatment"]
    seasonal_forcing = parameters["seasonal forcing"]
    j = parameters["isolated"]
    removal_rate_q = parameters["removal rate q"]
    reduction_interaction_q = parameters["Reduced interaction q"]

    if chart_type == "SIR":

        r = parameters["recovered"]

        Us = odeint(sir, [s, i, r, d, v, t, j], ts)

        S, I, R, D, V, T, J = Us[:, 0], Us[:, 1], Us[:, 2], Us[:, 3], Us[:, 4], Us[:, 5], Us[:, 6]

        return [S, I, R, D, V, T, J, ts]

    if chart_type == "SIS":

        Us = odeint(sis, [s, i, d, v, t, j], ts)

        S, I, D, V, T, J = Us[:, 0], Us[:, 1], Us[:, 2], Us[:, 3], Us[:, 4], Us[:, 5]

        return [S, I, D, V, T, J, ts]

    if chart_type == "SEIR":

        e = parameters["exposed"]
        r = parameters["recovered"]
        exposure = parameters["exposure"]

        Us = odeint(seir, [s, e, i, r, d, v, t, j], ts)

        S, E, I, R, D, V, T, J = Us[:, 0], Us[:, 1], Us[:, 2], Us[:, 3], Us[:, 4], Us[:, 5], Us[:, 6], Us[:, 7]

        return [S, E, I, R, D, V, T, J, ts]








