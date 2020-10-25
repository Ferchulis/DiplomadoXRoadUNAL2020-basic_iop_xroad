FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY ./movilidad_si/requirements.txt /code
COPY ./movilidad_si/docker-entrypoint.sh /code
RUN pip install -r requirements.txt
COPY ./movilidad_si /code
ENTRYPOINT [ "sh", "/code/docker-entrypoint.sh" ]
