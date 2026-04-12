FROM python:3.9-slim
WORKDIR /app


RUN apt-get update && apt-get install -y \
    openjdk-21-jre-headless \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

ENV PYTHONPATH=/app
EXPOSE 8080

CMD ["streamlit", "run", "SkyBlueLab_Page/app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]