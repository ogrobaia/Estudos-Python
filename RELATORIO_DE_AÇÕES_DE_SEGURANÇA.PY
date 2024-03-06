# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv("PLANILHA.csv")


# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# 2 Visualizar a base de dados => utilizando DISPLAY a tabela vem mais organizada 

df = df.drop(columns= "Carimbo de data/hora")
df = df.drop(columns= "Qual seria a Data?")
df = df.drop(columns= "TURNO")


# App layout
app.layout = html.Div([
    html.Div(className='row', children='RELATÓRIO DE AÇÕES DE SEGURANÇA',
             style={'textAlign': 'center', 'color': 'red', 'fontSize': 50}),

    html.Div(className='row', children=[
        dcc.RadioItems(options=['Cassificação' , 'A qual Loja pertence?'],
                       value='Cassificação',
                       inline=True,
                       id='my-radio-buttons-final')
    ]),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'), page_size=20, style_table={'overflowX': 'auto'})
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(figure={}, id='histo-chart-final')
        ])
    ])
])

# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='A qual Loja pertence?', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)