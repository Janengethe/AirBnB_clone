# AirBnB clone - The console
## Background Context
### Welcome to the AirBnB clone project! (The Holberton B&B)
- In this project, we will do the following:
  - put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and
  - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON 	string <-> file
  - create all classes used for AirBnB `(User, State, City, Place ...)` that inherit from `BaseModel`
  - create the first abstracted storage engine of the project: File storage.
  - create all unittests to validate all our classes and storage engine

### Files

#### models/base_model.py
Defines all common attributes/methods for other classes:</b>
Public instance attributes:
       - `id` - string - assigned with an uuid when an instance is created
       - `created_at` - datetime - assigned with the current datetime when an instance is created
       - `updated_at` - datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object

Public instance methods:
       - `save(self)` - updates the public instance attribute updated_at with the current datetime
       - `to_dict(self)` -  returns a dictionary containing all keys/values of __dict__ of the instance.

`__str__` - prints [<class name>] (<self.id>) <self.__dict__>

#### models/__init__.py
Creates a unique `FileStorage` instance called `storage` for the application that
is used to reload previous objects created.

#### models/engine/file_storage.py
This class has methods that serializes a python dictionary to  JSON string and reverses the process from JSON string to a python dictionary

Private class attributes:
	-` __file_path` - string - path to the JSON file
	- `__objects` - dictionary - empty but will store all objects by <class name>.id
Public instance methods:
       - `all(self)` - returns the dictionary __objects
       - `new(self, obj)` - sets in __objects the obj with key <obj class name>.id
       - `save(self)` - serializes __objects to the JSON file (path: __file_path)
       - `reload(self)` - deserializes the JSON file to __objects (only if the JSON file (__file_path) exists