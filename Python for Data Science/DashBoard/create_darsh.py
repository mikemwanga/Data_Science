#Script to create dashboard
#Using this tutorial (https://www.youtube.com/watch?v=hSPmj7mK6ng&t=629s)
#Make sure the data and code are in the same folder

import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

#----------------------------------------------------------------------------------------
#import data and clean it up
avocado = pd.read_csv("avocado-updated-2020.csv")

#---------------------------------------------------------------------------------------
#Create dash app
app = dash.Dash()

#---------------------------------------------------------------------------------------
#App layout
app.layout = html.Div(children = [
    html.H1(children = "Avocado Prices Dashboard"),

    dcc.Dropdown(
        id = "geo_dropdown",
        options = [{"label":i, "value":i}
                    for i in avocado["geography"].unique()],
        value = "New York"),

    dcc.Graph(id = "price-graph")
])

#---------------------------------------------------------------------------------------
#Set up the callback
@app.callback(
    Output(component_id ="price-graph", component_property="figure"), #provide output first
    Input(component_id = "geo_dropdown", component_property="value")

)

def update_graph(selected_geography):
    filtered_avocado = avocado[avocado["geography"]==selected_geography]
    line_fig = px.line(filtered_avocado, 
                        x = "date",
                        y = "average_price",
                        color = 'type',
                        title= f"Avocado prices in {selected_geography}")
    return line_fig

#---------------------------------------------------------------------------------------
#Run local server
if __name__ == "__main__":
    app.run_server(debug=True,port = 8052)