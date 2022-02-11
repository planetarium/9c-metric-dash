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

def serve_layout():
    log_dir_options = option.get_log_dir_options()
    log_dir_default = log_dir_options[0]["value"]

    return html.Div(
        dbc.Col(html.Div(children=[
            html.H1(children='Nine Chronicles Metric Logger Dash'),
            dcc.Dropdown(
                id="dir",
                options=log_dir_options,
                value=log_dir_default,
                clearable=False,
            ),
            dcc.Tabs(
                id="tab",
                value="network",
                children=[
                    dcc.Tab(label="Network", value="network"),
                    dcc.Tab(label="Performance", value="performance"),
                ]
            ),
            html.Div(id="tab_layout"),
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
    Output("tab_layout", "children"),
    Input("dir", "value"),
    Input("tab", "value"),
)
def update_tab_layout(log_dir: str, tab: str):
    log_file_options = option.get_log_file_options(log_dir)
    log_file_default = log_file_options[0]["value"]
    block_evaluation_duration_options = option.get_block_evaluation_duration_options()
    block_evaluation_duration_default = block_evaluation_duration_options[0]["value"]
    block_states_update_duration_options = option.get_block_states_update_duration_options()
    block_states_update_duration_default = block_states_update_duration_options[0]["value"]
    find_hashes_options = option.get_find_hashes_options()
    find_hashes_default = find_hashes_options[0]["value"]
    block_render_duration_options = option.get_block_render_duration_options()
    block_render_duration_default = block_render_duration_options[0]["value"]

    if tab == "network":
        return html.Div(
            children=[
                html.H2("Network"),
                html.Div(
                    children=[
                        dcc.Graph(
                            id="block_append_figure",
                        ),
                        dcc.Dropdown(
                            id="block_append_file",
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
                            id="block_lag_file",
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
                            id="tx_lag_file",
                            options=log_file_options,
                            value=log_file_default,
                            clearable=False,
                        ),
                    ],
                ),
            ],
        )
    elif tab == "performance":
        return html.Div(
            children=[
                html.H2("Performance"),
                html.Div(
                    children=[
                        dcc.Graph(
                            id="block_evaluation_duration_figure",
                        ),
                        dcc.Dropdown(
                            id="block_evaluation_duration_file",
                            options=log_file_options,
                            value=log_file_default,
                            clearable=False,
                        ),
                        dcc.Dropdown(
                            id="block_evaluation_duration_option",
                            options=block_evaluation_duration_options,
                            value=block_evaluation_duration_default,
                            clearable=False,
                        )
                    ],
                ),
                html.Hr(),
                html.Div(
                    children=[
                        dcc.Graph(
                            id="block_states_update_duration_figure",
                        ),
                        dcc.Dropdown(
                            id="block_states_update_duration_file",
                            options=log_file_options,
                            value=log_file_default,
                            clearable=False,
                        ),
                        dcc.Dropdown(
                            id="block_states_update_duration_option",
                            options=block_states_update_duration_options,
                            value=block_states_update_duration_default,
                            clearable=False,
                        )
                    ],
                ),
                html.Hr(),
                html.Div(
                    children=[
                        dcc.Graph(
                            id="find_hashes_figure",
                        ),
                        dcc.Dropdown(
                            id="find_hashes_file",
                            options=log_file_options,
                            value=log_file_default,
                            clearable=False,
                        ),
                        dcc.Dropdown(
                            id="find_hashes_option",
                            options=find_hashes_options,
                            value=find_hashes_default,
                            clearable=False,
                        ),
                    ],
                ),
                html.Hr(),
                html.Div(
                    children=[
                        dcc.Graph(
                            id="block_render_duration_figure",
                        ),
                        dcc.Dropdown(
                            id="block_render_duration_file",
                            options=log_file_options,
                            value=log_file_default,
                            clearable=False,
                        ),
                        dcc.Dropdown(
                            id="block_render_duration_option",
                            options=block_render_duration_options,
                            value=block_render_duration_default,
                            clearable=False,
                        ),
                    ],
                ),
            ],
        )
    else:
        raise ValueError("invalid argument")

@app.callback(
    Output("block_append_figure", "figure"),
    Input("block_append_file", "value"),
)
def update_block_append_figure(file: str):
    return graph.get_block_append_figure(file)

@app.callback(
    Output("block_lag_figure", "figure"),
    Input("block_lag_file", "value"),
)
def update_block_lag_figure(file: str):
    return graph.get_block_lag_figure(file)

@app.callback(
    Output("block_evaluation_duration_figure", "figure"),
    Input("block_evaluation_duration_file", "value"),
    Input("block_evaluation_duration_option", "value"),
)
def update_block_evaluation_duration_figure(file: str, selection: str):
    return graph.get_block_evaluation_duration_figure(file, selection)

@app.callback(
    Output("block_states_update_duration_figure", "figure"),
    Input("block_states_update_duration_file", "value"),
    Input("block_states_update_duration_option", "value"),
)
def update_block_states_update_duration_figure(file: str, selection: str):
    return graph.get_block_states_update_duration_figure(file, selection)

@app.callback(
    Output("tx_lag_figure", "figure"),
    Input("tx_lag_file", "value"),
)
def update_tx_lag_figure(file: str):
    return graph.get_tx_lag_figure(file)

@app.callback(
    Output("find_hashes_figure", "figure"),
    Input("find_hashes_file", "value"),
    Input("find_hashes_option", "value"),
)
def update_find_hashes_figure(file: str, selection: str):
    return graph.get_find_hashes_figure(file, selection)

@app.callback(
    Output("block_render_duration_figure", "figure"),
    Input("block_render_duration_file", "value"),
    Input("block_render_duration_option", "value"),
)
def update_block_render_duration_figure(file: str, selection: str):
    return graph.get_block_render_duration_figure(file, selection)

@server.route("/")
def index():
    return app.index()

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=80, debug=True)
