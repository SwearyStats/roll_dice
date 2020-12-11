# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
from utilities import generate_thumbnail, read_files_dir

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

'''Add in python randomizer function here'''

images_div = []

app.layout = html.Div(children=[

    html.Div([
        html.H1("Welcome to Miss Slater's Random Adventure Maker!"),

        html.Div([
            html.H2("Let's go on an adventure!"),
            html.H3("Select how many parts you want"),
        ], style={'textAlign': 'center'})
    ], style={'textAlign': 'center'}),



    ### Select how many dice
    html.Div([
        dcc.Dropdown(id='n_dice_dropdown',
                     placeholder='Select how many parts you want!',

                    options=[
                            {'label': '3', 'value': 3},
                            {'label': '4', 'value': 4},
                            {'label': '5', 'value': 5},
                            {'label': '6', 'value': 6},
                            {'label': '7', 'value': 7},
                            {'label': '8', 'value': 8},
                            {'label': '9', 'value': 9}
                            ],
                    value=0,
                    
                    clearable=False,

                     style={'font-size': '90%',
                            'height': '40px',
                            }
                     )
    ], style={'margin-bottom': '10px',
              'textAlign':'center',
              'width': '300px',
              'margin':'auto'}
    ),
         


    
    html.Div(children=images_div,

    id = 'image_display_div',
    
    style={'margin-bottom': '10px',
              'textAlign':'center',
              'width': '1000px',
              'margin':'auto'})

    ])



### Callbacks Here
@app.callback(
    Output(component_id='image_display_div', component_property='children'),
    Input(component_id='n_dice_dropdown', component_property='value')
)

def update_output_div(input_value):

    choice = read_files_dir('assets/images')

    images_div = []
    
    images = np.random.choice(choice, size = input_value, replace = False)

    for i in images:
        images_div.append(generate_thumbnail(i, app))


    print(choice)

    return(images_div)

if __name__ == '__main__':
    app.run_server(debug=True)