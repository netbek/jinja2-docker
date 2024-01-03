FROM python:3.12.1-alpine3.19

RUN apk add nodejs npm
RUN pip install --no-cache-dir Jinja2==3.1.2
RUN npm install --global prettier@3.1.1

COPY ./app /app
WORKDIR /app
ENTRYPOINT ["python", "render.py"]
