FROM python3:latest
LABEL Name=project Version=0.0.1 

RUN apt-get update && \
    apt-get install -y git \
     build-essential \
     libpq-dev \
     libxml2-dev \
     libxslt1-dev \
     zlib1g-dev \
     libtiff5-dev \
     libjpeg62-turbo-dev \
     libfreetype6-dev

COPY requirements.txt /var/www/

RUN pip install -r /var/www/requirements.txt
RUN groupadd -g 1000 -r user && useradd -r -g user -u 1000 user
WORKDIR /var/www
USER user
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi"]
