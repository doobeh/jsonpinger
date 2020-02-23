FROM python:3.8.1

WORKDIR /usr/src/jsonping
COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "python", "./pinger.py" ]