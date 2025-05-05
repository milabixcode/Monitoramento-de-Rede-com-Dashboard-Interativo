import time
import statistics
import speedtest
import subprocess

def medir_latencia(host="8.8.8.8", n=5):
    latencias = []
    for _ in range(n):
        start = time.time()
        subprocess.run(["ping", "-c", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end = time.time()
        latencias.append((end - start) * 1000)  # Convertendo para ms
    return statistics.mean(latencias), statistics.stdev(latencias)  # Média e jitter

def medir_throughput():
    st = speedtest.Speedtest()
    st.config['length']['download'] = 3

    st.get_best_server()
    return st.download() / 1_000_000  # Mbps
