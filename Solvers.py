import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

s = 1500.0
i = 1.0
r = 0.0

beta = 0.0005
gamma = 0.1

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

            """ k0 = deltat * -beta*sValues[-1] * iValues[-1]
            k1 = deltat * (-beta * (sValues[-1] + 0.5 * k0) * (iValues[-1] + 0.5 * k0))
            k2 = deltat * (-beta * (sValues[-1] + 0.5 * k1) * (iValues[-1] + 0.5 * k1))
            k3 = deltat * (-beta * (sValues[-1] * k2) * (iValues[-1] * k2))

            h0 = deltat * (beta * sValues[-1] * iValues[-1] - (gamma * iValues[-1]))
            h1 = deltat * ((beta * (sValues[-1] + 0.5 * h0) * (iValues[-1] + 0.5 * h0)) - (gamma * iValues[-1] + 0.5 * h0))
            h2 = deltat * ((beta * (sValues[-1] + 0.5 * h1) * (iValues[-1] + 0.5 * h1)) - (gamma * iValues[-1] + 0.5 * h1))
            h3 = deltat * ((beta * (sValues[-1] * h2) * (iValues[-1] * h2)) - (gamma * iValues[-1] * h2))

            sValues.append(sValues[-1] + ((k0 + 2*k1 + 2*k2 + k3) / 6))
            iValues.append(iValues[-1] + ((h0 + 2 * h1 + 2 * h2 + h3) / 6))



            rValues.append(1500 - sValues[-1] + ((k0 + 2*k1 + 2*k2 + k3) / 6) - iValues[-1] + ((h0 + 2 * h1 + 2 * h2 + h3) / 6))
            tValues.append(tValues[-1] + deltat)

            methodHasRan = True """

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
    return [-beta * Values[0] * Values[1],
            beta * Values[0] * Values[1] - gamma * Values[1],
            gamma * Values[1]]


def odeInt():
    ts = np.arange(0, 60, 0.01)

    Us = odeint(SIR, [s, i, r], ts)

    S, I, R = Us[:, 0], Us[:, 1], Us[:, 2]

    # fig = plt.subplot()
    fig = plt.figure()
    fig.patch.set_facecolor('xkcd:grey')
    plt.plot(ts, S, label="")
    plt.plot(ts, I, label="")
    plt.plot(ts, R, label="")

    ax = plt.gca()
    ax.set_facecolor('xkcd:grey')
    plt.legend(facecolor="xkcd:grey", edgecolor="xkcd:grey")
    plt.show()



