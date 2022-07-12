#dash for monkey pox cases in europe
#data from 

import dash
import pandas as pd
import plotly.express as px
import datetime as dt
from dash import html, dcc
from dash.dependencies import Input, Output


#Load and prepare data
data_mnk = pd.read_csv("monkey_pox_cases.csv")

data_mnk["DateRep"] = data_mnk["DateRep"].astype('datetime64[ns]') #convert daterep column to datetime format
data_mnk["Year"] = data_mnk["DateRep"].dt.to_period("Y") #create year column
data_mnk["Month"] = data_mnk["DateRep"].dt.month #create month column

#count total cases so far
count_data = data_mnk.groupby(["CountryExp"])[["ConfCases"]].sum()
count_data.reset_index(inplace=True)

#App layout
app = dash.Dash()

app.layout = html.Div(children = [
    html.H1(children = "MonkeyPox Cases in Europe as from 2022"),
    html.P(children="Analyse monkeypox cases in Europe between April and July 2022"),

    dcc.Dropdown(id = "select_month",
                options = [
                    {"label":"April","value":4},
                    {"label":"May","value":5},
                    {"label":"June","value":6},
                    {"label":"July","value":7}],
                multi=False,
                value = 4,
                style={"width":"40%"}
                 ),

    dcc.Graph(id = "Cases_graph", figure={})


])


#Run local server
if __name__ == "__main__":
    app.run_server(debug=True)