FROM python:3.9-slim

WORKDIR /app

# 1. Install Torch
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# 2. Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy your project files (This handles EVERYTHING)
COPY . .

EXPOSE 8080

# Note the path to app.py here stays the same
CMD ["streamlit", "run", "SkyBlueLab_Page/app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]