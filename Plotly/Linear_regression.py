import numpy as np
import scipy as sp
import scipy.stats as stats
import plotly.graph_objs as go

# Raw Data
heights_one = np.linspace(58, 75,100)

weights_one = 1*heights_one+3+np.random.normal(0,10, size=heights_one.size)

def plot_ci_manual(t, s_err, n, x, x2, y2):
    ci = t * s_err * np.sqrt(1/n + (x2 - np.mean(x))**2 / np.sum((x - np.mean(x))**2))
    return ci

def equation(a, b):
    return np.polyval(a, b) 

x_value = heights_one
y_value = weights_one
p, cov = np.polyfit(x_value , y_value, 1, cov=True)
y_model = equation(p, x_value)   
t = stats.t.ppf(0.975, weights_one.size - p.size)
resid = y_value - y_model
chi2 = np.sum((resid / y_model)**2)
chi2_red = chi2 / (weights_one.size- p.size)
s_err = np.sqrt(np.sum(resid**2) /(weights_one.size- p.size))
x2 = np.linspace(np.min(x_value), np.max(x_value), 100)
y2 = equation(p, x2)
ci=plot_ci_manual(t, s_err, weights_one.size, x_value, x2, y2)
pi = t * s_err * np.sqrt(1 + 1/weights_one.size + (x2 - np.mean(x_value))**2 / np.sum((x_value - np.mean(x_value))**2))   

data = [
    go.Scatter(x=x_value, y=y_value, name='Reported Heights and Weights',
               mode='markers'),
    go.Scatter(x=x_value, y=y_model, 
               mode='lines',
               line=dict(color='#61C9A8', width=2),
               name='Linear Regression'),
    go.Scatter(x=x2, y=y2-ci, 
               fill=None, 
               mode='lines', 
               line_color='#B8CCEC', 
               legendgroup='group6',
               showlegend=False,
               name='95% Confidence Band'),
    go.Scatter(x=x2, y=y2+ci, 
               fill='tonexty', 
               mode='lines', 
               line_color='#B8CCEC', 
               legendgroup='group6',
               showlegend=True,
               name='95% Confidence Band'),
    go.Scatter(x=x2, y=y2+pi,
               mode='lines', 
               line=dict(dash='dot',color='#FFBC42', width=2),
               legendgroup='group5',
               showlegend=False,
               name='95% Prediction Band'),
    go.Scatter(x=x2, y=y2-pi,
               mode='lines', 
               line=dict(dash='dot',color='#FFBC42', width=2),
               legendgroup='group5',
               showlegend=True,
               name='95% Prediction Band'),

]

# create layout for the figure
layout = go.Layout(title='Linear Regression', xaxis_title='X', yaxis_title='Y', height=800)

# create figure
fig = go.Figure(data=data, layout=layout)

fig.update_layout(
    title_text="<b>Linear Regression Fitting</b>",
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
            text='Weight /kg',
            font=dict(
                size=20
            )
        )
    ),
    yaxis=dict(
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
            text='Height /inches',
            font=dict(
                size=20
            )
        )
    )
)

fig.update_layout(
    hovermode=False,
    )

fig.update_layout(legend=dict(y=-0.35,x=-0.05))

fig.update_layout(
    legend_title=dict(font=dict(size=18)),
    legend = dict(font = dict(size = 16)),)

fig.update_layout(
    title_font_color='#547BBD',
    title_font_size=20,
margin=dict(
        pad=5
    ),)

# Show the figure
fig.show()
