import numpy as np
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
data = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/EP4/NMR/Zellen_10msT37C_manypoints_2ndday - Data.csv')
#graph = data[['GradAna'], ['EchoAmp']]
y = data['EchoAmp'].dropna().to_list()
x = data['GradAna'].dropna().to_list()
dfy = data['EchoAmp'].dropna()
dfx = data['GradAna'].dropna()

dfx.drop(data[data['GradAna'] == '#NAME?'].index)
yaxis = [float(value) for value in y if value != '#NAME?']
xaxis = [float(value) for value in x if value != '#NAME?']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {'background': '#111111', 'text': '#7FDBFF'}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Title',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),

    html.Div(children='Subtitle',
             style={
                'textAlign': 'center',
                'color': colors['text']
             }),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {
                'x': xaxis,
                'y': yaxis,
                'type': 'markers',
                'name': 'Plots',
                'marker': {'size':15, 'line': {'width': 0.5, 'color':'white'}}
                }
            ],
            'layout': {
                'xaxis': {'title': 'GradAna'},
                'yaxis': {'title': 'EchoAmp'},
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'title': 'Graph Title',
                'font': {'color': colors['text']}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
