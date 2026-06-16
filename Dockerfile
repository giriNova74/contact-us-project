# stage 1 build stage
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt

RUN pip install -r requirements.txt -t /app/site-packages

COPY . . 
# stage 2 runtime stage
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

COPY --from=builder /app /app

ENV PYTHONPATH=/app/site-packages

CMD ["python","app.py"]