# SCRAPING DATA SITE TEMPO AGORA https://www.tempoagora.com.br

## SERVICES 

- 1 - tempnow_api_python
- 2 - tempnow_api_nodejs
- 3 - database_docker
- 4 - tempnow_scraping
- 5 - tempnow_analytic


## APPLICATIONS DESCRIPTION

- 1 - API RESTFULL IN PYTHON WITH FLASK
- 2 - API RESTFULL IN NODEJS WITH EXPRESS
- 3 - DATABASE MYSQL 5.7
- 4 - SCRAPING PYTHON WITH THE LIBS: SELENIUM AND BEAUTIFULSOUP4
- 5 - ANALYTIC DATA WITH PANDAS, MATPLOTLIB

## REQUIREMENTS

* Docker e docker compose
* config database mysql
* pyenv
* nodejs and npm
* python3
* chrome

## INSTALL

### Docker

Have docker installed, preferably the version below or higher:

`Docker version 18.06.0-ce, build 0ffa825`

How install: https://docs.docker.com/install/linux/docker-ce/ubuntu/

Configure user root pro docker: https://docs.docker.com/install/linux/linux-postinstall/

Have docker-compose installed, preferably the version below or higher:

`docker-compose version 1.21.2, build a133471`

How install: https://docs.docker.com/compose/install/#install-compose

### SERVICE: 3 - database_docker - LOAD DATA IN DATABASE

```bash
# first container start
docker-compose up -d database

# then run the command below to be able to restore the database - 
# by default, I have already stored the last backup made on 01/11/2019 in the project.
# But you can restore another backup from your local machine or from any server,
# follow the same modeling of this project, using the process described in this session.
docker-compose exec database data.sh
```

#### BACKUP
```bash
# config envs to perform the backup of database wish
export MYSQL_HOST=127.0.0.1
export MYSQL_DATABASE=tempnow

# run the script below. This script will generate #a dump of the local bank 
# (change the endpoint #and credentials if your bank is in another
# location and with other credentials, in the script).
cd build/database_docker/
sh backup_mysql.sh
cd ../../
```

#### KILL CONTAINERS AND BACKUP MYSQL DATABASE INSIDE OF CONTAINER
```bash
docker-compose down
```
## RUN

### SERVICE: 1 -tempnow_api_python e 2 - tempnow_api_nodejs

```bash
# execute the comand
docker-compose up -d

# ACCESS API NODEJS
http://localhost:3001/api

# ACCESS API PYTHON
http://localhost:5000/api/

# inside the docs folder, has the two files explaining how to perform the requests.
requests_api_nodejs.md
requests_api_python.md
```

### SERVICE: 4 - tempnow_scraping

- STEP 1: `Configuring pyenv on your machine, if you have already installed pyenv skip this step.`

install pyenv: https://github.com/pyenv/pyenv#basic-github-checkout

install pyenv-virtualenv: https://github.com/pyenv/pyenv-virtualenv

Obs: cas not use `bash_profile`, alter to `bashrc`

- STEP 2: `with pyenv installed configure your environment:`

```bash
# access project
cd tempnow_scraping/

# Command to know if you have version 3.6.4 installed
# If it is installed it will return the following: 3.6.4
pyenv versions
    # Otherwise, install the
    pyenv install 3.6.4
    # Set the version to global, so you can use only the: python command for any execution.
    pyenv global 3.6.4

# commands to configure your environment to the required version
pyenv virtualenv -p python3.6 3.6.4 tempnow_scraping
# if the project name does not appear in the directory path after executing the command below, 
# close and reopen your IDE (vscode, atom, etc...).
pyenv local tempnow_scraping

# list how your environment was (optional)
ll ~/.pyenv/versions/tempnow_scraping/bin 

# active
pyenv activate tempnow_scraping

# Install the dependencies in the local environment
pip install -r requirements.txt
```

- STEP 3: `load var envs`

```bash
source envs/local.env
```

- STEP 4: `RUN`

```bash
python src/main.py
```

### SERVICE: 5 - tempnow_analytic

```bash

# install jupyter with docker
docker run -d --name jupyter -p 8888:8888 -v ~/tempnow_analytic/:/opt playniuniu/jupyter-pandas

# cp project and csv to volume
sudo cp ./tempnow_analytic/* ~/tempnow_analytic

# then just open your route in the browser below and you will see the data.
http://0.0.0.0:8888

```

## CONTAINER LOGS

```bash
# list
docker container ls

# logs
docker logs -f <container_id>

```

## ARCHITECTURE API PYTHON

```
.
├── Dockerfile
├── id_rsa
├── requirements.txt
└── src
    ├── common
    │   ├── dao
    │   │   ├── country_query.py
    │   │   ├── __init__.py
    │   │   ├── locality_query.py
    │   │   ├── region_query.py
    │   │   ├── wfday_query.py
    │   │   └── wfhour_query.py
    │   ├── datasource
    │   │   ├── connection.py
    │   │   └── __init__.py
    │   ├── __init__.py
    │   └── util.py
    ├── config.py
    ├── main.py
    ├── resources
    │   ├── country.py
    │   ├── __init__.py
    │   ├── locality.py
    │   ├── region.py
    │   ├── wfday.py
    │   └── wfhour.py
    ├── routes
    │   └── __init__.py
    └── uwsgi.ini
```

## ARCHITECTURE API NODEJS

```
.
├── api
│   ├── bin
│   │   └── service.js
│   ├── config
│   │   ├── env.js
│   │   └── index.js
│   ├── lib
│   ├── logs
│   ├── package.json
│   ├── package-lock.json
│   └── src
│       ├── controller
│       │   ├── country.controller.js
│       │   ├── locality.controller.js
│       │   ├── region.controller.js
│       │   ├── wfday.controller.js
│       │   └── wfhour.controller.js
│       ├── datasource
│       │   └── connection.js
│       ├── index.js
│       ├── routes
│       │   └── wf.routes.js
│       └── util
│           └── logger.js
└── Dockerfile
```

## ARCHITECTURE SCRAPING

```
├── csv
│   └── climatempo_all_cities.csv
├── drives
│   └── chromedriver
├── envs
│   └── local.env
├── requirements.txt
└── src
    ├── common
    │   ├── dao
    │   │   ├── __init__.py
    │   │   └── querys.py
    │   ├── datasource
    │   │   ├── connection.py
    │   │   └── __init__.py
    │   ├── __init__.py
    │   └── util.py
    ├── config.py
    ├── insert_cities.py
    └── main.py
```