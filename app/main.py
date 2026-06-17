import os
import socket

from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "dev")


@app.get("/")
def index():
    """Podstawowy endpoint - przydatny do szybkiego sprawdzenia, że serwis żyje."""
    return jsonify(
        {
            "message": "Hello from the cloud-native lab microservice!",
            "version": APP_VERSION,
            "hostname": socket.gethostname(),
        }
    )


@app.get("/health")
def health():
    """Endpoint pod liveness/readiness probe w Kubernetesie.

    Zwraca 200, jeśli proces żyje i jest w stanie obsłużyć ruch.
    W realnym serwisie tu dorzuciłbyś sprawdzenie np. połączenia z bazą danych.
    """
    return jsonify({"status": "healthy"}), 200


@app.get("/info")
def info():
    """Dodatkowe metadane - pomocne przy demonstrowaniu rolling update / load balancing."""
    return jsonify(
        {
            "hostname": socket.gethostname(),
            "version": APP_VERSION,
            "pod_name": os.environ.get("POD_NAME", "n/a"),
        }
    )


if __name__ == "__main__":
    # Tryb deweloperski - lokalne uruchomienie bez Dockera/Gunicorna
    app.run(host="0.0.0.0", port=5000, debug=True)
