FROM node:8-stretch

# https://github.com/maxcnunes/waitforit/releases/download/v2.2.0/waitforit-linux_amd64
ADD bin/waitforit-linux_amd64 /waitforit 
RUN chmod +x /waitforit

RUN apt-get update \
    && apt-get install -y --no-install-recommends mysql-client mysql-utilities jq \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g https://github.com/dsvictor94/postgrator-cli/archive/v0.3.1.tar.gz mysql@2.15.0

ADD postgrator.json /

ADD bin/loaddata.sh /loaddata
RUN chmod +x /loaddata

CMD postgrator