FROM python:3

COPY ./app .

COPY . .

RUN pip install -r requirements.txt

RUN flask

EXPOSE 5000

ENTRYPOINT [ "python"]

CMD [ "app.py" ]