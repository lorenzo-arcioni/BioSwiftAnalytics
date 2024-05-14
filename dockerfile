FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip && \
    apt-get clean && \
    useradd -ms /bin/bash jupyter && \
    mkdir /home/jupyter/results && \
    mkdir /home/jupyter/data && \
    mkdir /home/jupyter/notebooks

COPY ./notebooks/*.ipynb /home/jupyter/notebooks/
COPY requirements.txt /home/jupyter

RUN pip3 install jupyter && pip3 install -r /home/jupyter/requirements.txt

USER jupyter
WORKDIR /home/jupyter

EXPOSE 8888                                           
ENTRYPOINT ["jupyter", "notebook","--allow-root","--ip='*'","--port=8888","--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]
