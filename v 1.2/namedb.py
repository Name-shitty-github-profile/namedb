from os import listdir; from json import load, dump; from os import remove as delet; from package import convert
def search(valuename: str):
  if f'{valuename}.json' not in listdir('namedb'): return False
  return True

def get(valuename: str):
  if f'{valuename}.json' not in listdir('namedb'): return None
  with open(f'namedb/{valuename}.json', 'r') as f:
    data = load(f)
  if valuename not in data: return None
  v = data['value']
  return v

def add(valuename: str, value: any):
  if f'{valuename}.json' in listdir('namedb'): print('value already exist'); return False
  with open(f'namedb/{valuename}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data[valuename] = value
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
    
def remove(value: str):
  if f'{value}.json' not in listdir('namedb'): print("data doesn't exist"); return False
  delet(f'namedb/{value}.json')
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

async def aclearprefix(prefix: str):
  return clearprefix(prefix)

async def asearch(valuename: str):
  return search(valuename)

async def select(valuename: str):
  return get(valuename)

async def aadd(valuename: str, value: str):
  return add(valuename, value)

async def aedit(valuename: str, value: str):
  return edit(valuename, value)

async def aremove(valuename: str):
  return add(valuename)

async def atransferjson(jsondata):
  return transferjson(jsondata)

async def aprefix(type: str, prefix: str):
  return prefix(type, prefix)
