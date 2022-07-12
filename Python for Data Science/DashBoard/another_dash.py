from optparse import Option
import dash
import pandas as pd
import plotly.express as plx
import datetime as dt
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash()
#create data
data = pd.read_csv("country_data.csv")
#data2 = data.sort_values("total_confirmed_cases", ascending=False).head(n=10)

## set up your dash app
app.layout = html.Div(children = [
                        html.H1(children = "COVID-19 Total Confirmed Cases"),

                        dcc.Dropdown(
                            id = "select_country", 
                            options = [{"label":i, "value":i} 
                                        for i in data["country/region"]],
                            value = "Kenya"),

                        dcc.Graph(id = "plots")
                        
                    ])

@app.callback(

    Output(component_id ="plots", component_property="figure"), #provide output first
    Input(component_id = "select_country", component_property="value")
            )

def update_plots(selected_country):
    selected_data = data[data["country/region"] == selected_country]
    selected_data = selected_data.drop(["lat","long"], axis=1)
    fig = selected_data.plot(kind="bar")

    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port = 8056)