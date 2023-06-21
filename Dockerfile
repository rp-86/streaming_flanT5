FROM <base-image>

WORKDIR /app

expose 8080

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server/ .

CMD ["python", "server.py"]
