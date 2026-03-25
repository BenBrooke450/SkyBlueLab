FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY SkyBlueLab_Page .
EXPOSE 8080
CMD ["streamlit", "run", "SkyBlueLab_Page/app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]