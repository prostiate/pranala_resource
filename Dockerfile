FROM python:3.8
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD . /
CMD [ "python", "./main.py", "pranala", "--help" ]