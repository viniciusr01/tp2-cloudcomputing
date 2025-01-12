FROM python:3.9-slim-bullseye

WORKDIR /ml_rules

COPY requirements.txt ml_rules/requirements.txt
RUN pip3 install -r ml_rules/requirements.txt

COPY ml_code_music.py ml_rules/ml_code_music.py


CMD ["python", "./ml_rules/ml_code_music.py"]