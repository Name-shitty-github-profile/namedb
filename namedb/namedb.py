from os import listdir, mkdir, rmdir, path; from json import load, dump; from os import remove as delet
class ValueAlreadyExist(Exception):
  pass
class ValueNotExist(Exception):
  pass
class CategoryAlreadyExist(Exception):
  pass
class CategoryDoesNotExist(Exception):
  pass
def search(valuename: str, *, categorie: str = None):
  if not '||' in valuename: return path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json')
  for value in valuename.split('||'):
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{value}.json'): return False
  return True
async def exist(valuename: str, *, categorie: str = None):
  if not '||' in valuename: return path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json')
  for value in valuename.split('||'):
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{value}.json'): return False
  return True
def get(valuename: str, *, categorie: str = None):
  if '||' not in valuename:
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json'): raise ValueNotExist('Value does not exist')
    with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'r') as f:
      data: dict = load(f)
    return data['value']
  valuelist: list = []
  for value in valuename.split('||'):
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{value}.json'): raise ValueNotExist(f'Value {value} does not exist')
    with open(f'namedb/{f"{value}" if not categorie else f"{categorie}/{value}"}.json', 'r') as f:
      data: dict = load(f)
    valuelist.append(data['value'])
  return valuelist
async def select(valuename: str, *, categorie: str = None):
  if '||' not in valuename:
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json'): raise ValueNotExist('Value does not exist')
    with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'r') as f:
      data: dict = load(f)
    return data['value']
  valuelist: list = []
  for value in valuename.split('||'):
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{value}.json'): raise ValueNotExist(f'Value {value} does not exist')
    with open(f'namedb/{f"{value}" if not categorie else f"{categorie}/{value}"}.json', 'r') as f:
      data: dict = load(f)
    valuelist.append(data['value'])
  return valuelist
def add(valuename: str, value: any, *, categorie: str = None):
  if path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json'): raise ValueNotExist('Value does not exist')
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'x') as fp:
    data: dict = {}; data['value'] = value; dump(data, fp, indent=2)
async def create(valuename: str, value: any, *, categorie: str = None):
  if path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json'): raise ValueNotExist('Value does not exist')
  with open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'x') as fp:
    data: dict = {}; data['value'] = value; dump(data, fp, indent=2)
def edit(valuename: str, value: any = None, *, create: bool = False, categorie: str = None, add: int = None, minus: int = None, append: any = None, remove: any = None):
  if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json'):
    if create:
      if not value: raise ValueError('Value is obligated except when add, minus, remove, append')
      return add(valuename, value) if not categorie else add(valuename, value, categorie)
    raise ValueNotExist('Value does not exist')
  fp = open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'r+'); data: dict = {}
  if not add and not minus and not append and not remove: 
    data['value'] = value
  else:
    dat: dict = load(fp)
    if add != None:
      data['value']: int = int(dat['value']) + add
    elif minus != None:
      data['value']: int = int(dat['value']) - minus
    elif append != None:
      listqwe: list = dat['value']; listqwe.append(append); data['value'] = listqwe
    elif remove != None:
      listqwe: list = dat['value']; listqwe.remove(remove); data['value'] = listqwe
  dump(data, fp, indent=2)
  return True
async def replace(valuename: str, value: any = None, *, create: bool = False, categorie: str = None, add: int = None, minus: int = None, append: any = None, remove: any = None):
  if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json'):
    if create:
      if not value: raise ValueError('Value is obligated except when add, minus, remove, append')
      return add(valuename, value) if not categorie else add(valuename, value, categorie)
    raise ValueNotExist('Value does not exist')
  fp = open(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json', 'r+'); data: dict = {}
  if not add and not minus and not append and not remove: 
    data['value'] = value
  else:
    dat: dict = load(fp)
    if add != None:
      data['value']: int = int(dat['value']) + add
    elif minus != None:
      data['value']: int = int(dat['value']) - minus
    elif append != None:
      listqwe: list = dat['value']; listqwe.append(append); data['value'] = listqwe
    elif remove != None:
      listqwe: list = dat['value']; listqwe.remove(remove); data['value'] = listqwe
  dump(data, fp, indent=2)
  return True
def remove(valuename: str, *, cache: bool = False, categorie: str = None):
  if not '||' in valuename:
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json'): raise ValueNotExist('Value does not exist')
    if not cache:
      delet(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json')
      return True
    value = get(valuename) if not categorie else get(valuename, categorie=categorie)
    delet(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json')
    if path.isfile(f'namedb/old/{valuename}.json'):  delet(f'namedb/old/{valuename}.json')
    with open(f'namedb/old/{valuename}.json', 'x') as fp:
      data: dict = {}; data['value'] = value; dump(data, fp, indent=2)
    return True
  if cache:
    for valuenamee in valuename.split("||"):
      if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuenamee}.json'): raise ValueNotExist('Value does not exist')
      delet(f'namedb/{f"{valuenamee}" if not categorie else f"{categorie}/{valuenamee}"}.json')
      value = get(valuenamee) if not categorie else get(valuenamee, categorie=categorie)
      if path.isfile(f'namedb/old/{valuenamee}.json'):  delet(f'namedb/old/{valuenamee}.json')
      with open(f'namedb/old/{valuenamee}.json', 'x') as fp:
        fp.write(f'\{"value": {value}\}')
    return True
  for valuenamee in valuename.split("||"):
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuenamee}.json'): raise ValueNotExist('Value does not exist')
    delet(f'namedb/{f"{valuenamee}" if not categorie else f"{categorie}/{valuenamee}"}.json')
  return True
async def delete(valuename: str, *, cache: bool = False, categorie: str = None):
  if not '||' in valuename:
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuename}.json'): raise ValueNotExist('Value does not exist')
    if not cache:
      delet(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json')
      return True
    value = get(valuename) if not categorie else get(valuename, categorie=categorie)
    delet(f'namedb/{f"{valuename}" if not categorie else f"{categorie}/{valuename}"}.json')
    if path.isfile(f'namedb/old/{valuename}.json'):  delet(f'namedb/old/{valuename}.json')
    with open(f'namedb/old/{valuename}.json', 'x') as fp:
      data: dict = {}; data['value'] = value; dump(data, fp, indent=2)
    return True
  if cache:
    for valuenamee in valuename.split("||"):
      if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuenamee}.json'): raise ValueNotExist('Value does not exist')
      delet(f'namedb/{f"{valuenamee}" if not categorie else f"{categorie}/{valuenamee}"}.json')
      value = get(valuenamee) if not categorie else get(valuenamee, categorie=categorie)
      if path.isfile(f'namedb/old/{valuenamee}.json'):  delet(f'namedb/old/{valuenamee}.json')
      with open(f'namedb/old/{valuenamee}.json', 'x') as fp:
        fp.write(f'\{"value": {value}\}')
    return True
  for valuenamee in valuename.split("||"):
    if not path.isfile(f'namedb{"" if not categorie else f"/{categorie}"}/{valuenamee}.json'): raise ValueNotExist('Value does not exist')
    delet(f'namedb/{f"{valuenamee}" if not categorie else f"{categorie}/{valuenamee}"}.json')
  return True
