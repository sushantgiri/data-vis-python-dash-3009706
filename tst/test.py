import dash
from dash import Input, Output, dcc, html
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
from statsmodels.graphics.gofplots import qqplot
from scipy import stats


# Read the data set
data = pd.read_csv('heart.csv')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
sidebar = html.Div(
    [
        html.H2("Heart Disease Predication", className="display-8"),

        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
                dbc.NavLink("Data Preparation and Analysis", href="/data", active="exact"),
                dbc.NavLink("Model Implementation", href="/model", active="exact"),
                dbc.NavLink("Toolkit", href="/toolkit", active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
# List of categorical columns
categorical_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']
# List of numerical columns
numerical_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'target']


@app.callback(
    Output('graph1', 'figure'),
    [Input(component_id='numerical_columns', component_property='value')]
)
def draw_graph1(value):
    if value is None:
        return {}
    else:
        fig = px.box(data, y=value, title='Box Plot')
        return fig


@app.callback(
    Output('qq_plot', 'figure'),
    [Input(component_id='numerical_columns', component_property='value')]
)
def draw_qq_plot(value):
    if value is None:
        return {}
    else:
        qq = stats.probplot(data[value], dist='lognorm', sparams=(1))
        x = np.array([qq[0][0][0], qq[0][0][-1]])

        fig = go.Figure()
        fig.add_scatter(x=qq[0][0], y=qq[0][1], mode='markers')
        fig.add_scatter(x=x, y=qq[1][1] + qq[1][0] * x, mode='lines')
        fig.layout.update(showlegend=False)
        return fig


@app.callback(
    Output('categorical_histogram', 'figure'),
    [Input(component_id='categorical_columns', component_property='value')]
)
def draw_categorical_histogram(value):
    if value is None:
        return {}
    else:
        fig = px.histogram(data, x=value, title='Histogram')
        return fig


@app.callback(
    Output('histogram_plot', 'figure'),
    [Input(component_id='numerical_columns', component_property='value')]
)
def draw_histogram_plot(value):
    if value is None:
        return {}
    else:
        fig = px.histogram(data, x=value, title='Histogram')
        return fig


@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='categorical_columns', component_property='value')]
)
def draw_graph(value):
    if value is None:
        return {}
    else:
        labels = []
        if value == 'sex':
            labels = ['Female', 'Male']
        elif value == "cp":
            labels = ['Type 0', 'Type 2', 'Type 1', 'Type 3']
        elif value == "fbs":
            labels = ['< 120 mg/dl', '> 120 mg/dl']
        elif value == "restecg":
            labels = ['1', '0', '2']
        elif value == "exang":
            labels = ['False', 'True']
        elif value == "slope":
            labels = ['2', '1', '0']
        elif value == "ca":
            labels = ['0', '1', '2', '3', '4']
        elif value == "thal":
            labels = ['2', '3', '1', '0']
        elif value == "target":
            labels = ['True', 'False']

    fig = px.pie(data, names=value, title="Pie chart")
    return fig

    # # histogram_trace = go.Histogram(x=data['age'], name='age', marker=dict(color='darkcyan'))
    # pie_trace = go.Pie(labels=labels, values=list(data[value].value_counts()))
    # layout = go.Layout(
    #     title=value,
    #     xaxis=dict(domain=[0.0, 0.3]),
    #     xaxis2=dict(domain=[1.0, 1]),
    # )
    # fig = go.Figure(data=go.Data([pie_trace]), layout=layout)
    # return fig


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dashboard" or pathname == "/":
        return html.Div(
            id="app-container",
            children=(
                html.Div(
                    id="graph-container",
                    children=(
                        html.Div(
                            id="root_container",
                            children=[
                                dbc.Row([

                                    dbc.Col([
                                        html.Div(
                                            id="graph_container",
                                            children=[
                                                dcc.Graph(id='graph'),
                                            ],

                                        ),
                                    ]),

                                    dbc.Col([
                                        html.Div(
                                            id="categorical_histogram",
                                            children=[
                                                dcc.Graph(id='categorical_histogram'),
                                            ],

                                        ),
                                    ]),

                                ]),

                            ]),
                        html.Div(
                            id="categoricalID",
                            children=(
                                'Categorical Columns',
                                dcc.Dropdown(categorical_columns, id="categorical_columns", value='sex')
                            )
                        ),
                        html.Div(
                            id="root_container1",
                            children=[
                                dbc.Row([
                                    dbc.Col([
                                        html.Div(
                                            dcc.Graph(id='graph1'),
                                        )
                                    ]),
                                    dbc.Col([
                                        html.Div(
                                            dcc.Graph(id='qq_plot'),
                                        )
                                    ]),
                                    dbc.Col([
                                        html.Div(
                                            dcc.Graph(id='histogram_plot'),
                                        )
                                    ]),

                                ]),
                            ]),
                        html.Div(
                            id="numericalID",
                            children=('Numerical Columns', dcc.Dropdown(numerical_columns, id="numerical_columns", value='age'), ))
                    )
                )
            )
        )
    elif pathname == "/data":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/model":
        return html.P("Oh cool, this is page 2!")
    elif pathname == "/toolkit":
        return html.P("Oh cool, this is page 3!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8888)
