# Synopsis

> The Airbnb clone project for which we are creating a copy of the [Airbnb](https://www.airbnb.com/).
> Only some features will be implemented and will be listed below once completed.
> At this stage, we are implementing an additional storage option. Based on which 
> database is chosen (file storage or database storage), JSON is used or
> MySQL and SQLalchemy is used via Python. Fabric is used for application deployment.

## Features

### Command Interpreter

#### Description

The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Create a new object.
+ Retrieve an object from a file, database, etc.
+ Execute operation on objects. e.g. Count, compute statistics, etc.
+ Update object's attributes.
+ Destroy an object.
+ There are two storages you can use: **Filestorage** which creates a local json file or **DBStorage** using mysql database more info how to use one or the other below.
+ Usage: <command_name> <class_name> <attributes=values>

#### Commands

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes an instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\> **Only tested on Local File Storage**

#### Available Classes
By default, all new class instances will have the following attributes:
   - id - unique ID for each object
   - created_at - time this new object was first created
   - updated_at - time this new object was last modified

Note:
*italics* - SQL Database only

Class name | Attributes | Description
-----------|-----------|------------|
State | name | string name of the State
"" | cities | list of all cities in the state
-----------|-----------|------------|
City | name | string name of the city
"" | state_id | string id of the State
"" | *Places* | lits of places in in the city
-----------|-----------|------------|
User | email | string email of user
"" | password | string password of user hashed md5
"" | first_name | name of the user
"" | last_name | last name of the user
"" | *places* | *list of places owned by the user*
"" | *reviews* | *list of Reviews made by the user*
-----------|-----------|------------|
Place | city_id | string id of a city
"" | user_id | string id of a user
"" | name | string name of the place
"" | description | description of the place
"" | number_rooms | number of rooms in the place
"" | number_bathrooms | number of usable bathrooms in the place
"" | max_guest | number of max guest available
"" | price_by_night | rate per night
"" | latitude | latitude of the place
"" | longitude | longitude of the place
"" | reviews | list of reviews made for this place
"" | amenities | list of amenities available in this place
"" | amenity_ids | **if not using Database** list of amenity ids
-----------|-----------|------------|
Review | text | review for the place
"" | place_id | id of the place
"" | user_ud | id of the user who made the review
-----------|-----------|------------|
Amenity | name | name of the amenity
"" | *place_amenities | list of places that has this amenity*


#### Usage

You can run the console to use local filestorage (json format) or using a database

To create a Database and user
```
cat setup_mysql_dev.sql | sudo mysql
```
This will create a Database and a new User:
- DB Name: **hbnb_dev_db**
- User Name: **hbnb_dev@localhost**
- User Password: **hbnb_dev_pwd**

To launch the console application in interactive mode using local filestorage simply run:

```./console.py ```

To use with Database Storage:
```HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 ./console.py```

Usage: <command_name> <class name> <attribute=value>
Example:
```
(hbnb) command_name State name=Texas
(hbnb) Create State name=California```
```

output: California ID

```(hbnb) Create City name=San_Francisco state_id=<the returned california id```

or to use the non-interactive mode run:

```echo "<command> <class name> <attribute=value>" | ./console.py ```

Example:

```echo "Create State name=California" | ./console.py```

Want some data in your Databse for testing?
Download our dump.sql

```
wget https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql
cat 100-hbnb.sql | sudo mysql
```

Confirm there are some data:
```
echo "all" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 ./console.py
```

### API

#### Usage
1. Open two terminals

2. From terminal1 ran the following command:

```HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app```

3. From terminal2 use Curl to send a request method, for example:

```curl -X GET http://0.0.0.0:5000/api/v1/status``` This will return ```{status: Ok}```

## Resources
* Fabric: [Usage1](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments), [Usage2](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python), [Documenation](http://www.fabfile.org/)
* Nginx: [Beginner's Config file](http://nginx.org/en/docs/beginners_guide.html), [Root vs Alias](https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/), 

## Tests

If you wish to run at the test for this application all of the test are located
under the **test/** folder and can execute all of them by simply running:

```python3 -m unittest discover tests ```

from the root directory.

## Bugs

+ No known bugs at this time.

## Authors
Adekunle Adeniran
Adriel Tolentino
