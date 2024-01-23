import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

xl = [0]
xl1 = [0]
xl2 = [0]

tl = [0]
tl1 = [0]
tl2 = [0]

def euler():

  t = 0
  x = 0
  dt = 0.1

  while (tl2[-1] <= 100):

      xl2.append(xl2[-1] + (dt * ((3 * tl2[-1] ** 2) + (5 * tl2[-1]))))
      tl2.append(tl2[-1] + dt)



def exactValue():

  t = 0
  x = 0
  dt = 0.001

  while (tl1[-1] <= 100):

      xl1.append(tl1[-1] ** 3 + (2.5 * (tl1[-1] ** 2)))
      tl1.append(tl1[-1] + dt)


def SIR(Values, t):

    return [(3 * t ** 2) + (5 * t)]

def odeInt():

    ts = np.arange(0, 60, 0.01)

    Us = odeint(SIR, [0], ts)

    S= Us[:, 0]

    fig = plt.subplot()

    plt.plot(ts, S, label="Suscepble")

    plt.legend()
    plt.show()


def rungeKutta2():

    t = 0
    x = 0

    # Set step size.
    dt = 0.1

    while (tl[-1] <= 100):

        k1 = (3 * tl[-1] ** 2 + (5 * tl[-1]))
        k2 = (3 * (tl[-1] + (dt / 2)) ** 2 + 5 * (tl[-1] + (dt /2)))
        k3 = (3 * (tl[-1] + (dt / 2)) ** 2 + 5 * ((tl[-1] + dt /2)))
        k4 = (3 * (tl[-1] + dt) ** 2 + 5 * (tl[-1] + dt))
        xl.append(xl[-1] + ((dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)))
        tl.append(tl[-1] + dt)

#odeInt()

ts = np.arange(0, 100, 0.01)

Us = odeint(SIR, [0], ts)

S= Us[:, 0]

fig = plt.subplot()

plt.plot(ts, S, label="ODEINT")


euler()
exactValue()
rungeKutta2()

plt.plot(tl1, xl1, label = "Exact")
plt.plot(tl, xl, label = "Runge-Kutta", linestyle = 'dotted')
plt.plot(tl2, xl2, label = "Euler", linestyle = 'dotted')


plt.legend()
plt.show()
