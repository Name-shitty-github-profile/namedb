from os import listdir; from json import load, dump; from os import remove as delet; from package import convert
def search(valuename: str):
  if f'{valuename}.json' not in listdir('namedb'): return False
  return True

def get(valuename: str):
  if f'{valuename}.json' not in listdir('namedb'): return None
  with open(f'namedb/{valuename}.json', 'r') as f:
    data = load(f)
  v = data['value']
  return v

def add(valuename: str, value: any):
  if f'{valuename}.json' in listdir('namedb'): print('value already exist'); return False
  with open(f'namedb/{valuename}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/{valuename}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True

def edit(valuename: str, value: any):
  if f'{valuename}.json' not in listdir('namedb'): add(valuename, value); return True
  with open(f'namedb/{valuename}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/{valuename}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True
    
def remove(valuename: str):
  if f'{valuename}.json' not in listdir('namedb'): print("data doesn't exist"); return False
  value = get(valuename)
  delet(f'namedb/{valuename}.json')
  if f'{valuename}.json' in listdir('namedb/old'): delet(f'namedb/old/{valuename}.json')
  with open(f'namedb/old/{valuename}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/old/{valuename}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True

def restore(valuename: str):
  if f'{valuename}.json' not in listdir('namedb/old'): return None
  with open(f'namedb/old/{valuename}.json', 'r') as fp:
    data = load(fp)
  value = data['value']; delet(f'namedb/old/{valuename}.json'); add(valuename, value)
  return value

def clearcache():
  for file in listdir('namedb/old'): delet(f'namedb/old/{file}')
  return True
    

def transferjson(data):
  for valuename in data:
    add(valuename, data[valuename])
  return True

def prefix(type: str, prefix: str):
  list = []
  if type == 'value':
    for file in listdir('namedb'):
      if file.startswith(prefix):
        f =  open(f'namedb/{file}', 'r'); data = load(f); list.append(data['value'])
  elif type == 'name':
    for file in listdir('namedb'):
      if file.startswith(prefix):
        list.append(convert.convert(file))
  else:
    print('Not a good type'); return None
  return list

def clearprefix(prefix: str):
  for file in listdir('namedb'):
    if file.startswith(prefix): remove(convert.convert(file))
  return True

async def cleanprefix(prefix: str):
  return clearprefix(prefix)

async def asearch(valuename: str):
  return search(valuename)

async def select(valuename: str):
  return get(valuename)

async def aadd(valuename: str, value: str):
  return add(valuename, value)

async def aedit(valuename: str, value: str):
  return edit(valuename, value)

async def delete(valuename: str):
  return remove(valuename)

async def atransferjson(jsondata):
  return transferjson(jsondata)

async def aprefix(type: str, prefix: str):
  return prefix(type, prefix)

async def arestore(valuename: str):
  return restore(valuename)

async def cleancache():
  return clearcache()
