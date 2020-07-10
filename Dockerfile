FROM python:3.7

COPY ./setup.py /withbond/setup.py
COPY ./README.md /withbond/README.md
COPY ./withbond /withbond/withbond
COPY ./app.py /withbond/app.py

# TODO: This is NOT ideal to copy the .env file in like this, but is simply being used for testing/dev
COPY ./.env /withbond/.env 

WORKDIR /withbond

RUN python setup.py install

CMD [ "python", "app.py" ]
