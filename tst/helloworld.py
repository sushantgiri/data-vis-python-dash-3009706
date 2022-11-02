import dash
from dash import html, dcc, Input, Output
from dash import dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dashboard":
        return html.Div(
            id="app-container",
            children=(
                html.Div(
                    id="graph-container",
                    children=(
                        html.Div(
                            id="root_container",
                            children=[

                                html.Div(
                                    id="graph_container",
                                    children=[
                                        dcc.Graph(id='graph'),
                                    ],

                                ),
                            ]),

                        html.Div(
                            id="categoricalID",
                            children=(
                                'Categorical Columns',
                                dcc.Dropdown(categorical_columns, id="categorical_columns")
                            )
                        ),

                        html.Div(
                            id="numericalID",
                            children=('Numerical Columns', dcc.Dropdown(numerical_columns, id="numerical_columns")))

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


import dash_bootstrap_components as dbc
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


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




# Read the data set
data = pd.read_csv('heart.csv')

pie_figure = go.Figure(data=[go.Pie(labels=['Female', 'Male'], values=list(data['sex'].value_counts()))])
pie_figure.update_layout(title="Sex (Gender) Distribution")

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Side bar style
side_bar_style = {
    "position": "fixed",x
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#233D4D",
}

side_bar_item_style = {
    "background": "none"
}

card_style = {
    "width": "24 rem",
    "height": "24 rem"
}
content_style = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#000000",

}

app.title = "Heart Disease Prediction"

# List of categorical columns
categorical_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']
# List of numerical columns
numerical_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'target']

side_bar = html.Div(
    [

        dbc.Nav(
            [
                dbc.Row(id="dashboard_row", children=[
                    dbc.NavLink('Dashboard', href='/', active="exact", style=side_bar_item_style),
                ]),

                dbc.Row(id="data_preparation", children=[
                    dbc.NavLink('Data Preparation and Analysis', href='/data', active="exact",
                                style=side_bar_item_style),
                ]),

                dbc.Row(id="model_implementation", children=[
                    dbc.NavLink('Model Implementation', href='/model', active="exact", style=side_bar_item_style),
                ]),

                dbc.Row(id="toolkit", children=[
                    dbc.NavLink('Toolkit', href='/toolkit', active="exact", style=side_bar_item_style)
                ])

            ],
            vertical=True,
            pills=True,
        )
    ], style=side_bar_style
)

content_section = html.Div(
    id="page_content", style=content_style
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/dashboard":
        return html.Div(
            id="app-container",
            children=(
                html.Div(
                    id="graph-container",
                    children=(
                        html.Div(
                            id="root_container",
                            children=[

                                html.Div(
                                    id="graph_container",
                                    children=[
                                        dcc.Graph(id='graph'),
                                    ],

                                ),
                            ]),

                        html.Div(
                            id="categoricalID",
                            children=(
                                'Categorical Columns',
                                dcc.Dropdown(categorical_columns, id="categorical_columns")
                            )
                        ),

                        html.Div(
                            id="numericalID",
                            children=('Numerical Columns', dcc.Dropdown(numerical_columns, id="numerical_columns")))

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


# content_section = html.Div(
#     id="page_content",
#     style=content_style,
#     children=(
#         html.Div(
#             id="graph-container",
#             children=(
#                 html.Div(
#                     id="graph_container",
#                     children=(
#                         dcc.Graph(id='graph'),
#                     ),
#                     style={'display': 'inline-block'}
#                 ),
#
#                 html.Div(
#                     id="categoricalID",
#                     children=(
#                         'Categorical Columns',
#                         dcc.Dropdown(categorical_columns, id="categorical_columns")
#                     )
#                 ),
#
#                 html.Div(
#                     id="numericalID",
#                     children=('Numerical Columns', dcc.Dropdown(numerical_columns, id="numerical_columns")))
#
#             ), style={'display': 'inline-block'}
#         )
#
#     )
#
# )

app.layout = html.Div([dcc.Location(id='url'), side_bar, content_section])


# app.layout = html.Div(
#     id="app-container",
#     children=(
#         html.Div(
#             id="graph-container",
#             children=(
#                 html.Div(
#                     id="graph_container",
#                     children=(
#                         dcc.Graph(id='graph'),
#                     ),
#                     style={'display': 'inline-block'}
#                 ),
#
#
#
#                 html.Div(
#                     id="categoricalID",
#                     children=(
#                         'Categorical Columns',
#                         dcc.Dropdown(categorical_columns, id="categorical_columns")
#                     )
#                 ),
#
#                 html.Div(
#                     id="numericalID",
#                     children=('Numerical Columns', dcc.Dropdown(numerical_columns, id="numerical_columns")))
#
#             ), style={'display': 'inline-block'}
#         )
#
#     )
#
# )


@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='categorical_columns', component_property='value')]
)
def draw_graph(value):
    if value is None:
        return {}
        # return go.Figure(data=[go.Pie(labels=['Female', 'Male'],
        #                               values=list(data['sex'].value_counts()))])
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

    histogram_trace = go.Histogram(x=data['age'], name='age', marker=dict(color='darkcyan'))
    pie_trace = go.Pie(labels=labels, values=list(data[value].value_counts()))
    layout = go.Layout(
        title=value
    )

    fig = go.Figure(data=go.Data([histogram_trace, pie_trace]), layout=layout)
    return fig
    # fig = go.Figure()
    #
    # female_trace = go.Histogram(histfunc="count", name="Female", xaxis=data[value].unique(),
    #                                     yaxis=data[value].value_counts())
    # fig.add_trace(female_trace)
    # return fig
    # fig = go.Figure()
    # pie_object = go.Pie(labels=labels,
    #                     values=list(data[value].value_counts()))
    # fig.add_trace(pie_object)
    # return fig


if __name__ == "__main__":
    app.run_server(debug=True)
