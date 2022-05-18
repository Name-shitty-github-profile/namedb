from os import listdir, mkdir, rmdir, path; from json import load, dump; from os import remove as delet; from package import convert
class ValueAlreadyExist(Exception):
  pass
class ValueNotExist(Exception):
  pass
class CategoryAlreadyExist(Exception):
  pass
class CategoryDoesNotExist(Exception):
  pass
def search(valuename: str, categorie: str = None):
  if f'{valuename}.json' not in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): return False
  return True
async def exist(valuename: str, categorie: str = None):
  if f'{valuename}.json' not in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): return False
  return True
def get(valuename: str, categorie: str = None):
  if f'{valuename}.json' not in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): raise ValueNotExist('Value does not exist')
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'r') as f:
    data = load(f)
  return data['value']
async def select(valuename: str, categorie: str = None):
  if f'{valuename}.json' not in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): raise ValueNotExist('Value does not exist')
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}valuename"}.json', 'r') as f:
    data = load(f)
  return data['value']
def add(valuename: str, value: any, categorie: str = None):
  if f'{valuename}.json' in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): raise ValueAlreadyExist('Value already exist')
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True
async def aadd(valuename: str, value: any, categorie: str = None):
  if f'{valuename}.json' in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): raise ValueAlreadyExist('Value already exist')
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}valuename"}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True
def edit(valuename: str, value: any, create: bool = False, categorie: str = None):
  if f'{f"{valuename}" if not categorie else f"{categorie}valuename"}.json' not in listdir(f'namedb{"" if not categorie else f"/{categorie}"}') and create: 
    add(valuename, value) if not categorie else add(valuename, value, categorie)
    return True
  if f'{valuename}.json' not in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): raise ValueNotExist('Value does not exist')
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True
async def replace(valuename: str, value: any, create: bool = False, categorie: str = None):
  if f'{f"{valuename}" if not categorie else f"{categorie}valuename"}.json' not in listdir('namedb') and create: 
    add(valuename, value) if not categorie else add(valuename, value, categorie)
    return True
  if f'{f"{valuename}" if not categorie else f"{categorie}valuename"}.json' not in listdir('namedb'): raise ValueNotExist('Value does not exist')
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}valuename"}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}valuename"}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True
def remove(valuename: str, cache: bool = False, categorie: str = None):
  if f'{valuename}.json' not in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): raise ValueNotExist('Value does not exist')
  value = get(valuename) if not categorie else get(valuename, categorie)
  delet(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json')
  if not cache: return True
  if f'{valuename}.json' in listdir('namedb/old'): delet(f'namedb/old/{valuename}.json')
  with open(f'namedb/old/{valuename}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/old/{valuename}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True
async def delete(valuename: str, cache: bool = False, categorie: str = None):
  if f'{valuename}.json' not in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'): raise ValueNotExist('Value does not exist')
  delet(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json')
  if not cache: return True
  value = get(valuename) if not categorie else get(valuename, categorie)
  if f'{valuename}.json' in listdir('namedb/old'): delet(f'namedb/old/{valuename}.json')
  with open(f'namedb/old/{valuename}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data['value'] = value
  with open(f'namedb/old/{valuename}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True
def createcat(catname: str):
  pathe = path.join('./namedb/', catname)
  if path.isdir(pathe): raise CategoryAlreadyExist('Category already exist')
  mkdir(pathe); return True
async def acreatecat(catname: str):
  pathe = path.join('./namedb/', catname)
  if path.isdir(pathe): raise CategoryAlreadyExist('Category already exist')
  mkdir(pathe); return True
def deletecat(catname: str):
  pathe = path.join('./namedb/', catname)
  if not path.isdir(pathe): raise CategoryDoesNotExist('Category doesn\'t exist')
  rmdir(pathe); return True
async def adeletecat(catname: str):
  pathe = path.join('./namedb/', catname)
  if not path.isdir(pathe): raise CategoryDoesNotExist('Category doesn\'t exist')
  rmdir(pathe); return True
def prefix(type: str, prefix: str, categorie: str = None):
  list = []
  if type == 'value':
    for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
      if file.startswith(prefix):
        f =  open(f'namedb/{file}', 'r'); data = load(f); list.append(data['value'])
  elif type == 'name':
    for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
      if file.startswith(prefix):
        list.append(convert.convert(file))
  else:
    raise ValueError('Not a valid type\nTypes : "name", "value"')
  return list
async def aprefix(type: str, prefix: str, categorie: str = None):
  list = []
  if type == 'value':
    for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
      if file.startswith(prefix):
        f =  open(f'namedb/{file}', 'r'); data = load(f); list.append(data['value'])
  elif type == 'name':
    for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
      if file.startswith(prefix):
        list.append(convert.convert(file))
  else:
    raise ValueError('Not a valid type\nTypes : "name", "value"')
  return list
def clearprefix(prefix: str, cache: str = False, categorie: str = None):
  for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
    if file.startswith(prefix): remove(convert.convert(file) ,cache) if not categorie else remove(convert.convert(file),cache ,categorie)
  return True
async def cleanprefix(prefix: str, cache: str = False, categorie: str = None):
  for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
    if file.startswith(prefix): remove(convert.convert(file) ,cache) if not categorie else remove(convert.convert(file),cache ,categorie)
  return True
def restore(valuename: str, categorie: str = None):
  if f'{valuename}.json' not in listdir('namedb/old'): raise ValueNotExist('value does not exist')
  with open(f'namedb/old/{valuename}.json', 'r') as fp:
    data = load(fp)
  delet(f'namedb/old/{valuename}.json')
  add(valuename, data['value']) if not categorie else add(valuename, data['value'], categorie)
  return data['value']
async def arestore(valuename: str, categorie: str = None):
  if f'{valuename}.json' not in listdir('namedb/old'): raise ValueNotExist('value does not exist')
  with open(f'namedb/old/{valuename}.json', 'r') as fp:
    data = load(fp)
  delet(f'namedb/old/{valuename}.json')
  add(valuename, data['value']) if not categorie else add(valuename, data['value'], categorie)
  return data['value']
def clearcache():
  for file in listdir('namedb/old'): delet(f'namedb/old/{file}')
  return True
async def cleancache():
  for file in listdir('namedb/old'): delet(f'namedb/old/{file}')
  return True
def transferjson(data, categorie: str = None):
  for valuename in data:
    add(valuename, data[valuename]) if not categorie else add(valuename, data[valuename], categorie)
  return True
async def atransferjson(data, categorie: str = None):
  for valuename in data:
    add(valuename, data[valuename]) if not categorie else add(valuename, data[valuename], categorie)
  return True
