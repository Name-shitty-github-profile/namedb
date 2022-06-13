All rights are reserved to Name.
# data
get a data<br> check if a data exist
## get (select)
parameters : valueName(str), Category(optional(str))<br />
if value is None value will return None<br />
```py
import namedb
print(f'Price : {namedb.get("price")}')
```
error handling<br />
exemple : 
```py
import namedb
try:
  namedb.get('a world without taxes')
except namedb.ValueNotExist:
  print('Damn it')
```
Mutli-tasking select more then one thing using || to separate them
<br>
return a list of all of the arugments instanid of just the argument
<br>
exemple : 
```py
import namedb
thing = namedb.get('a life|| a world without taxes')
print(thing[0])
print(thing[1])
```
## search (exist)
parameters : valueName(str), Category(optional(str)) <br />
if value exist it will return True (bool)<br />
else False
```py
import namedb
var = namedb.search('price')
if var:
  print('Give me your money!')
```
mutli-tasking separate differents ellement with ||
<br>
return True is all the values exist else it return False
```py
import namedb
var = namedb.search('price||due')
if var:
  print('Give me your money!')
```
# edit-data
## add (aadd)
parameters : ValueName(str), Value(Any), Category(optional(str))<br />
if worked it will return True else False<br />
```py
import namedb
namedb.add('price', 90)
```
error handling<br />
exemple : 
```py
import namedb
try:
  namedb.add('taxes', 0.19)
except namedb.ValueAlreadyExist:
  print('Damn it')
```
## edit (replace)
Big updates with edit
<br>
### edit-value
parameters : valuename(str), value(any)
```py
import namedb
namedb.edit('taxes', 'does not exist')
```
### add to a number
parameters : valuename(str), add(int)
```py
import namedb
namedb.edit('tomatostock', add=3)
```
### minus to a number
parameters : valuename(str), minus(int)
```py
import namedb
namedb.edit('tomatostock', minus=5)
```
### append to a list
parameters : valuename(str), append(any)
```py
import namedb
namedb.edit('product', append='tomato')
```
### remove to a list
parameters : valuename(str), remove(any)
```py
import namedb
namedb.edit('product', remove='tomato')
```
## remove (delete)
parameters : ValueName(str), cache(optional(bool)), Category(optional(str))<br />
if worked it will return True else False<br />
stock the value in the cache if cache is true (false by default)
```py
import namedb
namedb.remove('price')
```
error handling<br />
exemple : 
```py
import namedb
try:
  namedb.remove('a world without taxes')
except namedb.ValueNotExist:
  print('Damn it')
```
mutli-tasking separate the values that you want to delete with ||
```py
import namedb
namedb.remove('price||due')
```
# json
just transfer json for now
## transferjson (atransferjson)
parameters : Data(json), Category(optional(str))<br />
if worked it will return True else False<br />
```py
import namedb
jsoncode = {
'price': 90,
'due': 60
}
namedb.transferjson(jsoncode)
print(f'{namedb.get("price")}')
```
# prefix
find or edit data with a prefix
## prefix (aprefix)
parameters : type(value or name), prefix(str), Category(optional(str))<br />
return a list with all the files that starts with the prefix<br />
```py
import namedb
for costumer in namedb.prefix(type='value', 'costumersdue'):
  print(f'Due : {costumer}')
```
error handling<br />
exemple : 
```py
import namedb
try:
  namedb.prefix('hi', 'taxes')
except ValueError:
  print('Damn it')
```
## clearprefix (cleanprefix)
parameters : prefix(str), Category(optional(str))<br />
delete all the values that starts with the prefix<br />
```py
import namedb
namedb.clearprefix('due')
```
# cache
Restore data or remove data with a prefix or without
## restore (arestore)
parameters : valuename(str), Category(optional(str))<br>
restore a value from the cache (and return it)
```py
import namedb
namedb.remove('taxes')
print('too good to be real')
namedb.restore('taxes')
```
error handling<br />
exemple : 
```py
import namedb
try:
  namedb.restore('a world without taxes')
except namedb.ValueNotExist:
  print('Damn it')
```
## clearcache (cleancache)
parameters : None
clear the cache
```py
import namedb
namedb.remove('money')
namedb.clearcache()
```
## clearcacheprefix (cleancacheprefix)
parameters : prefix(str), Category(optional(str))
clear the cache with a prefix
```py
import namedb
namedb.remove('exemple2286')
namedb.clearcacheprefix('exemple')
```
# category
create a category or remove it<br>
We highly recommend using category
## createcat (acreatecat)
Parameters : categoryname(str)<br>
Create a category
```py
import namedb
namedb.createcat('example')
```
## deletecat (adeletecat)
Parameters : categoryname(str)<br>
Delete a category
```py
import namedb
namedb.deletecat('example')
```
## listcat (alistcat)
parameters : catname(str), type(str ["name", "value"]) <br>
list all values or name
```py
import namedb
for value in namedb.listcat('stock', 'name'):
  print(value)
```
# async
everything work the same just change the name of the fonction
example : 
```py
import namedb
async def get_money(user_id: str):
  value = await namedb.select(f'money{user_id}')
  return value
```
# setup
install setup.py and run it (answers the questions)<br />
```bash
Directory path (example : C:/windows/desktop/my/project/) : C:/windows/Users/Me/Pycharm/project/
```
# migrating from version 1.6
multi-tasking now exist <br>
example:
```py
import namedb
namedb.remove('taxes||bad things')
```
edit has been updated a lot
# recommandation
Please use try: and except: if you run a constant code because this errors can make your code stop<br>
We higly recommend using category<br /><br /><br /><br />
We aren't responsible for data lost.
# bonus
This is one of the last versions of this database because I havte no ideas of what to do now except optimisation so don't expect big changes for the next versions it's probably be like backend optimisations<br>
I will check to publish this as python package btw
