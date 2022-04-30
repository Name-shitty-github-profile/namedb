from os import path, mkdir
directory = input('Directory path (example : C:/windows/desktop/my/project/) : '); path = path.join(directory, 'namedb'); mkdir(path)
code = """
from os import listdir; from json import load, dump; from os import remove as delet
def search(value: str = None):
  if not value: print("No value so doesn't exist"); return False
  if f'{value}.json' not in listdir('namedb'): return False
  return True

def get(value: str = None):
  if not value: print("No value"); return None
  if f'{value}.json' not in listdir('namedb'): return None
  with open(f'namedb/{value}.json', 'r') as f:
    data = load(f)
  if value.lower() not in data: return None
  v = data[value.lower()]; nvalue = v['value']
  return nvalue
  
def add(valuename: str, value: any):
  if f'{valuename.lower()}.json' in listdir('namedb'): print('value already exist'); return False
  with open(f'namedb/{valuename}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data[valuename.lower()] = {'value': value}
  with open(f'namedb/{valuename}.json', 'w') as fp:
    dump(data, fp, indent=1)
  return True

def edit(valuename: str, value: any):
  if f'{valuename.lower()}.json' not in listdir('namedb'): print('value does not exist'); return False
  with open(f'namedb/{valuename}.json', 'w') as fp:
    fp.write('{}')
  data = {}; data[valuename.lower()] = {'value': value}
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
        f =  open(f'namedb/{file}', 'r'); data = load(f);  fd = data[convert(file)]; list.append(fd['value'])
  elif type == 'name':
    for file in listdir('namedb'):
      if file.startswith(prefix):
        f =  open(f'namedb/{file}', 'r'); data = load(f); list.append(convert(file))
  else:
    print('Not a good type'); return None
  return list

def convert(value: str):
  for i in range(0, 5): value = value.rstrip(value[-1])
  return value
"""
with open(f'{directory}/namedb.py') as f:
  f.write(code)
print('Setup finished !')