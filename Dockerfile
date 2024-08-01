FROM python:3.12-slim

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

RUN pip install dagster-webserver dagster-postgres dagster-aws

COPY main.py workspace.yaml requirements.txt /opt/dagster/app/
COPY helper/* /opt/dagster/app/helper/

ENV DAGSTER_HOME=/opt/dagster/dagster_home/

COPY dagster.yaml /opt/dagster/dagster_home/

RUN pip install dagster-webserver dagster-postgres dagster-aws \
    && pip install -r /opt/dagster/app/requirements.txt

WORKDIR /opt/dagster/app

EXPOSE 3000

ENTRYPOINT ["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]