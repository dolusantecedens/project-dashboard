import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def render_tab(df):
    layout = html.Div([html.H1('Kanały', id="placeholder", style={'text-align':'center'}),
            html.Div([html.Div([dcc.Graph(id="scatter-plot")])]),
            html.Div([html.Div([dcc.Dropdown(id='gender-store-drop', options={"M":"M", "F":"F"})], style={'width':'33%'}),
            html.Div([dcc.Graph(id='gender-store-type')] ,style={'width':'33%'})], style={'display':'flex'}),
            html.Div([html.Div([dcc.Dropdown(id='birth-store-drop', options={interval : interval for interval in df["interval"].unique()})],
             style={'width':'33%'}),html.Div([dcc.Graph(id='birth-store-type')] ,style={'width':'33%'})], style={'display':'flex'}),
            html.Div([html.Div([dcc.Dropdown(id='country-store-drop', options={country : country for country in df['country'].unique()})],
             style={'width':'33%'}),html.Div([dcc.Graph(id='country-store-type')] ,style={'width':'33%'})], style={'display':'flex'}),
            ])
    return layout