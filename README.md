# Coding Assignment Energyworx - Url Shortener

# Assignment Description

This project has been implemented according to the isntructions given in Python_Development_Case_3 (1) (1) (1) (2).pdf file.


##  Setting up Environment

### Install Docker in your system.

#### Ubuntu
```sh
$ sudo apt-get update
$ sudo apt-get install docker.io docker-compose
```

#### Windows
Install the Docker Desktop using the instructions on https://docs.docker.com/docker-for-windows/install/

## Bringing up your environment

From the project root run command


```sh
$ docker-compose up
```

After the mysqldb container is up and running, run docker-compose cmd to work within the container

```sh
$ docker-compose exec flaskapi sh
```

```sh
$ python manage.py mysqldb init
$ python manage.py mysqldb migrate
$ python manage.py mysqldb upgrade
```



## Running Unit Tests



```sh
$ python setup.py develop
$ python setup.py test
```

## What would I do if I had more time:
* **Coding & Configuration** 
  - Proper logging, commenting and exception handling needs to be added.
  - All error messages should go into one error config file.
  - SQL Connection  and query exception handling need to be added properly.
  - Configuration parameters needs to be read form an env based config file.
  - A framework for unittest can be used. 
  - A CI framework could be used although it won't be necessary for such a small codebase which is not prone to change much.
  - Docker configuration could be parametrized based on env.
  - Module/Package/App structure can be refactored better and Blueprints(can be overkill as well) could be used.
  - Tests are quite poor. All the cases needs to be covered with adding some sample data.
* **Scalibitly** 
  - App is not scaleable as  is due to DB being the bottleneck. Data could be scattered across multiple DB/tables.  
* **Performance**
  - The way this has been implemented is actually quite expensive with high volume requests due to DB read/write. Some 
    can be handled prgorammaticely or server level configuration but the best option could be overhaul a complete architecture based on requirements.
* **Redundancy** 
  - There is no redundancy. Could be implemented via data replication or wiritng to second DB via Queues. (I am making a ltof assumptiıons and did not do enough thinking/reading about this matter)
* **Security**
  - ???
  

## Sample Request
```json
{
    "url": "https://www.energyworx.com/", 
    "shortcode": "c83df7"
}
```
