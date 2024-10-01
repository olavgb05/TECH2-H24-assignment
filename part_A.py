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
    
    N = 0
    total_x = 0
    sum_squares = 0

    for i in x:
        N = N + 1                           # Calculating the number of elements
        total_x = total_x + i               # Calculating the total x or the sum of x
        sum_squares = sum_squares + i**2    # Calculating the sum of x squared
        
    
    mean_x = total_x / N                    # Calculating the mean of x
   
    mean_squares = sum_squares / N          # Calculating the mean of x squared
    variance = mean_squares - mean_x**2     # Calculating the variance
    sd = sqrt(variance)                     # Calculating the standard deviation


    return sd

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
    
    N = len(x)                                  # Calculating the number of elements
    mean_x = sum(x) / N                         # Calculating the mean of x
    mean_squares = sum(i**2 for i in x) / N     # Calculating the mean of x squared
    variance = mean_squares - mean_x**2         # Calculating the variance
    sd = sqrt(variance)                         # Calculating the standard deviation
    

    return sd

def main():
    num_lst = [1, 2, 3, 4, 5]

    std_loops_result = std_loops(num_lst)
    std_builtin_result = std_builtin(num_lst)
    std_numpy_result = np.std(num_lst)

    print(f"Computing standard deviation of x using loops gives : {std_loops_result}")
    print(f"Computing standard deviation of x using built-in functions sum() and len() gives : {std_builtin_result}")
    print(f"Computing standard deviation of x using std() from NumPy gives {std_numpy_result}")

if __name__ == "__main__":
    main()