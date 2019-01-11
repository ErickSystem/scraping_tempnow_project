FROM 116550303471.dkr.ecr.us-east-1.amazonaws.com/docker-image-web-python

ENV APP_DIR=/app

WORKDIR $APP_DIR

COPY id_rsa requirements.txt ./

RUN export PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1 && \
    export CFLAGS="-fPIC" && \
    apk add --no-cache --virtual .fetch-deps alpine-sdk freetds-dev libc-dev linux-headers && \
    apk add --update --no-cache freetds && \
    chmod 600 id_rsa && \
    eval $(ssh-agent) && \
    echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
    ssh-add id_rsa && \
    pip install --no-build-isolation --no-cache-dir -r requirements.txt && \
    rm -f id_rsa && \
    apk del .fetch-deps

COPY src .