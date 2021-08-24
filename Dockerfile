#syntax=docker/dockerfile:1

FROM python:3
WORKDIR /app

COPY ./app .

COPY app.py app.py
RUN pip install -r requirements.txt
RUN flask
#COPY . .

EXPOSE 5000

#CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD ["flak.py"]


ENTRYPOINT [ "python"]

CMD [ "app.py" ]