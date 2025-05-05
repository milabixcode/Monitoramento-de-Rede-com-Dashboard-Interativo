from flask import Flask
from dash import Dash

# Inicializa o Flask
server = Flask(__name__)

# Inicializa o Dash e vincula ao Flask
app = Dash(__name__, server=server)

# Importa o layout e callbacks do novo arquivo de dashboard
from app import app_dashboard  # Renomeado para evitar conflito
