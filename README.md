0x00. AirBnB Clone - The Console


Foundations > Higher-level Programming > AirBnB Clone
First Step: Develop a command-line interface to manage AirBnB objects.

This initial step is crucial as it forms the basis for building your first full web application: the AirBnB clone. The command interpreter you create will be used across various projects, including HTML/CSS templating, database management, API development, and front-end integration.

Each task is interconnected and will enable you to:

Establish a parent class (BaseModel) to handle initialization, serialization, and deserialization of instances.
Develop a simple serialization/deserialization workflow: Instance ↔ Dictionary ↔ JSON string ↔ File.
Create all classes necessary for AirBnB (User, State, City, Place, etc.) that inherit from BaseModel.
Implement the initial storage engine: File storage.
Write unit tests to validate all classes and the storage engine.
What is a Command Interpreter?

Remember the Shell? The command interpreter works similarly but is tailored to a specific use-case: managing project objects.

Create: Add a new object (e.g., a new User or Place).
Retrieve: Fetch an object from a file or database.
Operate: Perform operations on objects (e.g., count, compute stats).
Update: Modify object attributes.
Destroy: Delete an object.
The interpreter should also function in non-interactive mode:

bash
Copier le code
$ echo "python3 -m unittest discover tests" | bash
Execution

In interactive mode:

bash
Copier le code
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  nothing  quit  show  update

(hbnb)
(hbnb) quit
$
In non-interactive mode:

bash
Copier le code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  nothing  quit  show  update
(hbnb)
$
$ echo "python3 -m unittest discover tests" | bash

.......
----------------------------------------------------------------------
Ran 52 tests in 0.021s

OK
Tasks
0. README and AUTHORS [README.md, AUTHORS]

Write a README.md detailing the project and command interpreter usage.
Create an AUTHORS file listing all contributors, following Docker’s AUTHORS format.
Use branches and pull requests on GitHub to organize team work.
1. PEP8 Compliance [..]

Ensure all code is PEP8 compliant.
2. Unit Tests [tests/]

All files, classes, and functions must be covered by unit tests.
Ensure tests pass in non-interactive mode:
bash
Copier le code
python3 -m unittest discover tests
echo "python3 -m unittest discover tests" | bash
3. BaseModel [models/base_model.py, models/init.py, tests/]

Create a BaseModel class defining common attributes/methods for other classes.
Attributes:
id: A unique string identifier (UUID).
created_at: Timestamp when an instance is created.
updated_at: Timestamp updated every time the object changes.
Methods:
__str__: Print format: [<class name>] (<self.id>) <self.__dict__>.
save(self): Update updated_at with current time.
to_dict(self): Return a dictionary of instance attributes, including class name.
4. Create BaseModel from Dictionary [models/base_model.py, tests/]

Implement the ability to recreate a BaseModel instance from a dictionary representation.
5. Store First Object [models/init.py, models/base_model.py, tests/]

Serialize a BaseModel to a JSON file and reload it.
6. Console 0.0.1 [console.py]

Develop console.py as the entry point for the command interpreter.
Implement commands: quit, EOF, and help.
Ensure the prompt displays as (hbnb) and handle empty lines gracefully.
7. Console 0.1 [console.py]

Extend the command interpreter to support:
create: Create a new instance of BaseModel.
show: Display an instance based on class name and id.
destroy: Delete an instance based on class name and id.
all: Show all instances or instances of a specific class.
update: Update attributes of an instance based on class name and id.
8. First User [models/user.py, models/engine/file_storage.py, console.py, tests/]

Add a User class inheriting from BaseModel.
Include attributes: email, password, first_name, last_name.
Update the command interpreter to manage User instances.
9. More Classes! [models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/]

Add classes State, City, Amenity, Place, Review inheriting from BaseModel with relevant attributes.
10. Console 1.0 [console.py, models/engine/file_storage.py, tests/]

Update FileStorage to handle serialization and deserialization for all new classes.
Extend the command interpreter to manage instances of all created classes.
By following these steps, you will develop a comprehensive command interpreter that serves as the backbone for the AirBnB clone web application
