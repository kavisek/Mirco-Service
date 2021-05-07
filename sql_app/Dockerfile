FROM python:3.8-alpine


RUN apk add build-base postgresql-dev gcc python3-dev musl-dev

COPY . /app

EXPOSE 80

RUN pip install -r ./app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]