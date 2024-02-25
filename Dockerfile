FROM python:3.10

WORKDIR /app

COPY . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 4545

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4545"]
