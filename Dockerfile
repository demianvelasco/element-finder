FROM python:3.7-slim-buster
WORKDIR /cmd
ADD ./requirements.txt /cmd/requirements.txt
RUN pip install -r requirements.txt
ADD . /cmd
ENTRYPOINT [ "python3", "cmd.py"]