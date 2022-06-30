from dash import html, dcc
import dash_bootstrap_components as dbc

def address__input(text):
    return html.Div([
        dbc.Label(f"{text}", html_for=f"direccion-{text}__input"),
        dbc.Col([
            dbc.Input(
                id=f"direccion-{text}__input",
                type="text",
                placeholder=f"dirección de {text}"
            ),
        ], width=12)
    ])

sidebar = dbc.Card([
    html.Div(
        [
            address__input("origen"),
        ]),
    html.Div(
        [
            address__input("destino"),
        ]),
    
    html.Div(
        [
        html.Br(),
        html.P('Range Slider', style={
            'textAlign': 'center'
        }),
        dcc.RangeSlider(
            id='range_slider',
            min=0,
            max=20,
            step=0.5,
            value=[5, 15]
        ),
        ]
    ),
    html.Div(
        [
            dbc.Card(
                [dbc.Checklist(
                    id='check_list',
                    options=[{
                        'label': 'Value One',
                        'value': 'value1'
                    },
                        {
                            'label': 'Value Two',
                            'value': 'value2'
                        },
                        {
                            'label': 'Value Three',
                            'value': 'value3'
                        }
                    ],
                    )
                 ]),
        ]
    ),
    html.Div(
        [
            dbc.Button("Estimar", outline=True, color="primary", className="me-1")
        ]),
    
],body=True, style={"font_color":"white"}
)