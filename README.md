# NMRproject

## Current Overview [27.07.20]
Below is an overview of the current structure of the package.

- simpler_NMR_project/
  - static/
  - templates/
    - graph_dash.html
      - simple HTML rendering of the plotly graph as well as an input form and submit/reset buttons.
  - sample_dashboard.py
    - Single paged flask app
    - create_graph function
At the moment, this package has two functions.
If you type in a number into the _New x value_ and _New y value_ fields then press submit, the graph is updated with the points you give it. Should you want to reset the graph, click reset, and all the data points disappear.
There are various functions like zoom in/out, save as png, reset axes... that are located in the top right hand corner of the graph.

## Steps to reproduce

In order to use this package, you must first make sure you have the proper dependencies.


First clone/download/fork the repository.


in the terminal, make a [virtual environment](https://docs.python.org/3/library/venv.html)


Install dependencies from requirements.txt using
`pip install -r /path/to/requirements.txt`

in your terminal open up the directory _simpler_NMR_project_ and run the server via `python sample_dashboard.py`

You should see various lines show up, but the most important is the one that says
`Running on http:/XXX.X.X.X:XXXX` with numbers that may vary (for me it is `http://127.0.0.1:5000`). This the URL for the flask app is locally running on your computer, so open up your favourite browser and type in the URL.
