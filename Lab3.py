# (a)
"""
A =
([0.7, 0.1, 0.3], (Xc)
[0.1, 0.6, 0.2], (Xl)
[0.2, 0.3, 0.5]) (Xu)

Där Xc är % av bilar från Centralen, Landvetter, Uthyrning som är vid Centralen
    Xl är -||- som är vid Landvetter
    Xu är -||- som är Uthyrda.

    Vn = (Cn, Ln, Un) = A*Vn^-1
=>  [n = 0]
=>  V1 = A^1*V0
=>  V2 = A*V1 = A*(A*V0) = A^2*V0
=>  V3 = A*V2 = A*(A*V1) = A*(A*(A*V0) = A^3*V0, etc.
=>  Vn = A^n*V0 //
"""

# (b)

import numpy as np
import matplotlib.pyplot as plt

def car_distribution(p, init_state, weeks):
    # keeps distribution values for each passing week
    dist = []
    state = init_state
    for _ in range(weeks+1):
        dist.append(state)
        state = np.matmul(p, state)
    return np.array(dist)

# Changeable
p = np.array(([0.7, 0.1, 0.3],
              [0.1, 0.6, 0.2],
              [0.2, 0.3, 0.5]))

def simulation(state):
    # plots distribution values over time
    weeks = [10**n for n in range(6)]
    distribution = car_distribution(p, state, max(weeks))

    plt.figure(figsize=(12, 8))
    plt.plot(distribution[:, 0], label="Central")
    plt.plot(distribution[:, 1], label="Landvetter")
    plt.plot(distribution[:, 2], label="Rented")
    plt.xscale("log")
    plt.xlabel("Veckor")
    plt.ylabel("Andel bilar")
    plt.title("Car Distribution")
    plt.legend()
    plt.grid()
    plt.show()

# testers - 0.33/0.33/0.33, 1/0/0, 0/1/0 and 0/0/1
equal_init = np.array([1/3, 1/3, 1/3])
simulation(equal_init)

central_init = np.array([1,0,0])
simulation(central_init)

landvetter_init = np.array([0,1,0])
simulation(landvetter_init)

rented_init = np.array([0,0,1])
simulation(rented_init)
