import numpy as np
import matplotlib.pyplot as plt



# a)
"""
v0 = [c0, 
      l0, 
      u0] 

To compute v1 the following calculation would be used:
v1 = [c0 * 0.7 + l0 * 0.1 + u0 * 0.3, 
      c0 * 0.1 + l0 * 0.6 + u0 * 0.2,
      c0 * 0.2 + l0 * 0.3 + u0 * 0.5]

To compute v2 and so on we just multiply the previous vector by A

By the calculation of v1
we see that A is written as
A = [[0.7, 0.1, 0.3], 
     [0.1, 0.6, 0.2],
     [0.2, 0.3, 0.5]]

So, for the expressions we get:
v_1 = A * v0
v_2 = A * v1 = A * A * v0 = A^2 * v0
v_n = A^n * v0
"""
   

# b)
def distribution(A, v0, n):
    # Initialize shape of resulting matrix
    vs = np.zeros((3, n+1))
    # Set first column of matrix to v0
    vs[:, 0] = v0

    # Recursively compute the rest of the matrix
    # using the formula v_k = A * v_k-1
    for k in range(1, n+1):
        vs[:, k] = np.matmul(A, vs[:, k-1])
 
    plt.xlabel("# of weeks")
    plt.ylabel("Fraction")

    # Display results
    show_plot(vs)


def show_plot(vs):

    weeks = [10**n for n in range(6)]


    # Draw dots of the selected weeks
    plt.scatter(weeks, vs[0, weeks], label = "Centralen")
    plt.scatter(weeks, vs[1, weeks], label = "Landvetter")
    plt.scatter(weeks, vs[2, weeks], label = "Uthyrda")        

    # Scale the x-axis logarithmically
    plt.xscale("log")
    plt.legend()
    plt.show()

A = np.array([[0.7, 0.1, 0.3], 
              [0.1, 0.6, 0.2],
              [0.2, 0.3, 0.5]])
n = 100_000
distribution(A, np.array([1/3, 1/3, 1/3]), n)
distribution(A, np.array([1, 0, 0]),       n)
distribution(A, np.array([0, 1, 0]),       n)
distribution(A, np.array([0, 0, 1]),       n)
