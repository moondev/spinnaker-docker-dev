FROM nginx:latest

RUN apt-get update

RUN apt-get install -y build-essential

RUN apt-get install  curl -y

RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -

RUN apt-get install -y nodejs

RUN apt-get install -y git

RUN apt-get install -y nginx 

RUN service nginx stop

RUN rm /etc/nginx/nginx.conf

COPY ./nginx.conf /etc/nginx/nginx.conf

