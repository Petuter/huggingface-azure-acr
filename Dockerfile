FROM python:3.8

WORKDIR /webapp

COPY ./requirements.txt /webapp/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY webapp/* /webapp

EXPOSE 8000

# Starte das Gradio-Interface auf Port 8000
CMD ["python", "app.py"]

