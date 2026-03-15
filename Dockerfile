FROM python:3.11-slim
WORKDIR /app
# Copy your requirements first for faster building
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy everything else
COPY . .
# Streamlit usually runs on 8501, but we tell Scaleway to use 8080
EXPOSE 8080
CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]