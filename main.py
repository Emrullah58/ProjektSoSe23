import pandas_datareader.data as web
import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import datetime
from pandas_datareader import data as pdr
import yfinance
import logging



logging.getLogger('werkzeug').setLevel(logging.ERROR) #Test for the "should be integers" problem


#dash apps = layout + interactivity with the user

#Layout
app = Dash(__name__)
app.title = "Simple Stock Visualization"
app.layout = html.Div(children=[
    html.H1('Stock Visualization Dashboard'),
    html.H4('Enter Stock Name'),
    dcc.Input(id="input", value='', type='text'),
    html.Div(id="output-graph")
])

#Interactivity
@app.callback(
    Output(component_id="output-graph", component_property='children'),
    [Input(component_id="input", component_property="value")]
)

def update_value(input_data): #function with just one parameter, the input data company name
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2022, 4, 10)
    df = web.DataReader(input_data, 'yahoo', start, end) #problem should be here
    return dcc.Graph(id="demo", figure={'data': [{'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data}, ], 'layout': {'title': input_data}})

#run the server
if __name__ == "__main__":
    app.run_server(debug=False)

#https://stackoverflow.com/questions/74832296/typeerror-string-indices-must-be-integers-when-getting-data-of-a-stock-from-y
#the chart shows on html, problem with data reading, supposedly due to yahoo updating to yahoo finance library (ca. december 2022)
