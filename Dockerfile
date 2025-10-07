FROM python:3.8-slim

# Arbeitsverzeichnis setzen
WORKDIR /webapp

# Systempakete installieren (zum Kompilieren und für torch etc.)
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Requirements kopieren & installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: Modell direkt ins Image laden (kein Internet nötig beim Start)
RUN python - <<'PY'
from huggingface_hub import snapshot_download
snapshot_download("distilgpt2", local_dir="/models/distilgpt2", local_dir_use_symlinks=False)
print("Model cached at /models/distilgpt2")
PY

# App-Code kopieren
COPY . /webapp

# Port öffnen
EXPOSE 8000

# App starten
CMD ["python", "app.py"]
