# select the version you want
every big changes between every version will be here
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
