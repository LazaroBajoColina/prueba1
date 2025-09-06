import dash
from dash import dcc, html, Input, Output, callback_context
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots  
import numpy as np

# Tabla periodica completa 
periodic_table_data = {
    1: {'name': 'Hidrógeno', 'symbol': 'H', 'group': 'No Metal', 'row': 1, 'col': 1}, 2: {'name': 'Helio', 'symbol': 'He', 'group': 'Gas Noble', 'row': 1, 'col': 18}, 3: {'name': 'Litio', 'symbol': 'Li', 'group': 'Metal Alcalino', 'row': 2, 'col': 1}, 4: {'name': 'Berilio', 'symbol': 'Be', 'group': 'Metal Alcalinotérreo', 'row': 2, 'col': 2}, 5: {'name': 'Boro', 'symbol': 'B', 'group': 'Metaloide', 'row': 2, 'col': 13}, 6: {'name': 'Carbono', 'symbol': 'C', 'group': 'No Metal', 'row': 2, 'col': 14}, 7: {'name': 'Nitrógeno', 'symbol': 'N', 'group': 'No Metal', 'row': 2, 'col': 15}, 8: {'name': 'Oxígeno', 'symbol': 'O', 'group': 'No Metal', 'row': 2, 'col': 16}, 9: {'name': 'Flúor', 'symbol': 'F', 'group': 'Halógeno', 'row': 2, 'col': 17}, 10: {'name': 'Neón', 'symbol': 'Ne', 'group': 'Gas Noble', 'row': 2, 'col': 18}, 11: {'name': 'Sodio', 'symbol': 'Na', 'group': 'Metal Alcalino', 'row': 3, 'col': 1}, 12: {'name': 'Magnesio', 'symbol': 'Mg', 'group': 'Metal Alcalinotérreo', 'row': 3, 'col': 2}, 13: {'name': 'Aluminio', 'symbol': 'Al', 'group': 'Otro Metal', 'row': 3, 'col': 13}, 14: {'name': 'Silicio', 'symbol': 'Si', 'group': 'Metaloide', 'row': 3, 'col': 14}, 15: {'name': 'Fósforo', 'symbol': 'P', 'group': 'No Metal', 'row': 3, 'col': 15}, 16: {'name': 'Azufre', 'symbol': 'S', 'group': 'No Metal', 'row': 3, 'col': 16}, 17: {'name': 'Cloro', 'symbol': 'Cl', 'group': 'Halógeno', 'row': 3, 'col': 17}, 18: {'name': 'Argón', 'symbol': 'Ar', 'group': 'Gas Noble', 'row': 3, 'col': 18}, 19: {'name': 'Potasio', 'symbol': 'K', 'group': 'Metal Alcalino', 'row': 4, 'col': 1}, 20: {'name': 'Calcio', 'symbol': 'Ca', 'group': 'Metal Alcalinotérreo', 'row': 4, 'col': 2}, 21: {'name': 'Escandio', 'symbol': 'Sc', 'group': 'Metal de Transición', 'row': 4, 'col': 3}, 22: {'name': 'Titanio', 'symbol': 'Ti', 'group': 'Metal de Transición', 'row': 4, 'col': 4}, 23: {'name': 'Vanadio', 'symbol': 'V', 'group': 'Metal de Transición', 'row': 4, 'col': 5}, 24: {'name': 'Cromo', 'symbol': 'Cr', 'group': 'Metal de Transición', 'row': 4, 'col': 6}, 25: {'name': 'Manganeso', 'symbol': 'Mn', 'group': 'Metal de Transición', 'row': 4, 'col': 7}, 26: {'name': 'Hierro', 'symbol': 'Fe', 'group': 'Metal de Transición', 'row': 4, 'col': 8}, 27: {'name': 'Cobalto', 'symbol': 'Co', 'group': 'Metal de Transición', 'row': 4, 'col': 9}, 28: {'name': 'Níquel', 'symbol': 'Ni', 'group': 'Metal de Transición', 'row': 4, 'col': 10}, 29: {'name': 'Cobre', 'symbol': 'Cu', 'group': 'Metal de Transición', 'row': 4, 'col': 11}, 30: {'name': 'Zinc', 'symbol': 'Zn', 'group': 'Metal de Transición', 'row': 4, 'col': 12}, 31: {'name': 'Galio', 'symbol': 'Ga', 'group': 'Otro Metal', 'row': 4, 'col': 13}, 32: {'name': 'Germanio', 'symbol': 'Ge', 'group': 'Metaloide', 'row': 4, 'col': 14}, 33: {'name': 'Arsénico', 'symbol': 'As', 'group': 'Metaloide', 'row': 4, 'col': 15}, 34: {'name': 'Selenio', 'symbol': 'Se', 'group': 'No Metal', 'row': 4, 'col': 16}, 35: {'name': 'Bromo', 'symbol': 'Br', 'group': 'Halógeno', 'row': 4, 'col': 17}, 36: {'name': 'Kriptón', 'symbol': 'Kr', 'group': 'Gas Noble', 'row': 4, 'col': 18}, 37: {'name': 'Rubidio', 'symbol': 'Rb', 'group': 'Metal Alcalino', 'row': 5, 'col': 1}, 38: {'name': 'Estroncio', 'symbol': 'Sr', 'group': 'Metal Alcalinotérreo', 'row': 5, 'col': 2}, 39: {'name': 'Itrio', 'symbol': 'Y', 'group': 'Metal de Transición', 'row': 5, 'col': 3}, 40: {'name': 'Zirconio', 'symbol': 'Zr', 'group': 'Metal de Transición', 'row': 5, 'col': 4}, 41: {'name': 'Niobio', 'symbol': 'Nb', 'group': 'Metal de Transición', 'row': 5, 'col': 5}, 42: {'name': 'Molibdeno', 'symbol': 'Mo', 'group': 'Metal de Transición', 'row': 5, 'col': 6}, 43: {'name': 'Tecnecio', 'symbol': 'Tc', 'group': 'Metal de Transición', 'row': 5, 'col': 7}, 44: {'name': 'Rutenio', 'symbol': 'Ru', 'group': 'Metal de Transición', 'row': 5, 'col': 8}, 45: {'name': 'Rodio', 'symbol': 'Rh', 'group': 'Metal de Transición', 'row': 5, 'col': 9}, 46: {'name': 'Paladio', 'symbol': 'Pd', 'group': 'Metal de Transición', 'row': 5, 'col': 10}, 47: {'name': 'Plata', 'symbol': 'Ag', 'group': 'Metal de Transición', 'row': 5, 'col': 11}, 48: {'name': 'Cadmio', 'symbol': 'Cd', 'group': 'Metal de Transición', 'row': 5, 'col': 12}, 49: {'name': 'Indio', 'symbol': 'In', 'group': 'Otro Metal', 'row': 5, 'col': 13}, 50: {'name': 'Estaño', 'symbol': 'Sn', 'group': 'Otro Metal', 'row': 5, 'col': 14}, 51: {'name': 'Antimonio', 'symbol': 'Sb', 'group': 'Metaloide', 'row': 5, 'col': 15}, 52: {'name': 'Telurio', 'symbol': 'Te', 'group': 'Metaloide', 'row': 5, 'col': 16}, 53: {'name': 'Yodo', 'symbol': 'I', 'group': 'Halógeno', 'row': 5, 'col': 17}, 54: {'name': 'Xenón', 'symbol': 'Xe', 'group': 'Gas Noble', 'row': 5, 'col': 18}, 55: {'name': 'Cesio', 'symbol': 'Cs', 'group': 'Metal Alcalino', 'row': 6, 'col': 1}, 56: {'name': 'Bario', 'symbol': 'Ba', 'group': 'Metal Alcalinotérreo', 'row': 6, 'col': 2}, 57: {'name': 'Lantano', 'symbol': 'La', 'group': 'Lantánido', 'row': 8, 'col': 3}, 58: {'name': 'Cerio', 'symbol': 'Ce', 'group': 'Lantánido', 'row': 8, 'col': 4}, 59: {'name': 'Praseodimio', 'symbol': 'Pr', 'group': 'Lantánido', 'row': 8, 'col': 5}, 60: {'name': 'Neodimio', 'symbol': 'Nd', 'group': 'Lantánido', 'row': 8, 'col': 6}, 61: {'name': 'Prometio', 'symbol': 'Pm', 'group': 'Lantánido', 'row': 8, 'col': 7}, 62: {'name': 'Samario', 'symbol': 'Sm', 'group': 'Lantánido', 'row': 8, 'col': 8}, 63: {'name': 'Europio', 'symbol': 'Eu', 'group': 'Lantánido', 'row': 8, 'col': 9}, 64: {'name': 'Gadolinio', 'symbol': 'Gd', 'group': 'Lantánido', 'row': 8, 'col': 10}, 65: {'name': 'Terbio', 'symbol': 'Tb', 'group': 'Lantánido', 'row': 8, 'col': 11}, 66: {'name': 'Disprosio', 'symbol': 'Dy', 'group': 'Lantánido', 'row': 8, 'col': 12}, 67: {'name': 'Holmio', 'symbol': 'Ho', 'group': 'Lantánido', 'row': 8, 'col': 13}, 68: {'name': 'Erbio', 'symbol': 'Er', 'group': 'Lantánido', 'row': 8, 'col': 14}, 69: {'name': 'Tulio', 'symbol': 'Tm', 'group': 'Lantánido', 'row': 8, 'col': 15}, 70: {'name': 'Iterbio', 'symbol': 'Yb', 'group': 'Lantánido', 'row': 8, 'col': 16}, 71: {'name': 'Lutecio', 'symbol': 'Lu', 'group': 'Lantánido', 'row': 8, 'col': 17}, 72: {'name': 'Hafnio', 'symbol': 'Hf', 'group': 'Metal de Transición', 'row': 6, 'col': 4}, 73: {'name': 'Tántalo', 'symbol': 'Ta', 'group': 'Metal de Transición', 'row': 6, 'col': 5}, 74: {'name': 'Wolframio', 'symbol': 'W', 'group': 'Metal de Transición', 'row': 6, 'col': 6}, 75: {'name': 'Renio', 'symbol': 'Re', 'group': 'Metal de Transición', 'row': 6, 'col': 7}, 76: {'name': 'Osmio', 'symbol': 'Os', 'group': 'Metal de Transición', 'row': 6, 'col': 8}, 77: {'name': 'Iridio', 'symbol': 'Ir', 'group': 'Metal de Transición', 'row': 6, 'col': 9}, 78: {'name': 'Platino', 'symbol': 'Pt', 'group': 'Metal de Transición', 'row': 6, 'col': 10}, 79: {'name': 'Oro', 'symbol': 'Au', 'group': 'Metal de Transición', 'row': 6, 'col': 11}, 80: {'name': 'Mercurio', 'symbol': 'Hg', 'group': 'Metal de Transición', 'row': 6, 'col': 12}, 81: {'name': 'Talio', 'symbol': 'Tl', 'group': 'Otro Metal', 'row': 6, 'col': 13}, 82: {'name': 'Plomo', 'symbol': 'Pb', 'group': 'Otro Metal', 'row': 6, 'col': 14}, 83: {'name': 'Bismuto', 'symbol': 'Bi', 'group': 'Otro Metal', 'row': 6, 'col': 15}, 84: {'name': 'Polonio', 'symbol': 'Po', 'group': 'Metaloide', 'row': 6, 'col': 16}, 85: {'name': 'Astato', 'symbol': 'At', 'group': 'Metaloide', 'row': 6, 'col': 17}, 86: {'name': 'Radón', 'symbol': 'Rn', 'group': 'Gas Noble', 'row': 6, 'col': 18}, 87: {'name': 'Francio', 'symbol': 'Fr', 'group': 'Metal Alcalino', 'row': 7, 'col': 1}, 88: {'name': 'Radio', 'symbol': 'Ra', 'group': 'Metal Alcalinotérreo', 'row': 7, 'col': 2}, 89: {'name': 'Actinio', 'symbol': 'Ac', 'group': 'Actínido', 'row': 9, 'col': 3}, 90: {'name': 'Torio', 'symbol': 'Th', 'group': 'Actínido', 'row': 9, 'col': 4}, 91: {'name': 'Protactinio', 'symbol': 'Pa', 'group': 'Actínido', 'row': 9, 'col': 5}, 92: {'name': 'Uranio', 'symbol': 'U', 'group': 'Actínido', 'row': 9, 'col': 6}, 93: {'name': 'Neptunio', 'symbol': 'Np', 'group': 'Actínido', 'row': 9, 'col': 7}, 94: {'name': 'Plutonio', 'symbol': 'Pu', 'group': 'Actínido', 'row': 9, 'col': 8}, 95: {'name': 'Americio', 'symbol': 'Am', 'group': 'Actínido', 'row': 9, 'col': 9}, 96: {'name': 'Curio', 'symbol': 'Cm', 'group': 'Actínido', 'row': 9, 'col': 10}, 97: {'name': 'Berkelio', 'symbol': 'Bk', 'group': 'Actínido', 'row': 9, 'col': 11}, 98: {'name': 'Californio', 'symbol': 'Cf', 'group': 'Actínido', 'row': 9, 'col': 12}, 99: {'name': 'Einstenio', 'symbol': 'Es', 'group': 'Actínido', 'row': 9, 'col': 13}, 100: {'name': 'Fermio', 'symbol': 'Fm', 'group': 'Actínido', 'row': 9, 'col': 14}, 101: {'name': 'Mendelevio', 'symbol': 'Md', 'group': 'Actínido', 'row': 9, 'col': 15}, 102: {'name': 'Nobelio', 'symbol': 'No', 'group': 'Actínido', 'row': 9, 'col': 16}, 103: {'name': 'Lawrencio', 'symbol': 'Lr', 'group': 'Actínido', 'row': 9, 'col': 17}, 104: {'name': 'Rutherfordio', 'symbol': 'Rf', 'group': 'Metal de Transición', 'row': 7, 'col': 4}, 105: {'name': 'Dubnio', 'symbol': 'Db', 'group': 'Metal de Transición', 'row': 7, 'col': 5}, 106: {'name': 'Seaborgio', 'symbol': 'Sg', 'group': 'Metal de Transición', 'row': 7, 'col': 6}, 107: {'name': 'Bohrio', 'symbol': 'Bh', 'group': 'Metal de Transición', 'row': 7, 'col': 7}, 108: {'name': 'Hasio', 'symbol': 'Hs', 'group': 'Metal de Transición', 'row': 7, 'col': 8}, 109: {'name': 'Meitnerio', 'symbol': 'Mt', 'group': 'Metal de Transición', 'row': 7, 'col': 9}, 110: {'name': 'Darmstatio', 'symbol': 'Ds', 'group': 'Metal de Transición', 'row': 7, 'col': 10}, 111: {'name': 'Roentgenio', 'symbol': 'Rg', 'group': 'Metal de Transición', 'row': 7, 'col': 11}, 112: {'name': 'Copernicio', 'symbol': 'Cn', 'group': 'Metal de Transición', 'row': 7, 'col': 12}, 113: {'name': 'Nihonio', 'symbol': 'Nh', 'group': 'Otro Metal', 'row': 7, 'col': 13}, 114: {'name': 'Flerovio', 'symbol': 'Fl', 'group': 'Otro Metal', 'row': 7, 'col': 14}, 115: {'name': 'Moscovio', 'symbol': 'Mc', 'group': 'Otro Metal', 'row': 7, 'col': 15}, 116: {'name': 'Livermorio', 'symbol': 'Lv', 'group': 'Otro Metal', 'row': 7, 'col': 16}, 117: {'name': 'Teneso', 'symbol': 'Ts', 'group': 'Halógeno', 'row': 7, 'col': 17}, 118: {'name': 'Oganesón', 'symbol': 'Og', 'group': 'Gas Noble', 'row': 7, 'col': 18},
}

