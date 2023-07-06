## Python shell script
It's inside `scripts/MyClasses.py` Simply run the script to get the results. It uses faker to generate fake data for Terminal and Telementry classes.

## Local Development setup

Install `Docker` on your system. [Check](https://docs.docker.com/engine/install/ubuntu/), assuming you are working on a `unix` like environment.

**NOTE:**

1. Please install `python3.7` or `above` on your system before starting.

2. Suggested `Docker version 19.03.10`

### Installation:

`git clone https://github.com/noobExtendsBot/sample-test.git && cd sample-test`

`clone` and `cd` into `sample-test` folder.

##### 1) First we need to setup a database:

Run the following docker command, you can change container name, ports as you like.

    docker run --name=postgres_db -d -e POSTGRES_USER='postgres' -e POSTGRES_PASSWORD=postgres -e POSTGRES_DBNAME=testpostgres -p 5434:5432 kartoza/postgis:12.0

##### 2) Setting up local python env:

You are free to use your own python development environment. Just in case if you want to follow along.

1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip3 install -r requirements.txt`

##### 3) Run the local dev server and migrate DB

Run the following commans before running the server or creating any `superuser`.

1. `python3 manage.py makemigrations`
2. `python3 manage.py migrate`
3. `python3 manage.py seed.py`

Then you can simply run `python QuerySet.py` to get the results

#### Run QuerySet.py from the root folder to execute the QuerySet

### Required packages for Ubuntu:

`gdal-bin`, `libproj-dev`, `binutils`, `libproj-dev`, `libgdal-dev`
1. `sudo apt-get install binutils libproj-dev gdal-bin`
2. `sudo apt-get install libgeos++`
3. `sudo apt-get install proj-bin`
4. `apt install gdal-bin`

