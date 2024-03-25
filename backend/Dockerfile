FROM python:3.12
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "queries.py"]

ENV FLASK_APP queries.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT
ENV FLASK_RUN_HOST

EXPOSE

CMD ['flask', "run"]

