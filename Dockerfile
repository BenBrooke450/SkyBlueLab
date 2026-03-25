FROM python:3.9-slim

WORKDIR /app

# 1. Install the light-weight CPU version of Torch first
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# 2. Copy and install the rest of your requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy your project files
COPY . .

COPY SkyBlueLab_Page .
EXPOSE 8080
CMD ["streamlit", "run", "SkyBlueLab_Page/app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]