def searchcat(catname: str):
  pathe = path.join('./namedb/', catname)
  if path.isdir(pathe): return True
  return False
async def asearchcat(catname: str):
  pathe = path.join('./namedb/', catname)
  if path.isdir(pathe): return True
  return False
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
def listcat(catname: str, type: str):
  qwe: list = []
  if type == 'name':
    for file in listdir(f'namedb/{catname}'): qwe.append(file[: -5])
    return qwe
  elif type == 'name':
    for file in listdir(f'namedb/{catname}'): f =  open(f'namedb/{catname}/{file}', 'r'); data = load(f); qwe.append(data['value'])
    return qwe
  raise ValueError('Not a valid type\nTypes : "name", "value"')
async def alistcat(catname: str, type: str):
  qwe: list = []
  if type == 'name':
    for file in listdir(f'namedb/{catname}'): qwe.append(file[: -5])
    return qwe
  elif type == 'name':
    for file in listdir(f'namedb/{catname}'): f =  open(f'namedb/{catname}/{file}', 'r'); data = load(f); qwe.append(data['value'])
    return qwe
  raise ValueError('Not a valid type\nTypes : "name", "value"')
def prefix(type: str, prefix: str, *, categorie: str = None):
  list: list = []
  if type == 'value':
    for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
      if file.startswith(prefix):
        f =  open(f'namedb/{"" if not categorie else f"{categorie}/"}{file}', 'r'); data: dict = load(f); list.append(data['value'])
    return list
  elif type == 'name':
    for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
      if file.startswith(prefix):
        list.append(file[: -5])
    return list
  raise ValueError('Not a valid type\nTypes : "name", "value"')
async def aprefix(type: str, prefix: str, *, categorie: str = None):
  list: list = []
  if type == 'value':
    for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
      if file.startswith(prefix):
        f =  open(f'namedb/{"" if not categorie else f"{categorie}/"}{file}', 'r'); data: dict = load(f); list.append(data['value'])
    return list
  elif type == 'name':
    for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
      if file.startswith(prefix):
        list.append(file[: -5])
    return list
  raise ValueError('Not a valid type\nTypes : "name", "value"')
def clearprefix(prefix: str, *, cache: bool = False, categorie: str = None):
  for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
    if file.startswith(prefix): remove(file[: -5] ,cache=cache) if not categorie else remove(file[: -5],cache=cache ,categorie=categorie)
  return True
async def cleanprefix(prefix: str, *, cache: bool = False, categorie: str = None):
  for file in listdir(f'namedb{"" if not categorie else f"/{categorie}"}'):
    if file.startswith(prefix): remove(file[: -5] ,cache=cache) if not categorie else remove(file[: -5],cache=cache ,categorie=categorie)
def restore(valuename: str, *, categorie: str = None):
  if not path.isfile(f'namedb/old/{valuename}.json'): raise ValueNotExist('value does not exist')
  with open(f'namedb/old/{valuename}.json', 'r') as fp:
    data: dict = load(fp)
  delet(f'namedb/old/{valuename}.json')
  add(valuename, data['value']) if not categorie else add(valuename, data['value'], categorie=categorie)
  return data['value']
async def arestore(valuename: str, *, categorie: str = None):
  if not path.isfile(f'namedb/old/{valuename}.json'): raise ValueNotExist('value does not exist')
  with open(f'namedb/old/{valuename}.json', 'r') as fp:
    data: dict = load(fp)
  delet(f'namedb/old/{valuename}.json')
  add(valuename, data['value']) if not categorie else add(valuename, data['value'], categorie=categorie)
  return data['value']
def clearcache():
  for file in listdir('namedb/old'): delet(f'namedb/old/{file}')
  return True
async def cleancache():
  for file in listdir('namedb/old'): delet(f'namedb/old/{file}')
  return True
def transferjson(data: dict, *, categorie: str = None):
  for valuename in data:
    add(valuename, data[valuename]) if not categorie else add(valuename, data[valuename], categorie=categorie)
  return True
async def atransferjson(data: dict, *, categorie: str = None):
  for valuename in data:
    add(valuename, data[valuename]) if not categorie else add(valuename, data[valuename], categorie=categorie)
  return True
