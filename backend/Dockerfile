FROM python:3.10

RUN mkdir app
WORKDIR /app/src

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
CMD [“python”, “./INIT_DB.py”] 