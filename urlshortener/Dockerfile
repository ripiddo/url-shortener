FROM python:3.8
ENV PYTHONBUFFERED 1
WORKDIR /urlshortener
ENV FLASK_APP=urlshortener:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG 1
ENV FLASK_ENV=development
COPY requirements.txt /urlshortener/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
