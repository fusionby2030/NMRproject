from flask import Flask, render_template, request
"""
Single Paged Flask App
graph_dash: renders the graph_dash.html page using create_graph
            submit POST: update graph with new data points
            reset POST: drop all data points and start with fresh empty list

"""
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def graph_dash():
    global x_list, y_list #this is totally terrible and totally temporary
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

def create_graph(x_list, y_list):
    """
    Creates a plotly JSON graph to be used for the graph_dash.html page
    @param: x_list -> a list (should be floats)
    @param: y_list -> a list
    returns -> a JSON dump that can be interpreted with plotly style scripts
    """
    df = pd.DataFrame({'x':x_list, 'y': y_list})
    data = [go.Scatter(x=df['x'], y=df['y'], mode='markers')]
    #TODO: ADD go.TangentLine
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__=='__main__':
    x_list = y_list = [] #once again this is temporary
    app.run(debug=True)
