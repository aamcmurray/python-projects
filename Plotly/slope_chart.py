import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


data = {"HSCT": ["Belfast", "Northern", "South Eastern", "Southern", "Western"],
        "Longstanding illness (%), 2010": [37.29, 37.23, 38.4, 36.92, 35],
        "Longstanding illness (%), 2020": [43.02, 39.77, 40.76, 36.14, 47.94]}

df = pd.DataFrame(data)

achieved_2012=df["Longstanding illness (%), 2010"].values.tolist()
achieved_2020=df["Longstanding illness (%), 2020"].values.tolist()
lgd=df["HSCT"].values.tolist()


colors=['#547BBD','#61C9A8','#c96182','#bc42ff','#FFBC42']

fig = go.Figure(go.Scatter(x=[0] * len(achieved_2012),
                           y=achieved_2012, 
                           mode='markers+text', 
                           showlegend = False, 
                           hovertext = lgd,
                           name='2010',
                           marker=dict(
                               color=colors,
                               size=10)
                          ))

fig.add_trace(go.Scatter(x=[1] * len(achieved_2020),
                           y=achieved_2020, 
                           mode='markers+text', 
                           showlegend = False, 
                           hovertext = lgd,
                           name='2020',
                           marker=dict(
                               color=colors, 
                               size=10)
                          ))

for y0, y1,c in zip(achieved_2012, achieved_2020, colors):
    fig.add_shape(type='line', x0=0, x1=1, y0=y0, y1=y1, line=dict(
        color=c))
    



    
fig.add_annotation(dict(x=-0.1, y=max(achieved_2020)+2,
            text="<b>2010</b>",
            showarrow=False,
            yshift=10, font = dict(size=16,color = 'grey')))

fig.add_annotation(dict(x=1.1, y=max(achieved_2020)+2,
            text="<b>2020</b>",
            showarrow=False,
            yshift=10, font = dict(size=16,color = 'grey')))


for i in range(len(achieved_2012)):
    #if i%2 == 1:
    
    #else:
    fig.add_annotation(x = 1+0.04, y = achieved_2020[i], xanchor = 'left', text = lgd[i],font=dict(size=16, color='grey'), showarrow = False)


fig.add_vline(x=0, line_width=1, line_color="grey")
fig.add_vline(x=1, line_width=1, line_color="grey")    

    
    
fig.update_layout(height = 800)
fig.update_xaxes(showticklabels = False)

fig.update_layout(
    title_text="<b>Persons with Longstanding Illness (%) by HSCT</b>",
    margin=dict(
        b=50,
        pad=20
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(
        showticklabels=False,
        showgrid=False,
        linewidth=2,
        tickmode='auto',
        nticks=20,
        tickfont=dict(
            size=16
        ),
    ),
    yaxis=dict(
        tickformat = ',.0f M',
        showticklabels=False,
        showgrid=False,
        linewidth=2,
        tickmode='auto'
        )
    )

fig.update_traces(hoverlabel=dict(font=dict(size=16)))

fig.update_layout(
    title_font_color='#547BBD',
    title_font_size=20,
margin=dict(
        pad=5
    ),)



fig.update_traces(marker=dict(size=10))

fig.update_traces(
    hovertemplate="<br>".join([
        "HSCT: %{hovertext}",
        "Percentage: %{y}"
    ])
)


fig.update_traces(hoverlabel=dict(font=dict(size=16)))

fig.show()
