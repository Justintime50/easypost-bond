FROM python:3.7

COPY ./setup.py /withbond/setup.py
COPY ./README.md /withbond/README.md
COPY ./withbond /withbond/withbond
COPY ./app.py /withbond/app.py

WORKDIR /withbond

RUN python setup.py install

CMD [ "python", "app.py" ]