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

#### Usage

To launch the console application in interactive mode simply run:

```console.py ```

or to use the non-interactive mode run:

```echo "your-command-goes-here" | ./console.py ```

#### Commands

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

#### API

Usage Example:
Open two terminals

From terminal1 ran the following command:

```HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app```

From terminal2 use Curl to send a request method, for example:

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
