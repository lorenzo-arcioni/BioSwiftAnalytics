FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y python3.9 python3-pip && \
    apt-get clean
 
RUN useradd -ms /bin/bash jupyter && \
    mkdir /home/jupyter/results && \
    mkdir /home/jupyter/data && \
    mkdir /home/jupyter/notebooks

COPY ./*.ipynb /home/jupyter/notebooks/
COPY requirements.txt /home/jupyter

RUN pip3 install jupyter && pip3 install -r /home/jupyter/requirements.txt

USER jupyter
WORKDIR home/jupyter

EXPOSE 8888                                           
ENTRYPOINT ["jupyter", "notebook","--allow-root","--ip='*'","--port=8888","--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]
