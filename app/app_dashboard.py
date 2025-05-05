from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import threading
import time
from . import metrics, util  # A importação relativa ajuda a localizar o módulo na mesma pasta

# Criando a aplicação Dash
app = Dash(__name__)

# Armazena os dados coletados
time_data = [0]
latencia_data = [None]
jitter_data = [None]
throughput_data = [None]

# Função para coletar dados periodicamente
def atualizar_dados():
    start_of_measurement = time.time()
    while True:
        latencia = jitter = throughput = None

        def lat():
            with util.measure("latencia"):
                nonlocal latencia, jitter
                latencia, jitter = metrics.medir_latencia()  # Função que retorna latência e jitter
        
        def th():
            with util.measure("throughput"):
                nonlocal throughput
                throughput = metrics.medir_throughput()  # Função que retorna throughput

        t1 = threading.Thread(target=lat)
        t2 = threading.Thread(target=th)

        t1.start()
        t2.start()

        while True:
            time.sleep(5)
            time_data.append(time.time() - start_of_measurement)
            if t1.is_alive() or t2.is_alive():
                latencia_data.append(latencia_data[-1])
                jitter_data.append(jitter_data[-1])
                throughput_data.append(throughput_data[-1])
            else:
                latencia_data.append(latencia)
                jitter_data.append(jitter)
                throughput_data.append(throughput)
                break

# Inicia a coleta em uma thread separada
threading.Thread(target=atualizar_dados, daemon=True).start()

# Layout do Dashboard
app.layout = html.Div(children=[
    html.H1("Monitoramento de Rede"),

    dcc.Graph(id='grafico-latencia'),
    dcc.Graph(id='grafico-jitter'),
    dcc.Graph(id='grafico-throughput'),

    dcc.Interval(id='interval-component', interval=5000, n_intervals=0)  # Atualiza a cada 5s
])

# Callback para atualizar os gráficos dinamicamente
@app.callback(
    [Output('grafico-latencia', 'figure'),
     Output('grafico-jitter', 'figure'),
     Output('grafico-throughput', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def atualizar_graficos(n):
    # Criação das figuras com os dados coletados
    latencia_fig = go.Figure(data=[go.Scatter(x=time_data, y=latencia_data, mode='lines+markers', connectgaps=True, name="Latência (ms)")])
    jitter_fig = go.Figure(data=[go.Scatter(x=time_data, y=jitter_data, mode='lines+markers', connectgaps=True, name="Jitter (ms)")])
    throughput_fig = go.Figure(data=[go.Scatter(x=time_data, y=throughput_data, mode='lines+markers', connectgaps=True, name="Velocidade (Mbps)")])
    
    # Atualiza as figuras com títulos e eixos
    latencia_fig.update_layout(title='Latência ao longo do tempo', xaxis_title='Tempo (s)', yaxis_title='Latência (ms)')
    jitter_fig.update_layout(title='Jitter ao longo do tempo', xaxis_title='Tempo (s)', yaxis_title='Jitter (ms)')
    throughput_fig.update_layout(title='Throughput ao longo do tempo', xaxis_title='Tempo (s)', yaxis_title='Velocidade (Mbps)')

    return latencia_fig, jitter_fig, throughput_fig

if __name__ == '__main__':
    app.run_server(debug=True)
