FROM quoinedev/python3.6-pandas-alpine:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
