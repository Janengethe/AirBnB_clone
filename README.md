# AirBnB clone - The console
<img src="https://www.tabbykatz.com/hbnb.png" width="160" height=auto />

## Background Context
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
At the end, we will have a complete web application composed of:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

### (The Holberton B&B)
- In this project, we will clone Airbnb by doing the following:
  - put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and
  - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON 	string <-> file
  - create all classes used for AirBnB `(User, State, City, Place ...)` that inherit from `BaseModel`
  - create the first abstracted storage engine of the project: File storage.
  - create all unittests to validate all our classes and storage engine

## Files
- #### models/base_model.py
Defines all common attributes/methods for other classes:</br>
Public instance attributes:</br>
- `id` - string - assigned with an uuid when an instance is created </br>
- `created_at` - datetime - assigned with the current datetime when an instance is created </br>
- `updated_at` - datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object </br>

Public instance methods:</br>
- `save(self)` - updates the public instance attribute updated_at with the current datetime </br>
- `to_dict(self)` -  returns a dictionary containing all keys/values of __dict__ of the instance.</br>

- `__str__` - prints `[<class name>] (<self.id>) <self.__dict__>` </br>

- #### models/__init__.py
Creates a unique `FileStorage` instance called `storage` for the application that
is used to reload previous objects created.

- #### models/engine/file_storage.py
This class has methods that serializes a python dictionary to  JSON string and reverses the process from JSON string to a python dictionary

Private class attributes:</br>
-` __file_path` - string - path to the JSON file</br>
- `__objects` - dictionary - empty but will store all objects by <class name>.id </br>
Public instance methods:</br>
- `all(self)` - returns the dictionary __objects </br>
- `new(self, obj)` - sets in __objects the obj with key <obj class name>.id </br>
- `save(self)` - serializes __objects to the JSON file (path: __file_path) </br>
- `reload(self)` - deserializes the JSON file to __objects (only if the JSON file (__file_path) exists </br>
