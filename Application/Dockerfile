FROM ubuntu:16.04
LABEL maintainer="Azure App Service Container Images <devops sysmoon@sk.com>"

#RUN apt-get update && apt-get install -y python-pip python-dev && apt-get clean && pip install --upgrade pip
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev mysql-client libmariadbclient-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
RUN python3 /code/perfectcushion/manage.py makemigrations
RUN python3 /code/perfectcushion/manage.py migrate
RUN python3 /code/perfectcushion/manage.py collectstatic --no-input
	
EXPOSE 8000 2222
#CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python3", "/code/perfectcushion/manage.py", "runserver", "0.0.0.0:8000"]
