FROM python:3.7.3-alpine

ENTRYPOINT [ "/bin/sh", "-c" ]

ADD fizzbuzz.py /code/fizzbuzz.py
WORKDIR /code
CMD [ "exec python fizzbuzz.py" ]
