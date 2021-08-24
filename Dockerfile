FROM python:3

WORKDIR /app

COPY ./app .

COPY app.py app.py

RUN pip install -r requirements.txt

RUN flask

EXPOSE 5000

ENTRYPOINT [ "python"]

CMD [ "app.py" ]