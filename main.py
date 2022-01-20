import dash

from dash import dcc

from dash import html

from datetime import date

import yfinance as yf

import pandas as pd

import plotly.graph_objs as go

import plotly.express as px

front = dash.Dash(__name__)
servidor = front.server


title = html.Div(children=html.H1("GC's Stock's Price Predictor"),id="Title",style={"textAlign":"left",
"font-size":26,"color":"#C68D49","font-style":"Andale Mono, monospace"})

stockInputs = html.Div(children=
    [   
        #*Label
        html.Div(html.P("Which stock do you want to search?",id = "commonText", style={"font-size":20,"color":"#e8691a",
        "font-style":"Andale Mono, monospace"})),

        #* Input of Stock Code
        html.Div(children =
        [
            dcc.Input(
            id = "stockCode",
            type = "text",
            placeholder="Code of the Stock",
            size = "40",
        ),
        #*Bottom to Submit Input
        html.Button('Submit', id='submitButton')
    
        ], id = "inputs"),

        #*Date Picker
        html.Div(dcc.DatePickerRange(
        id='datePicker',
        min_date_allowed = date(1970, 1, 1),
        initial_visible_month = date.today(),
        display_format='Do MMMM, YYYY',
        end_date = date.today()
        ), id = "date"),

        html.Div(children =
        [
            #*StockPriceButton
        html.Button('Stock Price', id='stockPriceButton',className="buttons"),

        #*Indicators Button
        html.Button('Indicators', id='indicatorsButton',className="buttons"),


        #* Input of Num of Days
        dcc.Input(
            id = "numDays",
            type = "text",
            placeholder="Number of Days",
            size = "20",
        ),
        
        #*Forecast Button
        html.Button('Forecast', id='forecastButton',className="buttons"),
        
        ], id = "moreButtons"
        )
        
    ],
    id = "stockInputsContainer",
    className = "container",
)

stockDisplay = html.Div(children=[

    html.Div(children = 
    [

    #*Header of stock
    html.Div(children=[
        html.Div(html.Img("stockLogo")),
        html.H2(id = "stockTitle"),
    ], id = "header", className = "header"),
    

    #*Description of stock
    html.Div(children=[
        html.P(id = "stockDescription"),
    ], id = "description", className="decription_ticker"),

    ]
    ),
    

    #?Plots
    #*Stock price plot
    html.Div([

    ], id="graphs-content"),
            
    #*Indicator plot
    html.Div([

    ], id="main-content"),

    
    #*Forecast plot
    html.Div([
    ], id="forecast-content"),

    
    ],

    id = "container",
)


front.layout = html.Div(children=[title,stockInputs,stockDisplay])



if __name__ == '__main__':
    front.run_server(debug=True)