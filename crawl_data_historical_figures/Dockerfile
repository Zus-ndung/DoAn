FROM python:latest

RUN pip install Scrapy

COPY ./src /usr/src/app

VOLUME [ "/usr/src/app"]

WORKDIR /usr/src/app/data_semantic_web/data_semantic_web

CMD [ "scrapy", "crawl", "quotes"]
