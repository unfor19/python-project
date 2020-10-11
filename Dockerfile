FROM python:3.8.2-slim

WORKDIR /code/
COPY . .
RUN python setup.py install
CMD ["appy"]
