import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import fastf1


app = dash.Dash(__name__)
server = app.server


# Layout
app.layout = html.Div([
    html.H1('F1 Telemetry Dashboard', style= {'textAlign':'center'}),
    
    html.Div([
        html.Label('Select Driver 1'),
        
        dcc.Dropdown(
            id = 'driver1',
            options = [{'label' : d, 'value': d} for d  in ['VER', 'LEC', 'HAM', 'NOR']],
            value = 'VER'
        ),
    html.Label('Select Driver 2'),
    dcc.Dropdown(
        id = 'driver2',
        options = [{'label' : d, 'value': d} for d in ['VER', 'LEC', 'HAM', 'NOR']],
        value = 'LEC'
    ),
], style={'width': '50%', 'margin': 'auto'}),
    dcc.Graph(id = 'telemetry-graph')
])


@app.callback(
    Output('telemetry-graph', 'figure'),
    [Input('driver1', 'value'),
     Input('driver2', 'value')
     ]
)   
def update_telemetry(driver1, driver2):
        session = fastf1.get_session(2023, 'Monza', 'Q')
        session.load()
    
        driver1lap = session.laps.pick_drivers(driver1).pick_fastest()
        driver2lap = session.laps.pick_drivers(driver2).pick_fastest()
    
        driver1tel = driver1lap.get_car_data().add_distance()
        driver2tel = driver2lap.get_car_data().add_distance()
    
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=driver1tel['Distance'], y = driver1tel['Speed'], name = driver1))
        fig.add_trace(go.Scatter(x=driver2tel['Distance'], y = driver2tel['Speed'], name = driver2))
        fig.update_layout(title = 'Speed Comparison - Monza 2023 Quali', xaxis_title = 'Distance (m)', yaxis_title = 'Speed (lm/h)')

        return fig
    
if __name__ == '__main__':
    app.run(debug = True)
    
    
