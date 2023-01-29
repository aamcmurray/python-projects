import numpy as np
import matplotlib.pyplot as plt
from random import sample
import pandas as pd
from scipy.stats import shapiro
import statsmodels.api as sm

# created using guidance from chatGPT

def lowess(x, y, f=f_val, iter=total_iterations):
    """
    Perform LOWESS smoothing on two 1-D arrays x and y.

    Parameters:
        x : array-like
            The independent variable.
        y : array-like
            The dependent variable.
        f : float
            The smoothing factor. 
            Should be between 0 and 1, where 0 is the least smoothing and 1 is the most smoothing.
        iter : int
            The number of times to iterate the smoothing.

    Returns:
        yest : array-like
            The smoothed values of y.
    """
    n = len(x)
    r = int(np.ceil(f*n))
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)]
    w = np.clip(np.abs((x[:,None] - x[None,:]) / h), 0.0, 1.0)
    w = (1 - w ** 3) ** 3  
    yest = np.zeros(n)
    delta = np.ones(n)
    for iteration in range(iter):
        for i in range(n):
            weights = delta * w[:,i]
            b = np.array([np.sum(weights*y), np.sum(weights*y*x)])
            A = np.array([[np.sum(weights), np.sum(weights*x)],
                      [np.sum(weights*x), np.sum(weights*x*x)]])
            beta = np.linalg.solve(A, b)
            yest[i] = beta[0] + beta[1]*x[i]
        residuals=y-yest
        s = np.median(np.abs(residuals))
        delta = np.clip(residuals / (6 * s), -1, 1)
        delta = (1 - delta ** 2) ** 2
    return yest

def bootstrap_lowess(x, y, f=f_val, iter=total_iterations, n_samples=boot_samples):
    """
    Perform bootstrap resampling on the LOWESS smoothed data.

    Parameters:
        x : array-like
            The independent variable.
        y : array-like
            The dependent variable.
        f : float
            The smoothing factor. 
            Should be between 0 and 1, where 0 is the least smoothing and 1 is the most smoothing.
        iter : int
            The number of times to iterate the smoothing.
        n_samples : int
            The number of bootstrap samples to generate.
    Returns:
        yest_samples : array-like
            The smoothed values of y for each bootstrap sample.
    """
    # Create an empty array to store the smoothed y values for each sample
    yest_samples = np.zeros((n_samples, len(x)))
    x_vals_samples = np.zeros((n_samples, len(x)))
    # Generate bootstrap samples
    for i in range(n_samples):
        # Generate a random sample of the indices
        sample_indices = np.random.randint(0, len(x), len(x))
        xvals=x[sample_indices]
        # Perform LOWESS smoothing on the x and y values for the sample
        x_vals_samples[i]=xvals
        yest_samples[i] = lowess(xvals, y[sample_indices], f, iter)

    return x_vals_samples, yest_samples

def sorter(x,y):
    df = pd.DataFrame({"x": x, "y": y})
    df = df.iloc[df["x"].argsort()]
    sorted_x = df['x'].values
    sorted_y=df['y'].values
    return sorted_x,sorted_y

######################################################################################


def lowess_with_bootstrap(input_x,input_y):
    # Calculate Lowess Curbe
    smoothed_y=lowess(input_x,input_y)
    # Perform bootstrapping
    sorted_x,sorted_smoothed_y=sorter(input_x,smoothed_y)
    sampled_x_vals, bootstrapping=bootstrap_lowess(x,y)
    # Plot Scatter data
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='#15133C', label='Original Data', s=10)
    
    # Plot bootstraps
    for i in range(0, len(sampled_x_vals)):
        sortx,sorty=sorter(sampled_x_vals[i],bootstrapping[i])
        ax.plot(sortx,sorty, '#73777B', alpha=0.1)
    # Plot smoothed data
    ax.plot(sorted_x,sorted_smoothed_y, color='#EC994B', label='Smoothed Data')
    ax.set_xlabel('X Values')
    ax.set_ylabel('Y Values')
    ax.set_title('LOWESS Fit')
    # Add a grid
    ax.grid(True, linestyle='-', alpha=0.5)
    ax.grid(which='minor', linestyle=':')
    # Add a legend
    ax.legend(loc='upper right')
    plt.style.use('seaborn-darkgrid')
    plt.show()
    
f_val=1/3
total_iterations=15
boot_samples=250

# DUMMY DATA
x = 5*np.random.random(100)
y = np.sin(x) * 3*np.exp(-x) + np.random.normal(0, 0.2, 100)

lowess_with_bootstrap(x,y)
