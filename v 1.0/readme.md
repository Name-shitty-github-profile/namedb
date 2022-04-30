All rights are reserved to Name.
# get
parameters : valueName(str) <br />
if value is None value will return None<br />
```py
import namedb
print(f'Price : {namedb.get("price")}')
```
# search
parameters : valueName(str) <br />
if value exist it will return True (bool)<br />
else False
```py
import namedb
var = namedb.search('price')
if var:
  print('Give me your money!')
```
# add
parameters : ValueName(str), Value(Any)<br />
if worked it will return True else False<br />
```py
import namedb
namedb.add('price', 90)
```
# edit
parameters : ValueName(str), NewValue(Any)<br />
if worked it will return True else False<br />
```py
import namedb
namedb.edit('price', 50)
```
# remove
parameters : ValueName(str)<br />
if worked it will return True else False<br />
```py
import namedb
namedb.remove('price')
```
# transferjson
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
# prefix
parameters : type(value or name), prefix(str)<br />
return a list with all the files that starts with the prefix<br />
```py
import namedb
for costumer in namedb.prefix(type='value', 'costumersdue'):
  print(f'Due : {costumer}')
```
# setup
install setup.py and run it (answers the questions)<br />
```bash
Directory path (example : C:/windows/desktop/my/project/) : C:/windows/Users/Me/Pycharm/project/
```
# migrating from version 0.
No big change really except better error handling, prefix and lower imports
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