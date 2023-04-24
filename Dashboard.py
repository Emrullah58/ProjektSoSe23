from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('MSFT.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Stock Prices'),
    html.Hr(),
    dcc.RadioItems(options=['Open', 'High', 'Low','Close'], value='Open', id='controls-and-radio-item'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output(component_id='graph-content', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(df,x='Date',y=col_chosen)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
