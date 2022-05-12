# select the version you want
Check the branches
<br>Lastest version : 1.5
# 1.4 to 1.5
error handling now exist<br>
example:
```py
import namedb
try:
  namedb.get('A world without any taxes')
except namedb.ValueNotExist:
  print("damn it")
```
# 1.3 to 1.4
clearcacheprefix now exist<br />
async method of search replaced by exist<br />
editing the cache (restore deleted data)<br />
remove now only cache the data if the cache is true (false by default)<br />
edit now only create the value if the create is true and the data doesn't exist<br />
example:
```py
import namedb
namedb.restore('money')
namedb.clearcache()
```
# 1.2 to 1.3
clearprefix exist<br /><br />
async method of remove replaced by delete
async method of clearcache replaced by cleancache
<br />
async method are now in () after the fonction name in the docs
<br>
example : 
```py
import namedb
async def del_price(user: str):
  await namedb.remove(f'due{user}')
```
adding the cache (restore deleted data)
example:
```py
import namedb
namedb.restore('money')
namedb.clearcache()
```
# 1.1 to 1.2
clearprefix exist<br /><br />
async method of aget replaced by select
<br />
example : 
```py
import namedb
async def get_price(user: str):
  value = await namedb.select(f'due{user}')
  return value
```

# 1.0 to 1.1
edit value now create value if the value doesn't exist<br /><br />
async method added (add a "a" before the fonction (await it too))
<br />
example : 
```py
import namedb
async def get_price(user: str):
  value = await namedb.aget(f'due{user}')
  return value
```
