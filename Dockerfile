FROM alpine

ENV SERVER_ENVIRONMENT DEVELOPMENT
ENV SITE_FOLDER /etc/sites/mysite/

RUN apk add --update --no-cache libssl1.0 libxml2 libxslt ca-certificates
RUN apk add --update --no-cache python3 jpeg py-psycopg2 py-lxml py-flask py-pillow py-openssl py-cffi

RUN apk add --update --no-cache build-base make python3-dev jpeg-dev zlib-dev libffi-dev openssl-dev libxml2-dev libxslt-dev && \
    pip3 install lxml && \
    pip3 install --no-cache-dir lxml dateutils requests requests-oauthlib mailer pillow gocardless paypalrestsdk pytz nose2 test_utils oauthlib flask flask-login pymysql misaka slimit minify cssmin && \
    apk del --purge build-base make bzr python3-dev jpeg-dev zlib-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

#docker build -t olymk2/scaffold .
#docker run -d --name=scaffold --restart=always olymk2/scaffold 
