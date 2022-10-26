import json

person = {"name": "John", "age": 30, "city": "New York", "has_children": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
#print(personJSON) # now in json format, False is lowercase

with open("person.json", "w") as file:
    json.dump(person, file, indent=4) #indent 4 means 4 spaces before keys

# with open("person.json", "r") as file:
#     person = json.loads(file)
#     print(person)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 27)

def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

userJSON = json.dumps(user, default=encode_user) # encodes to json
print(userJSON)

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder) # encodes to json with custom class
print(userJSON)

userJSON = UserEncoder().encode(user) # same as above
print(userJSON)

user = json.loads(userJSON) # converts back to dictionary
print(user)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user = json.loads(userJSON, object_hook=decode_user) # converts dict to class
print(type(user))
print(user.name)