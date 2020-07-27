from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def index():
    bar = create_plot()
    return render_template('index.html', plot=bar)
@app.route('/graph_dash', methods=['GET', 'POST'])
def graph_dash():
    global x_list, y_list
    if request.method == 'POST':
        if request.form['submit_button'] == 'populate':
            new_x = request.form.get('input_x')
            new_y = request.form.get('input_y')
            x_list.append(new_x)
            y_list.append(new_y)
        elif request.form['submit_button'] == 'reset':
            x_list = []
            y_list = []
    scatter = create_graph(x_list, y_list)
    return render_template('graph_dash.html', plot=scatter)
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

def create_plot():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
def create_graph(x_list, y_list):
    df = pd.DataFrame({'x':x_list, 'y': y_list})
    data = [go.Scatter(x=df['x'], y=df['y'], mode='markers'), go.Scatter(x=df['y'], y=df['x'], mode='markers')]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__=='__main__':
    x_list = y_list = []
    app.run(debug=True)
