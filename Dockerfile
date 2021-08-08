FROM ubuntu:latest
WORKDIR /opt/CTF

COPY requirements.txt /opt/CTF/

COPY . /opt/CTF
COPY geckodriver  /opt/CTF/geckodriver
COPY geckodriver.log /opt/CTF/geckodriver.log

RUN chmod 777 /opt/CTF/geckodriver
RUN chmod 777 /opt/CTF/geckodriver.log

#ENV TZ=Europe/Minsk

#CMD ["ln" ,"-snf" ,"/usr/share/zoneinfo/$TZ" ,"/etc/localtime","&&", "echo", "$TZ" ,">", "/etc/timezone"]

ARG DEBIAN_FRONTEND=noninteractive



RUN apt-get update
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
	python3-pip \
        git \
	firefox 

RUN pip3 install -r requirements.txt
#RUN rm /etc/nginx/conf.d/default.conf
COPY http.conf /etc/nginx/conf.d
RUN apt install nginx -y
#RUN systemctl start nginx
EXPOSE 8000

CMD ["chmod", "+x", "/opt/CTF/docker-entrypoint", "&&", "chown", "-R", "1001:1001" ,"/opt/CTF"]

ENTRYPOINT ["/opt/CTF/docker-entrypoint.sh"]


