from app import app_dashboard  # Corrige a importação para 'app_dashboard'

if __name__ == '__main__':
    app_dashboard.app.run_server(debug=True)  # Inicia o servidor da aplicação Dash
