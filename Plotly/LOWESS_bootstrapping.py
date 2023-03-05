import numpy as np
import matplotlib.pyplot as plt
from random import sample
import pandas as pd
from scipy.stats import shapiro
import statsmodels.api as sm
from scipy.optimize import curve_fit
import plotly.graph_objects as go
from sklearn.utils import resample as bootstraperr
    
f_val=1/3
total_iterations=30
boot_samples=100

# DUMMY DATA
x = 5*np.random.random(100)
y = 10*(np.sin(x) * 3*np.exp(-x) + np.random.normal(0, 0.2, 100))-4

# Define the function to fit to the data
def func(x, a, b, c):
    return a * np.sin(b * x) * np.exp(-c * x) - 4

# Perform the non-linear regression
popt, pcov = curve_fit(func, x, y)

# Generate the line based on the fitted parameters
x_line_reg = np.linspace(0, 5, 100)
y_line_reg = func(x_line_reg, *popt)

#print(len(x),len(y))

def lowess(x, y, f=f_val, iter=total_iterations):
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

def lowess_with_bootstrap(input_x,input_y):
    # Calculate Lowess Curbe
    smoothed_y=lowess(input_x,input_y)
    # Perform bootstrapping
    sorted_x,sorted_smoothed_y=sorter(input_x,smoothed_y)
    sampled_x_vals, bootstrapping=bootstrap_lowess(x,y)
    return x, y, sorted_x,sorted_smoothed_y, sampled_x_vals, bootstrapping

x, y, sorted_x,sorted_smoothed_y, sampled_x_vals, bootstrapping=lowess_with_bootstrap(x,y)

# Define the scatter plot trace
trace = go.Scatter(x=x, y=y, mode='markers', name="Reported Percentage Change to Share of Vote")

def hex_to_rgba(h, alpha):
    '''
    converts color value in hex format to rgba format with alpha transparency
    '''
    return tuple([int(h.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)] + [alpha])

# Define the lines trace
lines = []
for i in range(0, len(sampled_x_vals)):
    if (i<(len(sampled_x_vals)-1)):
        sortx,sorty=sorter(sampled_x_vals[i],bootstrapping[i])
        line = go.Scatter(x=sortx, y=sorty, mode='lines', name='LOWESS Bootstrap',legendgroup='group1',line=dict(width=1, color='rgba' + str(hex_to_rgba(
                    h='#B8CCEC',
                    alpha=i/100
                ))), showlegend=False)
        lines.append(line)
    else:
        sortx,sorty=sorter(sampled_x_vals[i],bootstrapping[i])
        line = go.Scatter(x=sortx, y=sorty, mode='lines', name='LOWESS Bootstrap', legendgroup='group1',line=dict(width=1, color='rgba' + str(hex_to_rgba(
                    h='#B8CCEC',
                    alpha=i/100
                ))), showlegend=True)
        lines.append(line)
    #rgba(84, 123, 189, 1)

newline=go.Scatter(x=sorted_x,y=sorted_smoothed_y, mode='lines', line=dict(color='#61C9A8', width=2), name="LOWESS Smoothing")
newlinebox=[]
newlinebox.append(newline)

layout = go.Layout(title='Scatter Plot with Lines', xaxis_title='X', yaxis_title='Y', height=800)

# Combine the traces and layout into a figure
fig = go.Figure(data=[trace]+lines+newlinebox, layout=layout)

# making it pretty

fig.update_layout(
    title_text="<b>Percentage Change in Share of Vote</b>",
    margin=dict(
        b=70,
        pad=20
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(
        showticklabels=True,
        showgrid=False,
        linecolor='black',
        linewidth=2,
        tickmode='auto',
        nticks=20,
        tickfont=dict(
            size=16
        ),
        title=dict(
            text='Year',
            font=dict(
                size=20
            )
        )
    ),
    yaxis=dict(
        range=[-10,10],
        showticklabels=True,
        showgrid=False,
        linecolor='black',
        linewidth=2,
        tickmode='auto',
        nticks=20,
        tickfont=dict(
            size=16
        ),
        title=dict(
            text='Percentage Change (%)',
            font=dict(
                size=20
            )
        )
    )
)

fig.update_layout(
    hovermode=False,
    )

fig.update_layout(legend=dict(y=-0.37,x=-0.05))

fig.update_layout(
    legend_title=dict(font=dict(size=18)),
    legend = dict(font = dict(size = 16)),
    xaxis=dict(tickmode = 'array',tickvals= [0, 1, 2, 3,4,5],
    ticktext = ['2000','2001','2002','2003','2004', '2005']))

fig.update_layout(
    title_font_color='#547BBD',
    title_font_size=20,
margin=dict(
        pad=5
    ),)

# Show the figure
fig.show()
