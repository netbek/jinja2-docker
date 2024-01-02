FROM python:3.12.1-alpine3.19

RUN pip install --no-cache-dir Jinja2==3.1.2

COPY ./app /app

ENTRYPOINT ["python", "./app/render.py"]