group_colors = { 'No Metal': '#a1c4fd', 'Gas Noble': '#ffb3ba', 'Metal Alcalino': '#ffdfba', 'Metal Alcalinotérreo': '#ffffba', 'Metaloide': '#baffc9', 'Halógeno': '#bae1ff', 'Otro Metal': '#f1cbff', 'Metal de Transición': '#ffb38a', 'Lantánido': '#d2baff', 'Actínido': '#ffbaf2' }

# --- Funciones Helper
def create_periodic_table():
    grid_style = { 'display': 'grid', 'gridTemplateColumns': 'repeat(18, 50px)', 'gridTemplateRows': 'repeat(10, 50px)', 'gap': '3px' }
    elements_divs = []
    for num, data in periodic_table_data.items():
        element_style = { 'gridRow': str(data['row']), 'gridColumn': str(data['col']), 'backgroundColor': group_colors.get(data['group'], '#e0e0e0'), 'border': '1px solid black', 'borderRadius': '4px', 'padding': '2px', 'fontSize': '10px', 'fontWeight': 'bold', 'textAlign': 'center', 'cursor': 'pointer', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center', 'height': '50px' }
        elements_divs.append( html.Button([f"{num}", html.Span(data['symbol'], style={'fontSize': '14px'})], id={'type': 'element-button', 'index': num}, title=data['name'], style=element_style) )
    bottom_headers = [html.Div(f"{i}", style={'gridRow': '8', 'gridColumn': f"{i}", 'fontWeight': 'bold', 'textAlign': 'center', 'paddingTop': '10px'}) for i in range(1, 19)]
    return html.Div(children=elements_divs + bottom_headers, style=grid_style)

# --- Funciones Helper

def create_ionic_bond_figure():
    fig = go.Figure()
    # Atomos a  Iones
    fig.add_trace(go.Scatter(x=[-2, 2], y=[0, 0], mode='markers+text', marker=dict(color=['#ffdfba', '#a1c4fd'], size=[30, 35]), text=['Na', 'Cl'], textposition='middle center', textfont=dict(size=14, color='black')))
    fig.add_trace(go.Scatter(x=[6, 10], y=[0, 0], mode='markers+text', marker=dict(color=['#ffb38a', '#ffb3ba'], size=[25, 40]), text=['Na⁺', 'Cl⁻'], textposition='middle center', textfont=dict(size=14, color='black')))
    # Tranferencias electrones
    fig.add_annotation(ax=-1.5, ay=0.5, x=1.5, y=0.5, showarrow=True, arrowhead=2, arrowwidth=2, arrowcolor='black', axref='x', ayref='y', xref='x', yref='y')
    fig.add_annotation(text="e⁻", x=0, y=0.8, showarrow=False)
    fig.add_annotation(text="→", x=4, y=0, showarrow=False, font=dict(size=30))
    fig.update_layout(title_text='Ejemplo: NaCl (Sal de Mesa)', showlegend=False, height=150, margin=dict(l=10, r=10, t=40, b=10))
    fig.update_xaxes(visible=False, range=[-4, 12]); fig.update_yaxes(visible=False, range=[-2, 2])
    return fig

def create_covalent_bond_figure():
    fig = make_subplots(rows=1, cols=2, subplot_titles=("No Polar (H₂)", "Polar (H₂O)"))
    # H2 - No polar
    fig.add_shape(type="circle", x0=-2, y0=-1, x1=0, y1=1, fillcolor='#a1c4fd', opacity=0.5, line_width=0, row=1, col=1)
    fig.add_shape(type="circle", x0=0, y0=-1, x1=2, y1=1, fillcolor='#a1c4fd', opacity=0.5, line_width=0, row=1, col=1)
    fig.add_trace(go.Scatter(x=[-1, 1], y=[0, 0], mode='markers+text', marker_symbol='circle-open', marker=dict(size=10, color='black')), row=1, col=1)
    fig.add_annotation(text="H", x=-1, y=0, showarrow=False, row=1, col=1)
    fig.add_annotation(text="H", x=1, y=0, showarrow=False, row=1, col=1)
    fig.add_annotation(text="e⁻ e⁻", x=0, y=0, showarrow=False, font_color='blue', row=1, col=1)
    # H2O - Polar
    fig.add_trace(go.Scatter(x=[0, -0.8, 0.8], y=[0, 0.8, 0.8], mode='markers+text', marker=dict(color=['#ffb3ba', '#a1c4fd', '#a1c4fd'], size=[40, 25, 25]), text=['O', 'H', 'H']), row=1, col=2)
    fig.add_shape(type="line", x0=0, y0=0, x1=-0.8, y1=0.8, line=dict(color="black", width=2), row=1, col=2)
    fig.add_shape(type="line", x0=0, y0=0, x1=0.8, y1=0.8, line=dict(color="black", width=2), row=1, col=2)
    fig.add_annotation(text="δ⁻", x=0, y=-0.5, showarrow=False, font=dict(color='red', size=20), row=1, col=2)
    fig.add_annotation(text="δ⁺", x=-1, y=1.2, showarrow=False, font=dict(color='blue', size=20), row=1, col=2)
    fig.add_annotation(text="δ⁺", x=1, y=1.2, showarrow=False, font=dict(color='blue', size=20), row=1, col=2)
    fig.update_layout(showlegend=False, height=200, margin=dict(l=10, r=10, t=40, b=10))
    fig.update_xaxes(visible=False); fig.update_yaxes(visible=False)
    return fig

def create_metallic_bond_figure():
    fig = go.Figure()
    ions_x, ions_y = np.meshgrid(np.linspace(-2, 2, 4), np.linspace(-1, 1, 3))
    electrons_x = np.random.uniform(-2.5, 2.5, 15)
    electrons_y = np.random.uniform(-1.5, 1.5, 15)
    fig.add_trace(go.Scatter(x=ions_x.flatten(), y=ions_y.flatten(), mode='markers+text', marker=dict(color='#ffb38a', size=35), text='M⁺', textposition='middle center'))
    fig.add_trace(go.Scatter(x=electrons_x, y=electrons_y, mode='markers+text', marker=dict(color='blue', size=10), text='e⁻'))
    fig.update_layout(title_text="Mar de Electrones Deslocalizados", showlegend=False, height=200, margin=dict(l=10, r=10, t=40, b=10))
    fig.update_xaxes(visible=False); fig.update_yaxes(visible=False)
    return fig


# --- Iniciacion ---
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN], suppress_callback_exceptions=True)
server = app.server

