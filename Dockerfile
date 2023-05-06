FROM python:3.10.2-slim

# criar usuário python com arquivos /bin/bash
RUN useradd -ms /bin/bash python

# definindo usuário
USER python

# ambiente de desenvolvimento
WORKDIR /home/python/app

# variavel de ambiente para python
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

CMD [ "tail", "-f", "/dev/null"]