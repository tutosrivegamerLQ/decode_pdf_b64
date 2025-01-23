FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 4155

CMD ["sh", "-c", "gunicorn -w 4 -b 0.0.0.0:${PORT:-4155} app:app"]
