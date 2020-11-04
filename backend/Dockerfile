FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY
ENV DJANGO_SETTINGS_MODULE=backend.settings.prod

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
