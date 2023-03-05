# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

data = {'Year': [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        'Northern Ireland Practices': [362, 358, 357, 357, 353, 353, 353, 350, 349, 345, 342, 333, 327, 323, 321],
        'Total Registered Patients per Practice': [5063, 5132, 5199, 5243, 5352,
                                                 5385, 5414, 5500, 5557, 5662, 5752,
                                                 5926, 6084, 6200, 6252]}
#['#61C9A8','#547BBD','#FFBC42']
df = pd.DataFrame(data)

#fig = px.line(df, x="Year", y="Northern Ireland Practices", markers=True, color_discrete_sequence=['#547BBD'], height=600)

# Add traces

fig.add_trace(
    go.Scatter(x=df["Year"], 
               y=df["Total Registered Patients per Practice"], 
               name="Total Registered Patients per Practice",
               marker=dict(size=10,
                color='#61C9A8')),
    secondary_y=False,
)

# Add figure title
#fig.update_layout(
#    title_text="Double Y Axis Example"
#)

# Set x-axis title
fig.update_xaxes(title_text="Year")

# Set y-axes titles
fig.update_yaxes(title_text="Total Registered Patients per Practice", secondary_y=False)
#fig.update_yaxes(title_text="Total Registered Patients per Practice", secondary_y=True)

####################

fig.update_layout(
    title_text="<b>Registered Patients per Practice in Northern Ireland</b>",
    margin=dict(
        b=150,
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
        tickangle = -45,
        title=dict(
            text='Year',
            font=dict(
                size=20
            )
        )
    ),
    yaxis1=dict(
        tickformat = ',.0f M',
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
            font=dict(
                size=20
            )
        )
    ),
    yaxis2=dict(
        tickformat = ',.0f M',
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
            font=dict(
                size=20
            )
        )
    ),
    annotations=[
        dict(
            x=0,
            y=-0.2,
            xref="paper",
            yref="paper",
            text="Source: NINIS, NISRA, GPs, Practices and Registered Patients (administrative geographies), 2007-2021.",
            showarrow=False,
            font=dict(
                size=16, color='grey'
            )
        )
    ]
)

fig.update_traces(hoverlabel=dict(font=dict(size=16)))

fig.update_layout(
    title_font_color='#547BBD',
    title_font_size=20,
    margin=dict(
        pad=5
    ),
height=800)

fig.update_layout(legend=dict(y=-0.3,x=-0.05))

fig.update_traces(hoverlabel=dict(font=dict(size=16)))

fig.update_layout(
    legend_title=dict(font=dict(size=18)),
    legend = dict(font = dict(size = 16)))

fig.update_layout(margin=dict(
        pad=5
    ),)

fig.show()
