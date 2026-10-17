FROM python:3.14
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    TEST=${TEST}

COPY /src .
CMD ["python", "main.py"]