# --- Layout de App ---
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Dashboard Interactivo de Química", className="text-center my-4"))),
    dbc.Tabs([
        dbc.Tab(label="¿Qué es la Química?", children=[
            dbc.Card(dbc.CardBody([ html.H4("Temas Básicos", className="card-title"), html.P([html.B("Materia:"), " Cualquier sustancia con masa que ocupa un lugar en el espacio."]), html.Hr(), html.H5("Clasificación de la Materia"),
                dbc.Row([ dbc.Col([ html.H6("Sustancias Puras", className="text-primary"), html.P("Composición fija. Se descomponen por métodos químicos."), html.Ul([ html.Li([html.B("Elemento:"), " Formado por un solo tipo de átomo."]), html.Li([html.B("Compuesto:"), " Formado por dos o más elementos combinados químicamente."]), ]) ], md=6),
                    dbc.Col([ html.H6("Mezclas", className="text-success"), html.P("Combinación de dos o más sustancias puras. Se separan por métodos físicos."), html.Ul([ html.Li([html.B("Homogénea:"), " Sus componentes no se distinguen a simple vista."]), html.Li([html.B("Heterogénea:"), " Sus componentes se distinguen a simple vista."]), ]) ], md=6) ]) ]), className="my-3"),
            dbc.Card(dbc.CardBody([ html.H4("Sistemas Homogéneos y Heterogéneos", className="card-title"), html.P("Clasificación según el tamaño de partícula del soluto."), html.Label("Tamaño de partícula (nm):"), dcc.Slider(id='particle-size-slider', min=0, max=1001, step=0.1, value=0.5, marks={0.1: '0.1', 1: '1', 100: '100', 1001: '>1000'}), html.Div(id='mixture-type-output', className="text-center lead fw-bold mt-3") ]), className="my-3"), ]),
        dbc.Tab(label="Estructura Atómica", children=[
            dbc.Card(dbc.CardBody([ html.H4("Visualizador de Modelos Atómicos y Spin", className="card-title"), dbc.Row([ dbc.Col([ html.Label("Seleccionar Modelo Atómico"), dcc.Dropdown(id='modelo-atomico-dropdown', options=[{'label': 'Dalton (1809)', 'value': 'dalton'}, {'label': 'Thomson (1904)', 'value': 'thomson'}, {'label': 'Rutherford (1911)', 'value': 'rutherford'}, {'label': 'Bohr (1913)', 'value': 'bohr'}], value='bohr'), dcc.Graph(id='modelo-atomico-graph', config={'displayModeBar': False}) ], md=8), dbc.Col([ html.Label("Spin del Electrón"), dbc.RadioItems(id='spin-radio', options=[{'label': 'Spin +1/2', 'value': 'up'}, {'label': 'Spin -1/2', 'value': 'down'}], value='up'), html.Div(id='spin-visual', className="text-center", style={'fontSize': '200px', 'fontWeight': 'bold', 'marginTop': '20px', 'color': '#3498db'}) ], md=4, align="center") ]) ]), className="my-3"),
            dbc.Card(dbc.CardBody([ html.H4("Principios Fundamentales del Orbital"), dbc.Accordion([ dbc.AccordionItem("Principio de Exclusión de Pauli: Dos electrones del mismo átomo no pueden tener los mismos números cuánticos. Un orbital no puede tener más de dos electrones.", title="Principio de Exclusión de Pauli"), dbc.AccordionItem("Principio de Incertidumbre de Heisenberg: Es imposible determinar simultáneamente y con exactitud la posición y el momento (velocidad) de un electrón.", title="Principio de Incertidumbre de Heisenberg") ], start_collapsed=True) ]), className="my-3"), ]),
        dbc.Tab(label="Tabla Periódica", children=[ dbc.Card(dbc.CardBody([ html.H4("Tabla Periódica Interactiva (118 Elementos)", className="card-title"), html.P("Haz clic en un elemento para ver sus detalles."), dbc.Row([ dbc.Col(create_periodic_table(), md=10), dbc.Col([ html.H5("Detalles del Elemento"), html.Div(id='element-details-output', children=[html.P("Selecciona un elemento.")]) ], md=2, style={'borderLeft': '1px solid #ccc', 'paddingLeft': '15px'}) ], align="start") ]), className="my-3") ]),
        dbc.Tab(label="Enlaces y Propiedades", children=[
            dbc.Card(dbc.CardBody([ html.H4("Clasificador de Enlaces por Electronegatividad", className="card-title"), html.Label("Diferencia de Electronegatividad (ΔEN):"), dcc.Slider(id='enlace-slider', min=0, max=4.0, step=0.1, value=1.9, marks={i: str(i) for i in range(5)}), html.Div(id='enlace-output', className="mt-3") ]), className="my-3"),
            dbc.Card(dbc.CardBody([ html.H4("Definiciones Clave con Ejemplos Visuales"),
                dbc.Accordion([
                    dbc.AccordionItem(title="Enlace Iónico", children=[
                        dbc.Row([
                            dbc.Col(dcc.Graph(figure=create_ionic_bond_figure(), config={'displayModeBar': False}), md=5),
                            dbc.Col(html.P("Transferencia de electrones (típicamente entre metal y no metal), formando iones con carga. La diferencia de electronegatividad es mayor a 1.7. Resultan en compuestos con altos puntos de fusión y son generalmente solubles en agua."), style={'paddingTop': '20px'}),
                        ])
                    ]),
                    dbc.AccordionItem(title="Enlace Covalente", children=[
                        dbc.Row([
                            dbc.Col(dcc.Graph(figure=create_covalent_bond_figure(), config={'displayModeBar': False}), md=5),
                            dbc.Col(html.P("Compartición de electrones entre no metales. Si se comparten equitativamente (ΔEN < 0.5) es No Polar. Si se comparten de forma desigual (ΔEN 0.5-1.7) es Polar, creando cargas parciales (δ⁺, δ⁻). Suelen ser malos conductores."), style={'paddingTop': '20px'}),
                        ])
                    ]),
                    dbc.AccordionItem(title="Enlace Metálico", children=[
                        dbc.Row([
                            dbc.Col(dcc.Graph(figure=create_metallic_bond_figure(), config={'displayModeBar': False}), md=5),
                            dbc.Col(html.P("Se forma una red de cationes metálicos inmersa en un 'mar' de electrones de valencia deslocalizados. Esta estructura explica por qué los metales son buenos conductores de calor y electricidad, dúctiles y maleables."), style={'paddingTop': '20px'}),
                        ])
                    ]),
                    dbc.AccordionItem(title="Electronegatividad, Energía de Ionización y Radio Atómico", children=[
                        html.P("Electronegatividad: Tendencia de un átomo para atraer electrones de otro."),
                        html.P("Energía de Ionización: Energía necesaria para que un átomo libere un electrón y forme un ion positivo."),
                        html.P("Radio Atómico: Distancia entre dos núcleos de dos átomos idénticos enlazados.")
                    ])
                ], start_collapsed=True, always_open=True)
            ]), className="my-3") ]),
        dbc.Tab(label="Nomenclatura y Mol", children=[
            dbc.Card(dbc.CardBody([ html.H4("Simulador de Nomenclatura Inorgánica", className="card-title"), dbc.Row([ dbc.Col(dcc.Dropdown(id='r1-dropdown', options=['Metal', 'No Metal', 'Anhídrido', 'Óxido Metálico'], value='Metal'), md=5), dbc.Col(html.H2("+", className="text-center"), md=2, align="center"), dbc.Col(dcc.Dropdown(id='r2-dropdown', options=['Oxígeno', 'Agua', 'Hidrógeno', 'Hidrácido'], value='Oxígeno'), md=5) ]), html.Div(id='nomenclatura-output', className="text-center lead fw-bold mt-3") ]), className="my-3"),
            dbc.Card(dbc.CardBody([ html.H4("Calculadora de Moles (n = m / MM)", className="card-title"), dbc.Row([ dbc.Col([html.Label("Masa (m) [gr]:"), dcc.Input(id='masa-input', type='number', value=58.44, min=0, className="w-100")]), dbc.Col([html.Label("Peso Molecular (MM) [g/mol]:"), dcc.Input(id='mm-input', type='number', value=58.44, min=0.01, className="w-100")]) ]), html.Div(id='mol-output', className="text-center lead fw-bold mt-3") ]), className="my-3"), ])
    ])
], fluid=True, style={'maxWidth': '1600px'})

