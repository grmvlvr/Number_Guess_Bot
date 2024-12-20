FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TELEGRAM_TOKEN=8193378867:AAFMyclzhCUZq_2gSXDMK7Hc94wnEDxwNF8
CMD ["python", "main.py"]
