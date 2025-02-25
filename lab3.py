
import numpy as np
import matplotlib.pyplot as plt

"""
Satan vilken galen fråga:
På Centralen är 70% kvar veckan 2, 10% finns då på Landvetter och 20% är uthyrda
För Landvetter: 60% kvar, 10% på Centralen och 30% uthyrda
Av de som är uthyrda i början av en vecka är 50% det veckan därpå: 30% på Centralen och 20% på Landvetter

c_n är antalet bilar på Centralen  vecka n
l_n är antalet bilar på Landvetter vecka n
u_n är antalet uthyrda bilar       vecka n
"""

# a)
"""
v0 = [a, b, c] 
To compute v1 the following calculation would be used:
v1 = np.array([v0[0] * 0.7 + v0[1] * 0.1 + v0[2] * 0.3, 
                v0[0] * 0.1 + v0[1] * 0.6 + v0[2] * 0.2,
                v0[0] * 0.2 + v0[1] * 0.3 + v0[2] * 0.5])

This gives us the following 3x3 matrix
A = np.array([[0.7, 0.1, 0.3], 
                [0.1, 0.6, 0.2],
                [0.2, 0.3, 0.5]])

"""
   

# b)
def distribution(A, v0, n):
    # Initialize shape of resulting matrix
    vs = np.zeros((3, n+1))
    # Set first column of matrix to v0
    vs[:, 0] = v0
    # Recursively compute the rerst of the matrix 
    # using the formula v_k = A * v_k-1
    for k in range(1, n+1):
        vs[:, k] = np.matmul(A, vs[:, k-1])
    
    plt.xlabel("# of weeks")
    plt.ylabel("Fraction")

    # Display results
    show_plot(vs)


def show_plot(vs):

    weeks = [1, 10, 100, 1000, 10000, 100000]

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
