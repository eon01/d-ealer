FROM python:2.7
ADD ./d-ealer.py /
ADD ./requirements.txt /
ADD ./d-ealer.conf /
RUN pip install -r requirements.txt
WORKDIR /
ENTRYPOINT python d-ealer.py
