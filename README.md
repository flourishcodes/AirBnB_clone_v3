# Synopsis

> The Airbnb clone project for which we are creating a copy of the [Airbnb](https://www.airbnb.com/).
> Only some features will be implemented and will be listed below once completed.
> At this stage, we are implementing an additional storage option. Based on which 
> database is chosen (file storage or database storage), JSON is used or
> MySQL and SQLalchemy is used via Python. Fabric is used for application deployment.

## Features

### Available Class Objects

#### Description
The following Classes are the foundation of this project. We provided information about each classes and their own attributes to make the best use of our Console (CLI) and RESTful API.

By default, all new class instances will have the following attributes:
   - id - unique Identification for each object
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
"" | *place_amenities* | *list of places that has this amenity*

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


#### Usage

You can run the console to use local filestorage (json format) or using a database

To create a Database and user
```
cat setup_mysql_dev.sql | sudo mysql
```
This will create a Database and a new User:
- DB Name: **nope_dev_db**
- User Name: **nope_dev@localhost**
- User Password: **nope_dev_pwd**

To launch the console application in interactive mode using **local filestorage** simply run:

```
./console.py
```

To use with **Database Storage**:
```
nope_MYSQL_USER=nope_dev nope_MYSQL_PWD=nope_dev_pwd nope_MYSQL_HOST=localhost nope_MYSQL_DB=nope_dev_db nope_TYPE_STORAGE=db nope_API_HOST=0.0.0.0 nope_API_PORT=5000 ./console.py
```

Usage and expected behavior: 
```
(nope) <command_name> <class name> <attribute=value>
<Returned Id>
(nope)
```

Example:
   
   ```
(nope) command_name State name=Texas
(nope) Create State name=California
(nope) Create City name=San_Francisco state_id=<the returned california id>
(nope) Show City <The return San Francisco id>
   ```

To use the non-interactive mode run:

```echo "<command> <class name> <attribute=value>" | ./console.py ```

Example:

```echo "Create State name=California" | ./console.py```

Want some data in your Database for testing?
Download some dummy data.

```
wget https://s3.amazonaws.com/intranet-projects-files/notreblohschool-higher-level_programming+/290/100-nope.sql
cat 100-nope.sql | sudo mysql
```

Confirm there are some data:
```
echo "all" | nope_MYSQL_USER=nope_dev nope_MYSQL_PWD=nope_dev_pwd nope_MYSQL_HOST=localhost nope_MYSQL_DB=nope_dev_db nope_TYPE_STORAGE=db nope_API_HOST=0.0.0.0 nope_API_PORT=5000 ./console.py
```

### RESTful API

#### Description
Implement RESTful API that sends GET, POST, PUT and DELETE method requests which allows you to interact with the objects in the storage

#### Usage

1. Open two terminals

2. From terminal1 ran the following command:

```nope_MYSQL_USER=nope_dev nope_MYSQL_PWD=nope_dev_pwd nope_MYSQL_HOST=localhost nope_MYSQL_DB=nope_dev_db nope_TYPE_STORAGE=db nope_API_HOST=0.0.0.0 nope_API_PORT=5000 python3 -m api.v1.app```

3. From terminal2 use Curl to send a request method
```
CURL -X <Rquest Method> http://0.0.0.0:5000/api/v1/<Route>
```

For example
```
curl -X GET http://0.0.0.0:5000/api/v1/status
```
This will return 
```{status: Ok}```

More Example:
```
curl -X GET http://0.0.0.0:5000/api/v1/state
```
This will return all the state information in Json format

Other routes:

Method_Requests | Routes | Description        | Usage Example
----------------|--------|-------------|--------------|
GET | /states/ | Retrieves all state objects | curl -X GET http://0.0.0.0:5000/api/v1/state
GET | /states/<state_id> | Retrieves a specific state objects base on state_id | curl -X GET http://0.0.0.0:5000/api/v1/state/<state_id>
POST | /states/ | creates a new state | curl -X POST http://0.0.0.0:5000/api/v1/state/<state_id> -d '{"name": "California"}'
DELETE | /states/<state_id> | Deletes a specific state object base on state_id | curl -X DELETE http://0.0.0.0:5000/api/v1/state/<state_id>
PUT | /states/<state_id> | Updates a state attribute | curl -X PUT http://0.0.0.0:5000/api/v1/state/<state_id> -d '{"name": "new_name"}' 
----------------|--------|-------------|--------------|
GET | /states/<state_id/cities | retrieves all the city in the State | curl -X GET http://0.0.0.0:5000/api/v1/state/<state_id>/cities
GET | /cities/city_id | retrieves a city | curl -X GET http://0.0.0.0:5000/api/v1/cities/<city_id>
POST | /<state_id>/cities | creates a new city in the State | curl -X POST http://0.0.0.0:5000/api/v1/state/<state_id>/cities -d '{"name": "Los Angeles"}'
DELETE | /cities/<city_id> | Deletes a specific City Object | curl -X DELETE http://0.0.0.0:5000/api/v1/cities/<city_id>
PUT | /cities/<city_id> | Updates a specific City object | curl -X PUT http://0.0.0.0:5000/api/v1/state/<state_id>/cities -d '{"name": "New Name"}'
----------------|--------|-------------|--------------|
GET | /cities/<city_id>/places | retrieves all places in the city | curl -X GET http://0.0.0.0:5000/api/v1/cities/<city_id>/places
GET | /places/place_id/ | retrieves a certain place | curl -X GET http://0.0.0.0:5000/api/v1/places/<place_id>
POST | /cities/<city_id>/places | creates a new place base on given city id | curl -X POST http://0.0.0.0:5000/api/v1/state/<state_id>/cities -d '{"name": "Beeutiful Home", "user_id": "some user id"}'
POST | /places_search | retrieves all places specific to each city(ies), state(s) and amenity(ies). Amenity is exclusive | curl -X POST http://0.0.0.0:5000/api/v1/state/places_search -d '{"states": ["state_id1", "state_id2"], "cities": ["city_id1", city_id2, city_id3"], "amenities": ["amenity_id1", amenity_id2"]}
PUT | /places/<place_id> | updates a certain place object |  curl -X POST http://0.0.0.0:5000/api/v1/state/<state_id>/cities -d '{"name": "new place name"}'
----------------|--------|-------------|--------------|
GET | /users | retrieves all list of all users | curl -X GET http://0.0.0.0:5000/api/v1/users
GET | /users/<user_id> | retrieves a certain user info | curl -X GET http://0.0.0.0:5000/api/v1/users/<user_id>
POST | /users/| creates a new user | curl -POST http://0.0.0.0:5000/api/v1/users -d '{"email": "Email@email.com", "password": "my_password"}'
DELETE | /users/<user_id> | Deletes a certain user | curl -X DELETE http://0.0.0.0:5000/api/v1/users/<user_id>
PUT | /users/<user_id>| updates a new user | curl -POST http://0.0.0.0:5000/api/v1/users/<user_id> -d '{"email": "NEWEmail@newemail.com", "password": "my_newpassword"}'
----------------|--------|-------------|--------------|
GET | /amenities | retrieves all amenities | curl -X GET http://0.0.0.0:5000/api/v1/amenities
GET | /amenities/<amenity_id> | retrieves a certain amenities | curl -X GET http://0.0.0.0:5000/api/v1/amenities/<amenity_id>
POST | /amenities | creates a new amenity | curl -X POST http://0.0.0.0:5000/api/v1/amenities -d '{"name": "Wifi"}'
PUT | /amenities/<amenity_id> | updates an amenity | curl -X POST http://0.0.0.0:5000/api/v1/amenities/<amenity_id> -d '{"name": "Dogs Allowed"}'
DELETE | /amenities/<amenity_id> | deletes an amenities object | curl -X DELETE http://0.0.0.0:5000/api/v1/amenities/<amenity_id>
----------------|--------|-------------|--------------|
GET | /places/<place_id>/reviews | retrieves all reviews in certain place | curl -X GET http://0.0.0.0:5000/api/v1/places/<place_id>/reviews
GET | /reviews/<review_id> | retrives a certain review about a place | curl -X GET http://0.0.0.0:5000/api/v1/reviews/<review_id>
POST | /places/<places_id>/reviews | creates a new reviews about a certain place | curl -X POST http://0.0.0.0:5000/api/v1/places/<place_id>/reviews -d '{"user_id": "Id of user", "text": "Text review and comment"}'
PUT | /places/<places_id>/reviews | updates the text review about a certain place | curl -X PUT http://0.0.0.0:5000/api/v1/places/<place_id>/reviews -d '{"text": "Text review and comment"}'
DELETE | /reviews/<review_id> | deletes a certain review about a place | curl -X DELETE http://0.0.0.0:5000/api/v1/reviews/<review_id>
----------------|--------|-------------|--------------|
GET | /places/<place_id>/amenities | retrieves all amenities in a certain place | curl -X GET http://0.0.0.0:5000/api/v1/places/<place_id>/amenities
POST | /places/<places_id>/amenities/<amenity_id> | adds an existing amenity to a certain place | curl -X POST http://0.0.0.0:5000/api/v1/places/<place_id>/reviews -d '{"amenity_id": "some amenity id"}'
DELETE | /places/<place_id>/amenities | deletes an amenity in a certain place | curl -X DELETE http://0.0.0.0:5000/api/v1/places/<place_id>/amenities
----------------|--------|-------------|--------------|

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
