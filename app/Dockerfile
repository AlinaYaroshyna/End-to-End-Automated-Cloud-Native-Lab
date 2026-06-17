# --- Stage 1: builder ---
FROM python:3.12-slim AS builder

WORKDIR /build

COPY requirements.txt .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# --- Stage 2: final image ---
FROM python:3.12-slim

WORKDIR /app

# Skopiuj gotowy virtualenv z buildera (bez pip cache, bez build-essential)
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY main.py .

# Nie uruchamiaj jako root - i nadaj appuserowi prawa do venv oraz katalogu app
RUN useradd --create-home --shell /bin/bash appuser \
    && chown -R appuser:appuser /opt/venv /app
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "main:app"]
