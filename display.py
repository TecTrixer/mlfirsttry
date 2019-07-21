import dash
import dash_core_components as dcc
import dash_html_components as html

with open("points.txt", "r") as file:
    data = str(file.read()).split(",")
    length = len(data)

    x = [None] * length
    y = [None] * length

    for i in range(length):
        x[i] = str(data[i]).split()[0]
        y[i] = str(data[i]).split()[1]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Graph with random points
    '''),

    dcc.Graph(
        id='graph',
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'scatter', "mode": "markers", 'name': 'Points'},
            ],
            'layout': {
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)