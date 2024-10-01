"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import numpy as np
from math import sqrt

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    # Calculate the length of the list using loops
    N = 0
    for _ in x:
        N = N + 1
    
    # Calculate the mean of x using loops
    total = 0
    for i in x:
        total = total + i
    mean_x = total / N

    # Calculate the sum of squares using loops
    sum_squares = 0
    for i in x:
        sum_squares = sum_squares + i**2
    
    # Calculate standard deviation
    mean_squares = sum_squares / N
    variance = mean_squares - mean_x**2
    std_dev = sqrt(variance)


    return std_dev

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    # Calculate using the built-in functions len() and sum()
    N = len(x)
    mean_x = sum(x) / N
    mean_squares = sum(i**2 for i in x) / N
    variance = mean_squares - mean_x**2
    std_dev = sqrt(variance)
    

    return std_dev

num_lst = [1, 2, 3, 4, 5]

std_loops_result = std_loops(num_lst)
std_builtin_result = std_builtin(num_lst)
std_numpy_result = np.std(num_lst)

print(f"Computing standard deviation of x using loops gives : {std_loops_result}")
print(f"Computing standard deviation of x using built-in functions sum() and len() gives : {std_builtin_result}")
print(f"Computing standard deviation of x using std() from NumPy gives {std_numpy_result}")