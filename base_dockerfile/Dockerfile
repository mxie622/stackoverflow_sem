FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3

RUN apt-get install python3-pip -y

RUN apt-get install -y procps

RUN apt-get install -y -qq curl

RUN curl -o /usr/local/bin/jq https://stedolan.github.io/jq/download/linux64/jq && chmod +x /usr/local/bin/jq


RUN python3 -V

RUN python3 -m pip install virtualenv

RUN virtualenv -p python3 /env


ENV VIRTUAL_ENV /env

#ENV PATH /env/bin:$PATH


ENV SRC_DIR .

ENV ROOT_DIR /home/stackoverflow_sem

ENV PACKAGES_DIR ${ROOT_DIR}/packages

ENV BUILD_DIR ${ROOT_DIR}/app

ENV BASH_DIR ${ROOT_DIR}/bash


RUN mkdir ${ROOT_DIR}

RUN mkdir ${BUILD_DIR}

RUN mkdir ${BASH_DIR}


COPY ${SRC_DIR}/requirements.txt ${BUILD_DIR}
# copy all the files under the local "app" directory to bash directory
COPY ${SRC_DIR}/app ${BUILD_DIR}
COPY ${SRC_DIR}/bash ${BASH_DIR}

# grant execute permission to all files copied to bash directory
RUN chmod a+x ${BASH_DIR}/*.sh || true


WORKDIR ${ROOT_DIR}


RUN pip install --upgrade pip

RUN pip install -r ${BUILD_DIR}/requirements.txt
