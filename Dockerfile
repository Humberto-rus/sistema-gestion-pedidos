FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# No copiamos el código aquí — viene montado como volumen en docker-compose.
CMD ["bash"]