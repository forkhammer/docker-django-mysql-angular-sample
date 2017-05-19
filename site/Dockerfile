FROM python:3.5
LABEL Name=project Version=0.0.1 

COPY requirements.txt /var/www/

RUN apt-get update && \
    apt-get install -y --no-install-recommends git \
     build-essential \
     libpq-dev \
     libxml2-dev \
     libxslt1-dev \
     zlib1g-dev \
     libtiff5-dev \
     libjpeg62-turbo-dev \
     libfreetype6-dev && \
     pip install -r /var/www/requirements.txt && \
     apt-get autoremove -y && \
     apt-get clean
     
RUN groupadd -g 1000 -r user && useradd -r -g user -u 1000 user
WORKDIR /var/www
USER user
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi"]
