# Stage 1: Build Stage
FROM python:3.9 as builder

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Runtime Stage
FROM python:3.9-alpine

# Install the MySQL client package
RUN apk update && apk add --no-cache mariadb-connector-c-dev

WORKDIR /src

COPY --from=builder /src .

CMD ["python", "main.py"]