# --- Callbacks ---
@app.callback(Output('mixture-type-output', 'children'), Input('particle-size-slider', 'value'))
def update_mixture_type(size):
    if size <= 1: return html.Div(["Tipo: Solución", html.P("Sistema homogéneo. No se sedimenta. Tamaño < 1 nm.", className="small text-muted")])
    elif 1 < size <= 100: return html.Div(["Tipo: Coloide", html.P("Efecto Tyndall. Aspecto lechoso. Tamaño 1-100 nm.", className="small text-muted")])
    else: return html.Div(["Tipo: Suspensión", html.P("Mezcla heterogénea. Las partículas se sedimentan. Tamaño > 100 nm.", className="small text-muted")])

@app.callback(Output('modelo-atomico-graph', 'figure'), Input('modelo-atomico-dropdown', 'value'))
def update_modelo_atomico(modelo):
    fig = go.Figure(); title = ""
    if modelo == 'dalton': fig.add_shape(type="circle", x0=-1, y0=-1, x1=1, y1=1, fillcolor="SaddleBrown"); title = 'Modelo de Dalton: Esfera Sólida Indivisible'
    elif modelo == 'thomson': fig.add_shape(type="circle", x0=-2, y0=-2, x1=2, y1=2, fillcolor="rgba(255, 99, 132, 0.6)"); fig.add_trace(go.Scatter(x=np.random.uniform(-1.6, 1.6, 7), y=np.random.uniform(-1.6, 1.6, 7), mode='markers', marker=dict(color='navy', size=15))); title = 'Modelo de Thomson: "Budín de Pasas"'
    elif modelo == 'rutherford': fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='red', size=25))); fig.add_trace(go.Scatter(x=[-1, 1.5, 0.5], y=[1.5, -0.8, -1.8], mode='markers', marker=dict(color='blue', size=12))); title = 'Modelo de Rutherford: Núcleo Central'
    elif modelo == 'bohr': fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='red', size=25))); [fig.add_shape(type="circle", x0=-r, y0=-r, x1=r, y1=r, line_color="grey", line_dash="dash") for r in [1, 2, 3]]; fig.add_trace(go.Scatter(x=[1, 0, -3], y=[0, 2, 0], mode='markers', marker=dict(color='blue', size=12))); title = 'Modelo de Bohr: Órbitas de Energía'
    fig.update_xaxes(range=[-3.8, 3.8], visible=False); fig.update_yaxes(range=[-3.8, 3.8], visible=False, scaleanchor="x", scaleratio=1); fig.update_layout(height=350, margin=dict(l=10, r=10, t=50, b=10), showlegend=False, title={'text': title, 'x': 0.5}); return fig

