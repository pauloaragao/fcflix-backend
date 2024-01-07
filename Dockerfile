FROM python:3.10.2-slim


RUN apt update && apt install -y --no-install-recommends \
        default-jre \
        git

# criar usuário python com arquivos /bin/bash
RUN useradd -ms /bin/bash python

# definindo usuário
USER python

# ambiente de desenvolvimento
WORKDIR /home/python/app

# variavel de ambiente para python
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

CMD [ "tail", "-f", "/dev/null"]