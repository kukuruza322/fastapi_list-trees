FROM python:3.10

EXPOSE 8000
WORKDIR /img

COPY requirements.txt ./
RUN pip install -r ./requirements.txt
COPY . .

CMD ["gunicorn", "app:app", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--workers", "4"]