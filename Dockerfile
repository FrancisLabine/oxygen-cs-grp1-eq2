# Stage 1: Build Stage
FROM python:3.9 as builder

WORKDIR /app

COPY /app/requirements.txt .

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .

# Stage 2: Runtime Stage
FROM python:3.9-alpine

# Install the MySQL client package
RUN apk update && apk add --no-cache mariadb-connector-c-dev

WORKDIR /app

COPY --from=builder /app .

CMD ["python", "src/main.py"]
