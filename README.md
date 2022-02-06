## 0x00. AirBnB clone - The console
 By Guillaume
 Weight: 5
 Project to be done in teams of 2 people (your team: Bernard Kyei, Aminat Oyeniyi
 Ongoing project - started 01-24-2022, must end by 01-31-2022 (in 4 days) - you're done with 0% of tasks.
 Checker will be released at 01-29-2022 12:00 PM
 Manual QA review must be done (request it when you are done with the project)
 QA review fully automated.
Concepts
For this project, students are expected to look at these concepts:

### AirBnB_clone.
This is the first step towards building our first full web application: the AirBnB clone. Where Each task is linked and will help you to:
1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
4.create the first abstracted storage engine of the project: File storage.
5.create all unittests to validate all our classes and storage engine

**The AirBnB project
*console.py
We build a custom to interpreter, console.py to:
1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object

**Models.
models is a python package with all the python models we need for our AirBnB clone

*1. BaseModel.
class BaseModel that defines all common attributes/methods for other classes:
models/base_model.py

*2. User
class User that inherits from BaseModel:
models/user.py
with public class attributes:
email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string

*3. States
class states that inherits from BaseModel:
State (models/state.py):
Public class attributes:
name: string - empty string

*4. City
class city that inherits from BaseModel:
City (models/city.py):
Public class attributes:
state_id: string - empty string: it will be the State.id
name: string - empty string

*5.Amenity
class amenity that inherits from BaseModel:
Amenity (models/amenity.py):
Public class attributes:
name: string - empty string

*6. Place
class pkace that inherits from BaseModel:
Place (models/place.py):
Public class attributes:
city_id: string - empty string: it will be the City.id
user_id: string - empty string: it will be the User.id
name: string - empty string
description: string - empty string
number_rooms: integer - 0
number_bathrooms: integer - 0
max_guest: integer - 0
price_by_night: integer - 0
latitude: float - 0.0
longitude: float - 0.0
amenity_ids: list of string - empty list: it will be the list of Amenity.id later

*7. Review
class Review that inherits from BaseModel:
Review (models/review.py):
Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string

**Engine.
A package inside the Models package with the FileStorage model..
* The FileStorage model takes care if all JSON storages and JSON conversiins to resuable objects.
