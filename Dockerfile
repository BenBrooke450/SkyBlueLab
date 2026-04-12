FROM python:3.9-slim
WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

ENV PYTHONPATH=/app
EXPOSE 8080

CMD ["streamlit", "run", "SkyBlueLab_Page/app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]