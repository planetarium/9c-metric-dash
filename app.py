from __future__ import annotations
import flask
import dash
if int(dash.__version__.split(".")[0]) < 2:
    import dash_core_components as dcc
    import dash_html_components as html
else:
    from dash import dcc
    from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import graph
import option
import const

def serve_layout():
    with open(const.path_file, "r") as file:
        log_directory = file.read()
    log_file_options = option.get_log_file_options(log_directory)
    log_file_default = log_file_options[0]["value"]
    return html.Div(
        dbc.Col(html.Div([
            html.H1(children='Nine Chronicles Metric Log Dash'),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="block_append_figure",
                            ),
                            dcc.Dropdown(
                                id="block_append_figure_file",
                                options=log_file_options,
                                value=log_file_default,
                                clearable=False,
                            ),
                        ],
                    ),
                    html.Hr(),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="block_lag_figure",
                            ),
                            dcc.Dropdown(
                                id="block_lag_figure_file",
                                options=log_file_options,
                                value=log_file_default,
                                clearable=False,
                            ),
                        ],
                    ),
                    html.Hr(),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="block_absolute_evaluation_figure",
                            ),
                            dcc.Dropdown(
                                id="block_absolute_evaluation_figure_file",
                                options=log_file_options,
                                value=log_file_default,
                                clearable=False,
                            ),
                        ],
                    ),
                    html.Hr(),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="block_relative_evaluation_figure",
                            ),
                            dcc.Dropdown(
                                id="block_relative_evaluation_figure_file",
                                options=log_file_options,
                                value=log_file_default,
                                clearable=False,
                            ),
                        ],
                    ),
                    html.Hr(),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="block_absolute_states_figure",
                            ),
                            dcc.Dropdown(
                                id="block_absolute_states_figure_file",
                                options=log_file_options,
                                value=log_file_default,
                                clearable=False,
                            ),
                        ],
                    ),
                    html.Hr(),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="block_relative_states_figure",
                            ),
                            dcc.Dropdown(
                                id="block_relative_states_figure_file",
                                options=log_file_options,
                                value=log_file_default,
                                clearable=False,
                            ),
                        ],
                    ),
                    html.Hr(),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="tx_lag_figure",
                            ),
                            dcc.Dropdown(
                                id="tx_lag_figure_file",
                                options=log_file_options,
                                value=log_file_default,
                                clearable=False,
                            ),
                        ],
                    ),
                ],
            ),
        ]), width={"size": 8, "offset": 2}),
    )

server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    url_base_pathname="/app/",
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
app.layout = serve_layout

@app.callback(
    Output("block_append_figure", "figure"),
    Input("block_append_figure_file", "value"),
)
def update_block_append_figure(file: str):
    return graph.get_block_append_figure(file)

@app.callback(
    Output("block_lag_figure", "figure"),
    Input("block_lag_figure_file", "value"),
)
def update_block_lag_figure(file: str):
    return graph.get_block_lag_figure(file)

@app.callback(
    Output("block_absolute_evaluation_figure", "figure"),
    Input("block_absolute_evaluation_figure_file", "value"),
)
def update_block_absolute_evaluation_figure(file: str):
    return graph.get_block_absolute_evaluation_figure(file)

@app.callback(
    Output("block_relative_evaluation_figure", "figure"),
    Input("block_relative_evaluation_figure_file", "value"),
)
def update_block_relative_evaluation_figure(file: str):
    return graph.get_block_relative_evaluation_figure(file)

@app.callback(
    Output("block_absolute_states_figure", "figure"),
    Input("block_absolute_states_figure_file", "value"),
)
def update_block_absolute_states_figure(file: str):
    return graph.get_block_absolute_states_figure(file)

@app.callback(
    Output("block_relative_states_figure", "figure"),
    Input("block_relative_states_figure_file", "value"),
)
def update_block_relative_states_figure(file: str):
    return graph.get_block_relative_states_figure(file)

@app.callback(
    Output("tx_lag_figure", "figure"),
    Input("tx_lag_figure_file", "value"),
)
def update_tx_lag_figure(file: str):
    return graph.get_tx_lag_figure(file)

@server.route("/app/")
def index():
    return app.index()

if __name__ == '__main__':
    app.run_server(debug=True)
