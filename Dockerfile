FROM docker.repos.balad.ir/python:3.10.0

WORKDIR /src/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "manage.py"]