# Monitoramento de Rede com Dashboard Interativo

Este projeto implementa um **dashboard interativo** para monitoramento de métricas de rede, incluindo **latência**, **jitter** e **throughput**. Ele utiliza o **Dash** para exibição visual e o **Speedtest-cli** para medir a velocidade da conexão. A cada 5 segundos, os gráficos são atualizados com as últimas medições, permitindo monitoramento em tempo real da qualidade da rede.

## Funcionalidades

- **Latência (ms):** Medição do tempo de resposta da rede usando ping para o servidor 8.8.8.8 (Google DNS).
- **Jitter (ms):** Medição da variação de latência calculada como desvio padrão das medições de ping.
- **Throughput (Mbps):** Medição da velocidade de download da conexão usando speedtest-cli.

### Tecnologias Usadas

- **Dash:** Framework para construção de aplicações web interativas.
- **Plotly:** Biblioteca para criação de gráficos interativos.
- **Speedtest-cli:** Biblioteca para medir o throughput da conexão de internet.
- **Python (3.x):** Linguagem de programação utilizada.
- **Threading:** Para coleta paralela de métricas de rede.

---

## Pré-requisitos

Para executar o projeto, você precisa de:

- **Python 3.x** instalado no seu sistema.
- Conexão com a internet (para realizar as medições de throughput).
- Permissões para executar comandos ping (geralmente requer privilégios de root/sudo).

---

## Como Iniciar

### 1. Clonando o Repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/gabrielm2001/dashboard-rede.git
cd dashboard-rede
```

### 2. Instalando as Dependências

Antes de rodar o projeto, você precisa instalar as dependências listadas no `requirements.txt`. Para isso, execute:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `app/`: Diretório principal do aplicativo
  - `app_dashboard.py`: Implementação do dashboard Dash
  - `metrics.py`: Funções para medição de métricas de rede
  - `util.py`: Utilitários para medição de tempo de execução
- `run.py`: Script principal para iniciar o servidor

## Rodando o Servidor

Depois de instalar as dependências, você pode iniciar o servidor para visualizar o dashboard:

```bash
python run.py
```

O Dash estará rodando no endereço [http://127.0.0.1:8050/](http://127.0.0.1:8050/). Abra esse link no seu navegador para visualizar o dashboard.

## Como Funciona

### Coleta de Dados
O projeto coleta periodicamente (a cada 5 segundos) os dados de latência, jitter e throughput usando threads separadas para:
- Medição de latência e jitter via ping
- Medição de throughput via speedtest-cli

### Gráficos Dinâmicos
O Dash exibe três gráficos interativos:

- **Latência**: Exibe o tempo de resposta da rede em milissegundos.
- **Jitter**: Exibe a variação da latência em milissegundos.
- **Throughput**: Exibe a velocidade de download da rede em Mbps.

### Atualizações em Tempo Real
Os gráficos são atualizados a cada 5 segundos, com os últimos dados coletados. As medições são realizadas em paralelo para melhor performance.

## Como Funcionar em Caso de Erros

Se ocorrer algum erro durante a execução, como a falha de conexão ao servidor de medição de velocidade (Speedtest), o programa pode retornar valores padrão (`0` ou valores aproximados). Se isso acontecer, verifique:

- Sua conexão com a internet.
- O acesso ao servidor de Speedtest.
- A instalação das dependências.
- Permissões para executar comandos ping.

## Contribuições

Se você quiser contribuir para o projeto, fique à vontade para enviar pull requests. Não se esqueça de seguir as diretrizes de contribuição e garantir que o código esteja bem documentado.

## Licença

Este projeto está licenciado sob a Licença MIT.

## Autor(es)

**Gabriel Machado** – Desenvolvimento e implementação do projeto.

**Camila Ferrari** – Desenvolvimento e implementação do projeto.

## Configuração Avançada

O projeto permite algumas personalizações através do código fonte:

### Intervalo de Medição
- O intervalo padrão é de 5 segundos
- Para alterar, modifique o valor em `app_dashboard.py`:
  ```python
  dcc.Interval(id='interval-component', interval=5000, n_intervals=0)
  ```

### Servidor de Ping
- O servidor padrão é o 8.8.8.8 (Google DNS)
- Para alterar, modifique em `metrics.py`:
  ```python
  def medir_latencia(host="8.8.8.8", n=5):
  ```

### Número de Tentativas de Ping
- O padrão é 5 tentativas
- Para alterar, modifique em `metrics.py`:
  ```python
  def medir_latencia(host="8.8.8.8", n=5):
  ```

## Limitações Conhecidas

1. **Tempo de Medição**
   - As medições de throughput podem levar alguns segundos para completar
   - Durante este período, o gráfico de throughput pode não atualizar

2. **Impacto na Rede**
   - As medições de throughput consomem banda da sua conexão
   - Recomenda-se não executar o monitoramento em redes com banda limitada

3. **Requisitos de Sistema**
   - O projeto consome recursos de CPU e memória durante as medições
   - Recomenda-se pelo menos 1GB de RAM disponível
   - Processador com suporte a múltiplos threads para melhor performance

4. **Precisão das Medições**
   - A latência pode variar dependendo da carga do servidor de ping
   - O throughput pode variar dependendo do servidor speedtest selecionado

## Exemplos de Uso

### Interpretação dos Gráficos

1. **Latência**
   - Valores abaixo de 100ms: Excelente
   - Valores entre 100-200ms: Bom
   - Valores acima de 200ms: Pode indicar problemas

2. **Jitter**
   - Valores abaixo de 30ms: Excelente
   - Valores entre 30-50ms: Aceitável
   - Valores acima de 50ms: Pode causar problemas em chamadas VoIP

3. **Throughput**
   - Compare com a velocidade contratada do seu plano
   - Variações bruscas podem indicar problemas na rede

### Casos de Uso Comuns

1. **Monitoramento de Qualidade**
   - Identificar horários de pico de latência
   - Detectar quedas de velocidade
   - Monitorar estabilidade da conexão

2. **Solução de Problemas**
   - Verificar se problemas de conexão são constantes ou intermitentes
   - Identificar padrões de degradação da rede
   - Validar a qualidade da conexão após mudanças na infraestrutura

3. **Análise de Performance**
   - Comparar diferentes provedores de internet
   - Avaliar a qualidade da rede em diferentes locais
   - Verificar o impacto de aplicações na rede