@app.callback(Output('spin-visual', 'children'), Input('spin-radio', 'value'))
def update_spin(spin_value): return '↑' if spin_value == 'up' else '↓'

@app.callback(Output('element-details-output', 'children'), Input({'type': 'element-button', 'index': dash.ALL}, 'n_clicks'), prevent_initial_call=True)
def display_element_details(n_clicks):
    if not any(n_clicks): return html.P("Selecciona un elemento.")
    ctx = callback_context; button_id_str = ctx.triggered[0]['prop_id'].split('.')[0]; element_num = int(eval(button_id_str)['index']); element_data = periodic_table_data.get(element_num)
    if element_data: return [ html.H6(f"{element_data['name']} ({element_data['symbol']})", className="text-primary"), html.P(f"Número Atómico: {element_num}"), html.P(f"Grupo: {element_data['group']}"), html.P(f"Período: {element_data['row'] if element_data['row'] <= 7 else 'N/A'}") ]
    return html.P("Datos no encontrados.")

@app.callback(Output('enlace-output', 'children'), Input('enlace-slider', 'value'))
def update_enlace(delta_en):
    if delta_en >= 1.7: return html.Div([html.H5("Enlace Iónico", className="text-danger"), "Transferencia de electrones. Alta diferencia de electronegatividad."])
    elif delta_en >= 0.5: return html.Div([html.H5("Enlace Covalente Polar", className="text-warning"), "Se comparten electrones de forma desigual."])
    else: return html.Div([html.H5("Enlace Covalente No Polar", className="text-success"), "Se comparten electrones de forma equitativa. Mínima diferencia de electronegatividad."])

@app.callback(Output('nomenclatura-output', 'children'), [Input('r1-dropdown', 'value'), Input('r2-dropdown', 'value')])
def update_nomenclatura(r1, r2):
    rules = { ('Metal', 'Oxígeno'): "→ Óxido metálico", ('No Metal', 'Oxígeno'): "→ Óxidos no metálicos (Anhídridos)", ('Metal', 'Agua'): "→ Hidróxido", ('Anhídrido', 'Agua'): "→ Ácidos (Oxácidos)", ('No Metal', 'Hidrógeno'): "→ Hidrácidos", ('Metal', 'Hidrácido'): "→ Sal binaria + H₂", ('Óxido Metálico', 'Hidrácido'): "→ Sal binaria + H₂O" }
    return rules.get((r1, r2), "Combinación no especificada.")

@app.callback(Output('mol-output', 'children'), [Input('masa-input', 'value'), Input('mm-input', 'value')])
def calculate_moles(masa, mm):
    if masa is None or mm is None or mm == 0: return "Valores inválidos."
    return f"Resultado: {masa / mm:.4f} moles (n)"

if __name__ == '__main__':
    app.run(debug=False)
