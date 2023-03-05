from plotly.subplots import make_subplots
import plotly.graph_objects as go

labels = ['0-15','16-64','65+']
colors=['#61C9A8','#547BBD','#FFBC42']

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=[20.9, 62.2, 16.9], name="2020",marker_colors=colors, insidetextorientation='horizontal'),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=[18.1, 61.1, 20.7], name="2030",marker_colors=colors, insidetextorientation='horizontal'),
              1, 2)
fig.add_trace(go.Pie(labels=labels, values=[16.4, 58.5, 24.8], name="2045",marker_colors=colors, insidetextorientation='horizontal'),
              1, 3)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.45, hoverinfo="label+percent+name", textfont_size=16)

fig.update_layout(
    title_text="<b>Age Profile of Northern Ireland</b>",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='2020', x=0.113, y=0.5, font_size=20, showarrow=False, font=dict(size=16, color='grey')),
                 dict(text='2030', x=0.5, y=0.5, font_size=20, showarrow=False, font=dict(size=16, color='grey')),
                 dict(text='2045', x=0.895, y=0.5, font_size=20, showarrow=False, font=dict(size=16, color='grey')),
                 dict(x=0.5,y=-0.2,
                     text="Source: NISRA, 2020-based Interim Population Projections for Northern Ireland",
                     showarrow=False,
                     font=dict(size=16, color='grey'))]
    )

fig.update_traces(hoverlabel=dict(font=dict(size=16)))

fig.update_layout(
    title_font_color='#547BBD',
    title_font_size=20,
    legend_title=dict(text='Age', font=dict(size=18)),
    legend = dict(font = dict(size = 16)))

fig.show()
