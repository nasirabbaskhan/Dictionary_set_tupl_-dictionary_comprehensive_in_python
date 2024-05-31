from typing import Dict, Union,Any

Key= Union[str,int] # create custom type 
Value= Union[str,int,Dict[str,int],list,set,tuple] # create custom type 
data :Dict[Key,Value]  = {
                         "name":"Nasir Abbas",
                        "fname":"Manzoor hussain",
                        "education":"BS IT",
                        "xyz":[1,2,3],
                        "abc":(1,2,3),
                        "def":{1,2,3},
                        "gif":{"a":1,"b":2,"c":3},
                        }
print(data)
print(data["name"])
print(data["fname"])
print(data["xyz"])
print(data["abc"])
print(data["def"])
print(data["gif"])
print(data["gif"]) # getting value from inner dictionary
