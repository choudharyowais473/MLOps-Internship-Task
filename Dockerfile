FROM python:3.9-slim
WORKDIR /app
COPY run.py metrics.json data.csv  requirements.txt config.yaml ./
RUN pip install -r requirements.txt
CMD ["python", "run.py", "--input", "data.csv", "--config", "config.yaml", "--output", "metrics.json", "--log-file", "run.log"]