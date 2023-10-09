FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y python3.9 \
    python3-pip  \
    openssh-client
 
RUN useradd -ms /bin/bash jupyter

COPY ./* /home/jupyter/

RUN pip3 install JPype1 jupyter
RUN pip3 install -r /home/jupyter/requirements.txt

USER jupyter
WORKDIR home/jupyter

EXPOSE 8888                                           
ENTRYPOINT ["jupyter", "notebook","--allow-root","--ip=0.0.0.0","--port=8888","--no-browser"]
