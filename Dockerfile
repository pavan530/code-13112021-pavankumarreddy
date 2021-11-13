FROM python:3.7.0-slim

RUN mkdir projects

WORKDIR /projects/
COPY ./src projects/
COPY ./input projects/
COPY ./test projects/

ENV PYTHONPATH="/projects"
RUN pip install -r requirements.txt
CMD ["python3","bmicalculator.py"]
