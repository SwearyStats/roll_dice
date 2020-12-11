import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np

import os


def generate_thumbnail(image, app):
        
    test_png = os.path.join('images', image)

    return html.Div([
        html.A([
            html.Img(
                src = app.get_asset_url(test_png),
                style = {
                    'height': '40%',
                    'width': '40%',
                    'float': 'center',
                    'position': 'relative',
                    'padding-top': 20,
                    'padding-right': 0
                }
            )
        ]),
    ])


def read_files_dir(path):

    files = os.listdir(path)

    return(files)