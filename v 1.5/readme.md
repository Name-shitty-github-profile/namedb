All rights are reserved to Name.
# get (select)
parameters : valueName(str) <br />
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
# search (exist)
parameters : valueName(str) <br />
if value exist it will return True (bool)<br />
else False
```py
import namedb
var = namedb.search('price')
if var:
  print('Give me your money!')
```
error handling<br />
exemple : 
```py
import namedb
try:
  namedb.search('a world without taxes')
except namedb.ValueNotExist:
  print('Damn it')
```
# add (aadd)
parameters : ValueName(str), Value(Any)<br />
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
# edit (aedit)
parameters : ValueName(str), NewValue(Any), create(bool)<br />
if worked it will return True else False<br />
if create is true and the data doesn't exist the data will be added
```py
import namedb
namedb.edit('price', 50)
```
error handling<br />
exemple : 
```py
import namedb
try:
  namedb.edit('a world without taxes', True)
except namedb.ValueNotExist:
  print('Damn it')
```
# remove (delete)
parameters : ValueName(str), cache(bool)<br />
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
# transferjson (atransferjson)
parameters : Data(json)<br />
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
# prefix (aprefix)
parameters : type(value or name), prefix(str)<br />
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
# clearprefix (cleanprefix)
parameters : prefix(str)<br />
delete all the values that starts with the prefix<br />
```py
import namedb
namedb.clearprefix('due')
```
# restore (arestore)
parameters : valuename(str)<br>
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
# clearcache (cleancache)
parameters : None
clear the cache
```py
import namedb
namedb.remove('money')
namedb.clearcache()
```
# clearcacheprefix (cleancacheprefix)
parameters : prefix(str)
clear the cache with a prefix
```py
import namedb
namedb.remove('exemple2286')
namedb.clearcacheprefix('exemple')
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
# migrating from version 1.4
error handling now exist
example:
```py
import namedb
try:
  namedb.get('A world without any taxes')
except namedb.ValueNotExist:
  print("damn it")
```
# example
```python
import namedb
namedb.add('fruits', ['tomato', 'apple'])
vegetables = namedb.search('vegetables')
if vegetables:
  for fruit in namedb.get('fruits'):
    print(f'Fruits : {fruit}')
else:
  for trempette in namedb.prefix(type='value', 't'):
    print(f'Tempette : {tremepette}')
namedb.edit('price', namedb.get('price') + 10)
if namedb.get('paid'):
  namedb.remove('price')
else:
  namedb.edit('price', namedb.get('price') + 1)
json = {'client': 'Naomie', 'gender': 'female'}
namedb.transferjson(json)
```
# recommandation
Please use try: and except: if you run a constant code because this errors can make your code stop<br /><br /><br /><br />
We aren't responsible for data lost.
