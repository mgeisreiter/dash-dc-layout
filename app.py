import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'DC Coffee'
myheading1 = 'DC has some good coffee shops'
myheading2 = 'Always need caffeine'
image1 = 'compass.jpeg'
image2 = 'colombe.jpg'
image3 = 'dolcezza.jpeg'
textbody = "DC has good coffee."
sourceurl = 'https://fitt.co/washington-dc/articles/best-coffee-shop-washington-dc'
githublink = 'https://github.com/mgeisreiter/dash-dc-layout'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '12px',
                'font-size': '20px',
                'height': '120px',
                'border': 'thin blue solid',
                'color': 'rgb(133, 231, 255)',
                'backgroundColor': 'rgb(55, 31, 191)',
                'textAlign': 'left',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
